from typing import Tuple, Dict, List, Optional
import pandas as pd


def _read_csv(upload) -> Tuple[pd.DataFrame, None, None]:
    """Lit un CSV (séparateur auto) ; DataFrame dtype=str sans NaN."""
    name = upload.name.lower()
    try:
        df = pd.read_csv(upload, dtype=str).fillna("")
    except pd.errors.ParserError:
        df = pd.read_csv(upload, sep=";", dtype=str).fillna("")
    return df, None, None


def _read_excel_single(upload, engine) -> Tuple[pd.DataFrame, None, None]:
    """Excel avec une seule feuille : ligne 1 = header normal."""
    df = pd.read_excel(upload, dtype=str, engine=engine).fillna("")
    return df, None, None


def _read_excel_multi(upload, engine) -> Tuple[pd.DataFrame, Dict[str, pd.DataFrame], List[str]]:
    """
    Lit tout le classeur, extrait la feuille 'Antitis'
    Ligne 0 = groupes   (à conserver)
    Ligne 1 = en-têtes  (base_columns)
    Ligne 2+ = données  (à traiter)
    """
    wb: Dict[str, pd.DataFrame] = pd.read_excel(
        upload, sheet_name=None, header=None, dtype=str, engine=engine
    )

    if "Antitis" not in wb:
        raise ValueError("Classeur : la feuille « Antitis » est absente.")

    ant = wb["Antitis"].fillna("")
    if ant.shape[0] < 2:
        raise ValueError("Feuille Antitis : moins de deux lignes (groupes + en-têtes).")

    groups_row: List[str] = ant.iloc[0].tolist()
    header_row: List[str] = ant.iloc[1].tolist()

    df_antitis = ant.iloc[2:].copy().reset_index(drop=True)
    df_antitis.columns = header_row
    df_antitis = df_antitis.fillna("")

    return df_antitis, wb, groups_row


def read_file(upload):
    """
    Routeur : CSV, Excel mono ou multi.
    Renvoie (df_antitis, workbook, groups_row)
    workbook == None      → simple (on ré-écrit comme avant)
    workbook == dict(...) → on ré-exporte toutes les feuilles
    """
    name = upload.name.lower()

    if name.endswith(".csv"):
        return _read_csv(upload)

    if name.endswith((".xls", ".xlsm", ".xlsx")):
        # Detecte engine, nécessaire pour .xlsm / .xls
        engine = "openpyxl" if name.endswith(".xlsx") else None
        from pandas.io.excel import ExcelFile

        with ExcelFile(upload, engine=engine) as xf:
            if len(xf.sheet_names) == 1:
                return _read_excel_single(upload, engine)
            return _read_excel_multi(upload, engine)

    raise ValueError("Format non pris en charge : CSV ou Excel uniquement.")
