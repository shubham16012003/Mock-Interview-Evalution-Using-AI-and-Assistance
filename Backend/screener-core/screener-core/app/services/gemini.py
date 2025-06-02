import requests
import logging
from app.utils.config import GEMINI_API_KEY, GEMINI_API_URL, INTERVIEW_CONFIG

def call_gemini_api(prompt):
    headers = {"Content-Type": "application/json"}
    payload = {
        "contents": [{"parts": [{"text": prompt}]}],
        "safetySettings": [{
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_ONLY_HIGH"
        }],
        "generationConfig": {
            "temperature": 0.7,
            "topP": 0.9,
            "maxOutputTokens": 1000
        }
    }

    try:
        response = requests.post(f"{GEMINI_API_URL}?key={GEMINI_API_KEY}", json=payload, headers=headers, timeout=30)
        response.raise_for_status()
        result = response.json()
        return result.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', '')
    except Exception as e:
        logging.error(f"Gemini API call failed: {str(e)}")
        return None

def generate_all_questions(resume_text):
    prompt = f"""
    Generate exactly {INTERVIEW_CONFIG['max_questions']} {INTERVIEW_CONFIG['mode']} interview questions 
    based on the following resume. Difficulty level: {INTERVIEW_CONFIG['difficulty']}.
    
    Resume Content:
    {resume_text}
    
    Format:
    1. Question
    2. Question
    ...
    """
    raw = call_gemini_api(prompt)
    if not raw:
        return None

    questions = []
    for line in raw.split('\n'):
        line = line.strip()
        if line and line[0].isdigit():
            questions.append(line.split('.', 1)[1].strip())
    return questions[:INTERVIEW_CONFIG['max_questions']]

def evaluate_answer(question, answer):
    prompt = f"""
    Evaluate this interview response.

    Question: {question}
    Answer: {answer}

    Structure:
    Technical Accuracy: (0-10)
    - Analysis:
    Communication: (0-10)
    - Analysis:
    Relevance: (0-10)
    - Analysis:
    Improvements:
    - Tip 1
    - Tip 2
    Overall Score: (0-100)
    - Summary:
    """
    return call_gemini_api(prompt)

def generate_summary(feedback):
    prompt = f"""
    Create a final evaluation based on this feedback:
    {feedback}

    Include:
    1. Overall Score
    2. Technical Competency
    3. Communication
    4. Strengths
    5. Improvements
    6. Learning Resources
    7. Hiring Recommendation
    """
    return call_gemini_api(prompt)

def generate_ats_score(resume_text):
    prompt = (
        "Analyze the following resume and provide:\n"
        "1. ATS Score (out of 100)\n"
        "2. Strengths\n"
        "3. Areas for Improvement\n"
        "4. Formatting or structure suggestions\n\n"
        f"{resume_text}"
    )
    return call_gemini_api(prompt)