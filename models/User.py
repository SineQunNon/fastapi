from typing import Optional
from pydantic import BaseModel, EmailStr, Field
from datetime import datetime

class User(BaseModel):
    email: EmailStr
    password: str
    nickname: str
    profileImage: Optional[str] = None
    createdAt: str = Field(default_factory=lambda: datetime.now().isoformat())
    modifiedAt: str = Field(default_factory=lambda: datetime.now().isoformat())

    def to_json(self):
        return self.model_dump()

    def to_response_json(self):
        data = self.model_dump()
        data.pop('password')
        return data

    def update_nickname(self, nickname: str):
        self.nickname = nickname

    def update_password(self, new_password):
        self.password = new_password

    def verify_password(self, password: str) -> bool:
        return self.password == password


