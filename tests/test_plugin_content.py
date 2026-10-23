import hashlib
import json
import re
import unittest

import support

CONTENT = ("skills", "agents", "hooks")


class Content(unittest.TestCase):
    def test_the_plugin_names_no_project_and_no_person(self) -> None:
        # The names stay out of this public repo too: only their SHA-256 is kept, compared word by word.
        forbidden = {
            "0446597c56a0163e2afe9be46c51c889d7b6c0407408c0fcc859eae685d911d5",
            "e1025e9718b1aeb757262510352237eec3651a8f48e523325542b09954fd4bb9",
            "85f5e10431f69bc2a14046a13aabaefc660103b6de7a84f75c4b96181d03f0b5",
        }
        for folder in CONTENT:
            for path in sorted((support.PLUGIN / folder).rglob("*")):
                if not path.is_file():
                    continue
                try:
                    text = path.read_text(encoding="utf-8")
                except UnicodeDecodeError:
                    continue
                words = set(re.findall(r"[a-z0-9]+", text.lower()))
                found = [w for w in words if hashlib.sha256(w.encode()).hexdigest() in forbidden]
                with self.subTest(path=str(path.relative_to(support.PLUGIN))):
                    self.assertEqual(found, [])

    def test_the_prose_has_no_em_dash(self) -> None:
        for path in sorted(support.REPO_ROOT.rglob("*.md")):
            if ".git" in path.parts:
                continue
            with self.subTest(path=str(path.relative_to(support.REPO_ROOT))):
                self.assertNotIn("—", path.read_text(encoding="utf-8"))


class Manifest(unittest.TestCase):
    def setUp(self) -> None:
        self.plugin = json.loads((support.PLUGIN / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))

    def test_the_version_lives_in_plugin_json_only(self) -> None:
        self.assertEqual(self.plugin["name"], "ai-delivery-gates")
        self.assertRegex(self.plugin["version"], r"^\d+\.\d+\.\d+$")
        self.assertFalse((support.PLUGIN / ".claude-plugin" / "marketplace.json").exists(),
                         "the plugin is served by the ikoro-labs marketplace, in ikoro-labs/forge")

    def test_the_changelog_opens_on_the_plugin_version(self) -> None:
        changelog = (support.REPO_ROOT / "CHANGELOG.md").read_text(encoding="utf-8")
        first = re.search(r"^## \[?(\d+\.\d+\.\d+)", changelog, re.MULTILINE)
        self.assertIsNotNone(first)
        self.assertEqual(first.group(1) if first else None, self.plugin["version"])

    def test_the_icon_is_a_square_png_the_plugin_directory_accepts(self) -> None:
        # The directory takes a PNG of 512 to 2048 px a side, under 2 MB, and no SVG.
        icon = (support.PLUGIN / ".claude-plugin" / "icon.png").read_bytes()
        self.assertEqual(icon[:8], b"\x89PNG\r\n\x1a\n")
        self.assertEqual(icon[12:16], b"IHDR")
        width, height = int.from_bytes(icon[16:20], "big"), int.from_bytes(icon[20:24], "big")
        self.assertEqual(width, height)
        self.assertTrue(512 <= width <= 2048, width)
        self.assertLess(len(icon), 2 * 1024 * 1024)
        self.assertTrue((support.REPO_ROOT / "docs" / "logo.svg").is_file())

    def test_the_repository_root_holds_the_mit_licence_the_manifest_names(self) -> None:
        licence = support.REPO_ROOT / "LICENSE"
        self.assertTrue(licence.is_file(), "no LICENSE at the repository root")
        self.assertTrue(licence.read_text(encoding="utf-8").startswith("MIT License"))
        self.assertEqual(self.plugin["license"], "MIT")


if __name__ == "__main__":
    unittest.main()
