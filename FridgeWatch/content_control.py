import json
import requests
import datetime

json.JSONEncoder

# reads out all data from the contents.json file
def get_from_file():
    # get data from json file
    with open('lib/contents.json') as json_file:
        data = json.load(json_file)
    # print(data)
    return data

# writes adapted data to the contents.json file (unnecessary?)
def write_to_file(data):
    # enter adapted data back into json file
    with open('lib/contents.json', 'w') as outfile:
        json.dump(data, outfile)

def add_item_to_data(data, new_item):
    data['items'].append(new_item)

# construct item to hand over to add_item_to_data
def construct_item(new_id, product_name, date):
    return {"item_id": new_id, "name": product_name, "date": date}

# gets the id of an item in the fridge using its name
def get_item_id(data, product_name):
    for item in data['items']:
        if(item['name'] == product_name):
            # print(item['item_id'])
            return item['item_id']

def remove_item(data, item_id):
    if (item_id != int):
        return any
    del data['items'][item_id-1]
    recalculate_ids(data)

# calculates the id for the item that is being put into the fridge next
def calc_new_id(data):
    number_of_items = len(data['items'])
    last_id_in_fridge = data['items'][number_of_items - 1]['item_id']
    return last_id_in_fridge + 1

# recalculates all ids to keep ids low and concurrent
def recalculate_ids(data):
    new_list = {"items": []}
    new_id = 1
    for item in data['items']:
        item['item_id'] = new_id
        new_id += 1
        new_list['items'].append(item)
#    print(new_list)
    write_to_file(new_list)

# Requesting Data from the openfoodfacts API. Helper function for the api.py
def request_item_data(product_code):
    item_data = requests.get('https://world.openfoodfacts.org/api/v0/product/' + str(product_code) + '.json')
    json_product = item_data.json()
    product_name = json_product['product']['product_name']
    return product_name