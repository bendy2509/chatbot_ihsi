Voici le fichier `README.md` complet, prêt à être copié-collé directement dans ton repository GitHub.

# 🤖 MHAVE RAG Chatbot – Assistant Statistique Haïtien

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![Ollama](https://img.shields.io/badge/ollama-local-green.svg)](https://ollama.com/)
[![ChromaDB](https://img.shields.io/badge/chromadb-vector-blue.svg)](https://www.trychroma.com/)

## 🎯 Objectif

Assistant conversationnel capable de répondre à des questions sur des données statistiques haïtiennes à partir d'un fichier Excel/CSV, en utilisant la technique **RAG (Retrieval-Augmented Generation)**.

*100% local** – Pas d'envoi de données vers le cloud  
**Conforme aux exigences de souveraineté** du MHAVE/IHSI

---

## 🧠 Stack technique

| Composant | Technologie |
|-----------|-------------|
| Embeddings | Ollama – `nomic-embed-text` |
| LLM (génération) | Ollama – `bge-m3` (ou `phi3:mini` pour faible RAM) |
| Base vectorielle | ChromaDB |
| Traitement des données | Pandas, openpyxl |
| Interface | Console + Gradio (optionnel) |

---

## 📁 Structure du projet

```
chatbot_ihsi/
├── generate_fake_data.py   # Génère des données synthétiques
├── indexer.py              # Indexe les données dans ChromaDB
├── chatbot.py              # Chatbot RAG (interface console)
├── requirements.txt        # Dépendances Python
└── README.md               # Ce fichier
```

---

## 🚀 Installation

### 1. Cloner le dépôt

```bash
git clone https://github.com/bendy2509/chatbot_ihsi.git
cd chatbot_ihsi
```

### 2. Créer l'environnement Conda

```bash
conda create -n rag-chatbot python=3.10 -y
conda activate rag-chatbot
```

### 3. Installer les dépendances

```bash
pip install -r requirements.txt
```

### 4. Installer les modèles Ollama

```bash
ollama pull nomic-embed-text
ollama pull bge-m3
```

> 💡 *RAM < 4GB ? Utilise `phi3:mini` : `ollama pull phi3:mini`*

---

## 📊 Générer des données de test

```bash
python generate_fake_data.py
```

Crée `statistiques_generes.xlsx` (50 000 lignes de données synthétiques).

---

## 🗂️ Indexer les données

```bash
python indexer.py
```

- Transforme chaque ligne en phrase naturelle
- Calcule l'embedding via Ollama
- Stocke dans ChromaDB

> ⏱️ *Indexation complète ~15 min sur CPU. Le chatbot reste utilisable pendant l'indexation !*

---

## 💬 Lancer le chatbot

```bash
python chatbot.py
```

**Exemples de questions :**

```
👉 Question : Quelle était la population totale en 2023 ?
👉 Question : PIB de la région Nord en 2022 ?
👉 Question : Taux de chômage à Port-au-Prince ?
```

Tape `quit` pour quitter.


## 📂 Format du fichier de données

| colonne | type | exemple |
|---------|------|---------|
| `annee` | int | 2023 |
| `indicateur` | string | Population |
| `valeur` | float/int | 12000000 |
| `region` | string | Total |

**Exemple de transformation :**
> *"En 2023, l'indicateur 'Population' était de 12000000 pour la région Total."*

---

## 🧪 Exemple de session

```
🤖 Chatbot statistique (tape 'quit' pour quitter)

👉 Question : Population totale en 2020
📊 Réponse : En 2020, la population totale d'Haïti était de 11 850 000 habitants.

👉 Question : Tendance du PIB entre 2020 et 2025
📊 Réponse : Le PIB a augmenté de 18,2 milliards USD en 2020 à 21,5 milliards USD en 2025.
```

---

## 🧠 Architecture RAG

```
📄 Excel/CSV → 🔄 Indexation (embedding) → 💾 ChromaDB
                                                    ↓
❓ Question → 🔍 Recherche top-k → 🧠 LLM → ✅ Réponse
```

---

## 📦 requirements.txt

```txt
chromadb>=1.5.0
pandas>=2.0.0
openpyxl>=3.1.0
ollama>=0.6.0
gradio>=6.0.0
```

---

## ⚠️ Dépannage

| Problème | Solution |
|----------|----------|
| `model requires more system memory` | Utilise `phi3:mini` au lieu de `bge-m3` |
| `refusing to merge unrelated histories` | `git pull origin main --allow-unrelated-histories` |
| Indexation lente | Réduis `NB_LIGNES` dans `generate_fake_data.py` |

---

## 📎 Contexte

Développé pour le **Ministère des Haïtiens Vivant à l'Étranger (MHAVE)** – IHSI.

Conformité : Directive 001/IHSI/2026 – Gouvernance Électronique Souveraine.

---

## 👤 Auteur

**Bendy Servilus** – [GitHub](https://github.com/bendy2509)

---

🙏 **Merci d'utiliser ce chatbot pour explorer les données statistiques haïtiennes !**