from pydantic import BaseModel


class CreatePostRequest(BaseModel):
    title: str
    content: str
    postImage: str | None = None

class UpdatePostRequest(BaseModel):
    title: str
    content: str
    postImage: str | None = None

class PostController:
    @staticmethod
    def createPost(request: CreatePostRequest):
        # TODO
        return {"message": "게시글을 성공적으로 작성했습니다"}

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
