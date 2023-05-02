from PIL import Image
from pytesseract import pytesseract

path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
img_path = 'number4.png'

img = Image.open(img_path)

pytesseract.tesseract_cmd = path

text = pytesseract.image_to_string(img)

print(text[:-1])