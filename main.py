from parser import load_logs
from analyzer import analyze
from report_generator import generate_report

logs = load_logs("sample_logs/cloudtrail_sample.json")

findings = analyze(logs)

report = generate_report(findings)

print(report)
