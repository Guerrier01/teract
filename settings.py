import os
import streamlit as st
from dotenv import load_dotenv
from openai import AzureOpenAI
import tiktoken

# Chargement variables .env / Secrets

load_dotenv()

API_KEY       = os.getenv("AZURE_OPENAI_API_KEY")
AZ_ENDPOINT   = os.getenv("AZURE_OPENAI_ENDPOINT")
API_VERSION   = os.getenv("AZURE_OPENAI_API_VERSION", "2024-05-01-preview")
DEPLOYMENT    = os.getenv("AZURE_OPENAI_DEPLOYMENT")

if not (API_KEY and AZ_ENDPOINT and DEPLOYMENT):
    st.error(
        "🚨 Variables d’environnement Azure manquantes (clé / endpoint / deployment). "
        "Voir Settings ➜ Secrets dans Streamlit Cloud.",
        icon="⚠️",
    )
    st.stop()

# Client AzureOpenAI

client = AzureOpenAI(
    api_key=API_KEY,
    azure_endpoint=AZ_ENDPOINT,
    api_version=API_VERSION,
)


# Constantes application

TEMPERATURE   = 0.5
MAX_RETRIES   = 3

# Encodage tokenisation (GPT-4o-Mini)
try:
    ENCODING = tiktoken.encoding_for_model("gpt-4o-mini")
except KeyError:
    ENCODING = tiktoken.get_encoding("o200k_base")
