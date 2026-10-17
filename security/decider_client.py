import os
import requests


def classify_security_action(action: str, environment: str) -> dict:
    base_url = os.environ.get("STRANDS_DECIDER_URL")

    if not base_url:
        raise RuntimeError(
            "STRANDS_DECIDER_URL is not set. "
            "Configure a running Strands Decider service first."
        )

    payload = {
        "state": (
            f"An AI agent requests action '{action}' "
            f"in the '{environment}' environment. "
            "Classify the security handling required."
        ),
        "model": "strands-decider-2b",
        "questions": {
            "security_decision": {
                "type": "choice",
                "instructions": (
                    "Choose the appropriate security handling "
                    "for this requested action."
                ),
                "criteria": {
                    "ALLOW": "The action is permitted.",
                    "DENY": "The action must be blocked.",
                    "REQUIRE_APPROVAL": (
                        "The action requires human approval."
                    ),
                },
            }
        },
    }

    response = requests.post(
        f"{base_url.rstrip('/')}/v1/systemone",
        json=payload,
        timeout=60,
    )
    response.raise_for_status()
    return response.json()
