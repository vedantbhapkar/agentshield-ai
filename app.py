import json
from pathlib import Path

import streamlit as st

from security.agent import assess_action
from security.audit import log_decision

AUDIT_FILE = Path("audit_logs/decisions.jsonl")

st.set_page_config(
    page_title="AgentShield AI",
    page_icon="🛡️",
    layout="wide",
)

st.title("🛡️ AgentShield AI")
st.caption("AI Agent Security Gateway | Policy Enforcement and Audit")

st.warning(
    "Demo mode: actions are evaluated only. "
    "No real database exports, deletions, or deployments are executed."
)

with st.form("security_check"):
    action = st.selectbox(
        "Select action",
        [
            "read_application_logs",
            "view_health_status",
            "export_customer_database",
            "delete_customer_data",
            "restart_service",
            "deploy_release",
            "unknown_action",
        ],
    )

    environment = st.selectbox(
        "Environment",
        ["dev", "test", "staging", "prod"],
        index=3,
    )

    submitted = st.form_submit_button("Evaluate security policy")

if submitted:
    try:
        with st.spinner("Evaluating policy and generating explanation..."):
            result = assess_action(action, environment)
            log_decision(result)

        st.subheader("Security decision")

        if result["decision"] == "ALLOW":
            st.success("ALLOW")
        elif result["decision"] == "DENY":
            st.error("DENY")
        else:
            st.warning("REQUIRE APPROVAL")

        st.write("**Action:**", result["action"])
        st.write("**Environment:**", result["environment"])
        st.write("**Explanation:**", result["explanation"])

    except Exception as exc:
        st.error(f"Evaluation failed: {exc}")

st.divider()
st.subheader("Audit history")

if AUDIT_FILE.exists():
    records = []

    with AUDIT_FILE.open(encoding="utf-8") as file:
        for line in file:
            try:
                records.append(json.loads(line))
            except json.JSONDecodeError:
                continue

    if records:
        st.metric("Recorded decisions", len(records))
        st.dataframe(
            list(reversed(records)),
            use_container_width=True,
        )
    else:
        st.info("No audit records yet.")
else:
    st.info("No audit records yet. Evaluate an action to create one.")
