from fastapi import APIRouter, UploadFile, File

router = APIRouter()

@router.post("/detect")
async def detect_damage(file: UploadFile = File(...)):
    return {
        "filename": file.filename,
        "message": "Backend working, model coming soon 👀"
    }