from pydantic import BaseModel, Field
from datetime import datetime

class Comment(BaseModel):
    comment_id: int
    post_id: int
    content: str
    author_email: str
    created_at: str = Field(default_factory=lambda: datetime.now().isoformat())
    modified_at: str = Field(default_factory=lambda: datetime.now().isoformat())

    def to_json(self):
        return self.model_dump()

    def update(self, content: str):
        self.content = content
        self.modified_at = datetime.now().isoformat()

    class Config:
        validate_assignment = True
