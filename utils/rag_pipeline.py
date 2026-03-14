import os
from langchain_community.vectorstores import Chroma
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from models.embeddings import get_embedding_model


VECTOR_DB_PATH = "./vector_db"
vectordb_instance = None

def create_vector_store(file_path, chunk_size=800, chunk_overlap=100):
    """
    Creates a Chroma vector database from a document.
    """

    try:
        if not os.path.exists(file_path):
            raise FileNotFoundError("Document not found")

        # Load PDF
        loader = PyPDFLoader(file_path)
        documents = loader.load()

        print(f"Loaded {len(documents)} pages from document")

        # Split into chunks
        splitter = RecursiveCharacterTextSplitter(
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap
        )

        chunks = splitter.split_documents(documents)

        print(f"Created {len(chunks)} text chunks")

        # Load embedding model
        embeddings = get_embedding_model()

        # Create vector database
        vectordb = Chroma.from_documents(
            documents=chunks,
            embedding=embeddings,
            persist_directory=VECTOR_DB_PATH
        )

        vectordb.persist()

        print("Vector database created successfully")

        return vectordb

    except Exception as e:
        raise RuntimeError(f"Vector DB creation failed: {str(e)}")


def retrieve_context(query, k=3):

    global vectordb_instance

    if vectordb_instance is None:
        embeddings = get_embedding_model()

        vectordb_instance = Chroma(
            persist_directory=VECTOR_DB_PATH,
            embedding_function=embeddings
        )

    docs = vectordb_instance.similarity_search(query, k=k)

    context = "\n\n".join([doc.page_content for doc in docs])

    return context