from pathlib import Path

import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_FILES = sorted(ROOT.glob("*/SKILL.md"))
ALLOWED_OPENCLAW_KEYS = {"os", "requires"}
ALLOWED_REQUIRE_KEYS = {"bins", "anyBins", "env", "files", "config"}


def _skills() -> dict[str, dict]:
    result = {}
    for path in SKILL_FILES:
        text = path.read_text()
        assert text.startswith("---\n"), path
        frontmatter = yaml.safe_load(text.split("---", 2)[1]) or {}
        openclaw = (frontmatter.get("metadata") or {}).get("openclaw") or {}
        assert set(openclaw) <= ALLOWED_OPENCLAW_KEYS, path
        requires = openclaw.get("requires") or {}
        assert set(requires) <= ALLOWED_REQUIRE_KEYS, path
        if "os" in openclaw:
            assert isinstance(openclaw["os"], list) and all(isinstance(v, str) for v in openclaw["os"]), path
        for key, values in requires.items():
            assert isinstance(values, list) and values, (path, key)
            assert all(isinstance(v, str) and v for v in values), (path, key)
        result[path.parent.name] = openclaw
    assert len(result) == len(SKILL_FILES)
    return result


def test_capability_metadata_schema_and_known_constraints() -> None:
    skills = _skills()
    assert "gog" in skills["capturing-customer-insights"]["requires"]["bins"]
    assert "AIRTABLE_TOKEN" in skills["running-problem-interviews"]["requires"]["env"]
    assert skills["running-problem-interviews"]["os"] == ["darwin"]
    assert skills["running-problem-interviews"]["requires"]["files"]
