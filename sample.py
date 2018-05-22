
# https://github.com/madmaze/pytesseract

from PIL import Image
import pytesseract

# pytesseract.pytesseract.tesseract_cmd = '/usr/local/Cellar/tesseract'
img = 'testocr.png'

print(pytesseract.image_to_string(Image.open(img)))
