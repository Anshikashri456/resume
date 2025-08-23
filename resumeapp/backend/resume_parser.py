import docx2txt
import fitz  # PyMuPDF

def extract_text(uploaded_file):
    if uploaded_file.type == "application/pdf":
        text = ""
        with fitz.open(stream=uploaded_file.read(), filetype="pdf") as doc:
            for page in doc:
                text += page.get_text()
        return text
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return docx2txt.process(uploaded_file)
    else:
        return uploaded_file.read().decode("utf-8")
