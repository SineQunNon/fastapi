from datetime import datetime

from pydantic import BaseModel, field_validator

postDatabase = {}
post_id_count = 1

class CreatePostRequest(BaseModel):
    title: str
    content: str
    authorEmail: str
    postImage: str | None = None

    @field_validator('title')
    @classmethod
    def valiateTitle(cls, value):
        if not value or not value.strip():
            raise ValueError("제목을 입력해주세요")

        if len(value) > 26:
            raise ValueError("제목은 26자 이하여야 합니다")

        return value

    @field_validator("content")
    @classmethod
    def validateContent(cls, value):
        if not value or not value.strip():
            raise ValueError("게시글 내용을 입력해주세요")

        return value

class UpdatePostRequest(BaseModel):
    title: str
    content: str
    postImage: str | None = None

class PostController:
    @staticmethod
    def createPost(request: CreatePostRequest):
        global post_id_count
        post_id = post_id_count
        post_id_count += 1

        postDatabase[post_id] = {
            "title": request.title,
            "content": request.content,
            "authorEmail": request.authorEmail,
            "postImage": request.postImage,
            "createdAt": datetime.now().isoformat(),
            "likes": 0,
            "views": 0,
        }

        return {
            "message": "게시글을 성공적으로 작성했습니다",
            "post_id": post_id
        }

    @staticmethod
    def getPosts():
        # TODO
        return {"message": "게시글 목록을 성공적으로 조회했습니다"}

    @staticmethod
    def getPost(post_id: int):
        return {"message": "게시글 상세 정보를 성공적으로 조회했습니다"}

    @staticmethod
    def updatePost(post_id: int, request: UpdatePostRequest):
        return {"message": "게시글을 성공적으로 수정했습니다"}

    @staticmethod
    def deletePost(post_id: int):
        return {"message": "게시글을 성공적으로 삭제했습니다"}
