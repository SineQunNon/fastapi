from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.Comment import Comment
from models.Post import Post
from schemas.CommentSchema import CreateCommentRequest, UpdateCommentRequest

class CommentController:
    @staticmethod
    def createComment(post_id: int, request: CreateCommentRequest, db: Session):
        post = db.query(Post).filter(Post.post_id == post_id).first()
        if not post:
            raise HTTPException(
                status_code=404,
                detail="게시글을 찾을 수 없습니다"
            )

        comment = Comment(
            post_id=post_id,
            content=request.content,
            author_email=request.email
        )
        db.add(comment)

        post.increment_comment_count()
        db.commit()
        db.refresh(comment)

        return {
            "message": "댓글 작성을 성공적으로 완료했습니다",
            "comment": comment.to_json()
        }

    @staticmethod
    def getComments(post_id: int, db: Session):
        post = db.query(Post).filter(Post.post_id == post_id).first()
        if not post:
            raise HTTPException(
                status_code=404,
                detail="게시글을 찾을 수 없습니다"
            )

        comments = db.query(Comment).filter(Comment.post_id == post_id).all()
        post_comments = [comment.to_json() for comment in comments]

        return {
            "message": "댓글 조회를 성공적으로 마쳤습니다",
            "comments": post_comments,
            "total": len(post_comments)
        }

    @staticmethod
    def updateComment(comment_id: int, request: UpdateCommentRequest, db: Session):
        comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()
        if not comment:
            raise HTTPException(
                status_code=404,
                detail="댓글을 찾을 수 없습니다"
            )

        if comment.author_email != request.email:
            raise HTTPException(
                status_code=403,
                detail="본인의 댓글만 수정할 수 있습니다"
            )

        comment.update(request.content)
        db.commit()
        db.refresh(comment)

        return {
            "message": "댓글 수정을 성공적으로 완료했습니다",
            "comment": comment.to_json()
        }

    @staticmethod
    def deleteComment(comment_id: int, email: str, db: Session):
        comment = db.query(Comment).filter(Comment.comment_id == comment_id).first()
        if not comment:
            raise HTTPException(
                status_code=404,
                detail="댓글을 찾을 수 없습니다"
            )

        if comment.author_email != email:
            raise HTTPException(
                status_code=403,
                detail="본인의 댓글만 삭제할 수 있습니다"
            )

        post_id = comment.post_id
        post = db.query(Post).filter(Post.post_id == post_id).first()
        if post:
            post.decrement_comment_count()

        db.delete(comment)
        db.commit()

        return {"message": "댓글을 성공적으로 삭제했습니다"}
