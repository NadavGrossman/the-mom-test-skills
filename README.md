# The Mom Test Skills

**Your agent can ship the product. Teach it to question the idea.**

<a href="https://www.momtestbook.com/"><img src="https://www.momtestbook.com/og-image.jpg" alt="The Mom Test by Rob Fitzpatrick" width="760"></a>

Turn customer conversations into evidence with three skills based on *The Mom Test*. For founders building with coding agents.

| Skill | What you get |
| --- | --- |
| [Prepare interviews](skills/ideation-prepare-interviews/SKILL.md) | Questions that uncover real behavior. |
| [Analyze interviews](skills/ideation-analyze-interviews/SKILL.md) | Facts, contradictions, and actual commitments. |
| [Choose the next experiment](skills/ideation-next-experiments/SKILL.md) | A small test of the assumption that matters most. |

## Install

### Claude Code

```sh
npx skills add NadavGrossman/the-mom-test-skills --agent claude-code --yes
```

Start with `/ideation-prepare-interviews`, then describe your idea.

### Codex

```sh
npx skills add NadavGrossman/the-mom-test-skills --agent codex --yes
```

Start with `$ideation-prepare-interviews`, then describe your idea.

Node.js 22.20+. Add `--global` to use across projects. Each skill is self-contained.

The agents help you prepare, interpret, and decide. Customer evidence comes from real people.

<details>
<summary>Contributing</summary>

Edit the canonical files in `references/` and `templates/`, then run:

```sh
python3 scripts/sync_resources.py
python3 scripts/sync_resources.py --check
```

</details>

---

Unofficial companion to [*The Mom Test* by Rob Fitzpatrick](https://www.momtestbook.com/). Book image hosted on the author’s site; the book itself is not included. [MIT](LICENSE) covers our original material only.
