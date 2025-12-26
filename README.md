# LLM_Council

# Overview
* This repository implements a minimal, end-to-end LLM Council designed to demonstrate how AI systems can be used to make decisions, not just summarize text. This project is intentionally minimal but complete, focusing on architecture, governance, and clarity over tooling complexity. This system demonstrates an alternative approach: AI as a decision engine, where outputs are evaluated, compared, and justified with evidence.

# Project Structure and File Responsibilities
llm_council/
│
├── main.py
├── config.py
├── decision_schema.py
│
├── agents/
│   ├── base.py
│   ├── generator.py
│   └── judge.py
│
├── council/
│   └── orchestrator.py
│
├── safety/
│   └── gate.py
│
├── audit/
│   └── logger.py
│
├── requirements.txt
├── .gitignore
└── README.md

# Environment & Install dependencies

* requirements.txt
pydantic==2.6.4
python-dotenv==1.0.1
openai==1.14.3

pydantic (schema enforcement)
python-dotenv (environment management)
openai (optional, abstracted)
Pinned versions ensure reproducibility on reviewer machines.

* Python Environment Use 3.10 

# Pipeline
User Query
   ➡
Safety Gate
   ➡
Generation Council (3 Agents)
   ➡
Judge Council (2 Agents, rubric-based)
   ➡
Decision Synthesis
   ➡
Structured Decision Object
   ➡
Audit Log (JSONL)

Running the system produces one final, authoritative decision, along with a full audit trail.

# config.py
* Purpose: Central place for system-wide constants and thresholds.

* Examples:
Number of generators
Number of judges
Risk thresholds
Model identifiers (abstracted)

* Why this matters:
Prevents hardcoded “magic numbers”
Makes governance and tuning explicit
Easy to extend for production systems

# decision_schema.py
* Purpose: Defines the Decision Object, which is the final output of the system.

* What it contains:

decision (APPROVE / REJECT / NEED_MORE_INFO)
confidence (0–1)
summary (human-readable rationale)
risks (explicitly documented)
citations (which agents influenced the decision)
dissent (optional disagreements)
audit_id (traceability identifier)

* Why this matters:
Enforces structure (via Pydantic)
Prevents free-text, unverifiable outputs
Makes decisions inspectable and machine-readable

# agents/base.py
* Purpose: Abstract base class for all agents.

* Why this matters:
Enforces a consistent interface (run)
Makes it easy to add new agent types
Encourages role-based reasoning

# agents/generator.py
* Purpose: Implements generation agents.

* Current agents:
Analyst
Researcher
Pragmatist

* Each agent:
Receives the same query
Produces an independent answer
Represents a different reasoning perspective

* Why this matters:
Reduces single-model bias
Encourages diversity of thought
Mirrors how human councils work

# agents/judge.py
* Purpose: Implements judge agents that evaluate generator outputs.

* Judging rubric includes:
Accuracy
Grounding
Risk
Clarity
Judges do not generate answers they evaluate them.

* Why this matters:
Separation of generation and evaluation
Enables governance and oversight
Prevents “self-approval” by generators

# council/orchestrator.py
* Purpose: Coordinates the entire decision flow.

* Responsibilities:
Runs all generation agents
Logs generation outputs
Runs all judge agents
Logs evaluations
Synthesizes a final decision
Emits a Decision Object

* Why this matters:
Centralized control flow
Clear lifecycle from input → decision
Easy to extend with new stages


# safety/gate.py
* Purpose:Implements basic safety gating.

* Current checks:
Input validation
Length constraints
Risk threshold checks (pluggable)

* Why this matters:
Demonstrates governance awareness
Allows early rejection of unsafe inputs
Foundation for policy-based controls


# main.py 
* Purpose: Single entry point that runs the entire pipeline.

What it does:

Defines the input query
Applies safety gating
Initializes generation agents
Initializes judge agents
Runs the council orchestration
Prints the final Decision Object

Why this matters:
One command to run (python main.py)
No hidden execution paths
Easy for reviewers to test on their own machine


# audit/logger.py
* Purpose: Writes structured audit events to audit_log.jsonl.
Logged events:
Generation
Judging
Final decision

* Format:
JSON Lines (one event per line)
Timestamped
Machine-readable

* Why this matters:
Enables post-hoc inspection
Supports compliance and review
Proves how a decision was made

Note: audit_log.jsonl is a runtime artifact and intentionally excluded from version control.

# OutPut 
(council)python main.py

FINAL DECISION
{
  "decision": "APPROVE",
  "confidence": 0.82,
  "summary": "Consensus reached among generators",
  "risks": [
    "Potential hallucination"
  ],
  "citations": [
    "Agent-A",
    "Agent-B",
    "Agent-C"
  ],
  "dissent": [],
  "audit_id": "c33df82b-0406-4256-ba07-469854f1606a"
}

(council) 

* A file audit_log.jsonl is also generated locally containing the full decision trace.
