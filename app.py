import sys, importlib.util
from datetime import datetime
from io import BytesIO
import pandas as pd
import streamlit as st

# Modules internes
from style import apply_style
import settings
from columns import BASE_COLUMNS, IA_COLUMNS
from data_io import read_file
from st_utils import preview_df
from llm_utils import build_user_prompt, call_llm

# STYLE CORPORATE (CSS + Fonts)

apply_style()

# UI PRINCIPALE

st.markdown("### Générateur de fiches marketing IA – Teract")
uploaded = st.file_uploader(
    "Chargez votre fichier aux formats acceptés : xls, xlsm, xlsx, csv",
    type=["xls", "xlsm", "xlsx", "csv"],
)

if uploaded:
    try:
        df = read_file(uploaded)
        df.columns = [c.replace("/", " ") for c in df.columns]

        # Validation structure
        missing = [c for c in BASE_COLUMNS if c not in df.columns]
        if missing:
            st.markdown(
                f"<div class='error-msg'>❌ Colonnes manquantes : {', '.join(missing)}</div>",
                unsafe_allow_html=True,
            )
            st.stop()

        # Ajout colonnes IA
        for col in IA_COLUMNS:
            if col not in df.columns:
                df[col] = ""

        st.markdown(
            "<div class='success-msg'>✅ Fichier conforme.</div>",
            unsafe_allow_html=True,
        )
        preview_df(df, "Aperçu du fichier d’entrée", "input_preview")

    except Exception as err:
        st.markdown(
            f"<div class='error-msg'>Erreur de lecture : {err}</div>",
            unsafe_allow_html=True,
        )
        st.stop()

    if st.button("🚀 Lancer la génération IA"):
        progress = st.progress(0, text="Appels LLM…")
        errors = 0

        for i, row in df.iterrows():
            try:
                r = call_llm(build_user_prompt(row))
                df.at[i, "Description Marketing Client 1"] = r["desc"]
                df.at[i, "Plus produit 1"] = r["plus1"]
                df.at[i, "Plus produit 2"] = r["plus2"]
                df.at[i, "Plus produit 3"] = r["plus3"]
                df.at[i, "IA DATA"] = 1
                df.at[i, "Token"] = r["tokens"]
                df.at[i, "Date"] = datetime.now().strftime("%d/%m/%Y %H:%M")
                df.at[i, "IAPLUS"] = 1
                df.at[i, "Commentaires"] = ""
            except Exception as e:
                errors += 1
                df.at[i, "IA DATA"] = 0
                df.at[i, "IAPLUS"] = 0
                df.at[i, "Commentaires"] = str(e)[:250]
            progress.progress((i + 1) / len(df))
        progress.empty()

        st.success(
            f"Génération terminée : {len(df) - errors} lignes OK, {errors} erreurs."
        )
        preview_df(df, "Aperçu du fichier enrichi", "output_preview")

        # Export Excel
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
        buf = BytesIO()
        df.to_excel(buf, index=False, engine=eng)
        buf.seek(0)
        fname = f"catalogue_enrichi_{datetime.now():%Y%m%d_%H%M}{ext}"
        st.download_button("💾 Télécharger le fichier", buf, file_name=fname, mime=mime)

        # Détail des erreurs
        with st.expander("Détails des erreurs"):
            err_df = df[df["IA DATA"] == 0][BASE_COLUMNS + IA_COLUMNS]
            if err_df.empty:
                st.write("Aucune.")
            else:
                st.dataframe(err_df, use_container_width=True)

else:
    st.info("Déposez un fichier pour commencer.")

st.markdown(
    "---\n<div style='text-align:center;font-size:0.85rem;'>© 2025 Teract – "
    "Tous droits réservés.</div>",
    unsafe_allow_html=True,
)
