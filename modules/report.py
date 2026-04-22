#!/usr/bin/env python3
"""Social Engineering Lab Report"""
from datetime import datetime

class SEReport:
    def __init__(self, results):
        self.results = results

    def save(self, filename):
        sim = self.results.get("simulation", {})
        training = self.results.get("training", [])

        sim_html = ""
        if sim:
            flags = "".join(f"<li class='warn'>{f}</li>" for f in sim.get("red_flags", []))
            sim_html = f"""<div class="card">
            <h2>Phishing Simulation</h2>
            <p>Template: <b>{sim.get('template','')}</b></p>
            <p>Subject: {sim.get('subject','')}</p>
            <p>Sender: {sim.get('sender','')}</p>
            <p>Targets: {sim.get('target_count', 0)} (simulation only)</p>
            <h3>Red Flags in Template</h3><ul>{flags}</ul>
            </div>"""

        train_html = ""
        for mod in training:
            quiz_html = "".join(f"<li><b>Q:</b> {q['q']}<br><b>A:</b> {q['a']}</li>" for q in mod.get("quiz", []))
            train_html += f"<div class='card'><h2>{mod['title']}</h2><p>{mod['content']}</p><ul>{quiz_html}</ul></div>"

        html = f"""<!DOCTYPE html>
<html><head><title>Social Engineer Lab Report</title>
<style>
body{{font-family:Arial;background:#0f172a;color:#e2e8f0;padding:20px}}
h1{{color:#818cf8}} h2{{color:#a5b4fc}} h3{{color:#c4b5fd}}
.card{{background:#1e293b;border-radius:8px;padding:15px;margin:10px 0;border:1px solid #334155}}
.warn{{color:#f87171}} li{{margin:8px 0}}
</style></head>
<body>
<h1>Social Engineer Lab Report</h1>
<p>{datetime.now().strftime('%Y-%m-%d %H:%M')}</p>
{sim_html}
{train_html}
</body></html>"""
        with open(filename, "w") as f:
            f.write(html)
        print(f"[+] Report: {filename}")
