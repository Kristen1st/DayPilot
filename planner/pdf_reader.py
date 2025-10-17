import pdfplumber
import os

def extract_text_from_pdf(pdf_path):
    if not os.path.exists(pdf_path):
        return ""
    text = []
    try:
        with pdfplumber.open(pdf_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text() or ""
                if page_text.strip():
                    text.append(page_text)
        return "\n".join(text).strip()
    except Exception as e:
        print(f"PDF read error: {e}")
        return ""
