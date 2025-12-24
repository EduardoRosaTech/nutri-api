from fastapi import FastAPI

app = FastAPI(
    title="Nutri API",
    version="1.0.0"
)

@app.get("/")
def root():
    return {
        "status": "online",
        "message": "Nutri API funcionando",
        "docs": "/docs"
    }
