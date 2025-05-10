from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from .load_documents import load_and_split_documents
import os

# Create topic-specific indexes from documents
def create_vectorstore_from_pdfs(pdf_dir, index_base_path="rag_index"):
    documents = load_and_split_documents(pdf_dir)
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    topic_to_docs = {}
    for doc in documents:
        topic = doc.metadata.get("topic", "general")
        topic_to_docs.setdefault(topic, []).append(doc)

    for topic, docs in topic_to_docs.items():
        topic_index_path = os.path.join(index_base_path, topic)
        os.makedirs(topic_index_path, exist_ok=True)
        vectorstore = FAISS.from_documents(docs, embeddings)
        vectorstore.save_local(topic_index_path)

# Load and query the correct index for a topic
def load_vectorstore_by_topic(topic, index_base_path="rag_index"):
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    index_path = os.path.join(index_base_path, topic)
    if not os.path.exists(index_path):
        raise ValueError(f"No index found for topic '{topic}'")
    return FAISS.load_local(index_path, embeddings, allow_dangerous_deserialization=True)

# Query only the matching topic's index
def query_vectorstore(question, topic, k=3):
    db = load_vectorstore_by_topic(topic)
    return db.similarity_search(question, k=k)
