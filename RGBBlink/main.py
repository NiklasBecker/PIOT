# libraries
import barcodereader
import requests
from content_control import *

product_code =  3033490506629
# barcodereader.BarcodeReader(Img.jpg)

response = requests.get('https://world.openfoodfacts.org/api/v0/product/' + str(product_code) + '.json')
# print(response.json())
json_product = response.json()
product_name = json_product['product']['product_name']
print(json_product['product']['product_name'])

contents = get_from_file()
new_id = calc_new_id(contents)
add_item_to_data(contents, new_id, product_name)
write_to_file(contents)

# # get data from json file
# with open('lib/contents.json') as json_file:
# data = json.load(json_file)

# number_of_items = len(data['items'])

# last_id_in_fridge = data['items'][number_of_items - 1]['item_id']

# new_id = last_id_in_fridge + 1
# data['items'].append({"item_id": new_id, "name": product_name})

# # enter adapted data back into json file
# with open('lib/contents.json', 'w') as outfile:
# json.dump(data, outfile)

# print(data)