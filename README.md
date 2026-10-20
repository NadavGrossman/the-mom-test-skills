# The Mom Test Skills

Three portable agent skills for customer discovery and ideation, based on Rob Fitzpatrick’s *The Mom Test*.

## Install

Use the open-source [Skills CLI](https://github.com/vercel-labs/skills) to choose your coding agent and skills:

```sh
npx skills add NadavGrossman/the-mom-test-skills
```

Install all three for Codex in the current project:

```sh
npx skills add NadavGrossman/the-mom-test-skills --agent codex --yes
```

Add `--global` for personal use across projects. The CLI requires Node.js 22.20 or newer. Alternatively, copy any complete directory under `skills/` into your agent’s skill directory. For Codex, use `.agents/skills/` in a project or `~/.agents/skills/` for personal skills.

Each skill includes its own handbook, coverage checklist, and interview template. No runtime dependencies, cross-skill dependencies, or access to this repository are required after installation. Tools for Drive, transcripts, or other sources are supplied by the host agent when needed.

## Use

| Skill | What it does | Example request |
| --- | --- | --- |
| `ideation-prepare-interviews` | Defines a focused segment, three learning goals, and neutral interview questions. | “Prepare discovery interviews for an early reporting tool for sales teams.” |
| `ideation-analyze-interviews` | Separates behavioral evidence from praise, speculation, and uncompleted commitments. | “Analyze these interview notes and show what they support, contradict, or leave unknown.” |
| `ideation-next-experiments` | Recommends the smallest useful test of the next important uncertainty. | “Given these findings, what should we test next before building?” |

Invoke a skill explicitly in Codex CLI with `$ideation-prepare-interviews`, `$ideation-analyze-interviews`, or `$ideation-next-experiments`. Other agents use their own skill selector or matching behavior.

Supply your idea or domain, current stage, decision, target customers, and existing evidence. The skills ask for missing context and leave unsupported claims unknown. They assist human interviews and team review; synthetic exercises are always labeled and excluded from demand evidence.

## Included

- [Interview template](templates/interview-template.md), including a five-minute pocket version.
- [Handbook](references/mom-test-handbook.md) and [coverage checklist](references/coverage-checklist.md): 39 explicit rules of thumb and 73 additional guidance entries, with PDF and printed page references.
- [Synthetic evaluations](evals/evals.json), six sample responses, and [review results](evals/review-results.md).

`skills/<name>/` contains a `SKILL.md`, `references/`, and `assets/`. Each folder can be installed on its own using the [Agent Skills format](https://agentskills.io/specification).

## Maintain

Edit the canonical handbook, coverage checklist, and template at the repository root. Then regenerate the bundled copies:

```sh
python3 scripts/sync_resources.py
python3 scripts/sync_resources.py --check
```

The check verifies metadata, all 39 rule IDs, and resource paths for each independently installed skill. Historical behavioral evaluations are synthetic smoke tests, not exhaustive proof of future agent behavior.

## Attribution

An independent, unofficial companion to *The Mom Test* by Rob Fitzpatrick. Instructions and prompts are original adaptations; the book and its PDF are not included. Agent evidence safeguards are identified separately from the book’s guidance.

[MIT License](LICENSE) covers the original material in this repository. It grants no rights to the book or its branding.
