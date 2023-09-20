# import chromadb
# client = chromadb.PersistentClient()

# posts = client.create_collection(
#     name = "posts"
# )

# post1 = 'apple is delicious'
# post2 = 'banana is sweet'
# post3 = 'I dont want to go to New yourk anymore before getting better'
# post4 = 'Paris is romantic city I have ever went'

# posts.add(
#     documents = [post1,post2,post3,post4],
#     ids=["1","2","3","4"]
# )

# result = posts.query(
#     query_texts = ['yello'],
#     n_results=1
# )

# print(result)