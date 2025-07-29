# docs.py ───────────────────────────────────────────────────────────────
"""
Guide utilisateur (markdown) – incluant cas multi-feuilles & Antitis.
"""

GUIDE_MD = """
## 📖 Guide utilisateur – Générateur Marketing IA Teract

### 1. Fichiers acceptés
| Type | Extensions | Particularités |
|------|------------|----------------|
| **CSV** | `.csv` | Encoding UTF-8 recommandé. Séparateur `,` ou `;` détecté automatiquement. |
| **Excel** | `.xls`, `.xlsm`, `.xlsx` | • Un onglet **ou** plusieurs.<br>• Si plusieurs : la feuille **Antitis** est obligatoirement présente.<br>• Les autres feuilles sont conservées telles quelles à l’export. |

### 2. Structure attendue de la feuille **Antitis**
- **Ligne 1** : groupes d’attributs (laissée intacte).  
- **Ligne 2** : noms exacts des colonnes (voir liste obligatoire ci-dessous).  
- **Ligne 3+** : données produits.

### 3. Colonnes obligatoires
`Action`, `Type`, `ID`, `Name`, `Nomenclature IVR`, `ID Regroupement`,  
`Nomenclature Jardiland`, `Nomenclature Jardiland.com`, `Nomenclature Gammvert`,  
`Nomenclature Nalod's`, `Nomenclature IVR web`, `Nomenclature Utilisateurs`,  
`Code fournisseur`, `MDM ID`, `Code Unique`, `MDM Name`,  
`Désignation produit Marketing Client`.

Les colonnes IA manquantes (`Description Marketing Client 1`, `Plus produit 1…`)  
sont créées automatiquement lors du traitement.

### 4. Procédure
1. Chargez votre fichier.  
2. Vérifiez l’aperçu de la feuille Antitis.  
3. Cliquez **🚀 Lancer la génération IA** et suivez la progression (lots de 10).  
4. Téléchargez le fichier enrichi : il contient les mêmes feuilles + Antitis complétée.  

### 5. Erreurs courantes
| Message | Cause | Solution |
|---------|-------|----------|
| `Feuille « Antitis » absente` | Classeur multi-onglets sans Antitis | Renommez / ajoutez la feuille. |
| `Colonnes manquantes` | Orthographe ou colonne omise | Corrigez puis relancez. |
| `Format de sortie inattendu` | Réponse GPT incorrecte | Relancez la ligne ou contactez le support. |

_Fermez ce guide via le même bouton pour continuer votre travail._
"""
