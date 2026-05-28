from fastapi import Depends, APIRouter
from database import get_db
from sqlalchemy.orm import Session
import models
import schemas

router = APIRouter()

def return_alert(type,alert):
    return {type: alert}

@router.get("/categories")
def categories(db: Session = Depends(get_db)):
    categories = db.query(models.Category).order_by(models.Category.id).all()
    if categories:
        return categories
    return return_alert("error","no categories")
@router.post("/categories")
def add_category(category: schemas.Category, db: Session = Depends(get_db)):
    new_category = models.Category(
        name = category.name
    )
    db.add(new_category)
    db.commit()
    db.refresh(new_category)
    return new_category