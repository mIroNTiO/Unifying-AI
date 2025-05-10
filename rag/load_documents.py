from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os

# Simple function to assign a topic based on filename keywords
def infer_topic_from_filename(filename: str) -> str:
    name = filename.lower()
    if "stoic" in name or "virtue" in name or "philosophy" in name:
        return "philosophy"
    elif "science" in name or "experiment" in name:
        return "science"
    elif "media" in name or "bias" in name or "news" in name:
        return "media_literacy"
    elif "critical" in name or "thinking" in name or "logic" in name:
        return "critical_thinking"
    else:
        return "general"

# Load and split documents from a directory, tagging each with its topic
def load_and_split_documents(directory_path):
    all_docs = []
    for filename in os.listdir(directory_path):
        if filename.endswith(".pdf"):
            full_path = os.path.join(directory_path, filename)
            loader = PyPDFLoader(full_path)
            topic = infer_topic_from_filename(filename)
            documents = loader.load()

            # Add topic metadata
            for doc in documents:
                doc.metadata["topic"] = topic
                doc.metadata["source"] = filename

            all_docs.extend(documents)

    # Split documents into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200
    )
    split_docs = splitter.split_documents(all_docs)
    return split_docs
