import chromadb
from chromadb.config import Settings

client = chromadb.HttpClient(host='0.0.0.0', port=55000, settings=Settings(allow_reset=True, anonymized_telemetry=False))

print(client.heartbeat())

# switch `create_collection` to `get_or_create_collection` to avoid creating a new collection every time
collection = client.get_or_create_collection(name="my_collection")

# switch `add` to `upsert` to avoid adding the same documents every time
# Add docs to the collection. Can also update and delete. Row-based API coming soon!
collection.add(
    documents=["This is document1", "This is document2"], # we handle tokenization, embedding, and indexing automatically. You can skip that and add your own embeddings as well
    metadatas=[{"source": "notion"}, {"source": "google-docs"}], # filter on these!
    ids=["doc1", "doc2"], # unique for each doc
)

# Query/search 2 most similar results. You can also .get by id
results = collection.query(
    query_texts=["This is a query document"],
    n_results=2
)

print(results)
