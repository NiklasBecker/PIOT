from fastapi import FastAPI
from content_control import get_from_file
from fastapi.middleware.cors import CORSMiddleware
import json

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8000",
    "http://localhost:5173"
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

@app.get("/trigger-new-item")
def new_item():
    return any