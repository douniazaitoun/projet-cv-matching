import pdfplumber
from docx import Document

def read_pdf_cv(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            page_text = page.extract_text()
            if page_text:
                text += page_text + "\n"
    return text

def read_docx_cv(docx_path):
    doc = Document(docx_path)
    text = []
    for paragraph in doc.paragraphs:
        if paragraph.text:
            text.append(paragraph.text)
    return "\n".join(text)

def read_cv_file(file_path):
    file_path = file_path.lower()

    if file_path.endswith(".pdf"):
        return read_pdf_cv(file_path)

    if file_path.endswith(".docx"):
        return read_docx_cv(file_path)

    raise ValueError("Unsupported file format. Use PDF or DOCX.")