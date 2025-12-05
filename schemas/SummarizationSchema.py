from pydantic import BaseModel, field_validator
from typing import Optional

INVALID_TEXT_EMPTY = "요약할 텍스트를 입력해주세요"
INVALID_MAX_LENGTH = "최대 길이는 10 이상이어야 합니다"
INVALID_MIN_LENGTH = "최소 길이는 5 이상이어야 합니다"

class SummarizeRequest(BaseModel):
    text: str
    max_length: Optional[int] = 150
    min_length: Optional[int] = 50

    @field_validator('text')
    @classmethod
    def validate_text(cls, value):
        if not value or not value.strip():
            raise ValueError(INVALID_TEXT_EMPTY)
        return value

    @field_validator('max_length')
    @classmethod
    def validate_max_length(cls, value):
        if value and value < 10:
            raise ValueError(INVALID_MAX_LENGTH)
        return value

    @field_validator('min_length')
    @classmethod
    def validate_min_length(cls, value):
        if value and value < 5:
            raise ValueError(INVALID_MIN_LENGTH)
        return value

class SummarizePostRequest(BaseModel):
    post_id: int
    max_length: Optional[int] = 150
    min_length: Optional[int] = 50

    @field_validator('max_length')
    @classmethod
    def validate_max_length(cls, value):
        if value and value < 10:
            raise ValueError(INVALID_MAX_LENGTH)
        return value

    @field_validator('min_length')
    @classmethod
    def validate_min_length(cls, value):
        if value and value < 5:
            raise ValueError(INVALID_MIN_LENGTH)
        return value
