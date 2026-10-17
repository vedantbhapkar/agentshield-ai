from security.agent import assess_action
from security.audit import log_decision

actions = [
    ("read_application_logs", "dev"),
    ("export_customer_database", "prod"),
    ("deploy_release", "prod"),
    ("restart_service", "staging"),
    ("unknown_action", "dev"),
]

for action, environment in actions:
    result = assess_action(action, environment)
    log_decision(result)

    print("\n===== AgentShield AI =====")
    print("Action:", result["action"])
    print("Environment:", result["environment"])
    print("Decision:", result["decision"])
    print("Explanation:", result["explanation"])

print("\nAudit records saved to audit_logs/decisions.jsonl")
