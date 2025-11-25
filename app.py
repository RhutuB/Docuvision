# app.py
import streamlit as st
from extractor import extract_text_from_pdf
from google import genai     # <-- Correct SDK for your setup

# -----------------------------
# Gemini API KEY
# -----------------------------
genai_client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

# Use a model that exists in your environment
MODEL_NAME = "models/gemini-2.5-flash"

# -----------------------------
# Streamlit UI
# -----------------------------
st.title("📄 AI PDF Q&A System")
st.write("Upload a PDF → Extract text → Ask any question about it.")

uploaded_file = st.file_uploader("Upload PDF", type=["pdf"])

if uploaded_file:
    file_bytes = uploaded_file.read()

    with st.spinner("Extracting text from PDF..."):
        extracted_text = extract_text_from_pdf(file_bytes)

    st.success("Text extracted successfully!")
    st.subheader("📜 Extracted Text Preview")
    st.text_area("Extracted Text", extracted_text[:3000], height=300)

    st.write("### ❓ Ask a question about the document")
    user_q = st.text_input("Your question:")

    if user_q:
        with st.spinner("Thinking..."):

            prompt = f"""
            You are an intelligent assistant.
            Answer the question strictly based on the following PDF text:

            TEXT:
            {extracted_text}

            QUESTION: {user_q}

            If the answer is not found, say: 'Not available in document.'
            """

            response = genai_client.models.generate_content(
                model=MODEL_NAME,
                contents=prompt
            )

        st.subheader("🧠 Answer")
        st.write(response.text)
