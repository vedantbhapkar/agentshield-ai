# Agent Action Guardrails Decision Pattern

## Purpose

Evaluate AI-agent actions before they reach protected tools.

## Possible outcomes

- ALLOW
- DENY
- REQUIRE_APPROVAL

## Workflow

1. Receive the requested action and environment.
2. Validate the inputs.
3. Apply deterministic security policies.
4. Use Strands Decider 2B for additional classification when available.
5. Never allow model output to override a mandatory policy denial.
6. Require human approval before protected production actions.
7. Record decisions in an audit log.
8. Fail safely if the decision service is unavailable.

## Example policies

- Read application logs: ALLOW.
- View service health: ALLOW.
- Export customer database: DENY.
- Delete customer data: DENY.
- Deploy to production: REQUIRE_APPROVAL.
- Restart a production service: REQUIRE_APPROVAL.
- Unknown actions: DENY.

## Implementation status

Live Decider integration, human approval, and real tool-execution enforcement remain to be implemented and tested.
