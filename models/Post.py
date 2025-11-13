from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional


class Post(BaseModel):
    post_id: int
    title: str
    content: str
    author_email: str
    postImage: Optional[str] = None
    createdAt: str = Field(default_factory=lambda: datetime.now().isoformat())
    modifiedAt: str = Field(default_factory=lambda: datetime.now().isoformat())
    likes: int = 0
    views: int = 0
    comment_count: int = 0

    def to_json(self):
        return self.model_dump()

    def update(self, title: str, content: str, postImage: Optional[str] = None):
        self.title = title
        self.content = content
        if postImage is not None:
            self.postImage = postImage
        self.modifiedAt = datetime.now().isoformat()

    def increment_views(self):
        self.views += 1

    def increment_comment_count(self):
        self.comment_count += 1

    def decrement_comment_count(self):
        if self.comment_count > 0:
            self.comment_count -= 1

    class Config:
        validate_assignment = True
