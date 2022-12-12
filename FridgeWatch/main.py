# libraries
import barcodereader
import requests
from content_control import *

product_code =  3033490506629
reader_data = barcodereader.read_barcode("img\Kinder.jpg")

code = reader_data.data

print(code)

response = requests.get('https://world.openfoodfacts.org/api/v0/product/' + str(product_code) + '.json')
# print(response.json())
json_product = response.json()
# product_name = json_product['product']['product_name']
print(json_product['product']['product_name'])

contents = get_from_file()
# new_id = calc_new_id(contents)
# add_item_to_data(contents, new_id, product_name)
# write_to_file(contents)

recalculate_ids(contents)