from security.policies import Decision, evaluate_action


def test_safe_action_is_allowed():
    assert evaluate_action("read_application_logs") == Decision.ALLOW


def test_database_export_is_denied():
    assert evaluate_action("export_customer_database") == Decision.DENY


def test_production_deployment_requires_approval():
    assert evaluate_action("deploy_release", "prod") == Decision.REQUIRE_APPROVAL


def test_unknown_action_is_denied():
    assert evaluate_action("unknown_action") == Decision.DENY


def test_development_restart_is_allowed():
    assert evaluate_action("restart_service", "dev") == Decision.ALLOW
