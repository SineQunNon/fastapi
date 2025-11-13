from fastapi import HTTPException

from controllers.UserController import userDatabase
from schemas.UserSchema import LoginRequest

class LoginController:
    @staticmethod
    def login(request: LoginRequest):
        if request.email not in userDatabase:
            raise HTTPException(
                status_code=401,
                detail="아이디 또는 비밀번호를 확인해주세요."
            )

        user = userDatabase[request.email]

        if not user.verify_password(request.password):
            raise HTTPException(
                status_code=401,
                detail="아이디 또는 비밀번호를 확인해주세요."
            )
        return {
            "message": "로그인에 성공했습니다",
            "user": {
                "email": user.email,
                "nickname": user.nickname
            }
        }
