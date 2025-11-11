from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/users", tags=["user"])

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    confirmedPassword: str
    nickname: str
    profileImage: str | None = None

@router.post("/register")
async def register(request: RegisterRequest):
    # TODO
    return {"message": "회원가입을 성공했습니다."}
