#  Stale Branch Cleaner 

Automatically deletes branches older than **1 days (Testing purpose)** daily using GitHub Actions.

##  Setup

1. Go to your repository **Settings → Secrets and variables → Actions**
2. Add the following secrets:
   - `PERSONAL_ACCESS_TOKEN` — your GitHub PAT (with `repo` access)
   - `TARGET_REPO` — your repo name in the form `username/repo-name`

##  How It Works

- Runs daily at midnight UTC
- Fetches all branches
- Checks each branch’s latest commit date
- If older than 30 days, deletes it (except `main` or `master`)

##  Safety

- `main` and `master` branches are always ignored
- Logs deletion activity in Actions run logs

##  Manual Trigger

You can manually run this workflow via **Actions tab** → `Delete Stale Branches` → `Run workflow`

---
