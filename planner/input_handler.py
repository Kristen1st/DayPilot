import os
from planner.ocr_reader import extract_text_from_image
from planner.pdf_reader import extract_text_from_pdf

def handle_input(text_input, file_path=None):
    contents = []

    if text_input:
        contents.append(text_input)

    if file_path:
        ext = file_path.rsplit('.', 1)[-1].lower()
        if ext in ['png', 'jpg', 'jpeg']:
            contents.append(extract_text_from_image(file_path))
        elif ext == 'pdf':
            contents.append(extract_text_from_pdf(file_path))
        elif ext == 'txt':
            with open(file_path, 'r', encoding='utf-8') as f:
                contents.append(f.read())

    all_text = "\n".join(contents).strip()
    if not all_text:
        raise ValueError("No valid content found in input.")

    tasks = [line.strip() for line in all_text.splitlines() if line.strip()]
    return tasks
