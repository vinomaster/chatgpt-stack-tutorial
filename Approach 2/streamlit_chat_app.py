import nltk
from nltk.corpus import stopwords
import spacy

nlp = spacy.load("en_core_web_sm")

def preprocess_text(text):
    doc = nlp(text.lower())
    tokens = [token.lemma_ for token in doc if token.is_alpha and token.lemma_ not in stopwords.words('english')]
    return ' '.join(tokens)

with open('corpus.txt', 'r') as file:
    corpus = file.read()

preprocessed_corpus = [preprocess_text(text) for text in corpus]

# Document Embeddings for Retrieval-Based Q&A
from sentence_transformers import SentenceTransformer
import numpy as np

model = SentenceTransformer('all-MiniLM-L6-v2')
embeddings = model.encode(preprocessed_corpus, show_progress_bar=True)

# Save embeddings
np.save('corpus_embeddings.npy', embeddings)

import os
import streamlit as st
from openai import OpenAI

# Estalish API Client Variable from Session Variable
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  
)

# Deprecated Models. See https://platform.openai.com/docs/deprecations/instructgpt-models
def query_openai(prompt, basemodel):
    response = client.completions.create(
        model=basemodel,
        prompt=prompt,
        max_tokens=150
    )
    return response.choices[0].text.strip()

from sklearn.metrics.pairwise import cosine_similarity

def get_most_relevant_texts(query, embeddings, corpus, model, top_k=5):
    query_embedding = model.encode([query])
    similarities = cosine_similarity(query_embedding, embeddings)
    most_relevant_indices = similarities.argsort()[0][-top_k:][::-1]
    return [corpus[i] for i in most_relevant_indices]

st.title("Domain-Specific Text Analytics Chat")

user_input = st.text_input("Ask your question about the corpus:")

if user_input:
    relevant_texts = get_most_relevant_texts(user_input, embeddings, preprocessed_corpus, model)
    response = query_openai(f"{user_input}\n\nContext: {relevant_texts}",model)
    st.write(response)
