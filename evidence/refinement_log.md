# BluePeak Pre-Summative Refinement Log

Before the final summative run, the controlled lab was reviewed for traceability and defensibility.

1. ATT&CK scenario descriptions were tightened so the simulated evidence supports the selected technique. Generic malware execution was replaced with an explicit malicious-file execution scenario; generic privilege escalation was replaced with explicit vulnerability exploitation; repeated authentication attempts were described as password guessing.
2. ATT&CK IDs were made more specific where supported: T1110.001 and T1204.002.
3. KPI calculations for valid processing, required-field normalization, and result capture were changed from fixed values to measurements derived from actual result objects.
4. Two intentionally invalid alerts were added for negative testing. The batch processor rejects them, records the reason, and produces no risk decision for those invalid inputs.
5. Automated tests were expanded to verify safe rejection and to prove that KPI percentages decrease when a result is deliberately omitted.

The original baseline evidence was retained under `evidence/baseline/` before these refinements.
