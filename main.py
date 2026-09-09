from parser import load_logs
from analyzer import analyze
from report_generator import generate_report

logs = load_logs("sample_logs/cloudtrail_sample.json")

findings = analyze(logs)

report = generate_report(findings)

print(report)

with open("reports/security_report.md", "w") as file:
    file.write(report)

print("\nSecurity report saved to reports/security_report.md") 