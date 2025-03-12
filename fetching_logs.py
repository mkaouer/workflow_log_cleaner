import requests
import time
import json

# GitHub Token (replace with your own)
GITHUB_TOKEN = 'YOUR_GITHUB_TOKEN'
HEADERS = {
    'Authorization': f'token {GITHUB_TOKEN}',
    'Accept': 'application/vnd.github.v3+json'
}

# Function to fetch failed workflows from a GitHub repository
def fetch_failed_workflows(owner, repo, page=1):
    url = f'https://api.github.com/repos/{owner}/{repo}/actions/runs'
    params = {'status': 'failure', 'page': page, 'per_page': 10}
    response = requests.get(url, headers=HEADERS, params=params)
    return response.json()

# Function to fetch the logs of a specific workflow run
def fetch_workflow_logs(owner, repo, run_id):
    url = f'https://api.github.com/repos/{owner}/{repo}/actions/runs/{run_id}/logs'
    response = requests.get(url, headers=HEADERS)
    return response.content

# Get failed workflows from a repository and download logs
def get_failed_workflow_logs(owner, repo, num_of_logs=50):
    logs = []
    page = 1
    while len(logs) < num_of_logs:
        # Fetch failed workflows
        workflows = fetch_failed_workflows(owner, repo, page)
        if 'workflow_runs' not in workflows:
            print("No failed workflows found.")
            break

        # Loop through each workflow to get logs
        for workflow in workflows['workflow_runs']:
            if len(logs) >= num_of_logs:
                break
            run_id = workflow['id']
            print(f"Fetching logs for run {run_id}...")
            try:
                logs_content = fetch_workflow_logs(owner, repo, run_id)
                logs.append(logs_content)
            except Exception as e:
                print(f"Error fetching logs for run {run_id}: {e}")
                continue
        page += 1
        time.sleep(2)  # Rate limit handling
    return logs

# Example Usage: Fetch failed workflow logs from a repo (example: "microsoft/vscode")
owner = 'microsoft'
repo = 'vscode'

logs = get_failed_workflow_logs(owner, repo, num_of_logs=50)

# Save logs to files
for idx, log in enumerate(logs):
    with open(f'github_failed_log_{idx+1}.txt', 'wb') as f:
        f.write(log)

print(f"{len(logs)} failed workflow logs downloaded.")
