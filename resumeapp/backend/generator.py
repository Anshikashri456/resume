from backend.llm_client import ask_llm

def generate_new_resume(resume_text):
    prompt = "Rewrite the following resume to be more ATS-friendly, keyword-optimized, and professional. Keep original content but improve structure and phrasing."
    return ask_llm(prompt, resume_text)
