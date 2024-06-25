import os
from openai import OpenAI

# Estalish API Client Variable from Session Variable
client = OpenAI(
  api_key=os.environ['OPENAI_API_KEY'],  
)

def generate_embeddings(texts):
    embeddings = []
    lineitem = 1
    for text in texts:
        response = client.embeddings.create(
            model="text-embedding-ada-002",
            input=text
        )
        # embeddings.append(response['data'][0]['embedding'])
        embeddings.append(response.data[0].embedding)
        print("Corpus line: "+lineitem)
    return embeddings

# Load Extracted Text Data
with open('corpus.txt', 'r') as file:
    corpus = file.read()

# Create Embeddings
embeddings = generate_embeddings(corpus)


