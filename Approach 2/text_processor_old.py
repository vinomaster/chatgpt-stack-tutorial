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

# Save preprocessed texts
with open('preprocessed_corpus.txt', 'w') as f:
    for text in preprocessed_corpus:
        f.write(text + '\n')

