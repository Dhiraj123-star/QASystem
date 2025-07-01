from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from openai_client import generate_answer
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI(title="QASystem", description="A simple question-answering system using OpenAI API")

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for testing; restrict in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/query/")
async def query(question: str):
    try:
        logger.info(f"Processing query: {question}")
        answer = generate_answer(question)
        logger.info(f"Generated answer for question: {question[:50]}...")
        return {"question": question, "answer": answer}
    except Exception as e:
        logger.error(f"Error processing query '{question}': {str(e)}")
        return {"status": "error", "message": str(e)}