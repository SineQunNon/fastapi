import re
from fastapi import HTTPException

from pydantic import BaseModel, EmailStr, field_validator

from controller.LoginController import userDatabase

INVALID_PASSWORD_FORM = "비밀번호는 8자 이상, 20자 이하이며, 대문자, 소문자, 숫자, 특수문자를 각각 최소 1개 포함해야 한다"
INVALID_PASSWORD_EMPTY = "비밀번호를 입력해주세요"
INVALID_EMAIL_FORM = "올바른 이메일 주소 형식을 입력해주세요(예: example@example.com)"
INVALID_NICKNAME_EMPTY = "닉네임을 입력해주세요"
INVALID_NICKNAME_EMPTY_SPACE = "닉네임에 공백을 포함할 수 없습니다"
INVALID_NICKNAME_LENGTH = "닉네임은 10자 이하여야 합니다"


class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    confirmedPassword: str
    nickname: str
    profileImage: str | None = None

    @field_validator("email")
    @classmethod
    def validateEmail(cls, value):
        if not value or not value.strip():
            raise ValueError(INVALID_EMAIL_FORM)
        return value

    @field_validator("password")
    @classmethod
    def validatePassword(cls, value):
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

    @field_validator("confirmedPassword")
    @classmethod
    def validateConfirmedPassword(cls, value):
        if not value or not value.strip():
            raise ValueError(INVALID_PASSWORD_EMPTY)
        return value

    @field_validator("nickname")
    @classmethod
    def validateNickname(cls, value):
        if not value:
            raise ValueError(INVALID_NICKNAME_EMPTY)
        if len(value) > 10:
            raise ValueError(INVALID_NICKNAME_LENGTH)
        if ' ' in value:
            raise ValueError(INVALID_NICKNAME_EMPTY_SPACE)
        return value

class UpdateUserRequest(BaseModel):
    nickname: str | None = None
    profileImage: str | None = None

class UserController:
    @staticmethod
    def register(request: RegisterRequest):
        if request.email in userDatabase:
            raise HTTPException(
                status_code=409,
                detail="중복된 이메일입니다"
            )

        if request.password != request.confirmedPassword:
            raise HTTPException(
                status_code=400,
                detail="비밀번호가 일치하지 않습니다"
            )

        userDatabase[request.email] = {
            "email": request.email,
            "password": request.password,
            "nickname": request.nickname,
            "profileImage": request.profileImage
        }

        return {
            "message": "회원가입을 성공했습니다",
            "user": {
                "email": request.email,
                "password": request.password,
                "nickname": request.nickname,
            }
        }

    @staticmethod
    def updateUser(email: str, request: UpdateUserRequest):
        # TODO
        return {"message": "회원정보 수정이 완료됐습니다"}

    @staticmethod
    def deleteUser(email: str):
        # TODO
        return {"message": "회원정보가 성공적으로 삭제되었습니다"}
