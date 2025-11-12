from fastapi import HTTPException

from pydantic import BaseModel, EmailStr, field_validator
import re

userDatabase = {
    "dleck28@gmail.com" : {
        "email": "dleck28@gmail.com",
        "password": "!@Rai12334",
        "nickname": "usher",
        "profileImage": None
    },
    "test@test.com" : {
        "email": "test@test.com",
        "password": "!Jin1234",
        "nickname": "testJin",
        "profileImage": None
    }
}

INVALID_PASSWORD_FORM = "비밀번호는 8자 이상, 20자 이하이며, 대문자, 소문자, 숫자, 특수문자를 각각 최소 1개 포함해야 한다."
INVALID_PASSWORD_EMPTY = "비밀번호를 입력해주세요"
INVALID_EMAIL_FORM = "올바른 이메일 주소 형식을 입력해주세요(예: example@example.com)"
INVALID_LOGIN_AUTH = "아이디 또는 비밀번호를 확인해주세요."

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

    @field_validator('email')
    @classmethod
    def validateEmail(cls, value: EmailStr):
        if not value or not value.strip():
            raise ValueError(INVALID_EMAIL_FORM)
        return value

    @field_validator('password')
    @classmethod
    def validatePassword(cls, value: str):
        if not value or not value.strip():
            raise ValueError(INVALID_PASSWORD_EMPTY)

        if len(value) < 8 or len(value) > 20:
            raise ValueError(INVALID_PASSWORD_FORM)
        if not re.search(r'[A-Z]', value):
            raise ValueError(INVALID_PASSWORD_FORM)
        if not re.search(r'[a-z]', value):
            raise ValueError(INVALID_PASSWORD_FORM)
        if not re.search(r'[0-9]', value):
            raise ValueError(INVALID_PASSWORD_FORM)
        if not re.search(r'[!@#$%^&*(),.?":{}|<>]', value):
            raise ValueError(INVALID_PASSWORD_FORM)
        return value

class LoginController:
    @staticmethod
    def login(request: LoginRequest):
        if request.email not in userDatabase:
            raise HTTPException(
                status_code=401,
                detail=INVALID_LOGIN_AUTH)
        user = userDatabase[request.email]
        if user["password"] != request.password:
            raise HTTPException(
                status_code=401,
                detail=INVALID_LOGIN_AUTH)

        return {
            "message": "로그인에 성공했습니다",
            "user": {
                "email": user["email"],
                "nickname": user["nickname"]
            }
        }
