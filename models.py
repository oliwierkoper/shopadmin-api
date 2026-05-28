from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    category_id = Column(Integer, ForeignKey("categories.id"))
    price = Column(Float)
    stock = Column(Integer)

class Category(Base):
    __tablename__ = "categories"
    id = Column(Integer, primary_key=True)
    name = Column(String)