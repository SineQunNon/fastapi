from sqlalchemy import Column, String, DateTime
from datetime import datetime
from db.database import Base

class User(Base):
    __tablename__ = "users"

    email = Column(String, primary_key=True, index=True)
    password = Column(String, nullable=False)
    nickname = Column(String, nullable=False)
    profileImage = Column(String, nullable=True)
    createdAt = Column(DateTime, default=datetime.now)
    modifiedAt = Column(DateTime, default=datetime.now, onupdate=datetime.now)

    def to_json(self):
        return {
            "email": self.email,
            "password": self.password,
            "nickname": self.nickname,
            "profileImage": self.profileImage,
            "createdAt": self.createdAt.isoformat() if self.createdAt else None,
            "modifiedAt": self.modifiedAt.isoformat() if self.modifiedAt else None
        }

    def to_response_json(self):
        return {
            "email": self.email,
            "nickname": self.nickname,
            "profileImage": self.profileImage,
            "createdAt": self.createdAt.isoformat() if self.createdAt else None,
            "modifiedAt": self.modifiedAt.isoformat() if self.modifiedAt else None
        }

    def update_nickname(self, nickname: str):
        self.nickname = nickname
        self.modifiedAt = datetime.now()

    def update_password(self, new_password):
        self.password = new_password
        self.modifiedAt = datetime.now()

    def verify_password(self, password: str) -> bool:
        return self.password == password

