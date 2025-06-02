# Interview Assistant API

A Flask‑based API that accepts a PDF resume, generates interview questions via the Gemini API, evaluates answers, and exports a feedback report as PDF.

---

## Features

- **Resume upload** — accepts only PDF files  
- **Text extraction** — uses PyMuPDF to pull text from the resume  
- **Question generation** — calls Gemini API to create technical questions  
- **Answer evaluation** — sends answers back to Gemini for scoring & feedback  
- **Session management** — tracks current question index & feedback in Flask session  
- **PDF report** — compiles all feedback into a downloadable PDF  

---

## Prerequisites

- **Python 3.8+**  
- **Git** (if cloning from a repo)  

---

## Installation & Setup

1. **Clone the repo**  
   ```bash
   git clone <your‑repo‑url> your_project
   cd your_project

2. **Use a clean venv (strongly recommended)**
    ```bash
    python3 -m venv venv
    # Activate:
    # Linux/Mac: source venv/bin/activate
    # Windows  : venv\Scripts\activate

3. **Upgrade pip(Optional)**
    ```bash
    python -m pip install --upgrade pip

3. **Install dependencies**
    ```bash
    pip install Flask python-dotenv pymupdf requests fpdf flask-cors
    pip freeze > requirements.txt

4. **Create a .env file in project root:**
    ```bash
    FLASK_SECRET_KEY=your‑secret‑key
    GEMINI_API_KEY=AIza…
    GEMINI_API_URL=https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent
    UPLOAD_FOLDER=temp_uploads
    MAX_QUESTIONS=5
    INTERVIEW_MODE=technical
    INTERVIEW_DIFFICULTY=medium\
    
5. **Run the app**
    ```bash
    export FLASK_APP=run.py
    export FLASK_ENV=development   # optional: enables debug & auto‑reload
    flask run

The API will be live at http://127.0.0.1:5000/.