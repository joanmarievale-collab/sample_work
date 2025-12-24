from sentiment_tool import SentimentTool
from llm import AgentLLM

class SupportAgent:
    def __init__(self):
        self.sentiment_tool = SentimentTool()
        self.llm = AgentLLM()

    def decide_action(self, sentiment: str, confidence: float) -> str:
        if sentiment == "negative" and confidence >= 80:
            return "escalate_to_support"
        if sentiment == "positive" and confidence >= 70:
            return "acknowledge_and_close"
        return "ask_clarifying_question"

    def response_text(self, action: str) -> str:
        return {
            "escalate_to_support": "I'm escalating this to our support team right now.",
            "ask_clarifying_question": "Could you tell me more so I can help you better?",
            "acknowledge_and_close": "Thanks for the feedback! Let us know if you need anything else."
        }[action]

    def handle(self, message: str) -> dict:
        sentiment_result = self.sentiment_tool.analyze(message)

        sentiment = sentiment_result["model_output"]
        confidence = sentiment_result["confidence_score"]

        action = self.decide_action(sentiment, confidence)

        reasoning = self.llm.reason(sentiment, confidence, message)

        return {
            "sentiment": sentiment,
            "confidence_score": confidence,
            "action": action,
            "reasoning": reasoning,
            "next_message": self.response_text(action)
        }
