#!/usr/bin/env python3
"""
Phishing Simulation Trainer
Generates awareness email templates for authorized security training
"""
import csv
from datetime import datetime

TEMPLATES = {
    "generic": {
        "subject": "Action Required: Verify Your Account",
        "body": """Dear {name},

We detected unusual activity on your account. Please verify your identity within 24 hours.

Click here to verify: {tracking_url}

Security Team""",
        "indicators": [
            "Urgency and time pressure",
            "Generic greeting",
            "Suspicious link",
            "Fear-based language"
        ]
    },
    "it_support": {
        "subject": "IT: Password Reset Required",
        "body": """Hi {name},

Your password expires today. Reset it immediately to avoid losing access.

Reset link: {tracking_url}

IT Department""",
        "indicators": [
            "False urgency",
            "IT impersonation",
            "Password phishing"
        ]
    },
    "invoice": {
        "subject": "Invoice #{invoice_num} - Payment Due",
        "body": """Dear {name},

Please find attached invoice #{invoice_num} for $2,847.00 due today.

View invoice: {tracking_url}

Accounts Department""",
        "indicators": [
            "Financial urgency",
            "Fake invoice",
            "Malicious attachment lure"
        ]
    }
}

class PhishingSimulator:
    def __init__(self, target_file, template_name="generic"):
        self.target_file = target_file
        self.template = TEMPLATES.get(template_name, TEMPLATES["generic"])
        self.targets = []

    def load_targets(self):
        try:
            with open(self.target_file) as f:
                reader = csv.DictReader(f)
                self.targets = list(reader)
            print(f"[+] Loaded {len(self.targets)} targets")
        except Exception as e:
            print(f"[-] Error loading targets: {e}")

    def prepare(self):
        self.load_targets()
        campaigns = []
        for i, target in enumerate(self.targets):
            tracking_id = f"trk_{i}_{datetime.now().strftime('%Y%m%d')}"
            email = self.template["body"].format(
                name=target.get("name", "User"),
                tracking_url=f"http://awareness-training.internal/track/{tracking_id}",
                invoice_num=f"INV-{2000+i}"
            )
            campaigns.append({
                "target": target.get("email", ""),
                "name": target.get("name", ""),
                "subject": self.template["subject"],
                "tracking_id": tracking_id,
                "template_indicators": self.template["indicators"]
            })
            print(f"[+] Prepared campaign for: {target.get('email','')}")
        return campaigns
