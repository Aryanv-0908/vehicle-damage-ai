from fastapi import APIRouter, UploadFile, File
from utils.file_handler import save_file
from services.model_service import run_detection

router = APIRouter()

@router.post("/detect")
async def detect_damage(file: UploadFile = File(...)):
    
    file_path = save_file(file)
    detections = run_detection(file_path)

    return {
        "detections": detections,
        "message": "Detection working 🚀"
    }