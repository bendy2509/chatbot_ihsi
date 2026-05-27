import ollama
import chromadb

# Configuration
COLLECTION_NAME = "statistiques"
CHROMA_PATH = "./chroma_db"
MODEL_GEN = "qwen2.5"   # ou "llama3", "mistral", selon ce que tu as téléchargé
MODEL_EMB = "nomic-embed-text"

client = chromadb.PersistentClient(path=CHROMA_PATH)
collection = client.get_collection(COLLECTION_NAME)

def repondre(question, k=5):
    """Récupère les k chunks les plus pertinents et génère une réponse."""
    # 1. Embedding de la question
    emb = ollama.embeddings(model=MODEL_EMB, prompt=question)["embedding"]
    
    # 2. Recherche vectorielle
    results = collection.query(
        query_embeddings=[emb],
        n_results=k,
        include=["documents", "metadatas"]
    )
    
    context = "\n\n".join(results["documents"][0])
    
    # 3. Construction du prompt
    prompt = f"""Tu es un assistant expert en données statistiques.
        Utilise UNIQUEMENT les extraits ci-dessous pour répondre à la question.
        Ne cite pas les extraits, donne une réponse claire et précise.
        Si l'information n'est pas dans les extraits, dis "Je ne trouve pas cette information dans les données."

        EXTRATS :
        {context}

        QUESTION : {question}
        RÉPONSE : 
    """

    # 4. Appel au LLM
    reponse = ollama.chat(
        model=MODEL_GEN,
        messages=[{"role": "user", "content": prompt}]
    )
    return reponse["message"]["content"]

# Interface interactive en console
if __name__ == "__main__":
    print("Chatbot statistique (tape 'quit' pour quitter)")

    # import gradio as gr
    # demo = gr.Interface(fn=repondre, inputs="text", outputs="text", title="Chatbot MHAVE Stats")
    # demo.launch()

    while True:
        q = input("\nQuestion : ")
        if q.lower() == "quit":
            break
        print("Réponse :", repondre(q))