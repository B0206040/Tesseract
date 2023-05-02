import cv2
import pytesseract
import mahotas

#img_name = 'number4.png'
#image = cv2.imread(img_name)
#cv2.imwrite('img.jpg',image)
def recon_borde(image):
    image=cv2.resize(image,(50,50))
    #t= mahotas.thresholding.otsu(image)
    t = 115
    counter = 0
    for k in range(50):
        for z in range(50):
            color=image[k,z]
            if color>t:
                image[k,z]=255
                
            else:
                counter +=1
                image[k,z]=0
    print(counter)
    thresh = image.copy()
    return thresh

img = cv2.imread('0.jpg',0)

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
#img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
#img = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
#thresh = recon_borde(img)
text = pytesseract.image_to_string(img, lang = "letsgodigital")
print('text  = ', text)
cv2.imshow('result',img)
cv2.waitKey(0)
    

#https://tesseract-ocr.github.io/tessdoc/4.0-with-LSTM.html#400-alpha-for-windows
#config = "--psm 13 -c tessedit_char_whitelist=0123456789"