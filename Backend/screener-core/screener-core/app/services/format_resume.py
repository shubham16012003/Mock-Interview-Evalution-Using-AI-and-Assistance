def generate_basic_template(pdf, details):
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Resume", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=f"Name: {details.get('name', '')}", ln=True)
    pdf.cell(200, 10, txt=f"Email: {details.get('email', '')}", ln=True)
    pdf.cell(200, 10, txt=f"Phone: {details.get('phone', '')}", ln=True)
    pdf.cell(200, 10, txt=f"Address: {details.get('address', '')}", ln=True)
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Education", ln=True)
    pdf.set_font("Arial", size=12)
    for edu in details.get('education', []):
        pdf.cell(200, 10, txt=f"{edu.get('degree', '')} from {edu.get('university', '')} ({edu.get('year', '')})", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Experience", ln=True)
    pdf.set_font("Arial", size=12)
    for exp in details.get('experience', []):
        pdf.cell(200, 10, txt=f"{exp.get('role', '')} at {exp.get('company', '')} ({exp.get('duration', '')})", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.cell(200, 10, txt="Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.cell(200, 10, txt=", ".join(details.get('skills', [])), ln=True)

def generate_professional_template(pdf, details):
    pdf.set_font("Arial", 'B', 20)
    pdf.set_text_color(50, 50, 50)
    pdf.cell(200, 10, txt=details.get('name', ''), ln=True, align="C")
    pdf.set_font("Arial", 'I', 12)
    pdf.cell(200, 10, txt=f"{details.get('email', '')} | {details.get('phone', '')} | {details.get('address', '')}", ln=True, align="C")
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Education", ln=True)
    pdf.set_font("Arial", size=12)
    for edu in details.get('education', []):
        pdf.cell(200, 10, txt=f"{edu.get('degree', '')}, {edu.get('university', '')}", ln=True)
        pdf.cell(200, 10, txt=f"Graduation: {edu.get('year', '')}", ln=True)
        pdf.ln(5)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Work Experience", ln=True)
    pdf.set_font("Arial", size=12)
    for exp in details.get('experience', []):
        pdf.cell(200, 10, txt=f"{exp.get('role', '')} at {exp.get('company', '')} ({exp.get('duration', '')})", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 14)
    pdf.cell(200, 10, txt="Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=", ".join(details.get('skills', [])))

def generate_creative_template(pdf, details):
    pdf.set_fill_color(255, 230, 204)
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(200, 10, txt="Creative Resume", ln=True, align="C", fill=True)
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 18)
    pdf.cell(200, 10, txt=details.get('name', ''), ln=True, align="C")
    pdf.ln(5)

    pdf.set_font("Arial", size=12)
    pdf.set_text_color(100, 100, 255)
    pdf.cell(100, 10, txt=f"Email: {details.get('email', '')}", border=1, ln=0)
    pdf.cell(100, 10, txt=f"Phone: {details.get('phone', '')}", border=1, ln=1)
    pdf.cell(200, 10, txt=f"Address: {details.get('address', '')}", border=1, ln=1)
    pdf.ln(10)

    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(255, 165, 0)
    pdf.cell(200, 10, txt="Education", ln=True)
    pdf.set_font("Arial", size=12)
    for edu in details.get('education', []):
        pdf.cell(200, 10, txt=f"{edu.get('degree', '')} at {edu.get('university', '')} ({edu.get('year', '')})", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(50, 205, 50)
    pdf.cell(200, 10, txt="Work Experience", ln=True)
    pdf.set_font("Arial", size=12)
    for exp in details.get('experience', []):
        pdf.cell(200, 10, txt=f"{exp.get('role', '')} at {exp.get('company', '')} ({exp.get('duration', '')})", ln=True)

    pdf.ln(10)
    pdf.set_font("Arial", 'B', 12)
    pdf.set_text_color(255, 69, 0)
    pdf.cell(200, 10, txt="Skills", ln=True)
    pdf.set_font("Arial", size=12)
    pdf.multi_cell(200, 10, txt=", ".join(details.get('skills', [])), border=1, fill=True)
