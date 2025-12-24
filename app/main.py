from fastapi import FastAPI
from app.routers import nutrition

app = FastAPI(
    title="Nutri API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "ok",
        "message": "Nutri API online",
        "docs": "/docs"
    }

app.include_router(nutrition.router)
