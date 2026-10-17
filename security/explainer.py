import json
import os

import boto3


REGION = os.getenv("AWS_REGION", "us-west-2")
PROFILE = os.getenv("AWS_PROFILE", "agentshield")
MODEL_ID = os.getenv("BEDROCK_MODEL_ID", "")


def explain_decision(action: str, environment: str, decision: str) -> str:
    if not MODEL_ID:
        return "Set BEDROCK_MODEL_ID to a model available to your AWS account."

    session = boto3.Session(
        profile_name=PROFILE,
        region_name=REGION,
    )
    client = session.client("bedrock-runtime")

    prompt = f"""
You are the explanation component of AgentShield AI.
Explain the security decision briefly and clearly.
Do not change the decision or authorize an action.

Action: {action}
Environment: {environment}
Enforced decision: {decision}

Explain why this decision is appropriate in 2-3 sentences.
"""

    response = client.converse(
        modelId=MODEL_ID,
        messages=[
            {
                "role": "user",
                "content": [{"text": prompt}],
            }
        ],
        inferenceConfig={"maxTokens": 180, "temperature": 0.2},
    )

    return response["output"]["message"]["content"][0]["text"]
