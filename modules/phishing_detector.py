#!/usr/bin/env python3
"""Phishing Email & URL Detector"""
import re
import email

PHISHING_KEYWORDS = [
    "urgent", "verify your account", "click here", "suspended",
    "confirm your password", "unusual activity", "you have won",
    "act now", "limited time", "your account will be closed"
]

SUSPICIOUS_PATTERNS = [
    r"bit\.ly/", r"tinyurl\.com/", r"goo\.gl/",
    r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}",  # IP in URL
    r"paypa1\.com", r"amaz0n\.com", r"g00gle\.com"  # Typosquatting
]

class PhishingDetector:
    def analyze_email(self, filepath):
        findings = []
        try:
            with open(filepath, "r") as f:
                content = f.read()

            msg = email.message_from_string(content)
            subject = msg.get("Subject", "")
            sender = msg.get("From", "")
            body = ""
            if msg.is_multipart():
                for part in msg.walk():
                    if part.get_content_type() == "text/plain":
                        body += part.get_payload(decode=True).decode(errors="ignore")
            else:
                body = msg.get_payload(decode=True).decode(errors="ignore")

            full_text = (subject + " " + body).lower()

            # Check phishing keywords
            for kw in PHISHING_KEYWORDS:
                if kw in full_text:
                    findings.append({"indicator": f"Phishing keyword: '{kw}'", "severity": "HIGH"})
                    print(f"[!] Phishing keyword: '{kw}'")

            # Check sender spoofing
            if re.search(r"@(?!gmail|yahoo|outlook|company\.com)", sender.lower()):
                findings.append({"indicator": f"Suspicious sender: {sender}", "severity": "MEDIUM"})

            # Check URLs in body
            urls = re.findall(r'https?://[^\s]+', body)
            for url in urls:
                self._check_url_patterns(url, findings)

        except Exception as e:
            findings.append({"indicator": f"Parse error: {e}", "severity": "INFO"})

        print(f"[+] Found {len(findings)} phishing indicators")
        return {"file": filepath, "findings": findings, "score": min(len(findings) * 15, 100)}

    def _check_url_patterns(self, url, findings):
        for pattern in SUSPICIOUS_PATTERNS:
            if re.search(pattern, url):
                findings.append({"indicator": f"Suspicious URL: {url[:80]}", "severity": "HIGH"})
                print(f"[!] Suspicious URL: {url[:60]}")
                break

    def check_url(self, url):
        findings = []
        self._check_url_patterns(url, findings)
        if not findings:
            print(f"[+] URL appears clean: {url}")
        return {"url": url, "findings": findings}
