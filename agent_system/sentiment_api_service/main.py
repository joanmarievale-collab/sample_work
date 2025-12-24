from fastapi import FastAPI
from app.api.sentiment_router import router as sentiment_router

app = FastAPI()
app.include_router(sentiment_router)
