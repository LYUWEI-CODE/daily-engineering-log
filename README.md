# Daily Engineering Log

An automated daily heartbeat repository powered by **GitHub Actions + Python**.

> **Transparency:** Files in `logs/` are automatically generated. They indicate that a scheduled workflow ran, **not** that manual engineering work was performed that day.

## How it works

- GitHub Actions runs daily at approximately **09:17 China Standard Time (UTC+8)**.
- A Python script creates `logs/YYYY-MM-DD.md` for the current Asia/Shanghai calendar date.
- The workflow commits a new file only if that date does not already exist.
- You can also trigger the workflow manually via **Actions → Daily Engineering Log → Run workflow**.
- Scheduled workflows can be delayed or skipped by GitHub; daily success is not guaranteed.

## Structure

```text
.
├── .github/workflows/daily.yml  # Scheduler and commit workflow
├── scripts/daily_log.py        # Generates one file per local day
├── logs/.gitkeep               # Folder placeholder
├── .gitignore
└── README.md
```

## Initial setup

1. Create a **public**, non-fork repository named `daily-engineering-log` under `LYUWEI-CODE`.
2. Upload all files, including the hidden `.github` directory, to the default `main` branch.
3. In **Settings → Secrets and variables → Actions → Variables**, add:
   - `COMMIT_NAME` = `LYUWEI-CODE` (or your preferred Git author name)
   - `COMMIT_EMAIL` = an email address verified on your GitHub account, preferably your GitHub-provided `noreply` email.
4. Under **Settings → Actions → General**, ensure Actions are allowed and workflow permissions permit repository content writes (the workflow also explicitly requests `contents: write`).
5. Go to **Actions → Daily Engineering Log → Run workflow** to test. Confirm a new `logs/YYYY-MM-DD.md` appears.

## Contribution attribution

For a commit to count toward your personal GitHub contribution graph, GitHub applies its own attribution requirements, including a verified author email and an eligible branch. A scheduled workflow's commits are not guaranteed to appear as personal contributions. Do not use a bot author email if your goal is attribution to your own account.

## Notes

- Timezone used for log dates: `Asia/Shanghai`.
- The cron expression uses **UTC**, not local time.
- The script is idempotent: multiple runs on the same day do not create extra commits.
- No paid service or personal access token is required for a normal repository using `GITHUB_TOKEN`.
