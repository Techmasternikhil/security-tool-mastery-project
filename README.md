# Security Tool Mastery Project

Portfolio project for a Network Security Specialist virtual internship. It documents the purpose, capabilities, limitations, and safe practical use of network and web security tools in an authorized local lab.

## Tools covered
- Nmap — scoped service discovery
- OWASP ZAP — web application baseline scanning
- Wireshark — packet and protocol analysis
- curl / PowerShell — HTTP response inspection
- Docker CLI — container and port-binding review
- Suricata — network intrusion detection
- Python — small risk-triage automation

## Repository structure
- `docs/Security_Tool_Mastery_Project_Report.docx` — Word report
- `docs/methodology.md` — scope and evidence-handling guidance
- `docs/findings-template.csv` — blank findings register
- `scripts/risk_triage.py` — simple likelihood × impact helper
- `evidence/` — place only actual, sanitized outputs and screenshots here
- `reports/` — generated scanner output; don't add sample reports as if they were real scans

## Run the risk triage helper
Requires Python 3:
```bash
python scripts/risk_triage.py 2 3
```

## Safety and evidence integrity
Only test assets you own or are explicitly authorized to assess. Start with non-destructive checks. Preserve raw outputs and document target, date/time, tool version, command, and limitations. A tool alert or open port does not by itself prove a vulnerability. Mark exercises pending unless actual results have been captured and reviewed.
