SEVERITY = {"low": 20, "medium": 40, "high": 60, "critical": 80}
CRITICALITY = {"low": 0, "medium": 5, "high": 10, "critical": 15}

def calculate_risk(alert):
    score = SEVERITY[alert["severity"]] + CRITICALITY.get(alert["asset_criticality"], 5)
    if alert["internet_exposed"]:
        score += 15
    if alert["known_exploited"]:
        score += 15
    if alert["privileged_account"]:
        score += 10
    score = min(score, 100)
    if score >= 85:
        priority = "critical"
    elif score >= 65:
        priority = "high"
    elif score >= 40:
        priority = "medium"
    else:
        priority = "low"
    return score, priority
