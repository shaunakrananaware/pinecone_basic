import pinecone
pinecone.init(api_key="8e480581-80e0-4c84-82b3-7ec344fba470",
              environment="us-west4-gcp-free")
# create index
pinecone.create_index("firstindex", dimension=4, metric="euclidean")
print("INDEXS: ", pinecone.list_indexes(), "\n\n")

# delete index
pinecone.delete_index("firstindex")

# insert data into index
index = pinecone.Index("firstindex")
index.upsert([
    ("A", [0.1, 0.1, 0.1, 0.1]),
    ("B", [0.2, 0.2, 0.2, 0.2]),
    ("C", [0.3, 0.3, 0.3, 0.3]),
    ("D", [0.4, 0.4, 0.4, 0.4]),
    ("E", [0.5, 0.5, 0.5, 0.5])
])

# query index
index = pinecone.Index("firstindex")
print("Query Result: ", 
index.query(
    vector = [0.3, 0.3, 0.3, 0.3], 
    top_k = 1, 
    include_values = True
))
