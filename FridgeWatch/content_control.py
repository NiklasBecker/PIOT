import json

def get_from_file():
    # get data from json file
    with open('lib/contents.json') as json_file:
        data = json.load(json_file)
    return data

def write_to_file(data):
    # enter adapted data back into json file
    with open('lib/contents.json', 'w') as outfile:
        json.dump(data, outfile)

def add_item_to_data(data, new_id, product_name):
    data['items'].append({"item_id": new_id, "name": product_name})

def calc_new_id(data):
    number_of_items = len(data['items'])
    last_id_in_fridge = data['items'][number_of_items - 1]['item_id']
    return last_id_in_fridge + 1
    
def recalculate_ids(data):
    new_id = 1 
    for item in data.items:
        item.item_id = new_id
        new_id += 1

# TODO
# get_item_id(data, product_name)
# def remove_item(data, item_id)
# def add_date_to_item(data, date, item_id)