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

_Fermez ce guide pour continuer votre travail._
"""
