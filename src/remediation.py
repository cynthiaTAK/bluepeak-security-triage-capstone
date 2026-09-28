def recommendation(alert, priority):
    source = alert["source"]
    if source == "vulnerability":
        action = "Validate the finding, confirm affected asset exposure, prioritize patching or mitigation, and rescan after remediation."
    elif source == "identity":
        action = "Validate the authentication context, review account activity and privilege, contain if compromise is confirmed, and document analyst findings."
    else:
        action = "Investigate correlated security telemetry, validate the event, contain confirmed malicious activity, and document analyst findings."
    if priority == "critical":
        action = "Escalate for immediate analyst review. " + action
    return action
