# Session 2 Practice: CI/CD with GitHub Actions

This repository trains a linear-regression model whenever
`training_data.csv` changes. Training runs on pull requests, while pushes to
`main` also publish the model to the `release` branch and create a GitHub
Release.

## Pipeline

1. Check out the repository and install Python dependencies.
2. Detect a change to `training_data.csv`.
3. Train the linear-regression model.
4. Publish `linear_model.txt` on the orphan `release` branch.
5. Create a release named `v<run-number>` and attach `linear_model.txt`.

## Run locally

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python train_model.py
```

On Windows PowerShell, activate the environment with:

```powershell
.\.venv\Scripts\Activate.ps1
```

## Test the automation

Add a row to `training_data.csv`, commit the change, and push it to `main`.
Then check the repository's **Actions**, **release** branch, and **Releases**
pages.
