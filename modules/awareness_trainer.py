#!/usr/bin/env python3
"""
Security Awareness Trainer
Teaches users how to identify social engineering attacks
"""

PHISHING_INDICATORS = {
    "Urgency / Fear": [
        "Act now or your account will be closed",
        "Verify within 24 hours",
        "Your account has been compromised",
        "Immediate action required"
    ],
    "Suspicious Sender": [
        "Email from free domains (gmail/yahoo) claiming to be a company",
        "Slight misspelling: paypa1.com vs paypal.com",
        "Display name doesn't match email address"
    ],
    "Suspicious Links": [
        "Hover over links — check URL before clicking",
        "Shortened URLs hiding destination",
        "HTTP instead of HTTPS",
        "URL doesn't match the displayed company"
    ],
    "Attachment Tricks": [
        "Unexpected invoice/document attachments",
        "Double extensions: invoice.pdf.exe",
        "Password-protected zip files"
    ],
    "Request for Credentials": [
        "Legitimate companies never ask for passwords via email",
        "Requests to verify SSN, credit card, or password"
    ]
}

VISHING_TACTICS = [
    "Caller ID spoofing — attacker appears as trusted number",
    "Pretexting — attacker creates false scenario (IT support, bank)",
    "Voice urgency — creates panic to bypass critical thinking",
]

PRETEXTING_SCENARIOS = [
    "IT Support: 'I need your password to fix your account'",
    "CEO Fraud: 'Wire transfer this amount immediately, it's urgent'",
    "Vendor: 'We updated our banking info, please use the new account'",
]

class AwarenessTrainer:
    def run(self):
        print("[*] Running security awareness training module...")
        training_content = {
            "phishing_indicators": PHISHING_INDICATORS,
            "vishing_tactics": VISHING_TACTICS,
            "pretexting_scenarios": PRETEXTING_SCENARIOS,
            "best_practices": [
                "Always verify requests via a separate channel (phone call)",
                "Never click links in unsolicited emails — go directly to the site",
                "Report suspicious emails to your security team",
                "Enable MFA on all accounts",
                "Think before you click — slow down when pressured"
            ]
        }
        print("[+] Training content loaded")
        return training_content

    def analyze_awareness(self):
        print("[*] Analyzing common SE attack patterns...")
        return {
            "most_common_attacks": ["Spear Phishing", "BEC Fraud", "Vishing", "Smishing"],
            "most_targeted_industries": ["Finance", "Healthcare", "Government", "Education"],
            "average_click_rate": "17% of employees click phishing links",
            "mitigation": "Regular training reduces click rates to below 5%"
        }
