from pyzbar.pyzbar import decode
from PIL import Image

decoded = decode(Image.open('RGBBlink/img/ean-13.jpg'))
print(decoded)
