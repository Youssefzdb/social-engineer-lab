#!/usr/bin/env python3
"""Awareness Training Scenarios"""

SCENARIOS = [
    {
        "id": 1,
        "title": "Suspicious Email",
        "scenario": "You receive an email saying 'Your Office 365 account will expire in 24h. Click here to verify.'",
        "correct_action": "Do NOT click. Report to IT security immediately.",
        "red_flags": ["Urgency", "Generic greeting", "Suspicious link", "Threat of account loss"],
        "category": "Phishing"
    },
    {
        "id": 2,
        "title": "IT Support Call",
        "scenario": "Someone calls claiming to be IT support, says they detected malware and need your login to fix it.",
        "correct_action": "Hang up. Call IT directly using the internal directory number.",
        "red_flags": ["Password request", "Unsolicited call", "Urgency", "Pressure tactics"],
        "category": "Vishing"
    },
    {
        "id": 3,
        "title": "USB Drop",
        "scenario": "You find a USB drive labeled 'Salary Info Q4' in the parking lot.",
        "correct_action": "Do NOT plug it in. Hand it to IT security.",
        "red_flags": ["Unknown origin", "Enticing label", "Physical bait"],
        "category": "Baiting"
    },
    {
        "id": 4,
        "title": "Tailgating",
        "scenario": "Someone in a delivery uniform asks you to hold the door to the server room.",
        "correct_action": "Politely decline. Ask them to use the reception process.",
        "red_flags": ["No badge", "Physical access request", "Social pressure"],
        "category": "Physical SE"
    }
]

class AwarenessTrainer:
    def get_scenarios(self):
        print(f"[+] Loaded {len(SCENARIOS)} training scenarios")
        return SCENARIOS
