#!/bin/bash
# Start FastAPI backend
uvicorn main:app --host 0.0.0.0 --port 8000 &

# Start Streamlit frontend
streamlit run frontend/frontend_app.py --server.port 8501
