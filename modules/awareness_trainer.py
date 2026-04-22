#!/usr/bin/env python3
"""Awareness Trainer - Generate security awareness training material"""

TRAINING_MODULES = [
    {
        "title": "Recognizing Phishing Emails",
        "content": "Learn to spot suspicious senders, urgent language, and fake links.",
        "quiz": [
            {"q": "An email from 'it-support@company-helpdesk.net' asks you to reset your password. What do you do?",
             "a": "Contact IT directly through official channels, never click the link."},
            {"q": "You receive an invoice from an unknown vendor. What's the red flag?",
             "a": "Unexpected invoice from unknown sender — verify with finance before opening."}
        ]
    },
    {
        "title": "Social Engineering Tactics",
        "content": "Understand pretexting, baiting, quid pro quo, and tailgating attacks.",
        "quiz": [
            {"q": "Someone calls claiming to be IT and asks for your password. What do you do?",
             "a": "Never share passwords by phone. Hang up and verify through official directory."}
        ]
    },
    {
        "title": "Password Security",
        "content": "Use strong passwords, enable MFA, and never reuse passwords.",
        "quiz": [
            {"q": "Which password is strongest? abc123 / P@ssw0rd / correct-horse-battery-staple",
             "a": "correct-horse-battery-staple — long passphrases are hardest to crack."}
        ]
    }
]

class AwarenessTrainer:
    def generate_material(self):
        print(f"[+] Generating {len(TRAINING_MODULES)} training modules")
        for module in TRAINING_MODULES:
            print(f"[*] Module: {module['title']}")
        return TRAINING_MODULES
