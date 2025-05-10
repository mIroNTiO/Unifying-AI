# 🧪 Dev Run Guide: Enlightenment AI

This guide explains how to test, run, and update your Enlightenment AI project.

---

## 🚀 1. Install Requirements

```bash
pip install -r requirements.txt
```

---

## 🧠 2. Index Your Documents (Manual or Auto)

### Option A: Auto-index if PDFs changed
```bash
python rag/metadata_tracker.py
```

### Option B: Force reindex all
```bash
python -c "from rag.vector_store import create_vectorstore_from_pdfs; create_vectorstore_from_pdfs('rag/sample_docs')"
```

---

## 🔄 3. Run the Backend (FastAPI)

```bash
uvicorn main:app --reload
```

- Runs at: http://127.0.0.1:8000
- Test `/ask` and `/feedback` endpoints

---

## 💬 4. Run the Frontend (Streamlit)

```bash
streamlit run frontend/frontend_app.py
```

- Opens in browser at: http://localhost:8501

---

## 📝 5. Add New Documents

1. Drop new PDFs into:
```
rag/sample_docs/
```

2. Run:
```bash
python rag/metadata_tracker.py
```

---

## 🔍 6. Ask Questions (Topics Auto-detected)

Example:
- “What do Stoics say about emotions?”
- “How can we spot media bias?”
- “What makes an argument valid?”

You’ll see:
- Response
- Confidence score
- Sources used
- Topic classification

---

## 📁 Project Layout Overview

| Path                        | Purpose                               |
|----------------------------|---------------------------------------|
| `main.py`                  | FastAPI backend                       |
| `frontend/frontend_app.py` | Streamlit UI                          |
| `rag/load_documents.py`    | PDF loader with topic tagging         |
| `rag/vector_store.py`      | Topic-specific FAISS indexer          |
| `rag/rag_chain.py`         | Core QA pipeline                      |
| `rag/metadata_tracker.py`  | Only reindexes changed PDFs           |
| `rag/sample_docs/`         | Drop trusted PDFs here                |
| `docs/`                    | Project charter and specs             |

---

## ✅ Pro Tips
- Keep PDFs clearly named by topic for better tagging
- Check `rag/metadata.json` for tracked file info
- Adjust prompt styles in `rag_chain.py` if needed

