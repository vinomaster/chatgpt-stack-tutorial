import os
from openai import OpenAI
import chromadb
from chromadb.config import Settings

# Estalish API Client Variable from Session Variable
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  
)

def generate_embeddings(texts):
    embeddings = []
    for text in texts:
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        # embeddings.append(response['data'][0]['embedding'])
        embeddings.append(response.data[0].embedding)
    return embeddings

def store_embeddings_in_chromadb(embeddings, texts, collection_name):
    client = chromadb.HttpClient(host='0.0.0.0', port=55000, settings=Settings(allow_reset=True, anonymized_telemetry=False))
    print("Database Connection Heartbeat: "+client.heartbeat())
    
    collection = client.get_or_create_collection(name=collection_name)

    for i, embedding in enumerate(embeddings):
        collection.add(
            documents=[texts[i]],
            metadatas=[{"source": f"document_{i}"}],
            embeddings=[embedding]
        )

# Load Extracted Text Data
with open('corpus.txt', 'r') as file:
    corpus = file.read()

# Create Embeddings
embeddings = generate_embeddings(corpus)

# Load Database
store_embeddings_in_chromadb(embeddings, corpus, "pdf_embeddings")