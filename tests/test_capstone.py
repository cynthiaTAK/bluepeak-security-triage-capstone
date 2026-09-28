import json, unittest
from pathlib import Path
from src.triage import triage_alert
from src.alert_normalizer import normalize_alert
from src.processor import process_alerts
from src.evaluate import evaluate
ROOT = Path(__file__).resolve().parents[1]
ALERTS = json.loads((ROOT/"data/sample_alerts.json").read_text())
INVALID = json.loads((ROOT/"data/invalid_alerts.json").read_text())
EXPECTED = json.loads((ROOT/"data/expected_results.json").read_text())

class BluePeakTests(unittest.TestCase):
    def test_all_valid_alerts_normalize(self):
        for alert in ALERTS:
            n = normalize_alert(alert)
            self.assertTrue({"id","source","event_type","asset","severity","description"}.issubset(n))

    def test_missing_required_field_rejected(self):
        bad = dict(ALERTS[0]); bad.pop("asset")
        with self.assertRaises(ValueError):
            normalize_alert(bad)

    def test_invalid_alerts_fail_safely_and_are_recorded(self):
        results, errors = process_alerts(INVALID)
        self.assertEqual(results, [])
        self.assertEqual(len(errors), len(INVALID))
        for error in errors:
            self.assertEqual(error["status"], "rejected")
            self.assertTrue(error["error"])

    def test_expected_priorities(self):
        results = {a["id"]: triage_alert(a) for a in ALERTS}
        for exp in EXPECTED:
            self.assertEqual(results[exp["id"]]["priority"], exp["expected_priority"])

    def test_expected_attack_mappings(self):
        results = {a["id"]: triage_alert(a) for a in ALERTS}
        for exp in EXPECTED:
            if exp.get("expected_attack_id"):
                self.assertEqual(results[exp["id"]]["attack_mapping"]["technique_id"], exp["expected_attack_id"])

    def test_human_review_always_required(self):
        for alert in ALERTS:
            result = triage_alert(alert)
            self.assertTrue(result["human_review_required"])
            self.assertFalse(result["automatic_remediation"])

    def test_kpis_are_derived_from_results(self):
        results = [triage_alert(a) for a in ALERTS]
        report = evaluate(results[:-1], EXPECTED)
        self.assertLess(report["kpis"]["valid_alert_processing_pct"], 100.0)
        self.assertLess(report["kpis"]["normalization_required_fields_pct"], 100.0)
        self.assertLess(report["kpis"]["logging_results_capture_pct"], 100.0)

    def test_acceptance_criteria(self):
        results = [triage_alert(a) for a in ALERTS]
        report = evaluate(results, EXPECTED)
        self.assertTrue(report["all_acceptance_criteria_met"])

if __name__ == "__main__": unittest.main()
