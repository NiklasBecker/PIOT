# libraries
import barcodereader
import requests

product_code = 3017620422003
# barcodereader.BarcodeReader(Img.jpg)

response = requests.get('https://world.openfoodfacts.org/api/v0/product/' + str(product_code) + '.json')
print(response.json())
print(response.json()['product']['product_name'])