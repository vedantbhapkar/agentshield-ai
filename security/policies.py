from enum import Enum


class Decision(str, Enum):
    ALLOW = "ALLOW"
    DENY = "DENY"
    REQUIRE_APPROVAL = "REQUIRE_APPROVAL"


def evaluate_action(
    action: str,
    environment: str = "dev",
) -> Decision:
    action = action.strip().lower()
    environment = environment.strip().lower()

    # Block dangerous data operations in every environment.
    if action in {
        "export_customer_database",
        "delete_customer_data",
    }:
        return Decision.DENY

    # Production changes require human approval.
    if action in {"restart_service", "deploy_release"}:
        if environment == "prod":
            return Decision.REQUIRE_APPROVAL
        if environment in {"dev", "test", "staging"}:
            return Decision.ALLOW

    # Permit read-only actions.
    if action in {
        "read_application_logs",
        "view_health_status",
    }:
        return Decision.ALLOW

    # Unknown actions or environments fail closed.
    return Decision.DENY
