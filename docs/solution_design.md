# Solution Design

The prototype models three simulated security sources: SIEM, vulnerability management, and identity security. Alerts are normalized into a shared JSON structure, scored with deterministic rules, prioritized, mapped to MITRE ATT&CK where applicable, and provided with investigation/remediation decision support. Every result requires human review and automatic remediation is disabled.
