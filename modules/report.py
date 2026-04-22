#!/usr/bin/env python3
from datetime import datetime
import json

class SEReport:
    def __init__(self, results):
        self.results = results

    def save(self, filename):
        training_html = ""
        for s in self.results.get("training", []):
            training_html += f"""
            <div class="scenario">
              <h3>Scenario {s['id']}: {s['title']} <span class="tag">{s['category']}</span></h3>
              <p><b>Situation:</b> {s['scenario']}</p>
              <p><b>Correct Action:</b> <span style="color:#22c55e">{s['correct_action']}</span></p>
              <p><b>Red Flags:</b> {', '.join(s['red_flags'])}</p>
            </div>"""

        phishing = self.results.get("phishing", {})
        phishing_html = ""
        for f in phishing.get("findings", []):
            phishing_html += f"<li class='{f['severity'].lower()}'>[{f['severity']}] {f['indicator']}</li>"

        html = f"""<!DOCTYPE html>
<html><head><title>SE Awareness Lab</title>
<style>
body{{font-family:Arial;background:#0f172a;color:#e2e8f0;padding:20px}}
h1{{color:#f59e0b}} h2{{color:#fbbf24}}
.scenario{{background:#1e293b;border-radius:8px;padding:15px;margin:10px 0;border-left:4px solid #f59e0b}}
.tag{{background:#1d4ed8;padding:2px 8px;border-radius:12px;font-size:0.8em}}
.high{{color:#ef4444}} .medium{{color:#f59e0b}} .low{{color:#22c55e}}
</style></head>
<body>
<h1>Social Engineering Awareness Lab</h1>
<p>{datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
<h2>Training Scenarios</h2>
{training_html}
{f'<h2>Phishing Analysis</h2><ul>{phishing_html}</ul>' if phishing_html else ''}
</body></html>"""
        with open(filename, "w") as f:
            f.write(html)
        print(f"[+] Report saved: {filename}")
