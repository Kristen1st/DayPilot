🧭 DayPilot — Smart Daily Planner (MVP)

[Live Demo](https://daypilot.onrender.com)  

DayPilot is an AI-powered smart daily planner built in Python. It allows you to seamlessly plan your day by accepting   text, PDF, or image inputs  . The app extracts tasks, automatically assigns times, and stores schedules for future reference.


🚀 Features
Automatic scheduling: Tasks are assigned timestamps intelligently.  
Multi-format input: Supports plain text, PDF, and images (via OCR).  
Persistent storage: Stores schedules in a SQLite database.  
Recent history: View your previous plans directly on the dashboard.  
Lightweight & portable: Runs locally or online on Render for free.  


🛠 Tech Stack
Backend: Python, Flask  
Text extraction: Tesseract OCR (`pytesseract`), PDF (`pdfplumber`)  
Database: SQLite  
Frontend: HTML, CSS, JavaScript  
Deployment: Render (Free Tier)

📂 Project Structure

DayPilot/
├── app.py
├── planner/
│ ├── input_handler.py
│ ├── scheduler.py
│ ├── ocr_reader.py
│ └── pdf_reader.py
├── static/
│ ├── style.css
│ └── script.js
├── templates/
│ └── index.html
├── data/
│ └── schedule.db
├── requirements.txt
├── Procfile
├── runtime.txt
└── README.md

⚡ How to Run Locally

1. Clone the repo:

Bash

git clone https://github.com/Kristen1st/DayPilot.git
cd DayPilot
Create a virtual environment and install dependencies:

Bash

python -m venv env
source env/bin/activate   # Windows: env\Scripts\activate
pip install -r requirements.txt
Install Tesseract OCR:

Ubuntu/Debian: sudo apt install tesseract-ocr

macOS (Homebrew): brew install tesseract

Run the app:

Bash

python app.py
Open http://localhost:5000 in your browser

🌐 Deployment
The app is deployed on Render (Free Tier):

Live URL: https://daypilot.onrender.com

Auto-deploys from GitHub on every commit

