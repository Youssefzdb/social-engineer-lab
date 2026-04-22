#!/usr/bin/env python3
"""Phishing Simulator - Generate awareness test templates (no real sending)"""

TEMPLATES = {
    "it_support": {
        "subject": "[IT Support] Urgent: Password Expiry Notice",
        "sender": "it-support@company-helpdesk.com",
        "body": """Dear {name},\n\nYour password will expire in 24 hours.\n
Please click the link below to reset it immediately:\n
https://company-portal-reset.com/auth?token=XYZ\n\nIT Support Team""",
        "red_flags": ["Suspicious sender domain", "Urgency tactic", "External link"]
    },
    "hr_policy": {
        "subject": "Important: Updated HR Policy - Action Required",
        "sender": "hr@company-updates.net",
        "body": """Dear {name},\n\nPlease review and sign the updated HR policy.\n
Download here: https://hr-docs-secure.com/policy.pdf\n\nHR Department""",
        "red_flags": ["Fake HR domain", "Attachment download prompt"]
    },
    "password_reset": {
        "subject": "Security Alert: Unusual login detected",
        "sender": "security@accounts-verify.com",
        "body": """We detected unusual login activity.\n
Verify your account: https://accounts-verify.com/secure\n\nSecurity Team""",
        "red_flags": ["Generic greeting", "Fake security domain", "Fear tactic"]
    },
    "invoice": {
        "subject": "Invoice #INV-2024-0892 - Payment Required",
        "sender": "billing@invoices-portal.com",
        "body": """Please find attached invoice #INV-2024-0892.\n
Total due: $4,750.00\nPay now: https://billing-secure-portal.com\n\nAccounts Team""",
        "red_flags": ["Unknown vendor", "Suspicious billing domain", "Unexpected invoice"]
    }
}

class PhishingSimulator:
    def __init__(self, template_name="it_support"):
        self.template = TEMPLATES.get(template_name, TEMPLATES["it_support"])
        self.template_name = template_name

    def run(self, targets_file=None):
        targets = []
        if targets_file:
            try:
                import csv
                with open(targets_file) as f:
                    reader = csv.DictReader(f)
                    targets = list(reader)
            except:
                targets = [{"name": "Demo User", "email": "user@example.com"}]
        else:
            targets = [{"name": "Demo User", "email": "user@example.com"}]

        print(f"[*] Phishing simulation: {self.template_name}")
        print(f"[*] Template subject: {self.template['subject']}")
        print(f"[!] Red flags in template: {', '.join(self.template['red_flags'])}")
        print(f"[*] Would target {len(targets)} users (simulation only - no emails sent)")

        return {
            "template": self.template_name,
            "subject": self.template["subject"],
            "sender": self.template["sender"],
            "red_flags": self.template["red_flags"],
            "target_count": len(targets),
            "status": "simulation_only"
        }
