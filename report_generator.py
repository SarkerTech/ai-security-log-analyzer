
def generate_report(findings):
    report = []
    report.append("# AI Security Report\n")

    for finding in findings:
        report.append(f"## {finding['severity']} Severity")
        report.append(f"- Finding: {finding['finding']}\n")

    return "\n".join(report)
