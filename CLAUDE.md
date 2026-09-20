# <Name>

<!-- setup: replace the title with the owner's first name and write two sentences: whose
ICM this is and how they think about it (a notebook, a second desk, a colleague).
Ask, do not guess. Delete this comment when done. -->

## First, always

Read `who-am-i.md` and `how-we-talk.md` before any answer, in every conversation. They are short
and carry tone, language, limits and the state of every area.

## Before you answer, add, research or decide: search the ICM

A duplicate record means two versions of one fact that drift apart.

```bash
rg -il "term" --glob '*.md'                 # which records mention it
rg -i "^description:.*term" --glob '*.md'   # by frontmatter description only
```

Order: the routing table below, then that area's `CONTEXT.md`, then `rg`. If a record exists it is
extended, not joined by a second one; if it contradicts a new finding, the owner hears about it.

## Map

| Path | What it holds |
| --- | --- |
| `who-am-i.md` | who the owner is, work, people, goals with dates, one paragraph of state per area |
| `how-we-talk.md` | language, tone, what they want from the work, what is never done, trigger words |
| `memory.md` | dated facts the owner said, one per line |
| `domains/` | areas of knowledge, each with its own `CONTEXT.md` |
| `skills/` | the owner's own procedures; `skills/CONTEXT.md` lists them |
| `_config/` | configures the factory, not the product: what `core/` reads about this ICM (labels, graph groups) |
| `core/` | icm-kit-core, vendored. Never edited here; updated with the `core-update` skill |
| `pages/` | built pages. Sources live with the skill or workflow that builds them |

Layers, as in the Interpretable Context Methodology; read downward only as far as needed:

| Layer | File | Answers |
| --- | --- | --- |
| 0 | this file | where am I |
| 1 | `domains/<area>/CONTEXT.md`, `skills/CONTEXT.md` | where do I go |
| 2 | a `SKILL.md`: the contract of one procedure | what do I do |
| 3 | `references/` in an area, `_config/` | what rules apply: other people's knowledge, the owner's settings |
| 4 | `output/` and `data/` in an area | what am I working with: the owner's decisions, tables that are appended to |

## Routing

| When they ask about | Go to |
| --- | --- |
| how the ICM works, connectors, routines, published pages | `domains/system/CONTEXT.md` |
| something personal with a date | `memory.md` |

<!-- setup: add one row per area created during setup. Rows are phrased in the owner's
words for the topic, not in folder names. -->

## Procedures

An area holds knowledge, a skill holds steps. When the owner asks for something to be **done**
rather than **known**, go to the skill first; the result goes to the area's `output/`.

| When they ask | Skill |
| --- | --- |
| run setup, continue setup, adopt an existing ICM | `core/skills/setup/` |
| update the system, a migration guide | `core/skills/core-update/` |
| a recovery USB, a new computer | `core/backup/` |
| phone and cloud access, keys, hooks, revocation | `core/adapters/claude/` |

## Words that trigger something

| Word | What you do |
| --- | --- |
| `remember` | one dated line in `memory.md` |
| `forget`, `do not keep` | removed from every file in the same session, no questions, no comment |
| `overview` | the state of an area from its `output/`, conclusion first |
| `send` | the checkpoint for anything that leaves the machine: the only word that unlocks an outside action, and only that one |

<!-- setup: translate the trigger words into the owner's language and keep the meaning. -->

## Rules

- Never invent a result. "Proposed" is not "done", "drafted" is not "sent". A result reported by
  another agent is checked before it is passed on.
- **Privacy beats the ICM.** On "forget" the thing enters no file, and if it did, it leaves in the
  same session and is not rebuilt from other traces.
- No outside action without an explicit "send". Passwords, tokens and keys stay out of the chat
  and out of every file.
- Every record has frontmatter: `type`, `title`, `description`, `status`, `trust_tier`, `tags`.
  `type`: `Reference`, `Output`, `Skill`, `Tracking`, `Decision`, `Architecture`, `Research`.
  `status`: `active`, `draft`, `paused`, `archived`. `trust_tier`: `authoritative` (the owner said
  it), `verified` (checked against a source), `machine-confirmed`, `unverified`. No dates in
  frontmatter: `git log --follow` knows when.
- `CONTEXT.md` routes and never holds content; up to 80 lines. Records up to 200, this file up to 200.
- **Canonical source**: every fact has one home, everything else points to it. An outdated fact is deleted, not struck
  through; why it went is in the commit.
- A rule a machine can check goes in a script, not a sentence. `.githooks/pre-commit` runs
  `core/scripts/` (once per clone: `git config core.hooksPath .githooks`).
- Push only to the encrypted remote, only `main`. `.githooks/pre-push` refuses anything else.

## Reflection at the end of a session

Before the end of any session that did something, one minute on two questions:

1. **What slowed me down**, and where to fix it so it does not repeat.
2. **What went better than usual and why**, so it becomes a procedure and not luck.

The fix goes into the ICM, not into a message: a repeated procedure becomes a skill, a tool
failure becomes a comment beside the code that handles it, a fact about the owner goes to its
area, how they want to work goes to `how-we-talk.md`, a rule for everything goes here. One fix per
session is enough. If nothing slowed you down, that is a finding too.

## Git log is the change journal

There is no `log.md`. A commit message has a title line and a body in full sentences: what was
learned, what changed, what it now contradicts.
