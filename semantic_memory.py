from langchain.vectorstores import FAISS
from langchain.embeddings import FastEmbedEmbeddings
from langchain.docstore.document import Document
import os
import faiss
from langchain.docstore import InMemoryDocstore

INDEX_PATH = "memory/semantic_memory/faiss_index"
embedding_model = FastEmbedEmbeddings(model_name="BAAI/bge-small-en")  # 384-dim

def load_faiss():
    if os.path.exists(INDEX_PATH):
        return FAISS.load_local(INDEX_PATH, embedding_model, allow_dangerous_deserialization=True)
    else:
        dim = 384  # for FastEmbed bge-small-en
        index = faiss.IndexFlatL2(dim)

        docstore = InMemoryDocstore()
        index_to_docstore_id = {}

        return FAISS(
            embedding_model.embed_query,  # embed_function
            index,                        # faiss.IndexFlatL2
            docstore,                     # InMemoryDocstore
            index_to_docstore_id           # dict
        )

def save_semantic_memory(entry: dict):
    vectorstore = load_faiss()
    doc = Document(
        page_content=entry["edited_text"],
        metadata={
            "query": entry["query"],
            "pdf_path": entry["pdf_path"],
            "references": entry.get("references", [])
        }
    )
    vectorstore.add_documents([doc])
    vectorstore.save_local(INDEX_PATH)

def search_semantic_memory(query: str, k: int = 3):
    vectorstore = load_faiss()
    return vectorstore.similarity_search(query, k=k)
