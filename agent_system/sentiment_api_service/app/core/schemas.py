from pydantic import BaseModel
from typing import List

class TextRequest(BaseModel):
    text: str


class BatchTextRequest(BaseModel):
    texts: List[str]


class SentimentResponse(BaseModel):
    model_output: str
    confidence_score: float
