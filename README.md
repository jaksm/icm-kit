# icm-kit

An ICM: a knowledge base about your own life and work that an AI agent can actually work in.

It is a folder of markdown files in a git repo. That is the whole trick. There is no vector
database, no embedding pipeline, no server, no app to keep running. The agent finds things the way
you would: a router file at the top, a routing file per area, then the record itself. You can open
every file and read it, and so can the agent, and `git log` tells you when and why anything changed.

## Is this for you

Yes, if all three hold:

- You already use Claude. Claude Code is the only harness supported today; the harness-specific
  part is an adapter, and Codex and Antigravity are next.
- You want one place that knows your context, so you stop re-explaining your situation in every
  new conversation: your projects, your numbers, your decisions and the reasons behind them.
- You are comfortable with basic git (clone, commit, push) and the idea of an encryption key you
  must not lose. The agent does the typing; you need to understand what it is doing.

No, if you want an app with a login, or you are not willing to put personal material in one place.
An ICM that knows you well personalizes better, at the price of concentrating private data. That
trade is the whole product, so it is worth deciding on purpose.

## What is in the box

| Path | What it is |
| --- | --- |
| `CLAUDE.md` | the router: the map, routing tables, trigger words, and the rules the agent works by |
| `who-am-i.md`, `how-we-talk.md`, `memory.md` | the three personal records, empty, each with a setup note telling the agent what to collect and how to ask |
| `domains/` | areas of knowledge. `system/` describes the ICM itself; `_example/` is the shape of every other area |
| `skills/` | your own procedures, plus the audit rule for skills you download |
| `_config/` | the few things `core/` needs to know about your ICM |
| `setup-prompt.md` | what you paste into your agent to start |
| `core/` | [icm-kit-core](https://github.com/jaksm/icm-kit-core), vendored: commit checks, the Claude adapter (phone and cloud access, sync hooks, key revocation), the component library for pages, the graph of your ICM |
| `.githooks/` | runs the checks before every commit, refuses any push that is not to the encrypted remote |

## What it can do for you

The folders and the three personal records are the base. On top of them, setup offers workflows
from the [catalog](https://github.com/jaksm/icm-kit-core/blob/main/catalog/index.md); nothing is
installed until you ask for it.

| Workflow | What you get |
| --- | --- |
| `sources` | newsletters, feeds and notices arrive by mail and are sorted by your provider's own rules, which are kept in the ICM |
| `morning-review` | a routine that files the inbox, leaves unread only what needs you, and writes a dated record with proof it ran |
| `feed` | a daily page for the phone: what is open in your ICM and what arrived from outside, as rows of cards, with a diary of what you looked at coming back |
| `expenses` | spending per month as aggregates and a page; the parser for your bank's statements is built for you from a recipe |
| `import` | an old notes app, another assistant's memory or an old disk, walked through with you five items at a time |

The graph of the ICM itself is part of `core/`; every ICM has it.

## What encryption does and does not do

The repo is pushed through `git-remote-gcrypt`, so the host only ever stores an encrypted blob.
That protects you if the repository or the hosting account is stolen. It does **not** hide anything
from the AI provider: whatever the agent reads in a session is sent to the model. What the provider
may do with it is set by its data retention terms, not by this kit.

For Claude on a Free, Pro or Max plan, Claude Code included: Anthropic keeps your data for 30 days
if you do not allow it to be used for model improvement, and for up to 5 years if you do; you
choose at [claude.ai/settings/data-privacy-controls](https://claude.ai/settings/data-privacy-controls),
and content flagged for a usage policy violation is kept for up to 2 years either way. Cloud
sessions follow the same terms. Sources, checked 2026-09-20:
[Claude Code data usage](https://code.claude.com/docs/en/data-usage) and
[How long do you store my data?](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data)
Turn model improvement off before you put anything personal in the ICM.

Other providers, and which subscription makes sense: [docs/providers.md](docs/providers.md).

## Start

The same in one page, with the prompt ready to copy: `site/index.html` (open it in a browser).

Paste the prompt from [setup-prompt.md](setup-prompt.md) into your agent. It asks a few questions
to learn how technical you are and how you like things explained, checks what is installed, clones
this template, fills the personal records in a conversation, makes your key and the encrypted
remote, recommends a recovery USB, sets up phone access, and offers the optional workflows from the
[catalog](https://github.com/jaksm/icm-kit-core/blob/main/catalog/index.md), and ends with an audit of the
whole system that shows you the proof. It spans several sessions and resumes where it stopped: say
"continue setup". An ICM that already exists is adopted, not rebuilt.

You need a paid Claude plan (Claude Code is not part of the free one), a GitHub account, and git,
GnuPG and `git-remote-gcrypt`, which setup installs with your permission. Setup has been run on
macOS; the steps for Windows and Linux are written and marked as not yet verified.

By hand, if you would rather read the steps yourself (`core/skills/setup/steps/`, the key and the
encrypted remote are steps 05 and 06):

```bash
git clone https://github.com/jaksm/icm-kit my-icm && cd my-icm
rm -rf .git && git init -b main && git config core.hooksPath .githooks
```

Then open the folder in Claude Code and say: read `CLAUDE.md` and run setup.

## Updates

`core/` is updated as a whole; everything else is yours and is never touched. Ask the agent to
update the system. It runs the `core-update` skill: it sees which core files you changed, reads the
migration guides between your version and the new one, and adapts your customizations instead of
overwriting them. By hand: `<icm-kit-core>/install.sh . --status` shows your version, the
available one and the core files you edited; `MIGRATIONS/` in icm-kit-core says what each release
moved and what you have to do outside `core/`.

## Lineage

ICM is the Interpretable Context Methodology by Jake Van Clief: the folder structure is the
orchestration layer, and one agent reading the right files at the right moment does what would
otherwise take a framework.
[RinDig/Interpretable-Context-Methodology](https://github.com/RinDig/Interpretable-Context-Methodology), MIT.
The vocabulary here is his: layers 0 to 4, canonical source, contract, checkpoint, `_config/`.
His workspace moves one piece of work through numbered stages. An ICM built from this kit holds
one person's knowledge in areas that have no order, on the same five layers.

MIT.
