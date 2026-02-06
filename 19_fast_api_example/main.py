from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(
    title="First FastAPI",
    description="This is the simplest possible FastAPI application",
    version="1.0.0",
)

class Item(BaseModel):
    id: int
    name: str
    price: float

items_db = {}

@app.get("/", tags=["Home"])
def read_root():
    """
    This is the simple root endpoint.
    """
    return {"message": "Welcome to FastAPI!"}

@app.get("/items", tags=["Order"])
def read_items():
    return items_db

@app.get("/items/{item_id}", tags=["Order"])
def read_item(item_id: int):
    """
    Get an item by ID
    - **item_id** - The ID of the item to get
    """
    return items_db[item_id]

@app.post("/items", tags=["Order"])
def create_item(item: Item):
    items_db[item.id] = item
    return {"item_id": item.id}