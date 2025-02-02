import pytesseract 
from pdf2image import convert_from_path
from PIL import Image
from docx2pdf import convert
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"
from process_image import img2str
from summarizer import summarize
from storage import store

docx_file = r"C:\Users\Lenovo\Desktop\New folder\uploads\out.docx"
def convertdocxtopdf(docx_file,pdf_file):
    convert(docx_file,pdf_file)
    return pdf_file

#Initialize empty string
text1 = ''
def convertpdftoimg(pdf_file):
    images1 = convert_from_path(pdf_file)
    text1 = "\n".join([pytesseract.image_to_string(img) for img in images1])
    return text1
convertdocxtopdf("word.docx","file.pdf")
convertpdftoimg("file.pdf")

#Calling summarize function
summ_txt = summarize(text1)
#storing it in temp file
store(summ_txt)

