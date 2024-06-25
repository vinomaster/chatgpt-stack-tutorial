import os
import streamlit as st
from PyPDF2 import PdfReader
from sentence_transformers import SentenceTransformer, util
import chromadb
from chromadb.config import Settings
from ulid import ULID
import torch

# Extract text from PDFs
def extract_text_from_pdfs(folder_path):
    texts = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'rb') as file:
                reader = PdfReader(file)
                text = ""
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text += page.extract_text()
                texts.append(text)
    return texts

# Generate embeddings locally
def generate_embeddings_locally(texts):
    model = SentenceTransformer('all-MiniLM-L6-v2')  # Choose an appropriate model
    embeddings = model.encode(texts, convert_to_tensor=True)
    print("Number of Embeddings: "+str(len(embeddings)))
    return embeddings

# Store embeddings in ChromaDB
def store_embeddings_in_chromadb(embeddings, texts, collection_name="myData"):
    client = chromadb.HttpClient(host='0.0.0.0', port=55000, settings=Settings(allow_reset=True, anonymized_telemetry=False))
    print("Database Connection Heartbeat: "+str(client.heartbeat()))
    
    collection = client.get_or_create_collection(name=collection_name)

    # Build list of unque identifiers for embeddings
    _ulid = ULID()
    idList = [f"{_ulid.generate()}" for _ in range(len(embeddings))]

    for i, embedding in enumerate(embeddings):
        collection.add(
            ids=idList[i],
            documents=[texts[i]],
            metadatas=[{"source": f"document_{i}"}],
            embeddings=[embedding.tolist()]  # Convert tensor to list
        )

# Basic Query ChromaDB
def basic_query_chromadb(query, top_k=10, collection_name="myData"):
    client = chromadb.HttpClient(host='0.0.0.0', port=55000, settings=Settings(allow_reset=True, anonymized_telemetry=False))
    print("Database Connection Heartbeat: "+str(client.heartbeat()))
    
    collection = client.get_or_create_collection(name=collection_name)

    model = SentenceTransformer('all-MiniLM-L6-v2')  # Use the same model for querying
    query_embedding = model.encode(query, convert_to_tensor=True).tolist()

    limit = min(top_k, len(query))
    print("Database Connection Heartbeat: "+str(client.heartbeat()))
    results = collection.query(query_embeddings=query_embedding, n_results=limit)

    return results['documents']


# Semantic Query ChromaDB
def semantic_query_chromadb(query, corpus, top_k=10, collection_name="myData"):
    client = chromadb.HttpClient(host='0.0.0.0', port=55000, settings=Settings(allow_reset=True, anonymized_telemetry=False))
    print("Database Connection Heartbeat: "+str(client.heartbeat()))
    
    collection = client.get_or_create_collection(name=collection_name)

    model = SentenceTransformer('all-MiniLM-L6-v2')  # Use the same model for querying
    corpus_embeddings = model.encode(corpus, convert_to_tensor=True)
    query_embeddings = model.encode(query, convert_to_tensor=True)

    # Find the closest 5 sentences of the corpus for each query sentence based on cosine similarity
    # We use cosine-similarity and torch.topk to find the highest 5 scores
    limit = min(top_k, len(corpus))
    similarity_scores = model.similarity(query_embeddings, corpus_embeddings)[0]
    scores, indices = torch.topk(similarity_scores, k=limit)

    semantic_hits = util.semantic_search(query_embeddings, corpus_embeddings, top_k=limit)
  
    return list(zip(scores, indices)), semantic_hits

# Streamlit UI
st.title("PDF Corpus Query System")

query = st.text_input("Enter your query:")

corpus = ""

if query:
    results = basic_query_chromadb(query, 5, "pdf_embeddings")
    st.write("Basic Query Results:")
    for result in results:
        st.write(result)
    semantic_results, hits = semantic_query_chromadb(query, corpus, 5, "pdf_embeddings")
    st.write("Semantic Results:")
    st.write("\n   Query:", query)
    st.write("\n   Top 5 most similar sentences in corpus:")
    #print(semantic_results)
    for i in range(len(semantic_results)):
        print(semantic_results[i])
        st.write(semantic_results[i])
    #for score, idx in semantic_results:
     #   st.write(corpus[idx], "(Score: {:.4f})".format(score))
    hits = hits[0]      #Get the hits for the first query
    for hit in hits:
        print(corpus[hit['corpus_id']], "(Score: {:.4f})".format(hit['score']))

if st.button("Extract Text from PDFs"):
    pdf_directory = '../pdf_files'
    st.success("Performing Data Extraction Process...")
    corpus = extract_text_from_pdfs(pdf_directory)
    st.success("Generating Local Embeddings...")
    embeddings = generate_embeddings_locally(corpus)
    store_embeddings_in_chromadb(embeddings, corpus, "pdf_embeddings")
    st.success("Text extracted and embeddings stored successfully!")
