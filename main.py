#!/usr/bin/env python3
"""social-engineer-lab - Social Engineering Simulation & Awareness Platform"""
import argparse
from modules.phishing_sim import PhishingSimulator
from modules.awareness_scorer import AwarenessScorer
from modules.reporter import SEReporter

def main():
    parser = argparse.ArgumentParser(description="social-engineer-lab - SE Awareness")
    parser.add_argument("--mode", choices=["phishing", "score", "report"], default="report")
    parser.add_argument("--target-list", help="File with target emails (simulation)")
    parser.add_argument("--results", help="JSON results file to score")
    parser.add_argument("--output", default="se_report.json")
    args = parser.parse_args()

    results = {}
    if args.mode == "phishing" and args.target_list:
        sim = PhishingSimulator(args.target_list)
        results["simulation"] = sim.generate_campaign()
    
    if args.results:
        scorer = AwarenessScorer(args.results)
        results["awareness"] = scorer.score()

    reporter = SEReporter(results)
    reporter.save(args.output)
    print(f"[+] SE Lab report: {args.output}")

if __name__ == "__main__":
    main()
