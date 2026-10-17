from security.policies import evaluate_action
from security.explainer_qwen import explain_decision

def assess_action(action: str, environment: str = "dev") -> dict:
    decision = evaluate_action(action, environment)

    explanation = explain_decision(
        action=action,
        environment=environment,
        decision=decision.value,
    )

    return {
        "action": action,
        "environment": environment,
        "decision": decision.value,
        "explanation": explanation,
    }
