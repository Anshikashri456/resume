import streamlit as st

st.set_page_config(page_title="AI Resume Analyzer", layout="wide")

st.sidebar.title("📂 Navigation")
st.sidebar.markdown("### Choose a feature:")

pages = {
    "Analyze Resume": "1_Analyze_Resume",
    "Resume Feedback According to Job Description": "2_Score_Resume",
    "Generate New Resume": "3_Generate_Resume"
}


for name in pages.keys():
    st.sidebar.markdown(f"[{name}](/{pages[name]})")
