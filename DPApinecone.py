import pinecone
pinecone.init(api_key="<YOUR_API_KEY>",
              environment="us-west4-gcp-free")
# create index
pinecone.create_index("<YOUR_INDEX_NAME>", dimension=4, metric="euclidean")
print("INDEXS: ", pinecone.list_indexes(), "\n\n")

# delete index
pinecone.delete_index("<YOUR_INDEX_NAME>")

# insert data into index
index = pinecone.Index("<YOUR_INDEX_NAME>")
index.upsert([
    ("A", [0.1, 0.1, 0.1, 0.1]),
    ("B", [0.2, 0.2, 0.2, 0.2]),
    ("C", [0.3, 0.3, 0.3, 0.3]),
    ("D", [0.4, 0.4, 0.4, 0.4]),
    ("E", [0.5, 0.5, 0.5, 0.5])
])

# query index
index = pinecone.Index("<YOUR_INDEX_NAME>")
print("Query Result: ", 
index.query(
    vector = [0.3, 0.3, 0.3, 0.3], 
    top_k = 1, 
    include_values = True
))
