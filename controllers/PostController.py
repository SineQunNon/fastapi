from fastapi import HTTPException
from models.Post import Post
from schemas.PostSchema import CreatePostRequest, UpdatePostRequest

postDatabase = {}
post_id_counter = 1

class PostController:
    @staticmethod
    def createPost(request: CreatePostRequest):
        global post_id_counter

        post = Post(
            post_id=post_id_counter,
            title=request.title,
            content=request.content,
            author_email=request.email,
            postImage=request.postImage
        )

        postDatabase[post_id_counter] = post
        post_id_counter += 1

        return {
            "message": "게시글을 성공적으로 작성했습니다",
            "post": post.to_json()
        }

    @staticmethod
    def getPosts():
        posts = [post.to_json() for post in postDatabase.values()]

        return {
            "message": "게시글 목록을 성공적으로 조회했습니다",
            "posts": posts,
            "total": len(posts)
        }

    @staticmethod
    def getPost(post_id: int):
        if post_id not in postDatabase:
            raise HTTPException(
                status_code=404,
                detail="게시글을 찾을 수 없습니다"
            )

        post = postDatabase[post_id]
        post.increment_views()  # 조회수 증가

        return {
            "message": "게시글 상세 정보를 성공적으로 조회했습니다",
            "post": post.to_json()
        }

    @staticmethod
    def updatePost(post_id: int, request: UpdatePostRequest):
        if post_id not in postDatabase:
            raise HTTPException(
                status_code=404,
                detail="게시글을 찾을 수 없습니다"
            )

        post = postDatabase[post_id]

        if post.author_email != request.email:
            raise HTTPException(
                status_code=403,
                detail="본인의 게시글만 수정할 수 있습니다"
            )
        post.update(request.title, request.content, request.post_image)

        return {
            "message": "게시글을 성공적으로 수정했습니다",
            "post": post.to_json()
        }

    @staticmethod
    def deletePost(post_id: int, email: str):
        if post_id not in postDatabase:
            raise HTTPException(
                status_code=404,
                detail="게시글을 찾을 수 없습니다"
            )

        post = postDatabase[post_id]

        if post.author_email != email:
            raise HTTPException(
                status_code=403,
                detail="본인의 게시글만 삭제할 수 있습니다"
            )
        del postDatabase[post_id]

        return {"message": "게시글을 성공적으로 삭제했습니다"}
