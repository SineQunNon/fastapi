from pydantic import BaseModel, EmailStr

class RegisterRequest(BaseModel):
    email: EmailStr
    password: str
    confirmedPassword: str
    nickname: str
    profileImage: str | None = None

class UpdateUserRequest(BaseModel):
    nickname: str | None = None
    profileImage: str | None = None

class UserController:
    @staticmethod
    def register(request: RegisterRequest):
        #TODO
        return {"message": "회원가입을 성공했습니다."}

    @staticmethod
    def updateUser(email: str, request: UpdateUserRequest):
        # TODO
        return {"message": "회원정보 수정이 완료됐습니다."}

    @staticmethod
    def deleteUser(email: str):
        # TODO
        return {"message": "회원정보가 성공적으로 삭제되었습니다."}
