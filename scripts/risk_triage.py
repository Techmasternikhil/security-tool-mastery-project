#!/usr/bin/env python3
import argparse

def classify(score: int) -> str:
    if score >= 17:
        return "Critical"
    if score >= 10:
        return "High"
    if score >= 5:
        return "Medium"
    return "Low"

parser = argparse.ArgumentParser(description="Qualitative likelihood x impact triage helper (not CVSS)")
parser.add_argument("likelihood", type=int, choices=range(1, 6), help="Likelihood from 1 to 5")
parser.add_argument("impact", type=int, choices=range(1, 6), help="Impact from 1 to 5")
args = parser.parse_args()
score = args.likelihood * args.impact
print(f"Score: {score}/25")
print(f"Qualitative label: {classify(score)}")
print("Note: this is a simple triage aid, not a standardized CVSS score.")
