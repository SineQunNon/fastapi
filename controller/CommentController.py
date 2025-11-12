from datetime import datetime
from fastapi import HTTPException

from pydantic import BaseModel, field_validator

from controller.PostController import postDatabase

commentDatabase = {
    1: {
        "post_id" : 1,
        "comment_id" : 1,
        "content": "그것이 왜 알고 싶은가요?",
        "authorEmail": "test11@gmail.com",
        "createAt": datetime.now().isoformat(),
        "modifiedAt": datetime.now().isoformat()
    },
    2: {
        "post_id" : 1,
        "comment_id" : 2,
        "content": "그러게요",
        "authorEmail": "test22@gmail.com",
        "createAt": datetime.now().isoformat(),
        "modifiedAt": datetime.now().isoformat()
    },
}
comment_id_count = 3

class CreateCommentRequest(BaseModel):
    post_id: int
    content: str
    authorEmail: str

    @field_validator("content")
    @classmethod
    def validateContent(cls, value):
        if not value or not value.strip():
            raise ValueError("댓글 내용을 입력해주세요")
        return value


class UpdateCommentRequest(BaseModel):
    content: str

class CommentController:
    @staticmethod
    def createComment(request: CreateCommentRequest):
        if request.post_id not in postDatabase:
            raise HTTPException(
                status_code=404,
                detail="게시글을 찾을 수 없습니다"
            )
        global  comment_id_count
        comment_id = comment_id_count
        comment_id_count += 1

        now = datetime.now().isoformat()

        commentDatabase[comment_id] = {
            "post_id": request.post_id,
            "comment_id": comment_id,
            "content": request.content,
            "authorEmail": request.authorEmail,
            "createdAt": now,
            "modifiedAt": now
        }
        return {
            "message": "댓글 작성을 성공적으로 완료했습니다",
            "comment_id" : comment_id
        }

    @staticmethod
    def getComments(post_id: int):
        if post_id not in postDatabase:
            raise HTTPException(
                status_code=404,
                detail="게시글을 찾을 수 없습니다"
            )
        post_comments = []

        for comment in commentDatabase.values():
            if comment["post_id"] == post_id:
                post_comments.append(comment)
        return {
            "message" : "댓글 조회를 성공적으로 마쳤습니다",
            "comments" : post_comments,
            "total" : len(post_comments)
        }

    @staticmethod
    def updateComment(comment_id: int, request: UpdateCommentRequest):
        if comment_id not in commentDatabase:
            raise HTTPException(
                status_code=404,
                detail="댓글을 찾을 수 없습니다"
            )
        comment = commentDatabase[comment_id]
        comment["content"] = request.content
        comment["modifiedAt"] = datetime.now().isoformat()

        return {
            "message": "댓글 수정을 성공적으로 완료했습니다",
            "comment" : comment
        }

    @staticmethod
    def deleteComment(comment_id: int):
        # TODO
        return {"message": "댓글을 성공적으로 삭제했습니다"}
