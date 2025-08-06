# docs.py ───────────────────────────────────────────────────────────────
"""
Guide utilisateur – version feuille **Entities**.
"""

GUIDE_MD = """
## 📖 Guide utilisateur – Générateur Marketing IA Teract

### 1. Fichiers acceptés
| Type | Extensions | Particularités |
|------|------------|----------------|
| **CSV**   | `.csv` | Encodage UTF-8 recommandé. Séparateur `,` ou `;` détecté automatiquement. |
| **Excel** | `.xls`, `.xlsm`, `.xlsx` | • Un onglet **ou** plusieurs.<br>• Si plusieurs : la feuille **Entities** doit exister.<br>• Les autres feuilles sont conservées telles quelles à l’export. |

### 2. Structure attendue de la feuille **Entities**
- **Ligne 1** : groupes d’attributs (laissée intacte).  
- **Ligne 2** : noms exacts des colonnes (voir liste obligatoire ci-dessous).  
- **Ligne 3+** : données produits.

### 3. Colonnes obligatoires
`Action`, `Type`, `ID`, `Name`, `Nomenclature IVR`, `ID Regroupement`,  
`Nomenclature Jardiland`, `Nomenclature Jardiland.com`, `Nomenclature Gammvert`,  
`Nomenclature Nalod's`, `Nomenclature IVR web`, `Nomenclature Utilisateurs`,  
`Code fournisseur`, `MDM ID`, `Code Unique`, `MDM Name`,  
`Désignation produit Marketing Client`.

### 4. Procédure
1. Chargez votre fichier.  
2. Vérifiez l’aperçu de la feuille **Entities**.  
3. Cliquez **🚀 Lancer la génération IA** et suivez la progression (lots de 10).  
4. Téléchargez le fichier enrichi : mêmes feuilles + Entities complétée.  

### 5. Erreurs courantes
| Message | Cause | Solution |
|---------|-------|----------|
| `Feuille « Entities » absente` | Classeur sans onglet Entities | Renommez / ajoutez la feuille. |
| `Colonnes manquantes` | Colonne obligatoire manquante | Corrigez puis relancez. |

### 6. Prompt actuel
Tu es un expert en création de contenus produits pour un site e-commerce spécialisé dans le jardinage, l’alimentation animales et la décoration extérieure.

**Règles générales**  
• Langue française, ton dynamique, professionnel et accessible.  
• Ne paraphrase pas ; réorganise les idées pour produire un texte original.  
• N’invente jamais de caractéristique absente des données.  
• Aucune date, aucun nom d’enseigne ou d’événement.  
• Unités : Ø L l H P ép. g Kg V W (espace avant V/W).  
• « Bulbes » = bulbes floraux (pas de contenu sexuel).  
• Majuscule initiale pour les marques/produits.  
• Chiffres : sépare V et W par un espace (« 12 V », « 100 W »).  
• Si dimensions, poids ou type de batterie ne sont pas fournis, n’écris rien à ce sujet.

---

### Contenu à produire  

1. **DESCRIPTION** :  
   - ≤ 1000 caractères.  
   - Structure conseillée :  
     • Présentation brève du produit.  
     • Bénéfices principaux.  
     • Détails ingrédients/matériaux.  
     • Conseils et usages possibles.  
   - Aucune répétition inutile.

2. **PLUS PRODUIT** (3 atouts consommateurs) :  
   - *PLUS1* = bénéfice majeur.  
   - *PLUS2* & *PLUS3* = bénéfices complémentaires.  
   - ≤ 40 caractères chacun.
   
_Fermez ce guide pour continuer votre travail._
"""
