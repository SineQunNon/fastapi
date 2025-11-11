from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/login", tags=["login"])

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

@router.post("/")
async def login(request: LoginRequest):
    # TODO
    return {"message": "로그인에 성공했습니다"}

