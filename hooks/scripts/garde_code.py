#!/usr/bin/env python3
"""Garde-code du playbook IA.

Hook PreToolUse sur Write / Edit / MultiEdit / NotebookEdit.
Refuse l'écriture de code applicatif tant que la phase 1 (cadrage) n'est pas
close dans docs/projet/etat.md. Ne fait rien si le projet n'est pas suivi
par le playbook (pas de fichier d'état), si garde_code vaut off, ou si la
phase 1 figure dans phases_closes.

Toujours autorisé : docs/, spike/, .claude/, fichiers .md et .txt,
.gitignore, LICENSE, et tout chemin hors du projet.
"""
import json
import os
import re
import sys

ALLOWED_PREFIXES = ("docs/", "spike/", ".claude/")
ALLOWED_SUFFIXES = (".md", ".txt")
ALLOWED_NAMES = {".gitignore", "LICENSE", "LICENSE.md"}


def main() -> int:
    try:
        data = json.load(sys.stdin)
    except Exception:
        return 0

    tool_input = data.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("notebook_path") or ""
    if not path:
        return 0

    root = os.environ.get("CLAUDE_PROJECT_DIR") or data.get("cwd") or os.getcwd()
    etat = os.path.join(root, "docs", "projet", "etat.md")
    if not os.path.isfile(etat):
        return 0

    try:
        with open(etat, encoding="utf-8") as f:
            head = f.read(6000)
    except Exception:
        return 0

    if re.search(r"^garde_code:\s*off\s*$", head, re.M):
        return 0

    m = re.search(r"^phases_closes:\s*\[(.*?)\]", head, re.M)
    closes = [x.strip() for x in m.group(1).split(",")] if m else []
    if "1" in closes:
        return 0

    abs_path = os.path.abspath(os.path.join(root, path)) if not os.path.isabs(path) else path
    rel = os.path.relpath(abs_path, root).replace("\\", "/")
    if rel.startswith("../"):
        return 0
    if rel.startswith(ALLOWED_PREFIXES) or rel.endswith(ALLOWED_SUFFIXES) or os.path.basename(rel) in ALLOWED_NAMES:
        return 0

    reason = (
        "Garde-code du playbook IA : la phase 1 (cadrage) n'est pas close dans docs/projet/etat.md, "
        f"donc pas d'écriture de code applicatif ({rel}). Autorisés : docs/, spike/, fichiers .md. "
        "Pour lever la garde : clore la phase 1 via le skill revue-de-phase, ou écrire garde_code: off "
        "dans l'en-tête de l'état avec un motif daté dans le journal."
    )
    print(json.dumps({
        "hookSpecificOutput": {
            "hookEventName": "PreToolUse",
            "permissionDecision": "deny",
            "permissionDecisionReason": reason,
        }
    }))
    return 0


if __name__ == "__main__":
    sys.exit(main())
