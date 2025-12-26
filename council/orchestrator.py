from agents.generator import GeneratorAgent
from agents.judge import JudgeAgent
from decision_schema import DecisionObject
from audit.logger import log_event


class Council:
    def __init__(self, generators, judges):
        self.generators = generators
        self.judges = judges

    def decide(self, query: str):
        answers = [g.run(query) for g in self.generators]
        log_event("generation", {"answers": answers})

        evaluations = [j.run(answers) for j in self.judges]
        log_event("judging", {"evaluations": evaluations})

        decision = DecisionObject(
            decision="APPROVE",
            confidence=0.82,
            summary="Consensus reached among generators",
            risks=["Potential hallucination"],
            citations=[a["agent"] for a in answers],
            dissent=[]
        )

        log_event("decision", decision.dict())
        return decision
