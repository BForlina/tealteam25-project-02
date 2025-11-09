
# GitHub CI/CD File Checker

This project checks that your repo contains the required files before merging or deploying.
If all required files exist, it logs a success message to **AWS CloudWatch**.

## What It Does
1. Every time you **open a Pull Request**, the workflow checks for:
   - `README.md`
   - `.gitignore`
   - If everything is good it logs to `/github-actions/required-files-checker/beta`
2. When you **merge to main**, it does the same check and logs to:
   - `/github-actions/required-files-checker/prod`

---

## Files in this Project

| File | Purpose |
|------|----------|
| `check_required_files.py` | Checks that the required files exist |
| `.github/workflows/on_pull_request.yml` | Runs checks for pull requests |
| `.github/workflows/on_merge.yml` | Runs checks for main merges |
| `README.md` | Explains the project |
| `.gitignore` | Tells Git which files to ignore |

---

## How to Test Locally

```bash
python3 check_required_files.py
