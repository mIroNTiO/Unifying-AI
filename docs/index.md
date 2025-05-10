---
title: Enlightenment AI
---

# 🧠 Enlightenment AI

A local-first, open-source AI assistant designed to help users understand the world through logic, philosophy, and critical thinking — while protecting their privacy.

---

## 🎯 Project Goals

- Educate users using sourced, explainable answers
- Promote media literacy, reasoning, and awareness
- Stay fully offline-capable and privacy-respecting
- Support multiple topics (philosophy, science, media)

---

## 🔍 How It Works

Enlightenment AI uses a local model (like Phi-2 or Mistral), Retrieval-Augmented Generation (RAG), and topic-specific prompts. You load your own trusted PDFs, and it gives answers based on real content.

---

## 🛠 Technologies

- Python, LangChain, FastAPI, Streamlit
- FAISS vector search
- Local-only HuggingFace models
- Docker-ready for deployment

---

## 📦 Repository Highlights

- `main.py` – FastAPI backend
- `frontend/` – Streamlit UI
- `rag/` – All logic for RAG, indexing, classifiers
- `dev_run.md` – Full local test guide

---

## 🧪 Try It

```bash
pip install -r requirements.txt
python rag/metadata_tracker.py
uvicorn main:app --reload
streamlit run frontend/frontend_app.py
```

---

## 📄 License

Creative Commons Attribution-NonCommercial 4.0  
[View license](https://creativecommons.org/licenses/by-nc/4.0/)

---

*Built by one human and one AI working in harmony.*
