from .alert_normalizer import normalize_alert
from .risk_scoring import calculate_risk
from .attack_mapper import map_attack
from .remediation import recommendation
from .human_review import review_control

def triage_alert(raw):
    alert = normalize_alert(raw)
    score, priority = calculate_risk(alert)
    result = {
        "id": alert["id"],
        "source": alert["source"],
        "asset": alert["asset"],
        "normalized_alert": alert,
        "risk_score": score,
        "priority": priority,
        "attack_mapping": map_attack(alert),
        "recommendation": recommendation(alert, priority),
    }
    result.update(review_control())
    return result
