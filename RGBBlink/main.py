# libraries
import barcodereader
import requests

product_code = 9781911223139
# barcodereader.BarcodeReader(Img.jpg)

response = requests.get('https://world.openfoodfacts.org/api/v0/product/' + str(product_code) + '.json')
print(response.json())