from fastapi import HTTPException
from models.Comment import Comment
from schemas.CommentSchema import CreateCommentRequest, UpdateCommentRequest
from controllers.PostController import postDatabase

commentDatabase = {}
comment_id_counter = 1

class CommentController:
    @staticmethod
    def createComment(post_id: int, request: CreateCommentRequest):
        if post_id not in postDatabase:
            raise HTTPException(
                status_code=404,
                detail="게시글을 찾을 수 없습니다"
            )

        global comment_id_counter

        comment = Comment(
            comment_id=comment_id_counter,
            post_id=post_id,
            content=request.content,
            author_email=request.email
        )
        commentDatabase[comment_id_counter] = comment

        post = postDatabase[post_id]
        post.increment_comment_count()

        comment_id_counter += 1

        return {
            "message": "댓글 작성을 성공적으로 완료했습니다",
            "comment": comment.to_json()
        }

    @staticmethod
    def getComments(post_id: int):
        if post_id not in postDatabase:
            raise HTTPException(
                status_code=404,
                detail="게시글을 찾을 수 없습니다"
            )

        post_comments = [
            comment.to_json()
            for comment in commentDatabase.values()
            if comment.post_id == post_id
        ]

        return {
            "message": "댓글 조회를 성공적으로 마쳤습니다",
            "comments": post_comments,
            "total": len(post_comments)
        }

    @staticmethod
    def updateComment(comment_id: int, request: UpdateCommentRequest):
        if comment_id not in commentDatabase:
            raise HTTPException(
                status_code=404,
                detail="댓글을 찾을 수 없습니다"
            )
        comment = commentDatabase[comment_id]

        if comment.author_email != request.email:
            raise HTTPException(
                status_code=403,
                detail="본인의 댓글만 수정할 수 있습니다"
            )

        comment.update(request.content)

        return {
            "message": "댓글 수정을 성공적으로 완료했습니다",
            "comment": comment.to_json()
        }

    @staticmethod
    def deleteComment(comment_id: int, email: str):
        if comment_id not in commentDatabase:
            raise HTTPException(
                status_code=404,
                detail="댓글을 찾을 수 없습니다"
            )

        comment = commentDatabase[comment_id]

        if comment.author_email != email:
            raise HTTPException(
                status_code=403,
                detail="본인의 댓글만 삭제할 수 있습니다"
            )

        post_id = comment.post_id
        if post_id in postDatabase:
            post = postDatabase[post_id]
            post.decrement_comment_count()

        del commentDatabase[comment_id]

        return {"message": "댓글을 성공적으로 삭제했습니다"}
