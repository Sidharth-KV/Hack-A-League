import cv2
import pytesseract



def img2str():
    pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    path = r"C:\Users\Lenovo\Desktop\download.jpeg" # path to image
    try:    
        image = cv2.imread(path)
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        #blur = cv2.GaussianBlur(gray, (3,3), 0)
        thresh = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]


        # Morph open to remove noise
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3,3))
        #opening = cv2.morphologyEx(thresh, cv2.MORPH_OPEN, kernel, iterations=1)
        #invert = 255 - opening ---> inverting


        # Perform text extraction
        data = pytesseract.image_to_string(gray, lang='eng', config='--psm 6')#output data
        return data
        cv2.waitKey()
    except Exception as e:
        print(f"Error: {str(e)}")
        return None
