from langchain.chains import LLMChain
from langchain.llms import HuggingFacePipeline
from langchain.prompts import PromptTemplate
from .model_loader import load_local_model
from .vector_store import query_vectorstore
from .topic_classifier import classify_topic

# Load model and wrap in LangChain
llm_pipeline = load_local_model()
llm = HuggingFacePipeline(pipeline=llm_pipeline)

# Prompt templates per topic
PROMPTS = {
    "philosophy": PromptTemplate(
        input_variables=["context", "question"],
        template="""You are a thoughtful philosophical guide. Using the context below, provide a reasoned answer.

Context:
{context}

Question: {question}
Answer:"""
    ),
    "science": PromptTemplate(
        input_variables=["context", "question"],
        template="""You are a scientific assistant. Provide a clear, factual answer using the context below.

Context:
{context}

Question: {question}
Answer:"""
    ),
    "media_literacy": PromptTemplate(
        input_variables=["context", "question"],
        template="""You are a media literacy coach. Use the context to explain how to evaluate the claim.

Context:
{context}

Question: {question}
Answer:"""
    ),
    "critical_thinking": PromptTemplate(
        input_variables=["context", "question"],
        template="""You are a critical thinking guide. Use logic and the context to answer the question.

Context:
{context}

Question: {question}
Answer:"""
    ),
    "general": PromptTemplate(
        input_variables=["context", "question"],
        template="""Using the context below, answer the question clearly and truthfully.

Context:
{context}

Question: {question}
Answer:"""
    )
}

def ask_with_langchain(question):
    topic = classify_topic(question)
    prompt = PROMPTS.get(topic, PROMPTS["general"])
    docs = query_vectorstore(question)
    context = "\n\n".join([doc.page_content for doc in docs])
    chain = LLMChain(llm=llm, prompt=prompt)
    response = chain.run({"context": context, "question": question})
    return {
        "response": response,
        "sources": [doc.metadata.get("source", "static PDF") for doc in docs],
        "confidence": 0.88,
        "topic": topic
    }
