from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Simple API Project")

app.include_router(router)