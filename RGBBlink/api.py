from fastapi import FastAPI

app = FastAPI()

@app.get("/fridge-items")
def fridge_items():
    return {"Hello TEST!"}
