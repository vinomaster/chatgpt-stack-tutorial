import os
from PyPDF2 import PdfReader

def extract_text_from_pdfs(folder_path):
    texts = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.pdf'):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'rb') as file:
                reader = PdfReader(file)
                text = ""
                for page_num in range(len(reader.pages)):
                    page = reader.pages[page_num]
                    text += page.extract_text()
                texts.append(text)
    return texts

pdf_directory = '../pdf_files'
corpus = extract_text_from_pdfs(pdf_directory)

# Save extracted texts
with open('corpus.txt', 'w') as f:
    for text in corpus:
        f.write(text + '\n')
