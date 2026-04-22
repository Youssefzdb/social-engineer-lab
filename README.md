# social-engineer-lab 🎭

Security Awareness Training & SE Attack Simulation Framework

> For authorized security awareness training and red team exercises ONLY.

## Features
- Phishing email analyzer (keywords, URL patterns, sender spoofing)
- Pretexting awareness guide (IT fraud, CEO fraud, vendor impersonation)
- Interactive training scenarios (phishing, vishing, baiting, tailgating)
- HTML awareness report

## Usage
```bash
pip install -r requirements.txt

# Analyze suspicious email
python main.py --mode detect --email suspicious.eml

# Check URL
python main.py --mode detect --url https://suspicious-link.com

# Run all training scenarios
python main.py --mode train

# Full report
python main.py --mode full
```
