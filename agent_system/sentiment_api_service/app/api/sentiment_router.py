from fastapi import APIRouter
from app.core.model import SentimentService
from app.core.schemas import (
    TextRequest,
    BatchTextRequest,
    SentimentResponse
)

router = APIRouter(prefix="/sentiment", tags=["Sentiment"])

sentiment_service = SentimentService()


@router.get("/health")
def health_check():
    return {"status": "ok"}


@router.post("/predict", response_model=SentimentResponse)
def predict(request: TextRequest):
    return sentiment_service.predict(request.text)


@router.post("/predict-batch")
def predict_batch(request: BatchTextRequest):
    return [
        sentiment_service.predict(text)
        for text in request.texts
    ]
