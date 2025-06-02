import fitz  # PyMuPDF
import logging
import io

def extract_text_from_pdf(file_data):
    try:
        text = ""
        with fitz.open(stream=io.BytesIO(file_data), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text("text") + "\n"
        return text.strip(), None
    except Exception as e:
        logging.error(f"PDF extraction failed: {str(e)}")
        return None, f"PDF processing error: {str(e)}"
