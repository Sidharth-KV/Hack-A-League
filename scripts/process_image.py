import cv2
import pytesseract
from storage import store
from summarizer import summarize



def img2str():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    path = r"C:\Users\Lenovo\Desktop\New folder\uploads\out.pdf" # path to image
    try:    
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]
        # Morph open to remove noise
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        text = pytesseract.image_to_string(gray, lang='eng', config='--psm 6')#output data
        summ_txt = summarize(text)
        store(summ_txt)
        cv2.waitKey()
        return summ_txt   
        
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
    
img2str()

    
