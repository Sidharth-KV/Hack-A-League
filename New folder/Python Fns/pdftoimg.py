import pytesseract 
from pdf2image import convert_from_path
from PIL import Image
from docx2pdf import convert
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convertpdftoimg(pdf_file):
    images1 = convert_from_path(pdf_file)
    text1 = "\n".join([pytesseract.image_to_string(img) for img in images1])
    print(text1)


convertpdftoimg("file.pdf")
