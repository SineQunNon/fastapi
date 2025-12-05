from fastapi import HTTPException
from sqlalchemy.orm import Session
from models.Post import Post
from schemas.PostSchema import CreatePostRequest, UpdatePostRequest

class PostController:
    @staticmethod
    def createPost(request: CreatePostRequest, db: Session):
        post = Post(
            title=request.title,
            content=request.content,
            author_email=request.email,
            postImage=request.postImage
        )

        db.add(post)
        db.commit()
        db.refresh(post)

        return {
            "message": "게시글을 성공적으로 작성했습니다",
            "post": post.to_json()
        }

    @staticmethod
    def getPosts(db: Session):
        posts = db.query(Post).all()
        posts_json = [post.to_json() for post in posts]

        return {
            "message": "게시글 목록을 성공적으로 조회했습니다",
            "posts": posts_json,
            "total": len(posts_json)
        }

    @staticmethod
    def getPost(post_id: int, db: Session):
        post = db.query(Post).filter(Post.post_id == post_id).first()
        if not post:
            raise HTTPException(
                status_code=404,
                detail="게시글을 찾을 수 없습니다"
            )

        post.increment_views()
        db.commit()

        return {
            "message": "게시글 상세 정보를 성공적으로 조회했습니다",
            "post": post.to_json()
        }

    @staticmethod
    def updatePost(post_id: int, request: UpdatePostRequest, db: Session):
        post = db.query(Post).filter(Post.post_id == post_id).first()
        if not post:
            raise HTTPException(
                status_code=404,
                detail="게시글을 찾을 수 없습니다"
            )

        if post.author_email != request.email:
            raise HTTPException(
                status_code=403,
                detail="본인의 게시글만 수정할 수 있습니다"
            )

        post.update(request.title, request.content, request.post_image)
        db.commit()
        db.refresh(post)

        return {
            "message": "게시글을 성공적으로 수정했습니다",
            "post": post.to_json()
        }

    @staticmethod
    def deletePost(post_id: int, email: str, db: Session):
        post = db.query(Post).filter(Post.post_id == post_id).first()
        if not post:
            raise HTTPException(
                status_code=404,
                detail="게시글을 찾을 수 없습니다"
            )

        if post.author_email != email:
            raise HTTPException(
                status_code=403,
                detail="본인의 게시글만 삭제할 수 있습니다"
            )

        db.delete(post)
        db.commit()

        return {"message": "게시글을 성공적으로 삭제했습니다"}
