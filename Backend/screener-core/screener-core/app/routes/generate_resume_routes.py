from flask import Blueprint, request, send_file
import fitz
from fpdf import FPDF
from app.services.format_resume import generate_basic_template, generate_creative_template, generate_professional_template
import tempfile

generate_resume_bp = Blueprint("generate_resume_bp", __name__)

@generate_resume_bp.route('/generate-resume', methods=['POST'])
def generate_resume():
    data = request.get_json()
    template = data.get('template', 'basic')

    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    if template == "basic":
        generate_basic_template(pdf, data)
    elif template == "professional":
        generate_professional_template(pdf, data)
    elif template == "creative":
        generate_creative_template(pdf, data)

    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    pdf.output(temp_file.name)
    return send_file(temp_file.name, as_attachment=True, download_name=f"resume_{template}.pdf")
