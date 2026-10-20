#!/usr/bin/env python3
"""Bundle canonical resources and check independently installable skills."""
import argparse
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RESOURCES = {
    "references/mom-test-handbook.md": "references/mom-test-handbook.md",
    "references/coverage-checklist.md": "references/coverage-checklist.md",
    "templates/interview-template.md": "assets/interview-template.md",
}
SKILLS = (
    "ideation-prepare-interviews",
    "ideation-analyze-interviews",
    "ideation-next-experiments",
)


def check_skill(skill):
    text = (skill / "SKILL.md").read_text()
    match = re.match(r"---\n(.*?)\n---\n", text, re.S)
    if not match:
        raise ValueError(f"{skill.name}: missing frontmatter")
    fields = dict(re.findall(r"^(name|description): (.+)$", match[1], re.M))
    if fields.get("name") != skill.name or not fields.get("description"):
        raise ValueError(f"{skill.name}: invalid name or description")
    if len(text.splitlines()) > 500:
        raise ValueError(f"{skill.name}: SKILL.md exceeds 500 lines")
    for target in re.findall(r"`([^`]+\.md)`", text):
        resource = (skill / target).resolve()
        if not resource.is_relative_to(skill.resolve()) or not resource.is_file():
            raise ValueError(f"{skill.name}: missing or external resource {target}")
    for name in ("mom-test-handbook.md", "coverage-checklist.md"):
        ids = re.findall(r"^\| (R\d+) \|", (skill / "references" / name).read_text(), re.M)
        if ids != [f"R{i:02}" for i in range(1, 40)]:
            raise ValueError(f"{skill.name}: incomplete rule inventory in {name}")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check without writing")
    args = parser.parse_args()
    for name in SKILLS:
        skill = ROOT / "skills" / name
        for source, target in RESOURCES.items():
            expected = (ROOT / source).read_bytes()
            output = skill / target
            if args.check:
                if not output.exists() or output.read_bytes() != expected:
                    raise ValueError(f"{name}: stale resource {target}; run {parser.prog}")
            else:
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_bytes(expected)
        check_skill(skill)
    print(f"{len(SKILLS)} self-contained skills; all resources and 39-rule inventories checked.")


if __name__ == "__main__":
    main()
