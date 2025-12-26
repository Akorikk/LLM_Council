#!/bin/bash

# Exit on error
set -e

echo "Creating LLM Council project structure..."

# Root-level files (excluding README.md and llm_council/)
touch main.py
touch config.py
touch decision_schema.py

# Safety
mkdir -p safety
touch safety/gate.py

# Agents
mkdir -p agents
touch agents/base.py
touch agents/generator.py
touch agents/judge.py

# Council
mkdir -p council
touch council/orchestrator.py
touch council/synthesizer.py

# Audit
mkdir -p audit
touch audit/logger.py

echo "✅ Project structure created successfully."
