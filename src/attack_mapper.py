MAPPINGS = {
    "password_guessing_then_success": {"technique_id": "T1110.001", "technique": "Password Guessing"},
    "malicious_file_execution": {"technique_id": "T1204.002", "technique": "Malicious File"},
    "suspicious_powershell": {"technique_id": "T1059.001", "technique": "PowerShell"},
    "credential_misuse": {"technique_id": "T1078", "technique": "Valid Accounts"},
    "exploit_privilege_escalation": {"technique_id": "T1068", "technique": "Exploitation for Privilege Escalation"},
}

def map_attack(alert):
    return MAPPINGS.get(alert["event_type"])
