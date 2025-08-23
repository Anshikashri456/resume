import streamlit as st
from backend.resume_parser import extract_text
from backend.generator import generate_new_resume

st.title("✍ Generate a New Resume from Old One")
uploaded_file = st.file_uploader("Upload Old Resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
resume_text = st.text_area("Or paste your old resume:", height=300)

if uploaded_file:
    resume_text = extract_text(uploaded_file)

if st.button("Generate New Resume"):
    if resume_text.strip():
        with st.spinner("Generating an improved resume..."):
            new_resume = generate_new_resume(resume_text)
        st.subheader("✨ Improved Resume")
        st.text_area("Here is your improved resume:", value=new_resume, height=400)
    else:
        st.error("Please upload or paste your old resume.")
