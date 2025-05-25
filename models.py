from pydantic import BaseModel
from typing import List

class Product(BaseModel):
    product_id: str
    name: str
    description: str
    available_colors: List[str]
    available_sizes: List[str]
    price: int
    units_left: int
    image_url: str
    product_url: str

class ProductSelection(BaseModel):
    product_id: str
    selected_color: str
    selected_size: str
