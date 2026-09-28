# Formative Defect Log

## F-001 — Internet-exposed medium vulnerability under-prioritized
- Scenario: `BP-VULN-003`
- Expected priority: High
- Initial actual result: Medium (risk score 60)
- Cause: The initial exposure weight (+10) did not elevate a medium-severity finding on a high-criticality, internet-exposed asset to the predefined High threshold.
- Corrective action: Increased the deterministic internet-exposure weight from +10 to +15.
- Retest: Passed. The scenario now scores 65 and is classified High.
- Scope note: The change is a student-created prototype scoring rule for the simulated BluePeak environment; it is not presented as an industry-standard risk formula.

## F-002 — Expected result did not reflect the documented scoring rule after F-001
- Scenario: `BP-SIEM-005`
- Initial expected priority: High
- Actual after the F-001 exposure-weight correction: Critical (risk score 85)
- Cause: The expected-results fixture had not been updated to reflect the same predefined scoring rule applied to all internet-exposed alerts.
- Corrective action: Corrected the expected result to Critical rather than weakening the scoring rule for this one scenario.
- Retest: Passed.
