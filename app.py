import streamlit as st
from google import genai
from pypdf import PdfReader
from dotenv import load_dotenv
import os

load_dotenv()
API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=API_KEY)

st.title("Document Q&A Bot")
st.write("Upload a PDF and ask questions about it.")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file is not None:
    reader = PdfReader(uploaded_file)
    notes = ""
    for page in reader.pages:
        text = page.extract_text()
        if text:
            notes += text

    if not notes.strip():
        st.error("Couldn't extract text from this PDF (it might be scanned images).")
    else:
        st.success("PDF loaded! Ask a question below.")

        with st.form("question_form"):
            question = st.text_input("Ask a question about the document:")
            submitted = st.form_submit_button("Ask")

        if submitted and question:
            prompt = f"Based on this document:\n\n{notes}\n\nAnswer this question: {question}"
            with st.spinner("Thinking..."):
                try:
                    response = client.models.generate_content(
                        model="gemini-3.6-flash",
                        contents=prompt
                    )
                    st.write("**Answer:**")
                    st.write(response.text)
                except Exception as e:
                    st.error(f"Something went wrong: {e}")