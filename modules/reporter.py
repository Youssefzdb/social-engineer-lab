#!/usr/bin/env python3
"""SE Reporter"""
import json
from datetime import datetime

class SEReporter:
    def __init__(self, results):
        self.results = results

    def save(self, filename):
        report = {
            "tool": "social-engineer-lab v1.0",
            "generated": datetime.now().isoformat(),
            "results": self.results
        }
        with open(filename, "w") as f:
            json.dump(report, f, indent=2)
