from chromadb.utils import embedding_functions

openai_ef = embedding_functions.OpenAIEmbeddingFunction(
                model_name="text-embedding-ada-002",
                openAI_api_key = "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"
                
            )
students_embeddings = openai_ef([student_info, club_info, university_info])
print(students_embeddings)