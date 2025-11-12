from pydantic import BaseModel


class CreateCommentRequest(BaseModel):
    post_id: int
    content: str

class UpdateCommentRequest(BaseModel):
    content: str

class CommentController:
    @staticmethod
    def createComment(request: CreateCommentRequest):
        # TODO
        return {"message": "댓글 작성을 성공적으로 완료했습니다."}

    @staticmethod
    def getComments(post_id: int):
        # TODO
        return {"message" : "댓글 조회를 성공적으로 마쳤습니다"}

    @staticmethod
    def updateComment(comment_id: int, request: UpdateCommentRequest):
        # TODO
        return {"message": "댓글 수정을 성공적으로 완료했습니다"}

    @staticmethod
    def deleteComment(comment_id: int):
        # TODO
        return {"message": "댓글을 성공적으로 삭제했습니다"}
