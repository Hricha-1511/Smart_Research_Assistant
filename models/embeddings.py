from langchain_community.embeddings import HuggingFaceEmbeddings

embedding_model = None

def get_embedding_model():
    global embedding_model

    if embedding_model is None:
        embedding_model = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    return embedding_model