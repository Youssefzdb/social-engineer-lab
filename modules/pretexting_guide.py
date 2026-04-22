#!/usr/bin/env python3
"""Pretexting Awareness Guide - Know the red flags"""

class PretextingGuide:
    def get_indicators(self):
        return {
            "common_pretexts": [
                {"scenario": "IT Support Call", "red_flags": ["Asks for password", "Claims urgent issue", "Requests remote access without ticket"]},
                {"scenario": "CEO Fraud / BEC", "red_flags": ["Unusual wire transfer request", "Bypass normal process", "Marked urgent/confidential"]},
                {"scenario": "Vendor Impersonation", "red_flags": ["New bank account details", "Unusual invoice", "Different email domain"]},
                {"scenario": "Survey / Research", "red_flags": ["Asks for credentials under guise of research", "Too many personal questions"]},
            ],
            "defense_tips": [
                "Always verify caller identity through official channels",
                "Never share passwords — IT will never ask for them",
                "Call back on known numbers, not numbers provided by caller",
                "Follow change management procedures — no exceptions",
                "When in doubt, escalate to security team",
            ]
        }
