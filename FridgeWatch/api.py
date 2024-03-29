from fastapi import FastAPI
from content_control import get_from_file
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import json
import datetime
import barcodereader as bcr
import content_control as cc

class Item(BaseModel):
    name: str
    date: int

app = FastAPI()

origins = [
    "http://192.168.192.50:5173",
    "http://192.168.192.50:8000",
    "http://192.168.192.50:5173/",
    "http://192.168.192.50:8000/",
    "http://172.17.162.81",
    "http://192.168.192.34",
    "http://172.17.162.81/",
    "http://192.168.192.34/",
    "http://localhost:5173",
    "http://localhost:8000"
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/fridge-items")
def fridge_items():
    data = get_from_file()
    return data

@app.post("/add-new-item")
def new_item(body: Item):
    dt = datetime.datetime.fromtimestamp(body.date/1000).isoformat()
    contents = cc.get_from_file()
    new_id = cc.calc_new_id(contents)
    new_item = cc.construct_item(new_id, body.name, dt)
    cc.add_item_to_data(contents, new_item)
    cc.write_to_file(contents)
    return {"Wrote it!"}

@app.post("/add-new-item-with-barcode")
def new_item(body: Item):
    dt = datetime.datetime.fromtimestamp(body.date/1000).isoformat()
    contents = cc.get_from_file()
    new_id = cc.calc_new_id(contents)
    item_code = bcr.read_barcode('img/Kinder.jpg')
    item_name = cc.request_item_data(item_code)
    new_item = cc.construct_item(new_id, item_name, dt)
    cc.add_item_to_data(contents, new_item)
    cc.write_to_file(contents)
    return {"Wrote it according to barcode data!"}