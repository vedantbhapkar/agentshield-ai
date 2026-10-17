import os
from openai import OpenAI

key = os.environ.get("BEDROCK_API_KEY")
if not key:
    raise SystemExit("ERROR: BEDROCK_API_KEY is missing")

client = OpenAI(
    api_key=key,
    base_url="https://bedrock-mantle.us-west-2.api.aws/v1",
)

response = client.chat.completions.create(
    model="qwen.qwen3-vl-235b-a22b-instruct",
    messages=[
        {
            "role": "user",
            "content": "Explain in two sentences why an AI agent should block an unauthorized customer database export."
        }
    ],
    max_tokens=100,
)

print(response.choices[0].message.content)
