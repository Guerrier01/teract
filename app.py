import sys, importlib.util
from datetime import datetime
from io import BytesIO

import pandas as pd
import streamlit as st

# Modules internes
from style import apply_style
import settings                            # Azure & SMTP
from columns import BASE_COLUMNS, IA_COLUMNS
from data_io import read_file
from st_utils import preview_df
from llm_utils import build_user_prompt, call_llm
from docs import GUIDE_MD
import notify

apply_style()

if "show_doc" not in st.session_state:
    st.session_state["show_doc"] = False


def _toggle_doc():
    st.session_state["show_doc"] = not st.session_state["show_doc"]


st.sidebar.button("📖 Guide utilisateur", on_click=_toggle_doc)

if st.session_state["show_doc"]:
    st.sidebar.markdown(GUIDE_MD, unsafe_allow_html=True)

# ───────────────────────────────────
# 2. Upload fichier
# ───────────────────────────────────
st.markdown("### Chargez votre fichier Teract")
uploaded = st.file_uploader(
    "Formats acceptés : xls, xlsm, xlsx, csv",
    type=["xls", "xlsm", "xlsx", "csv"],
)

if uploaded:
    # Lecture & validation
    try:
        df, workbook, groups_row = read_file(uploaded)
        df.columns = [c.replace("/", " ") for c in df.columns]   # normalise '/'

        missing = [c for c in BASE_COLUMNS if c not in df.columns]
        if missing:
            st.markdown(
                f"<div class='error-msg'>❌ Colonnes manquantes : {', '.join(missing)}</div>",
                unsafe_allow_html=True,
            )
            st.stop()

        # Ajout colonnes IA si absentes
        for col in IA_COLUMNS:
            df.setdefault(col, "")

        st.markdown(
            "<div class='success-msg'>✅ Fichier conforme.</div>",
            unsafe_allow_html=True,
        )
        preview_df(df, "Aperçu de la feuille Antitis", "input_preview")

    except Exception as err:
        st.markdown(
            f"<div class='error-msg'>Erreur : {err}</div>",
            unsafe_allow_html=True,
        )
        st.stop()

    # ───────────────────────────────────
    # 3. Lancement génération
    # ───────────────────────────────────
    if st.button("🚀 Lancer la génération IA"):
        total        = len(df)
        errors       = 0
        total_tokens = 0

        progress_bar = st.progress(0)
        counter_ph   = st.empty()

        for start in range(0, total, 10):           # lots de 10
            end = min(start + 10, total)

            for i in range(start, end):
                row = df.iloc[i]
                try:
                    r = call_llm(build_user_prompt(row))
                    df.at[i, "Description Marketing Client 1"] = r["desc"]
                    df.at[i, "Plus produit 1"]                = r["plus1"]
                    df.at[i, "Plus produit 2"]                = r["plus2"]
                    df.at[i, "Plus produit 3"]                = r["plus3"]
                    df.at[i, "IA DATA"] = 1
                    df.at[i, "Token"]   = r["tokens"]
                    df.at[i, "Date"]    = datetime.now().strftime("%d/%m/%Y %H:%M")
                    df.at[i, "IAPLUS"]  = 1
                    df.at[i, "Commentaires"] = ""
                    total_tokens += r["tokens"]
                except Exception as e:
                    errors += 1
                    df.at[i, "IA DATA"] = 0
                    df.at[i, "IAPLUS"]  = 0
                    df.at[i, "Commentaires"] = str(e)[:250]

            processed = end
            progress_bar.progress(processed / total)
            counter_ph.markdown(
                f"<div style='font-weight:600;color:var(--primary);text-align:center;'>"
                f"{processed}/{total} lignes traitées</div>",
                unsafe_allow_html=True,
            )

        progress_bar.empty()
        counter_ph.empty()

        ok_lines = total - errors
        st.success(f"Génération terminée : {ok_lines} lignes OK, {errors} erreurs.")
        preview_df(df, "Aperçu de la feuille enrichie", "output_preview")

        # ───────────────────────────────────
        # 4. Reconstruction classeur & export
        # ───────────────────────────────────
        buf = BytesIO()

        if workbook is None:
            # CSV ou Excel simple
            has_xlwt = importlib.util.find_spec("xlwt") and sys.version_info < (3, 12)
            eng, ext, mime = (
                ("xlwt", ".xls", "application/vnd.ms-excel")
                if has_xlwt
                else (
                    "openpyxl",
                    ".xlsx",
                    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
                )
            )
            df.to_excel(buf, index=False, engine=eng)
        else:
            # Classeur multi-feuilles : on reconstruit Antitis (2 lignes header)
            header_row = df.columns.tolist()
            groups_row_extended = groups_row + [""] * (len(header_row) - len(groups_row))
            top_df = pd.DataFrame([groups_row_extended, header_row])
            out_sheet = pd.concat([top_df, df], ignore_index=True)

            # Remplace la feuille puis ré-écrit toutes les autres intactes
            workbook["Antitis"] = out_sheet
            with pd.ExcelWriter(buf, engine="openpyxl") as writer:
                for sheet_name, sheet_df in workbook.items():
                    sheet_df.to_excel(
                        writer,
                        sheet_name=sheet_name,
                        index=False,
                        header=False if sheet_name == "Antitis" else True,
                    )

            ext = ".xlsx"
            mime = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

        buf.seek(0)
        fname = f"catalogue_enrichi_{datetime.now():%Y%m%d_%H%M}{ext}"
        st.download_button("💾 Télécharger le fichier", buf, file_name=fname, mime=mime)

        # Détails erreurs
        with st.expander("Détails des erreurs"):
            err_df = df[df["IA DATA"] == 0][BASE_COLUMNS + IA_COLUMNS]
            st.write("Aucune." if err_df.empty else "")
            if not err_df.empty:
                st.dataframe(err_df, use_container_width=True)

        # Notification e-mail
        notify.send_report(total, ok_lines, errors, total_tokens)

else:
    st.info("Déposez un fichier pour commencer.")

st.markdown(
    "---\n<div style='text-align:center;font-size:0.85rem;'>© 2025 Teract – "
    "Réservé au service Innovation.</div>",
    unsafe_allow_html=True,
)
