from fastapi import FastAPI
from a2wsgi import WSGIMiddleware
from flask import Flask, render_template, request
from datetime import datetime
from pydantic import BaseModel

app = FastAPI(
    title="My First FastAPI",
    description="This is the simplest FastAPI example",
    version="1.0.0",
)

fapp = Flask(__name__)

class Item(BaseModel):
    id: int
    name: str
    price: float

items_db = {}

@fapp.route("/")
def index():
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", time=current_time)


@app.get("/", tags=["Home"])
def read_root():
    """
    This is the simple root endpoint
    """
    return {"message": "Welcome to FastAPI!"}

@app.get("/items", tags=["Order"])
def read_items():
    """
    Get all the items from Database
    """
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
    """
    Create an item
    - **item** - The item to create
    """
    items_db[item.id] = item
    return {"item_id": item.id}

app.mount("/f", WSGIMiddleware(fapp))

