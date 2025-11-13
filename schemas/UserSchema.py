from typing import Optional

from pydantic import BaseModel, EmailStr, field_validator
import re

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
    profileImage: Optional[str] = None

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

class UpdateNicknameRequest(BaseModel):
    email: str
    nickname: str

    @field_validator("nickname")
    @classmethod
    def validate_nickname(cls, value):
        if not value:
            raise ValueError(INVALID_NICKNAME_EMPTY)
        if len(value) > 10:
            raise ValueError(INVALID_NICKNAME_LENGTH)
        if ' ' in value:
            raise ValueError(INVALID_NICKNAME_EMPTY_SPACE)
        return value

class UpdatePasswordRequest(BaseModel):
    email: str
    new_password: str
    new_password_confirm: str

    @field_validator("new_password", "new_password_confirm")
    @classmethod
    def validate_password(cls, value):
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

class UpdateUserRequest(BaseModel):
    nickname: str
    profileImage: str | None = None

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
