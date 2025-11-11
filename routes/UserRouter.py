from fastapi import APIRouter
from pydantic import BaseModel, EmailStr

router = APIRouter(prefix="/users", tags=["user"])

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    confirmedPassword: str
    nickname: str
    profileImage: str | None = None

class UpdateUserRequest(BaseModel):
    nickname: str | None = None
    profileImage: str | None = None

@router.post("/register")
async def register(request: RegisterRequest):
    # TODO
    return {"message": "회원가입을 성공했습니다."}

@router.put("/{email}")
async def updateUser(email: str, request: UpdateUserRequest):
    # TODO
    return {"message": "회원정보 수정이 완료됐습니다."}

@router.delete("/{email}")
async def deleteUser(email: str):
    # TODO
    return {"message": "회원정보가 성공적으로 삭제되었습니다."}
