from fastapi import FastAPI
from app.routers import nutrition

app = FastAPI(title="Nutri AI API")

app.include_router(nutrition.router)
