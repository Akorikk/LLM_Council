from agents.base import BaseAgent


class GeneratorAgent(BaseAgent):
    def run(self, input_text: str):
        # Placeholder logic (LLM call comes later)
        return {
            "agent": self.name,
            "answer": f"[{self.role}] analysis of: {input_text}",
            "confidence": 0.7
        }
