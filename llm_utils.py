import re, time
from settings import client, DEPLOYMENT, TEMPERATURE, MAX_RETRIES
from prompts import SYSTEM_PROMPT



# Prompt USER

def build_user_prompt(row) -> str:
    """Construit le prompt USER à partir d'une ligne de DataFrame."""
    designation = str(row.get("Désignation produit Marketing Client", "")).strip()
    name        = str(row.get("Name", "")).strip()
    ncl         = str(row.get("Nomenclature IVR", "")).strip()

    source = (
        f"Désignation produit : {designation}"
        if designation
        else f"Nom brut : {name}\nCatégorie : {ncl}"
    )

    return (
        "Voici les données produit.\n"
        f"{source}\n"
        "Génère la DESCRIPTION et les PLUS PRODUIT comme demandé."
    )


# Appel LLM

def call_llm(prompt: str) -> dict:
    """
    Appelle Azure OpenAI et renvoie un dict :
        {desc, plus1, plus2, plus3, tokens}
    Lève RuntimeError si le format de sortie est invalide
    après MAX_RETRIES tentatives.
    """
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            rep = client.chat.completions.create(
                model=DEPLOYMENT,
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user",   "content": prompt},
                ],
                temperature=TEMPERATURE,
            )

            txt, usage = rep.choices[0].message.content.strip(), rep.usage.total_tokens
            m = re.fullmatch(
                r"DESCRIPTION::\s*(.*?)\s*PLUS1::\s*(.*?)\s*PLUS2::\s*(.*?)\s*PLUS3::\s*(.*)",
                txt,
                flags=re.S | re.I,
            )
            if not m:
                raise RuntimeError("Format de sortie inattendu")

            return dict(
                desc=m[1].strip(),
                plus1=m[2].strip(),
                plus2=m[3].strip(),
                plus3=m[4].strip(),
                tokens=usage,
            )

        except Exception as e:
            if attempt == MAX_RETRIES:
                raise RuntimeError(e) from e
            time.sleep(1.5 * attempt)
