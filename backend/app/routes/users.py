from fastapi import APIRouter, HTTPException
from ..models import User

router = APIRouter()

# In-memory demo storage
users_db: dict[int, dict] = {}

@router.post("/", status_code=201)
def create_user(user: User):
    if user.id in users_db:
        raise HTTPException(status_code=400, detail="User exists")
    users_db[user.id] = user.dict()
    return users_db[user.id]

@router.get("/{user_id}")
def get_user(user_id: int):
    user = users_db.get(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user