from backend.llm_client import ask_llm

def score_resume_with_job(resume_text, job_description):
    prompt = f"Compare the resume with the job description:\n{job_description}\n\nGive:\n1. A match score out of 100\n2. Missing keywords\n3. How to improve match."
    return ask_llm(prompt, resume_text)
