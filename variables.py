from dotenv import load_dotenv
# Load environment variables from a .env file
load_dotenv()

from langchain_experimental.text_splitter import SemanticChunker
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.embeddings import FastEmbedEmbeddings
from langchain_groq import ChatGroq

# text_splitter = RecursiveCharacterTextSplitter(
#     chunk_size=20000,
#     chunk_overlap=500,
# )

embedding_model = FastEmbedEmbeddings(model_name="BAAI/bge-small-en")
# embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

text_splitter = SemanticChunker(embedding_model)

# Create the ChatGroq model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    )