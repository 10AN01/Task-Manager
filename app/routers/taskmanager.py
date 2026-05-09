from fastapi import APIRouter

router = APIRouter()
@router.get("/create")
def test():
    return {"message": "Task manager works"}