import chromadb
chroma_client = chromadb.Client()


collection.add(
    documents = ["this is a document", "this is spartar"],
    metadatas = [{"source" : "my_source"},{"source" : "delicious"}],
    ids=["id1","id2"]
)

results =  collection.query(
    query_texts=["this is a spartar"],
    n_results=2
)