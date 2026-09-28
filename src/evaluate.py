REQUIRED_NORMALIZED_FIELDS = {"id", "source", "event_type", "asset", "severity", "description"}
REQUIRED_RESULT_FIELDS = {
    "id", "source", "asset", "normalized_alert", "risk_score", "priority",
    "attack_mapping", "recommendation", "human_review_required", "automatic_remediation"
}

def evaluate(results, expected):
    by_id = {r["id"]: r for r in results}
    total = len(expected)
    processed = 0
    normalized = 0
    priority_matches = 0
    mapping_total = 0
    mapping_matches = 0
    review_matches = 0
    captured = 0
    details = []

    for exp in expected:
        actual = by_id.get(exp["id"])
        processed_ok = actual is not None
        processed += int(processed_ok)
        if not processed_ok:
            details.append({"id": exp["id"], "processed": False, "normalization_required_fields": False,
                            "priority_match": False, "attack_mapping_match": False,
                            "human_review_enforced": False, "result_captured": False})
            if exp.get("expected_attack_id"):
                mapping_total += 1
            continue

        normalized_ok = REQUIRED_NORMALIZED_FIELDS.issubset(actual.get("normalized_alert", {}))
        normalized += int(normalized_ok)
        p_ok = actual.get("priority") == exp["expected_priority"]
        priority_matches += int(p_ok)
        r_ok = actual.get("human_review_required") is True and actual.get("automatic_remediation") is False
        review_matches += int(r_ok)
        captured_ok = REQUIRED_RESULT_FIELDS.issubset(actual)
        captured += int(captured_ok)

        m_ok = True
        if exp.get("expected_attack_id"):
            mapping_total += 1
            mapping = actual.get("attack_mapping")
            m_ok = bool(mapping) and mapping.get("technique_id") == exp["expected_attack_id"]
            mapping_matches += int(m_ok)

        details.append({"id": exp["id"], "processed": processed_ok,
                        "normalization_required_fields": normalized_ok, "priority_match": p_ok,
                        "attack_mapping_match": m_ok, "human_review_enforced": r_ok,
                        "result_captured": captured_ok})

    pct = lambda a, b: round((a / b) * 100, 1) if b else 100.0
    kpis = {
        "valid_alert_processing_pct": pct(processed, total),
        "normalization_required_fields_pct": pct(normalized, total),
        "priority_accuracy_pct": pct(priority_matches, total),
        "attack_mapping_accuracy_pct": pct(mapping_matches, mapping_total),
        "human_review_enforcement_pct": pct(review_matches, total),
        "logging_results_capture_pct": pct(captured, total),
    }
    acceptance = {
        "valid_alert_processing": kpis["valid_alert_processing_pct"] == 100.0,
        "normalization_accuracy": kpis["normalization_required_fields_pct"] >= 95.0,
        "priority_accuracy": kpis["priority_accuracy_pct"] >= 90.0,
        "attack_mapping_accuracy": kpis["attack_mapping_accuracy_pct"] >= 90.0,
        "human_review_enforcement": kpis["human_review_enforcement_pct"] == 100.0,
        "logging_results_capture": kpis["logging_results_capture_pct"] == 100.0,
    }
    return {"kpis": kpis, "acceptance": acceptance,
            "all_acceptance_criteria_met": all(acceptance.values()), "test_details": details}
