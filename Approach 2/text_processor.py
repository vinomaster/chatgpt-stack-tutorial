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
