from pydantic import BaseModel, field_validator

INVALID_CONTENT_EMPTY = "댓글 내용을 입력해주세요"

class CreateCommentRequest(BaseModel):
    email: str
    content: str

    @field_validator("content")
    @classmethod
    def validate_content(cls, value):
        if not value or not value.strip():
            raise ValueError(INVALID_CONTENT_EMPTY)
        return value


class UpdateCommentRequest(BaseModel):
    email: str
    content: str

    @field_validator("content")
    @classmethod
    def validate_content(cls, value):
        if not value or not value.strip():
            raise ValueError(INVALID_CONTENT_EMPTY)
        return value
