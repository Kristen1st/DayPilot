import pytesseract
from PIL import Image
import os

def extract_text_from_image(image_path):
    if not os.path.exists(image_path):
        return ""
    try:
        img = Image.open(image_path)
        img = img.convert("RGB")
        text = pytesseract.image_to_string(img)
        return text.strip()
    except Exception as e:
        print(f"OCR error: {e}")
        return ""
