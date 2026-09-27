from pathlib import Path
from typing import Any

import pytest
import yaml


ROOT = Path(__file__).resolve().parents[1]
SKILL_FILES = sorted(ROOT.glob("*/SKILL.md"))
ALLOWED_OPENCLAW_KEYS = {"os", "requires"}
# Only keys OpenClaw's skill parser actually reads. Anything else (for example
# `files`) is silently dropped and the skill stays eligible without it.
ALLOWED_REQUIRE_KEYS = {"bins", "anyBins", "env", "config"}


def _frontmatter(path: Path) -> dict[str, Any]:
    text = path.read_text()
    assert text.startswith("---\n"), path
    return yaml.safe_load(text.split("---", 2)[1]) or {}


def _openclaw(path: Path) -> dict[str, Any]:
    return (_frontmatter(path).get("metadata") or {}).get("openclaw") or {}


def test_every_skill_folder_is_collected() -> None:
    assert SKILL_FILES
    assert len({p.parent.name for p in SKILL_FILES}) == len(SKILL_FILES)


@pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
def test_skill_name_matches_folder(path: Path) -> None:
    assert _frontmatter(path).get("name") == path.parent.name


@pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
def test_skill_has_description(path: Path) -> None:
    description = _frontmatter(path).get("description")
    assert isinstance(description, str) and description.strip()


@pytest.mark.parametrize("path", SKILL_FILES, ids=lambda p: p.parent.name)
def test_capability_metadata_schema(path: Path) -> None:
    openclaw = _openclaw(path)
    assert set(openclaw) <= ALLOWED_OPENCLAW_KEYS
    requires = openclaw.get("requires") or {}
    assert set(requires) <= ALLOWED_REQUIRE_KEYS
    if "os" in openclaw:
        assert isinstance(openclaw["os"], list)
        assert all(isinstance(v, str) for v in openclaw["os"])
    for key, values in requires.items():
        assert isinstance(values, list) and values, key
        assert all(isinstance(v, str) and v for v in values), key


def test_known_capability_constraints() -> None:
    insights = _openclaw(ROOT / "capturing-customer-insights" / "SKILL.md")
    assert insights["requires"] == {"bins": ["gog"]}

    interviews = _openclaw(ROOT / "running-problem-interviews" / "SKILL.md")
    assert interviews["os"] == ["darwin"]
    assert interviews["requires"] == {"env": ["AIRTABLE_TOKEN"]}


def test_problem_interview_description_keeps_triggers_and_routing() -> None:
    description = _frontmatter(ROOT / "running-problem-interviews" / "SKILL.md")[
        "description"
    ]
    for phrase in (
        "prep a problem interview with [person]",
        "help me run a problem interview",
        "managing-finances-bb",
        "preparing-for-meetings",
        "searching-meeting-transcripts",
    ):
        assert phrase in description
