import json
from pathlib import Path
from .processor import process_alerts
from .evaluate import evaluate
ROOT = Path(__file__).resolve().parents[1]

def load(name):
    return json.loads((ROOT / "data" / name).read_text())

def main():
    alerts = load("sample_alerts.json")
    invalid_alerts = load("invalid_alerts.json")
    expected = load("expected_results.json")
    results, valid_errors = process_alerts(alerts)
    _, negative_test_errors = process_alerts(invalid_alerts)
    evaluation = evaluate(results, expected)
    (ROOT / "output").mkdir(exist_ok=True)
    (ROOT / "output" / "triage_results.json").write_text(json.dumps(results, indent=2))
    (ROOT / "output" / "evaluation_results.json").write_text(json.dumps(evaluation, indent=2))
    (ROOT / "output" / "processing_errors.json").write_text(json.dumps({
        "valid_input_errors": valid_errors,
        "negative_test_rejections": negative_test_errors
    }, indent=2))
    print(f"Processed {len(results)} of {len(alerts)} valid simulated alerts")
    print(f"Rejected {len(negative_test_errors)} of {len(invalid_alerts)} intentionally invalid test alerts")
    for k, v in evaluation["kpis"].items():
        print(f"{k}: {v}")
    print(f"All acceptance criteria met: {evaluation['all_acceptance_criteria_met']}")

if __name__ == "__main__":
    main()
