from fastapi import FastAPI
from database import engine, Base
import models
from routers import products

app = FastAPI()

app.include_router(products.router)

Base.metadata.create_all(bind=engine)

