import os
from dotenv import load_dotenv

load_dotenv()

INTERVIEW_CONFIG = {
    "max_questions": 6,
    "mode": "technical",
    "difficulty": "medium"
}

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GEMINI_API_URL = os.getenv("GEMINI_API_URL")