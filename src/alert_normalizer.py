REQUIRED = {"id", "source", "event_type", "asset", "severity", "description"}
VALID_SOURCES = {"siem", "vulnerability", "identity"}
VALID_SEVERITIES = {"low", "medium", "high", "critical"}

def normalize_alert(alert):
    missing = sorted(REQUIRED - set(alert))
    if missing:
        raise ValueError(f"Missing required fields: {', '.join(missing)}")
    source = str(alert["source"]).strip().lower()
    severity = str(alert["severity"]).strip().lower()
    if source not in VALID_SOURCES:
        raise ValueError(f"Unsupported source: {source}")
    if severity not in VALID_SEVERITIES:
        raise ValueError(f"Unsupported severity: {severity}")
    return {
        "id": str(alert["id"]),
        "source": source,
        "event_type": str(alert["event_type"]).strip().lower(),
        "asset": str(alert["asset"]),
        "severity": severity,
        "description": str(alert["description"]),
        "asset_criticality": str(alert.get("asset_criticality", "medium")).lower(),
        "internet_exposed": bool(alert.get("internet_exposed", False)),
        "known_exploited": bool(alert.get("known_exploited", False)),
        "privileged_account": bool(alert.get("privileged_account", False)),
    }
