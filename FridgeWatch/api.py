from fastapi import FastAPI
from content_control import get_from_file
import json

app = FastAPI()
data = get_from_file()

@app.get("/fridge-items")
def fridge_items():
    return json.dumps(data)
