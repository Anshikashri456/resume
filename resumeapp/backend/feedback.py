from backend.llm_client import ask_llm

def analyze_resume(resume_text):
    prompt = "You are a professional resume reviewer. Analyze the resume, give strengths, weaknesses, and improvement tips in bullet points."
    return ask_llm(prompt, resume_text)
