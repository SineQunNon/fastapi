from fastapi import APIRouter
from schemas.SummarizationSchema import SummarizeRequest, SummarizePostRequest
from controllers.SummarizationController import SummarizationController

router = APIRouter(prefix="/api/summarization", tags=["summarization"])


@router.post("/text", status_code=200)
async def summarize_text(request: SummarizeRequest):
    """
    일반 텍스트 요약 API

    - **text**: 요약할 텍스트 (필수)
    - **max_length**: 요약 최대 길이 (기본값: 150)
    - **min_length**: 요약 최소 길이 (기본값: 50)
    """
    return SummarizationController.summarize_text(request)


@router.post("/post", status_code=200)
async def summarize_post(request: SummarizePostRequest):
    """
    게시글 요약 API - post_id로 게시글을 조회하여 요약

    - **post_id**: 요약할 게시글 ID (필수)
    - **max_length**: 요약 최대 길이 (기본값: 150)
    - **min_length**: 요약 최소 길이 (기본값: 50)
    """
    return SummarizationController.summarize_post(request)


@router.get("/posts", status_code=200)
async def summarize_all_posts():
    """
    모든 게시글 요약 API

    모든 게시글의 제목과 내용을 요약하여 반환합니다.
    """
    return SummarizationController.summarize_all_posts()
