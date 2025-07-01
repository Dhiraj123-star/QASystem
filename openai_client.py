from openai import OpenAI
from dotenv import load_dotenv
import os
import logging

# Configure logging
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    logger.error("OPENAI_API_KEY not found in environment variables")
    raise ValueError("OPENAI_API_KEY not found")
client = OpenAI(api_key=api_key)

def generate_answer(question: str) -> str:
    try:
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": question}]
        )
        logger.info(f"Generated answer for question: {question[:50]}...")
        return response.choices[0].message.content
    except Exception as e:
        logger.error(f"Error generating answer: {str(e)}")
        raise