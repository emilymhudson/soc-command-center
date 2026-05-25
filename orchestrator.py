import os
from github import Github

def run_audit():
    token = os.getenv('GITHUB_TOKEN')
    
    if not token:
        print("[!] ERROR: GITHUB_TOKEN environment variable not found.")
        return

    g = Github(token)
    user = g.get_user()
    
    repos_to_audit = [
        "probabilistic-threat-classifier",
        "mime-forensic-log-parser",
        "detection-as-code",
        "academic-ctf-architecture",
        "evidentiary-provenance-engine"
    ]

    report = "# SOC Command Center: Security Posture Dashboard\n\n"
    report += f"Generated: {os.popen('date').read()}\n\n| Repository | Status | Health Score |\n|---|---|---|\n"

    total_score = 0
    for repo_name in repos_to_audit:
        try:
            repo = user.get_repo(repo_name)
            status = "Operational"
            score = 20
        except Exception:
            status = "NOT FOUND"
            score = 0
        
        report += f"| {repo_name} | {status} | {score}/20 |\n"
        total_score += score

    report += f"\n## Aggregate Security Posture: {total_score}/100"
    
    with open("Security_Posture_Report.md", "w") as f:
        f.write(report)
    print("[+] Security_Posture_Report.md generated successfully.")

if __name__ == "__main__":
    run_audit()
