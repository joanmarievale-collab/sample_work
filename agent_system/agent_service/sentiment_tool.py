import os
import requests

HOST = os.getenv("SENTIMENT_AGENT_HOST", "localhost")
PORT = os.getenv("SENTIMENT_AGENT_PORT", "8001")

SENTIMENT_API_URL = f"http://{HOST}:{PORT}/sentiment/predict"


class SentimentTool:
    def analyze(self, text: str) -> dict:
        response = requests.post(
            SENTIMENT_API_URL,
            json={"text": text},
            timeout=5
        )
        response.raise_for_status()
        return response.json()
