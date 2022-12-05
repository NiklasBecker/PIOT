# libraries
import barcodereader
import requests
import json

product_code = 42354024
# barcodereader.BarcodeReader(Img.jpg)

response = requests.get('https://world.openfoodfacts.org/api/v0/product/' + str(product_code) + '.json')
# print(response.json())
json_product = response.json()
product_name = json_product['product']['product_name']
print(json_product['product']['product_name'])

# get data from json file
with open('lib/contents.json') as json_file:
    data = json.load(json_file)

number_of_items = len(data['items'])

last_id_in_fridge = data['items'][number_of_items - 1]['item_id']

new_id = last_id_in_fridge + 1
data['items'].append({"item_id": new_id, "name": product_name})

# enter adapted data back into json file
with open('lib/contents.json', 'w') as outfile:
    json.dump(data, outfile)

print(data)