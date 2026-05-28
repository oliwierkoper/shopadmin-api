from fastapi import Depends, APIRouter
from database import engine, Base, get_db
from sqlalchemy.orm import Session
import models
import schemas

router = APIRouter()

def return_alert(type,alert):
    return {type: alert}

@router.get("/products")
def products(db: Session = Depends(get_db)):
    products = db.query(models.Product).order_by(models.Product.id).all()
    if products:
        return products
    return return_alert("error","no products found")
@router.post("/products")
def add_product(product: schemas.Product, db: Session = Depends(get_db)):
    new_product = models.Product(
        name = product.name,
        category = product.category
    )
    db.add(new_product)
    db.commit()
    db.refresh(new_product)
    return new_product
@router.delete("/products/{product_id}")
def del_product(product_id: int, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product:
        db.delete(product)
        db.commit()
        return return_alert("message","product deleted")
    return return_alert("error","no such product")
@router.patch("/products/{product_id}")
def patch_product(product_id: int, new_product: schemas.Product, db: Session = Depends(get_db)):
    product = db.query(models.Product).filter(models.Product.id == product_id).first()
    if product:
        product.name = new_product.name
        product.category = new_product.category
        db.commit()
        db.refresh(product)
        return return_alert("message","product patched")
    return return_alert("error","no such product")
@router.get("/products/low-stock")
def low_stock(db: Session = Depends(get_db)):
    products = db.query(models.Product).filter(models.Product.stock <= 3).order_by(models.Product.id).all()
    if products:
        return products
    return return_alert("error","no products found")