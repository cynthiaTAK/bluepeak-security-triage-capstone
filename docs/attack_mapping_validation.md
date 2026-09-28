# MITRE ATT&CK Mapping Validation

The BluePeak prototype maps ATT&CK techniques only when the simulated scenario contains behavior that supports the mapping. The controlled mappings used for final testing are:

- `password_guessing_then_success` → T1110.001 Password Guessing
- `malicious_file_execution` → T1204.002 Malicious File
- `suspicious_powershell` → T1059.001 PowerShell
- `credential_misuse` → T1078 Valid Accounts
- `exploit_privilege_escalation` → T1068 Exploitation for Privilege Escalation

Mappings are contextual decision-support labels for the simulated scenarios and do not independently prove adversary intent.
