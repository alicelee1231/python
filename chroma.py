import chromadb
client = chromadb.PersistentClient(path= "/content/" )

# collection = client.create_collection("my_information6") 

collection.add( 
    documents=["This is a document containing car information", 
    "This is a document containing information about dogs", 
    "This document contains four wheeler catalogue"], 
    metadatas=[{"source": "Car Book"},{"source": "Dog Book"},{'source':'Vechile Info'}], 
    ids=["id1", "id2", "id3"]
)

# collection.update( ids=["id2"], documents=["This is a document containing information about Cats"], metadatas=[{"source": "Cat Book"}],
# )

# collection.delete(ids = ['id1'])
# results = collection.query( query_texts=["Felines"], n_results=2
# ) 
# print(results)
#
# results = collection.query( query_texts=["Car"], n_results=2
# ) 
# print(results)
# 
# results = collection.query( query_texts=["Felines"], n_results=1
# ) 
# print(results)

my_collection = client.get_collection(name="my_information2") 
print(my_collection)