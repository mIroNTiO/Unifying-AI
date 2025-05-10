# Enlightenment AI

A local-first, open-source AI assistant designed to educate, explain, and help humanity detect misinformation — all while protecting user privacy.

---

## 🎯 Project Goals

- Promote critical thinking, philosophy, science, and media literacy
- Cite real, trusted sources using RAG (Retrieval-Augmented Generation)
- Be transparent, explainable, and non-intrusive
- Stay offline-friendly and user-controlled

---

## 🧠 Features

- ✅ Chat interface (Streamlit UI)
- ✅ FastAPI backend with topic-aware prompts
- ✅ Local model support (e.g. Phi-2, Mistral)
- ✅ Document tagging by topic (philosophy, science, etc.)
- ✅ Topic-specific vector indexing (FAISS)
- ✅ Smart feedback system
- ✅ Auto-update PDF indexing (only re-index changed files)
- ✅ Fully GDPR-friendly (no tracking or PII storage)

---

## 📦 Folder Structure

```
.
├── main.py               # FastAPI backend entry
├── frontend/             # Streamlit app
├── rag/                  # Core logic (RAG, vector store, classifiers)
├── docs/                 # Planning & diagrams
├── dev_run.md            # Step-by-step usage guide
├── requirements.txt      # Python dependencies
└── README.md             # GitHub overview
```

---

## 🚀 Quick Start

```bash
pip install -r requirements.txt
python rag/metadata_tracker.py     # Index PDFs if changed
uvicorn main:app --reload          # Start API backend
streamlit run frontend/frontend_app.py  # Launch UI
```

---

## 🤖 Ask Questions Like:

- “What do Stoics say about fear?”
- “How to spot fake news?”
- “What’s the difference between deductive and inductive logic?”

Answers are based on your local documents — no internet required.

---

## 📚 Add Your Own Knowledge

Place trusted PDFs in:
```
rag/sample_docs/
```

Then run:
```bash
python rag/metadata_tracker.py
```

The assistant will automatically detect topics and update its index.

---

## ✅ License

This project is open-source for non-commercial use. Designed to empower, not exploit.

---

## 🙌 Credits

Built by a human with help from ChatGPT, open-source tools, and a mission to help humanity learn, think, and evolve.
