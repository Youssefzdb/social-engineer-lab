#!/usr/bin/env python3
"""
social-engineer-lab - Social Engineering Simulation & Awareness Platform
Simulates phishing campaigns and measures employee security awareness
"""
import argparse
from modules.phishing_simulator import PhishingSimulator
from modules.awareness_trainer import AwarenessTrainer
from modules.report import SEReport

def main():
    parser = argparse.ArgumentParser(description="Social Engineer Lab")
    parser.add_argument("--mode", choices=["simulate", "train", "report"], default="simulate")
    parser.add_argument("--targets", help="CSV file with target emails")
    parser.add_argument("--template", default="it_support", choices=["it_support", "hr_policy", "password_reset", "invoice"])
    parser.add_argument("--output", default="se_report.html")
    args = parser.parse_args()

    results = {}

    if args.mode == "simulate":
        sim = PhishingSimulator(args.template)
        results["simulation"] = sim.run(args.targets)

    elif args.mode == "train":
        trainer = AwarenessTrainer()
        results["training"] = trainer.generate_material()

    report = SEReport(results)
    report.save(args.output)
    print(f"[+] Report: {args.output}")

if __name__ == "__main__":
    main()
