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
    *
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