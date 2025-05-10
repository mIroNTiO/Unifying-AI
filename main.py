from fastapi import FastAPI
from pydantic import BaseModel
import logging
from rag.rag_chain import ask_with_langchain

app = FastAPI()

# Configure logging
logging.basicConfig(filename='logs/interaction_log.txt', level=logging.INFO)

# Sample model for user input
class QueryRequest(BaseModel):
    question: str

class FeedbackRequest(BaseModel):
    question: str
    response: str
    rating: str  # 'up' or 'down'

@app.get("/")
def read_root():
    return {"message": "Welcome to Enlightenment AI Backend"}

@app.post("/ask")
def ask_question(data: QueryRequest):
    result = ask_with_langchain(data.question)
    logging.info(f"Question: {data.question} | Response: {result['response']}")
    return {
        "question": data.question,
        "response": result['response'],
        "sources": result['sources'],
        "confidence": result['confidence']
    }

@app.post("/feedback")
def receive_feedback(feedback: FeedbackRequest):
    log_entry = f"FEEDBACK | Q: {feedback.question} | R: {feedback.response} | Rating: {feedback.rating}"
    logging.info(log_entry)
    return {"status": "Feedback received"}
