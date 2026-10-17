# AgentShield AI

An AI-agent security gateway for policy enforcement and auditing.

## Security decisions

- ALLOW: The action is permitted by policy.
- DENY: The action must be blocked.
- REQUIRE_APPROVAL: Human approval is required before execution.

## Technology stack

- Python
- Streamlit
- Strands Decider 2B
- Amazon Bedrock Mantle with Qwen
- Pytest
- JSONL audit logging

## Current features

- Deterministic security policies
- Natural-language decision explanations
- Streamlit dashboard
- JSONL audit logs
- Unit tests

## Run tests

    python -m pytest -v

## Run dashboard

    streamlit run app.py

## Security limitations

Live Strands Decider integration and human approval enforcement are still in progress. The dashboard does not execute real destructive actions.

Never commit API keys or AWS credentials.
