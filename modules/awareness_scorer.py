#!/usr/bin/env python3
"""Awareness Scorer - Score employee phishing awareness"""
import json

class AwarenessScorer:
    def __init__(self, results_path):
        self.path = results_path

    def score(self):
        try:
            with open(self.path) as f:
                data = json.load(f)

            total = data.get("sent", 0)
            clicked = data.get("clicked", 0)
            reported = data.get("reported", 0)

            if total == 0:
                return {"error": "No data"}

            click_rate = (clicked / total) * 100
            report_rate = (reported / total) * 100
            awareness_score = max(0, 100 - click_rate + report_rate)

            level = "POOR" if awareness_score < 40 else "FAIR" if awareness_score < 70 else "GOOD"

            print(f"[+] Awareness Score: {awareness_score:.1f}/100 ({level})")
            print(f"[*] Click rate: {click_rate:.1f}% | Report rate: {report_rate:.1f}%")

            return {
                "total_targets": total,
                "click_rate": round(click_rate, 2),
                "report_rate": round(report_rate, 2),
                "awareness_score": round(awareness_score, 2),
                "level": level
            }
        except Exception as e:
            return {"error": str(e)}
