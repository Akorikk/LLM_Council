from agents.base import BaseAgent


class JudgeAgent(BaseAgent):
    def run(self, answers: list):
        # Minimal rubric-based evaluation
        scores = []
        for ans in answers:
            scores.append({
                "agent": ans["agent"],
                "accuracy": 0.7,
                "grounding": 0.6,
                "risk": 0.3,
                "clarity": 0.8
            })

        return {
            "judge": self.name,
            "scores": scores,
            "comment": "Evaluation completed"
        }
