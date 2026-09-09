
def analyze(logs):
    findings = []

    for event in logs["Records"]:

        if event["eventName"] == "CreateAccessKey":
            findings.append({
                "severity": "High",
                "finding": "Access Key Created"
            })

        if event["eventName"] == "TerminateInstances":
            findings.append({
                "severity": "Medium",
                "finding": "EC2 Instance Termination"
            })

    return findings
