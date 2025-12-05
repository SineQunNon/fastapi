from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from datetime import datetime
from typing import Optional
from db.database import Base

class Post(Base):
    __tablename__ = "posts"

    post_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    author_email = Column(String, ForeignKey("users.email"), nullable=False)
    postImage = Column(String, nullable=True)
    createdAt = Column(DateTime, default=datetime.now)
    modifiedAt = Column(DateTime, default=datetime.now, onupdate=datetime.now)
    likes = Column(Integer, default=0)
    views = Column(Integer, default=0)
    comment_count = Column(Integer, default=0)

    def to_json(self):
        return {
            "post_id": self.post_id,
            "title": self.title,
            "content": self.content,
            "author_email": self.author_email,
            "postImage": self.postImage,
            "createdAt": self.createdAt.isoformat() if self.createdAt else None,
            "modifiedAt": self.modifiedAt.isoformat() if self.modifiedAt else None,
            "likes": self.likes,
            "views": self.views,
            "comment_count": self.comment_count
        }

    def update(self, title: str, content: str, postImage: Optional[str] = None):
        self.title = title
        self.content = content
        if postImage is not None:
            self.postImage = postImage
        self.modifiedAt = datetime.now()

    def increment_views(self):
        self.views += 1

    def increment_comment_count(self):
        self.comment_count += 1

    def decrement_comment_count(self):
        if self.comment_count > 0:
            self.comment_count -= 1
