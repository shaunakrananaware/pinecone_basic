import pinecone
pinecone.init(api_key="8e480581-80e0-4c84-82b3-7ec344fba470",
              environment="us-west4-gcp-free")
#create index
pinecone.create_index("firstindex", dimension=4, metric="euclidean")
print("INDEXS: ", pinecone.list_indexes(), "\n\n")
