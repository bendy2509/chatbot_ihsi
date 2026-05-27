import ollama
import chromadb
import pandas as pd

# Configuration
DATA_FILE = "statistiques_generes.xlsx"
COLLECTION_NAME = "statistiques"
CHROMA_PATH = "./chroma_db"

def ligne_vers_texte(row):
    """Transforme une ligne du DataFrame en une phrase explicite."""
    return f"En {row['annee']}, l'indicateur '{row['indicateur']}' était de {row['valeur']} pour la région {row['region']}."

# Lecture des données
df = pd.read_excel(DATA_FILE)
print(f"Fichier chargé : {len(df)} lignes.")

# Connexion a ChromaDB (persistant)
client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_or_create_collection(name=COLLECTION_NAME)

# Indexation (boucle sur les lignes)
for idx, row in df.iterrows():
    texte = ligne_vers_texte(row)
    
    # Calcul de l'embedding via Ollama
    embedding = ollama.embeddings(model="nomic-embed-text", prompt=texte)["embedding"]
    
    # Ajout a ChromaDB
    collection.add(
        ids=[str(idx)],
        embeddings=[embedding],
        documents=[texte],
        metadatas=[
            {
                "annee": int(row["annee"]),
                "indicateur": row["indicateur"],
                "region": row["region"],
                "valeur": str(row["valeur"])
            }
        ]
    )
    
    if idx % 5000 == 0:
        print(f"Indexé {idx} / {len(df)}")

print("Indexation terminée.")