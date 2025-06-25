# data_io.py ────────────────────────────────────────────────────────────
from typing import Union
import pandas as pd

def read_file(upload) -> pd.DataFrame:
    """Lit un fichier xls/xlsx/csv et renvoie un DataFrame (dtype=str)."""
    name = upload.name.lower()
    if name.endswith((".xls", ".xlsm", ".xlsx")):
        return pd.read_excel(upload, dtype=str).fillna("")
    if name.endswith(".csv"):
        try:
            return pd.read_csv(upload, dtype=str).fillna("")
        except pd.errors.ParserError:
            return pd.read_csv(upload, sep=";", dtype=str).fillna("")
    raise ValueError("Format non pris en charge")