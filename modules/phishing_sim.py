#!/usr/bin/env python3
"""Phishing Simulation - Generate awareness campaign templates"""

TEMPLATES = {
    "it_support": {
        "subject": "Urgent: Password Reset Required",
        "body": "Dear {name},\n\nOur security team detected suspicious activity on your account.\nPlease reset your password immediately: {link}\n\nIT Support Team",
        "indicators": ["urgency language", "generic greeting", "suspicious link", "no personalization"]
    },
    "ceo_fraud": {
        "subject": "Quick favor needed",
        "body": "Hi {name},\n\nI need you to urgently process a wire transfer. Please keep this confidential.\nAmount: $25,000 to account: {account}\n\nCEO",
        "indicators": ["authority pressure", "urgency", "secrecy request", "financial request"]
    },
    "package_delivery": {
        "subject": "Your package could not be delivered",
        "body": "Dear customer,\n\nWe tried to deliver your package but failed.\nTrack here: {link}\n\nDelivery Service",
        "indicators": ["vague sender", "suspicious link", "no order details", "urgency"]
    }
}

class PhishingSimulator:
    def __init__(self, target_list_path):
        self.path = target_list_path

    def generate_campaign(self):
        targets = []
        try:
            with open(self.path) as f:
                targets = [l.strip() for l in f if l.strip()]
        except:
            pass

        campaigns = []
        for template_name, template in TEMPLATES.items():
            campaigns.append({
                "template": template_name,
                "subject": template["subject"],
                "target_count": len(targets),
                "red_flags": template["indicators"],
                "awareness_tips": [f"Watch for: {ind}" for ind in template["indicators"]]
            })
            print(f"[+] Campaign template: {template_name}")
        return campaigns
