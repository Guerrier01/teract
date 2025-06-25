# settings.py ───────────────────────────────────────────────────────────
import os
import streamlit as st
from dotenv import load_dotenv
import openai, tiktoken

# 1. Clés Azure OpenAI
load_dotenv()

openai.api_type       = "azure"
openai.api_key        = os.getenv("AZURE_OPENAI_API_KEY")
openai.azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT")
openai.api_version    = os.getenv("AZURE_OPENAI_API_VERSION", "2024-05-01-preview")
DEPLOYMENT_NAME       = os.getenv("AZURE_OPENAI_DEPLOYMENT")

if not (openai.api_key and openai.azure_endpoint and DEPLOYMENT_NAME):
    st.error(
        "🚨 Variables d’environnement Azure manquantes (clé / endpoint / deployment). "
        "Voir Settings ➜ Secrets dans GitHub.",
        icon="⚠️",
    )
    st.stop()

# 2. Constantes
TEMPERATURE, MAX_RETRIES = 0.5, 3
ENCODING = tiktoken.encoding_for_model("gpt-4o-mini")