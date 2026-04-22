#!/usr/bin/env python3
"""
social-engineer-lab - Security Awareness Training & SE Attack Simulation
For security awareness training and authorized red team exercises ONLY
"""
import argparse
from modules.phishing_detector import PhishingDetector
from modules.pretexting_guide import PretextingGuide
from modules.awareness_trainer import AwarenessTrainer
from modules.report import SEReport

def main():
    parser = argparse.ArgumentParser(description="Social Engineering Awareness Lab")
    parser.add_argument("--mode", choices=["detect", "train", "guide", "full"], default="full")
    parser.add_argument("--email", help="Email file to analyze for phishing")
    parser.add_argument("--url", help="URL to check for phishing indicators")
    parser.add_argument("--output", default="se_report.html")
    args = parser.parse_args()

    results = {}
    print("[*] Social Engineer Lab - Awareness Training Mode")

    if args.mode in ["detect", "full"] and args.email:
        detector = PhishingDetector()
        results["phishing"] = detector.analyze_email(args.email)

    if args.mode in ["detect", "full"] and args.url:
        detector = PhishingDetector()
        results["url_check"] = detector.check_url(args.url)

    if args.mode in ["train", "full"]:
        trainer = AwarenessTrainer()
        results["training"] = trainer.get_scenarios()

    if args.mode in ["guide", "full"]:
        guide = PretextingGuide()
        results["guide"] = guide.get_indicators()

    report = SEReport(results)
    report.save(args.output)
    print(f"[+] Report saved: {args.output}")

if __name__ == "__main__":
    main()
