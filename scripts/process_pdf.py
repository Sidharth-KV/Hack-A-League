#PDF to TXT Conversion

import PyPDF2
from summarizer import summarize

pdf_path = r"C:\Users\Lenovo\Desktop\New folder\uploads\out.pdf"
print("niga")

def pdf_to_text(pdf_path):
    # Open the PDF file in read-binary mode
    with open(pdf_path, 'rb') as pdf_file:
        # Create a PdfReader object instead of PdfFileReader
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        # Initialize an empty string to store the text
        text = ''

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            text += page.extract_text()
    return summarize(text)


pdf_to_text(pdf_path)