from fastapi import HTTPException

from models.User import User
from schemas.UserSchema import RegisterRequest, UpdateUserRequest, UpdateNicknameRequest

userDatabase = {}

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

        user = User(
            email=request.email,
            password=request.password,
            nickname=request.nickname,
            profileImage=request.profileImage
        )

        userDatabase[request.email] = user

        return {
            "message": "회원가입에 성공했습니다",
            "user": user.to_response_json()
        }

    @staticmethod
    def getUser(email: str):
        if email not in userDatabase:
            raise HTTPException(
                status_code=404,
                detail="존재하지 않는 회원입니다."
            )

        user = userDatabase[email]
        return {
            "email": user.email,
            "nickname": user.nickname
        }

    @staticmethod
    def updateNickname(request: UpdateNicknameRequest):
        if request.email not in userDatabase:
            raise HTTPException(
                status_code=404,
                detail="사용자를 찾을 수 없습니다"
            )

        user = userDatabase[request.email]
        user.update_nickname(request.nickname)

        return {
            "message": "닉네임을 성공적으로 수정했습니다"
        }

    @classmethod
    def updatePassword(cls, request):
        if request.email not in userDatabase:
            raise HTTPException(
                status_code=404,
                detail="사용자를 찾을 수 없습니다"
            )

        user = userDatabase[request.email]
        if not user.verify_password(request.current_password):
            raise HTTPException(
                status_code=401,
                detail="현재 비밀번호가 일치하지 않습니다"
            )

        if request.new_password != request.new_password_confirm:
            raise HTTPException(
                status_code=400,
                detail="새 비밀번호가 일치하지 않습니다"
            )

        user.update_password(request.new_password)
        return {
            "message": "비밀번호를 성공적으로 수정했습니다"
        }

    @staticmethod
    def updateUser(email: str, request: UpdateUserRequest):
        if email not in userDatabase:
            raise HTTPException(
                status_code=404,
                detail="사용자를 찾을 수 없습니다"
            )

        user = userDatabase[email]
        user['nickname'] = request.nickname

        if request.profileImage is not None:
            user['profileImage'] = request.profileImage

        return {
            "message": "회원정보 성공적으로 수정했습니다",
            "user": {
                "email": user["email"],
                "nickname": user["nickname"],
                "profileImage": user["profileImage"]
            }
        }

    @staticmethod
    def deleteUser(email: str):
        if email not in userDatabase:
            raise HTTPException(
                status_code=404,
                detail="사용자를 찾을 수 없습니다"
            )

        del userDatabase[email]

        return {"message": "회원정보가 성공적으로 삭제되었습니다"}
