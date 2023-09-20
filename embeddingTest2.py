from chromadb.utils import embedding_functions

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                model_name="text-embedding-ada-002"
            )
students_embeddings = openai_ef([student_info, club_info, university_info])
print(students_embeddings)