from fastapi import APIRouter

router = APIRouter()

@router.get("/stats")
def stats():
    # dummy data
    return {"users_count": 0}  
