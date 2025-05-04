from fastapi import FastAPI
from pydantic import BaseModel
from datetime import date

app = FastAPI()

class Item(BaseModel):
    day: date
    calories: float
    carbohydrates: float
    protein: float
    fat: float 

@app.get("/")
def health():
    return "health check"

@app.get("items/{item_id}")
def read_item(item_id: float):
    return {"item_id": item_id}

@app.post()