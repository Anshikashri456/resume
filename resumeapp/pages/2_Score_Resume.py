import streamlit as st
from backend.resume_parser import extract_text
from backend.scoring import score_resume_with_job

st.title("✅ Score Resume based on Job Description")
uploaded_file = st.file_uploader("Upload Resume (PDF/DOCX/TXT)", type=["pdf", "docx", "txt"])
resume_text = st.text_area("Or paste your resume:", height=200)
job_desc = st.text_area("Paste Job Description:", height=200)

if uploaded_file:
    resume_text = extract_text(uploaded_file)

if st.button("Score Resume"):
    if resume_text.strip() and job_desc.strip():
        with st.spinner("Scoring your resume against the job description..."):
            result = score_resume_with_job(resume_text, job_desc)
        st.subheader("📊 Score & Analysis")
        st.write(result)
    else:
        st.error("Please provide both resume and job description.")
