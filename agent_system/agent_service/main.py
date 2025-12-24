from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import logging
from dotenv import load_dotenv
import os

load_dotenv()
from agent import SupportAgent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

app = FastAPI(
    title="Support Agent API",
    description="AI-powered customer support agent",
    version="1.0.0"
)

agent = SupportAgent()

class AgentRequest(BaseModel):
    user_id: str
    message: str

class AgentResponse(BaseModel):
    sentiment: str
    confidence_score: float
    action: str
    reasoning: str
    next_message: str

@app.get("/health")
def health():
    return {"status": "ok"}

@app.post("/agent/run", response_model=AgentResponse)
def run_agent(request: AgentRequest):
    try:
        logger.info(f"Processing message from {request.user_id}: {request.message}")
        
        result = agent.handle(request.message)
        
        return AgentResponse(
            sentiment=result["sentiment"],
            confidence_score=result["confidence_score"],
            action=result["action"],
            reasoning=result["reasoning"],
            next_message=result["next_message"]
        )
    except Exception as e:
        logger.error(f"Error processing agent request: {e}", exc_info=True)
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8001)
