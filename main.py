from fastapi import FastAPI
from database import engine, Base
import models
from routers import products, categories

app = FastAPI()

app.include_router(products.router)
app.include_router(categories.router)

Base.metadata.create_all(bind=engine)

