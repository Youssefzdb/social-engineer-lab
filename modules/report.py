#!/usr/bin/env python3
from datetime import datetime
import json

class SEReport:
    def __init__(self, results):
        self.results = results

    def save(self, filename):
        content = json.dumps(self.results, indent=2, default=str)
        training = self.results.get("training", {})
        best_practices = training.get("best_practices", [])
        bp_html = "".join(f"<li>{bp}</li>" for bp in best_practices)

        indicators = training.get("phishing_indicators", {})
        ind_html = ""
        for category, items in indicators.items():
            ind_html += f"<h3>{category}</h3><ul>"
            ind_html += "".join(f"<li>{i}</li>" for i in items)
            ind_html += "</ul>"

        html = f"""<!DOCTYPE html><html><head><title>SE Awareness Report</title>
<style>
body{{font-family:Arial;background:#0a1628;color:#e2e8f0;padding:20px}}
h1{{color:#60a5fa}} h2{{color:#93c5fd}} h3{{color:#bfdbfe}}
.card{{background:#1e3a5f;border-radius:8px;padding:15px;margin:10px 0}}
li{{margin:5px 0;line-height:1.6}}
</style></head>
<body>
<h1>Social Engineering Awareness Report</h1>
<p>{datetime.now().strftime('%Y-%m-%d %H:%M')} | For authorized security training use only</p>
<div class="card"><h2>Phishing Indicators</h2>{ind_html}</div>
<div class="card"><h2>Best Practices</h2><ul>{bp_html}</ul></div>
<div class="card"><h2>Raw Data</h2><pre style="font-size:0.8em;overflow:auto">{content[:2000]}</pre></div>
</body></html>"""
        with open(filename, "w") as f:
            f.write(html)
        print(f"[+] Report saved: {filename}")
