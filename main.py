#!/usr/bin/env python3
"""
social-engineer-lab - Security Awareness & Phishing Simulation Framework
For internal awareness training and security education ONLY
"""
import argparse
from modules.phishing_sim import PhishingSimulator
from modules.awareness_trainer import AwarenessTrainer
from modules.report import SEReport

def main():
    parser = argparse.ArgumentParser(description="Social Engineering Awareness Lab")
    parser.add_argument("--mode", choices=["simulate", "train", "analyze"], default="train")
    parser.add_argument("--target-file", help="CSV file with target users (for authorized simulations)")
    parser.add_argument("--template", default="generic", help="Phishing template name")
    parser.add_argument("--output", default="se_report.html")
    args = parser.parse_args()

    print(f"[*] Social Engineer Lab | mode: {args.mode}")
    print("[!] WARNING: Use only on systems/users you have WRITTEN AUTHORIZATION for")

    results = {}

    if args.mode == "train":
        trainer = AwarenessTrainer()
        results["training"] = trainer.run()
    elif args.mode == "simulate" and args.target_file:
        sim = PhishingSimulator(args.target_file, args.template)
        results["simulation"] = sim.prepare()
    elif args.mode == "analyze":
        trainer = AwarenessTrainer()
        results["analysis"] = trainer.analyze_awareness()

    SEReport(results).save(args.output)
    print(f"[+] Report: {args.output}")

if __name__ == "__main__":
    main()
