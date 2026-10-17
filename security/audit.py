import json
from datetime import datetime, timezone
from pathlib import Path

AUDIT_FILE = Path("audit_logs/decisions.jsonl")

def log_decision(result: dict) -> None:
    AUDIT_FILE.parent.mkdir(parents=True, exist_ok=True)

    record = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "action": result["action"],
        "environment": result["environment"],
        "decision": result["decision"],
        "explanation": result["explanation"],
    }

    with AUDIT_FILE.open("a", encoding="utf-8") as file:
        file.write(json.dumps(record) + "\n")
