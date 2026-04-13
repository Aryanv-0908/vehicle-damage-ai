from fastapi import FastAPI
from routes.detect import router as detect_router

app = FastAPI(title="Vehicle Damage Detection API")

app.include_router(detect_router, prefix="/api")

@app.get("/")
def home():
    return {"message": "Backend is running 🚀"}