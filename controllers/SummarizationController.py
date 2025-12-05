from fastapi import HTTPException
from transformers import pipeline
from controllers.PostController import postDatabase
from schemas.SummarizationSchema import SummarizeRequest, SummarizePostRequest

# KoBART 요약 모델 초기화 (lazy loading)
summarizer = None

def get_summarizer():
    global summarizer
    if summarizer is None:
        try:
            # KoBART 한국어 요약 모델 로드
            summarizer = pipeline(
                "summarization",
                model="gogamza/kobart-summarization",
                device=-1  # CPU 사용 (-1), GPU 사용 시 0
            )
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"요약 모델을 로드하는데 실패했습니다: {str(e)}"
            )
    return summarizer

class SummarizationController:
    @staticmethod
    def summarize_text(request: SummarizeRequest):
        """
        일반 텍스트 요약 API
        """
        try:
            model = get_summarizer()

            # 요약 생성
            summary = model(
                request.text,
                max_length=request.max_length,
                min_length=request.min_length,
                do_sample=False
            )

            return {
                "message": "텍스트 요약이 완료되었습니다",
                "original_text": request.text,
                "summary": summary[0]['summary_text'],
                "original_length": len(request.text),
                "summary_length": len(summary[0]['summary_text'])
            }
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"요약 생성 중 오류가 발생했습니다: {str(e)}"
            )

    @staticmethod
    def summarize_post(request: SummarizePostRequest):
        """
        게시글 요약 API - post_id로 게시글을 조회하여 요약
        """
        # 게시글 존재 여부 확인
        if request.post_id not in postDatabase:
            raise HTTPException(
                status_code=404,
                detail="게시글을 찾을 수 없습니다"
            )

        post = postDatabase[request.post_id]

        # 제목과 내용을 합쳐서 요약
        full_text = f"{post.title}. {post.content}"

        try:
            model = get_summarizer()

            # 요약 생성
            summary = model(
                full_text,
                max_length=request.max_length,
                min_length=request.min_length,
                do_sample=False
            )

            return {
                "message": "게시글 요약이 완료되었습니다",
                "post_id": request.post_id,
                "post_title": post.title,
                "original_content": post.content,
                "summary": summary[0]['summary_text'],
                "original_length": len(full_text),
                "summary_length": len(summary[0]['summary_text'])
            }
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"게시글 요약 생성 중 오류가 발생했습니다: {str(e)}"
            )

    @staticmethod
    def summarize_all_posts():
        """
        모든 게시글 요약 - 게시글 목록을 조회하면서 간단한 요약 제공
        """
        if not postDatabase:
            return {
                "message": "요약할 게시글이 없습니다",
                "summaries": []
            }

        try:
            model = get_summarizer()
            summaries = []

            for post_id, post in postDatabase.items():
                full_text = f"{post.title}. {post.content}"

                # 짧은 요약 생성
                summary = model(
                    full_text,
                    max_length=100,
                    min_length=30,
                    do_sample=False
                )

                summaries.append({
                    "post_id": post_id,
                    "title": post.title,
                    "author_email": post.author_email,
                    "summary": summary[0]['summary_text'],
                    "views": post.views,
                    "likes": post.likes,
                    "created_at": post.createdAt
                })

            return {
                "message": "모든 게시글 요약이 완료되었습니다",
                "total": len(summaries),
                "summaries": summaries
            }
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"전체 게시글 요약 생성 중 오류가 발생했습니다: {str(e)}"
            )
