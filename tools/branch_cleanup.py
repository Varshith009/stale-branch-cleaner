import requests
from datetime import datetime, timedelta
import os

GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO = os.getenv("GITHUB_REPO")

headers = {
    "Authorization": f"token {GITHUB_TOKEN}",
    "Accept": "application/vnd.github+json"
}

def get_stale_branches():
    url = f"https://api.github.com/repos/{REPO}/branches"
    response = requests.get(url, headers=headers)
    branches = response.json()

    stale = []
    for branch in branches:
        branch_name = branch['name']
        if branch_name == 'main' or branch_name == 'master':
            continue
        commit_url = branch['commit']['url']
        commit_data = requests.get(commit_url, headers=headers).json()
        commit_date = datetime.strptime(commit_data['commit']['author']['date'], '%Y-%m-%dT%H:%M:%SZ')

        if datetime.utcnow() - commit_date > timedelta(days=30):
            stale.append(branch_name)

    return stale

def delete_branch(branch_name):
    url = f"https://api.github.com/repos/{REPO}/git/refs/heads/{branch_name}"
    response = requests.delete(url, headers=headers)
    if response.status_code == 204:
        print(f"Deleted branch: {branch_name}")
    else:
        print(f"Failed to delete branch: {branch_name} — Status: {response.status_code}")

if __name__ == "__main__":
    stale_branches = get_stale_branches()
    if stale_branches:
        print(f"Stale branches found: {stale_branches}")
        for branch in stale_branches:
            delete_branch(branch)
    else:
        print("No stale branches found.")
