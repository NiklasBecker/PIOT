# libraries
import barcodereader
import requests
from content_control import *
import datetime

product_code =  3033490506629
reader_data = barcodereader.read_barcode("img/Kinder.jpg")

response = requests.get('https://world.openfoodfacts.org/api/v0/product/' + str(product_code) + '.json')
# print(response.json())
json_product = response.json()
product_name = json_product['product']['product_name']
print(json_product['product']['product_name'])

date = datetime.datetime.now()

contents = get_from_file()
new_id = calc_new_id(contents)
new_item = construct_item(new_id, product_name, date.isoformat())
add_item_to_data(contents, new_item)
write_to_file(contents)

index = get_item_id(contents, "Nutella")

test = requests.get("http://localhost:8000/trigger-new-item")
print(test.json())

# remove_item(contents, index)