from pydantic import BaseModel, field_validator
from typing import Optional

INVALID_TITLE_EMPTY = "제목을 입력해주세요"
INVALID_TITLE_LENGTH = "제목은 26자 이하여야 합니다"
INVALID_CONTENT_EMPTY = "게시글 내용을 입력해주세요"

class CreatePostRequest(BaseModel):
    email: str
    title: str
    content: str
    postImage: Optional[str] = None

    @field_validator('title')
    @classmethod
    def validate_title(cls, value):
        if not value or not value.strip():
            raise ValueError(INVALID_TITLE_EMPTY)
        if len(value) > 26:
            raise ValueError(INVALID_TITLE_LENGTH)
        return value

    @field_validator("content")
    @classmethod
    def validate_content(cls, value):
        if not value or not value.strip():
            raise ValueError(INVALID_CONTENT_EMPTY)
        return value

class UpdatePostRequest(BaseModel):
    email: str
    title: str
    content: str
    post_image: Optional[str] = None

    @field_validator('title')
    @classmethod
    def validate_title(cls, value):
        if not value or not value.strip():
            raise ValueError(INVALID_TITLE_EMPTY)
        if len(value) > 26:
            raise ValueError(INVALID_TITLE_LENGTH)
        return value

    @field_validator("content")
    @classmethod
    def validate_content(cls, value):
        if not value or not value.strip():
            raise ValueError(INVALID_CONTENT_EMPTY)
        return value
