import json
import tempfile
import unittest
from pathlib import Path

import support

ETAT = """---
nom: essai
profil: perso
phase_courante: {phase}
phases_closes: [{closes}]
garde_code: {garde}
---

# État du projet essai
"""


class GardeCode(unittest.TestCase):
    def setUp(self) -> None:
        self._tmp = tempfile.TemporaryDirectory()
        self.project = Path(self._tmp.name)

    def tearDown(self) -> None:
        self._tmp.cleanup()

    def etat(self, closes: str = "", garde: str = "on", phase: int = 1) -> None:
        folder = self.project / "docs" / "projet"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "etat.md").write_text(ETAT.format(phase=phase, closes=closes, garde=garde), encoding="utf-8")

    def write(self, path: str, tool: str = "Write") -> dict | None:
        key = "notebook_path" if tool == "NotebookEdit" else "file_path"
        result = support.run_hook(self.project, {"tool_name": tool, "tool_input": {key: path}})
        self.assertEqual(result.returncode, 0, result.stderr)
        return json.loads(result.stdout) if result.stdout.strip() else None

    def assertDenied(self, decision: dict | None) -> None:
        self.assertIsNotNone(decision)
        output = decision["hookSpecificOutput"] if decision else {}
        self.assertEqual(output["hookEventName"], "PreToolUse")
        self.assertEqual(output["permissionDecision"], "deny")
        self.assertIn("phase 1", output["permissionDecisionReason"])

    def test_a_project_without_state_file_is_not_guarded(self) -> None:
        self.assertIsNone(self.write("src/app.py"))

    def test_application_code_is_refused_while_phase_1_is_open(self) -> None:
        self.etat(closes="0")
        self.assertDenied(self.write("src/app.py"))
        self.assertDenied(self.write(str(self.project / "src" / "app.py")))
        self.assertDenied(self.write("pyproject.toml", tool="Edit"))
        self.assertDenied(self.write("analyse.ipynb", tool="NotebookEdit"))

    def test_the_refusal_names_the_file(self) -> None:
        self.etat()
        decision = self.write("src/app.py")
        self.assertIn("src/app.py", decision["hookSpecificOutput"]["permissionDecisionReason"] if decision else "")

    def test_documents_and_spikes_stay_writable(self) -> None:
        self.etat()
        for path in ("docs/projet/01-cadrage/fiche.md", "docs/schema.py", "spike/essai.py",
                     ".claude/settings.json", "NOTES.md", "notes.txt", ".gitignore", "LICENSE"):
            with self.subTest(path=path):
                self.assertIsNone(self.write(path))

    def test_a_path_outside_the_project_is_not_guarded(self) -> None:
        self.etat()
        outside = self.project.parent / "ailleurs.py"
        self.assertIsNone(self.write(str(outside)))

    def test_closing_phase_1_lifts_the_guard(self) -> None:
        self.etat(closes="0, 1", phase=2)
        self.assertIsNone(self.write("src/app.py"))

    def test_garde_code_off_lifts_the_guard(self) -> None:
        self.etat(garde="off")
        self.assertIsNone(self.write("src/app.py"))

    def test_an_unreadable_payload_never_blocks(self) -> None:
        self.etat()
        result = support.run_hook(self.project, None, raw="pas du json")
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "")


class HookDeclaration(unittest.TestCase):
    def test_the_hook_runs_through_uv_on_every_writing_tool(self) -> None:
        hooks = json.loads((support.PLUGIN / "hooks" / "hooks.json").read_text(encoding="utf-8"))
        entry = hooks["hooks"]["PreToolUse"][0]
        self.assertEqual(set(entry["matcher"].split("|")), {"Write", "Edit", "MultiEdit", "NotebookEdit"})
        command = entry["hooks"][0]["command"]
        self.assertIn("uv run --no-project --quiet python", command)
        self.assertIn("${CLAUDE_PLUGIN_ROOT}/hooks/scripts/garde_code.py", command)
        self.assertNotIn("python3", command)


if __name__ == "__main__":
    unittest.main()
