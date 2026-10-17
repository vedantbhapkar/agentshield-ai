import os
from openai import OpenAI


def explain_decision(action: str, environment: str, decision: str) -> str:
    key = os.environ.get("BEDROCK_API_KEY")
    if not key:
        raise RuntimeError("BEDROCK_API_KEY is missing")

    client = OpenAI(
        api_key=key,
        base_url="https://bedrock-mantle.us-west-2.api.aws/v1",
    )

    response = client.chat.completions.create(
        model="qwen.qwen3-vl-235b-a22b-instruct",
        messages=[
            {
                "role": "system",
                "content": (
                    "You explain security policy decisions clearly. "
                    "The supplied decision is final. Never override it. "
                    "Explain the reason in 2 or 3 concise sentences."
                ),
            },
            {
                "role": "user",
                "content": (
                    f"Action: {action}\n"
                    f"Environment: {environment}\n"
                    f"Final policy decision: {decision}\n"
                    "Explain why this decision is appropriate."
                ),
            },
        ],
        max_tokens=150,
    )

    return (
        response.choices[0].message.content
        or "No explanation returned."
    )
