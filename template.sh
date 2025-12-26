#!/bin/bash

# Exit immediately if something fails
set -e

echo "Creating LLM Council internal structure..."

touch main.py
touch config.py
touch decision_schema.py

# Agents
mkdir -p agents
touch agents/__init__.py
touch agents/base.py
touch agents/generator.py
touch agents/judge.py

# Council
mkdir -p council
touch council/__init__.py
touch council/orchestrator.py

# Safety
mkdir -p safety
touch safety/__init__.py
touch safety/gate.py

# Audit
mkdir -p audit
touch audit/__init__.py
touch audit/logger.py

echo "LLM Council structure created successfully."
