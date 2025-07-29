from typing import Tuple, Dict, List, Optional
import pandas as pd


def _read_csv(upload) -> Tuple[pd.DataFrame, None, None]:
    name = upload.name.lower()
    try:
        df = pd.read_csv(upload, dtype=str).fillna("")
    except pd.errors.ParserError:
        df = pd.read_csv(upload, sep=";", dtype=str).fillna("")
    return df, None, None


def _read_excel_single(upload, engine):
    df = pd.read_excel(upload, dtype=str, engine=engine).fillna("")
    return df, None, None


def _read_excel_multi(upload, engine):
    wb: Dict[str, pd.DataFrame] = pd.read_excel(
        upload, sheet_name=None, header=None, dtype=str, engine=engine
    )

    if "Entities" not in wb:
        raise ValueError("Classeur : la feuille « Entities » est absente.")

    ent = wb["Entities"].fillna("")
    if ent.shape[0] < 2:
        raise ValueError("Feuille Entities : moins de deux lignes (groupes + en-têtes).")

    groups_row: List[str] = ent.iloc[0].tolist()
    header_row: List[str] = ent.iloc[1].tolist()

    df_entities = ent.iloc[2:].copy().reset_index(drop=True)
    df_entities.columns = header_row
    df_entities = df_entities.fillna("")

    return df_entities, wb, groups_row


def read_file(upload):
    name = upload.name.lower()

    if name.endswith(".csv"):
        return _read_csv(upload)

    if name.endswith((".xls", ".xlsm", ".xlsx")):
        engine = "openpyxl" if name.endswith(".xlsx") else None
        from pandas.io.excel import ExcelFile

        with ExcelFile(upload, engine=engine) as xf:
            if len(xf.sheet_names) == 1:
                return _read_excel_single(upload, engine)
            return _read_excel_multi(upload, engine)

    raise ValueError("Format non pris en charge : CSV ou Excel uniquement.")
