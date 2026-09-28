from .triage import triage_alert

def process_alerts(alerts):
    results, errors = [], []
    for raw in alerts:
        try:
            results.append(triage_alert(raw))
        except (ValueError, KeyError, TypeError) as exc:
            errors.append({
                "id": str(raw.get("id", "unknown")),
                "status": "rejected",
                "error": str(exc),
            })
    return results, errors
