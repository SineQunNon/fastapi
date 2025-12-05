from fastapi import HTTPException
from sqlalchemy.orm import Session

from models.User import User
from schemas.UserSchema import RegisterRequest, UpdateUserRequest, UpdateNicknameRequest, UpdatePasswordRequest

class UserController:
    @staticmethod
    def register(request: RegisterRequest, db: Session):
        existing_user = db.query(User).filter(User.email == request.email).first()
        if existing_user:
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

        db.add(user)
        db.commit()
        db.refresh(user)

        return {
            "message": "회원가입에 성공했습니다",
            "user": user.to_response_json()
        }

    @staticmethod
    def getUser(email: str, db: Session):
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(
                status_code=404,
                detail="존재하지 않는 회원입니다."
            )

        return {
            "email": user.email,
            "nickname": user.nickname
        }

    @staticmethod
    def updateNickname(request: UpdateNicknameRequest, db: Session):
        user = db.query(User).filter(User.email == request.email).first()
        if not user:
            raise HTTPException(
                status_code=404,
                detail="사용자를 찾을 수 없습니다"
            )

        user.update_nickname(request.nickname)
        db.commit()

        return {
            "message": "닉네임을 성공적으로 수정했습니다"
        }

    @staticmethod
    def updatePassword(request: UpdatePasswordRequest, db: Session):
        user = db.query(User).filter(User.email == request.email).first()
        if not user:
            raise HTTPException(
                status_code=404,
                detail="사용자를 찾을 수 없습니다"
            )

        if request.new_password != request.new_password_confirm:
            raise HTTPException(
                status_code=400,
                detail="새 비밀번호가 일치하지 않습니다"
            )

        user.update_password(request.new_password)
        db.commit()

        return {
            "message": "비밀번호를 성공적으로 수정했습니다"
        }

    @staticmethod
    def updateUser(email: str, request: UpdateUserRequest, db: Session):
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(
                status_code=404,
                detail="사용자를 찾을 수 없습니다"
            )

        user.nickname = request.nickname
        if request.profileImage is not None:
            user.profileImage = request.profileImage

        db.commit()
        db.refresh(user)

        return {
            "message": "회원정보 성공적으로 수정했습니다",
            "user": {
                "email": user.email,
                "nickname": user.nickname,
                "profileImage": user.profileImage
            }
        }

    @staticmethod
    def deleteUser(email: str, db: Session):
        user = db.query(User).filter(User.email == email).first()
        if not user:
            raise HTTPException(
                status_code=404,
                detail="사용자를 찾을 수 없습니다"
            )

        db.delete(user)
        db.commit()

        return {"message": "회원정보가 성공적으로 삭제되었습니다"}

    @staticmethod
    def getUsers(db: Session):
        users = db.query(User).all()
        return {user.email: user for user in users}
