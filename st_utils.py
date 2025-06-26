import streamlit as st
import pandas as pd

def preview_df(df: pd.DataFrame, label: str, key: str) -> None:
    """Affiche les n premières lignes ; bouton 'Voir plus' incrémente n."""
    if key not in st.session_state:
        st.session_state[key] = 5
    n = st.session_state[key]

    st.subheader(label)
    st.dataframe(
        df.head(n),
        use_container_width=True,
        height=min(400, 60 + n * 35),
    )

    if n < len(df):
        if st.button("Voir plus ➜", key=f"more_{key}"):
            st.session_state[key] = min(n + 20, len(df))
            st.experimental_rerun()
