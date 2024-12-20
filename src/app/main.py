from fastapi import FastAPI
from src.app.routes import router

app = FastAPI()

app.include_router(router)