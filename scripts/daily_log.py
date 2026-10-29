#!/usr/bin/env python3
"""Write an idempotent daily automation heartbeat (not a manual activity log)."""
from datetime import datetime, timezone
from pathlib import Path
from zoneinfo import ZoneInfo

ROOT = Path(__file__).resolve().parents[1]
now = datetime.now(timezone.utc)
local = now.astimezone(ZoneInfo('Asia/Shanghai'))
day = local.strftime('%Y-%m-%d')
path = ROOT / 'logs' / f'{day}.md'
path.parent.mkdir(parents=True, exist_ok=True)
if path.exists():
    print(f'Already recorded: {path.relative_to(ROOT)}')
else:
    path.write_text(
        f'# Automated heartbeat — {day}\n\n'
        '> This file was generated automatically by GitHub Actions. '
        'It does not represent manual coding or learning activity.\n\n'
        f'- Local date (Asia/Shanghai): {day}\n'
        f'- Run time (UTC): {now.strftime("%Y-%m-%d %H:%M:%S")}\n'
        '- Workflow: Daily Engineering Log\n',
        encoding='utf-8',
    )
    print(f'Created: {path.relative_to(ROOT)}')
