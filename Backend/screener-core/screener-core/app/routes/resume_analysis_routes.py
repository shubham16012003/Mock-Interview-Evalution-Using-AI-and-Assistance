from flask import Blueprint, request, jsonify
from app.services.gemini import generate_ats_score
from app.services.extraction import extract_text_from_pdf

resume_analysis_bp = Blueprint("resume_analysis_routes", __name__)

@resume_analysis_bp.route('/get-ats-score', methods=['POST'])
def upload_resume():
    if 'resume' not in request.files:
        return jsonify({"error": "No resume file uploaded"}), 400

    file = request.files['resume']
    if file.filename == '':
        return jsonify({"error": "Empty file uploaded"}), 400

    file_bytes = file.read()
    resume_text, error = extract_text_from_pdf(file_bytes)

    if error:
        return jsonify({"error": "Failed to extract text", "details": error}), 500
    if not resume_text.strip():
        return jsonify({"error": "Extracted resume text is empty"}), 400

    try:
        # Call Gemini API and get raw response
        raw_response = generate_ats_score(resume_text)

        # Return as JSON string (frontend will handle parsing and cleaning)
        return jsonify({"result": raw_response.strip()})

    except Exception as e:
        return jsonify({
            "error": "Failed to analyze resume",
            "details": str(e)
        }), 500
