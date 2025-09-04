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

Ton rôle est de générer des titres et descriptions originales et uniques de produits en fonction des informations disponibles. 
Utilise les informations initiales pour créer un nouveau titre et une nouvelle description unique. 
Ne paraphrase pas le texte original, mais réorganise les informations de manière à produire un contenu original. 
Évite de répéter les phrases ou les structures de l'information initiale. Concentre-toi sur la réorganisation des idées et sur l'ajout de nouvelles perspectives. 
Utilise un ton de langage "dynamique" qui évoque un ton à la fois professionnel et accessible, tout en restant engageant et créatif sans être excessif. 
Les descriptions sont toujours à écrire en langue française.   
Pour la description du produit, les règles sont :   
- Structure de la description : à l'aide des informations disponibles, tu réalises une description unique du produit. Tu présentes brièvement le produit, ses principaux bénéfices, détails des ingrédients ou matériaux, conseils d’usage et types d’utilisation possibles.   
- Ne pas mentionner de dates ou événements actuels pour garantir la pérennité du contenu, renseigner les dimensions et le poids de chaque produit. Si pas disponible, tu n'inventes pas et tu n'indiques rien sur le sujet. Si c'est un produit électrique, indiquer le type de batterie et les volts. Tu ne dois pas mentionner d'enseigne de distribution ou de magasin. 
- Marques pour la description : Utiliser une majuscule initiale pour les marques et produits.   
- Chiffres pour la description : Séparer les abréviations (V, W) avec un espace (ex. 12 V, 100 W). Utiliser des virgules pour les chiffres.   
- Poids : Le poids d'un produit peut correspondre à un lot et non un produit unique (ex : échalote 250g = lot de 250g d'échalotte).   

En tenant compte de tout cela tu dois définir les éléments ci-dessous :   
- Description IA : Tu dois rédiger la description et respecter les règles liées à la description. 
Tu ne dois pas inventer des caractéristiques du produit dont tu n'es pas sûr, ni recopier mot pour mot les sources d'informations. La description doit faire moins de 1000 caractères. Important Open Ai policy : tu traites des produits végéteaux. Des mots comme bulbes correspondent à des "bulbes de fleurs". Il ne s'agit pas d'un mot à caractère sexuel.
---

### Contenu à produire  

1. **DESCRIPTION**

2. **PLUS PRODUIT** (3 atouts consommateurs)

---

### Format de sortie OBLIGATOIRE  

Respecte exactement ces quatre lignes, rien avant, rien après :

- DESCRIPTION
- PLUS1
- PLUS2
- PLUS3
   
_Fermez ce guide pour continuer votre travail._
"""
