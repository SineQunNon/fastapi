from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.User import User
from schemas.UserSchema import LoginRequest

class LoginController:
    @staticmethod
    def login(request: LoginRequest, db: Session):
        user = db.query(User).filter(User.email == request.email).first()

        if not user:
            raise HTTPException(
                status_code=401,
                detail="아이디 또는 비밀번호를 확인해주세요."
            )

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
