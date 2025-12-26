from agents.generator import GeneratorAgent
from agents.judge import JudgeAgent
from council.orchestrator import Council
from safety.gate import input_safe


def main():
    query = "Should we approve deploying this AI model?"

    if not input_safe(query):
        print("Input rejected by safety gate")
        return

    generators = [
        GeneratorAgent("Agent-A", "Analyst"),
        GeneratorAgent("Agent-B", "Researcher"),
        GeneratorAgent("Agent-C", "Pragmatist"),
    ]

    judges = [
        JudgeAgent("Judge-1", "Quality"),
        JudgeAgent("Judge-2", "Risk"),
    ]

    council = Council(generators, judges)
    decision = council.decide(query)

    print("\nFINAL DECISION")
    print(decision.model_dump_json(indent=2))

if __name__ == "__main__":
    main()
