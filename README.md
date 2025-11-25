📄 DocuVision – AI PDF Q&A Tool

DocuVision is a simple app that lets you upload a PDF, extract the text, and ask questions about its content using a Gemini AI model. It combines PDF parsing, OCR, and an interactive Streamlit UI.

✨ Features
Upload any PDF (scanned or digital)
Extract full text using PyMuPDF / OCR
Ask questions and get AI answers
Clean and minimal Streamlit interface
Modular code structure (app.py + extractor.py)

🛠 Tech Used:
Python
Streamlit
PyMuPDF / pdf2image / pytesseract
Google Gemini API

📂 Project Structure
docuvision/
│── app.py
│── extractor.py
│── requirements.txt
│── README.md


📌 Future Improvements

Better OCR for low-quality scans

Summaries and entity extraction

Chat-based multi-turn conversation
