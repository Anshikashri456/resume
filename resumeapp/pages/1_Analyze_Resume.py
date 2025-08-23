import streamlit as st
from backend.resume_parser import extract_text
from backend.feedback import analyze_resume

st.title("🧐 Analyze Resume using AI")
uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
resume_text = st.text_area("Or paste your resume:", height=300)

if uploaded_file:
    resume_text = extract_text(uploaded_file)

if st.button("Analyze Resume"):
    if resume_text.strip():
        with st.spinner("Analyzing your resume..."):
            feedback = analyze_resume(resume_text)
        st.subheader("✅ Feedback")
        st.write(feedback)
    else:
        st.error("Please upload or paste a resume.")
