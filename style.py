import streamlit as st

def apply_style() -> None:
    """Initialise la page Streamlit + injecte le CSS Teract."""
    st.set_page_config(
        page_title="Teract • Générateur Marketing IA",
        page_icon="🌿",
        layout="wide",
    )

    # Couleurs & police Teract (bleu #0047FF / vert #36B37E)
    st.markdown(
        """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');
html, body, [class*="css"]  { font-family: 'Inter', sans-serif; }
:root  { --primary:#0047FF; --accent:#36B37E; }
h1 { color: var(--primary); font-weight:600; }
.stButton>button { background:var(--primary); color:#fff; border:none;
                   border-radius:6px; padding:0.6rem 1.2rem; font-weight:500; }
.stButton>button:hover { background:#003add; }
.stDownloadButton>button { background:var(--accent); }
.error-msg { color:#D11149; font-weight:500; }
.success-msg { color:var(--accent); font-weight:500; }
table tbody tr th { background:#F5F7FA; }
</style>
""",
        unsafe_allow_html=True,
    )
