from PIL import Image,ImageFilter
import pytesseract
path = 'img_1.jpg'
captcha = Image.open(path)
result = pytesseract.image_to_string(captcha)
print(result)
