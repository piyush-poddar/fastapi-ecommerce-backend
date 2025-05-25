from fastapi import FastAPI, HTTPException
from pymongo import MongoClient
from models import Product, ProductSelection
from typing import Optional

app = FastAPI()

client = MongoClient("mongodb://localhost:27017/")
db = client["shopDB"]
products_collection = db["products"]

@app.get("/products/{product_id}", response_model=Product)
def get_product(product_id: str) -> Optional[Product]:
    product = products_collection.find_one({"product_id": product_id}, {"_id": 0})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@app.post("/products/select")
def select_product(selection: ProductSelection) -> dict:
    product = products_collection.find_one({"product_id": selection.product_id})
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    if selection.selected_color not in product.get("available_colors", []):
        raise HTTPException(status_code=400, detail="Invalid color selected")
    
    if selection.selected_size not in product.get("available_sizes", []):
        raise HTTPException(status_code=400, detail="Invalid size selected")

    return {
        "message": "Product selection successful",
        "product_id": selection.product_id,
        "selected_color": selection.selected_color,
        "selected_size": selection.selected_size
    }
