"""Paths of the plugin under test, and a runner for its hook as Claude Code launches it."""

import json
import os
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
PLUGIN = REPO_ROOT
HOOK = PLUGIN / "hooks" / "scripts" / "garde_code.py"


def run_hook(project: Path, payload: object, raw: str | None = None) -> subprocess.CompletedProcess:
    """Runs garde_code.py on a PreToolUse payload, in a project, without the session's CLAUDE_ variables."""
    env = {k: v for k, v in os.environ.items() if not k.startswith("CLAUDE_")}
    env["CLAUDE_PROJECT_DIR"] = str(project)
    return subprocess.run(
        [sys.executable, str(HOOK)],
        input=raw if raw is not None else json.dumps(payload),
        capture_output=True,
        text=True,
        encoding="utf-8",
        env=env,
        cwd=project,
        timeout=30,
    )
