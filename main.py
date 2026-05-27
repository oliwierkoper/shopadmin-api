from fastapi import FastAPI, Depends
from database import engine, Base, get_db
from sqlalchemy.orm import Session
import models
import schemas

app = FastAPI()

Base.metadata.create_all(bind=engine)

@app.get("/")
def home():
    return {"message":"api works"}

@app.get("/products")
def products(db: Session = Depends(get_db)):
    products = db.query(models.Product).order_by(models.Product.id).all()
    return products
@app.post("/products")
def add_product(product: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(
        name = product.name,
        category = product.category
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product