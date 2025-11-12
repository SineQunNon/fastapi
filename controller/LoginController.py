from pydantic import BaseModel, EmailStr

userDatabase = {}

class LoginRequest(BaseModel):
    email: EmailStr
    password: str

class LoginController:
    @staticmethod
    def login(request: LoginRequest):
        # TODO
        return {"message": "로그인에 성공했습니다"}
