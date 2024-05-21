# DepBotPy - Automated Dependency Updates for Python

GitHub Actions to automate the process of updating Python dependencies.

## Features

- Automatically checks for outdated dependencies on a scheduled basis (default: every Sunday at midnight)
- Creates a separate branch and pull request for each dependency update
- Skips updates for dependencies that already have an open pull request
- Assigns labels to the created pull requests for easy identification and categorization

## Usage

1. Add this GitHub Actions workflow to your repository by creating a new file named `.github/workflows/update-dependencies.yml` and copying the contents of the provided workflow.
2. Create a `requirements.txt` file in the root directory of your repository with your Python dependencies.
3. Commit and push the changes to your repository.

## Configuration

- To modify the schedule for running the workflow, update the `cron` syntax in the `schedule` section of the workflow file.
- To change the labels assigned to the pull requests, modify the `--label` options in the `gh pr create` command in the workflow file.
