import fitz  # PyMuPDF
import os

def extract_text_from_pdfs(pdf_directory):
    texts = []
    for filename in os.listdir(pdf_directory):
        if filename.endswith(".pdf"):
            with fitz.open(os.path.join(pdf_directory, filename)) as doc:
                text = ""
                for page in doc:
                    text += page.get_text()
                texts.append(text)
    return texts

pdf_directory = 'pdf_files'  # Folder with PDF files
corpus = extract_text_from_pdfs(pdf_directory)

# Save extracted texts
with open('corpus.txt', 'w') as f:
    for text in corpus:
        f.write(text + '\n')
