from flask import Blueprint, request, jsonify
from app.services.extraction import extract_text_from_pdf
from app.services.gemini import generate_all_questions, evaluate_answer, generate_summary

bp = Blueprint('interview', __name__)

@bp.route('/get-interiew-questions', methods=['POST'])
def start_interview():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume uploaded"}), 400
    file = request.files['resume']
    if not file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "Only PDF files are allowed"}), 400

    file_bytes = file.read()

    resume_text, error = extract_text_from_pdf(file_bytes)
    if error or not resume_text:
        return jsonify({"error": error or "Empty resume"}), 500

    questions = generate_all_questions(resume_text)
    print(questions)
    if not questions:
        return jsonify({"error": "Failed to generate questions"}), 500


    return jsonify({
        "questions": questions,
    })


@bp.route('/submit-answers', methods=['POST'])
def submit_answers():
    # 1. Validate resume
    if 'resume' not in request.files:
        return jsonify({"error": "Resume file is missing"}), 400
    resume_file = request.files['resume']
    if not resume_file.filename.lower().endswith('.pdf'):
        return jsonify({"error": "Only PDF files are allowed"}), 400

    resume_bytes = resume_file.read()
    resume_text, error = extract_text_from_pdf(resume_bytes)
    if error or not resume_text:
        return jsonify({"error": error or "Failed to extract text from resume"}), 500

    # 2. Parse qa_payload
    qa_payload = request.form.get('qa_payload')
    if not qa_payload:
        return jsonify({"error": "Missing qa_payload"}), 400

    try:
        import json
        qa_list = json.loads(qa_payload)
        if not isinstance(qa_list, list):
            raise ValueError("qa_payload must be a list")
    except Exception as e:
        return jsonify({"error": f"Invalid qa_payload format: {str(e)}"}), 400

    feedback = []

    for entry in qa_list:
        question = entry.get('question', '').strip()
        answer = entry.get('answer', '').strip()

        if not question or not answer:
            continue

        evaluation = evaluate_answer(question, answer)
        if not evaluation:
            continue

        feedback.append({
            "question": question,
            "answer": answer,
            "evaluation": evaluation
        })

    if not feedback:
        return jsonify({"error": "No valid Q&A entries processed"}), 400

    summary = generate_summary(feedback)

    return jsonify({
        "summary": summary,
        "feedback": feedback
    })