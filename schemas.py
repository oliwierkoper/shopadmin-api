from pydantic import BaseModel

class Product(BaseModel):
    name: str
    category_id: int
    price: float
    stock: int
class Category(BaseModel):
    name: str