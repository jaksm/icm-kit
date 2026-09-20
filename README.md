# icm-kit

A knowledge base about your own life and work that an AI agent can actually work in.

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
A base that knows you well personalizes better, at the price of concentrating private data. That
trade is the whole product, so it is worth deciding on purpose.

## What is in the box

| Path | What it is |
| --- | --- |
| `CLAUDE.md` | the router: the map, routing tables, trigger words, and the rules the agent works by |
| `who-am-i.md`, `how-we-talk.md`, `memory.md` | the three personal records, empty, each with a note telling the agent what to collect and how to ask |
| `domains/` | areas of knowledge. `system/` describes the base itself; `_example/` is the shape of every other area |
| `skills/` | your own procedures, plus the audit rule for skills you download |
| `config/` | the few things `core/` needs to know about your repo |
| `core/` | [icm-kit-core](https://github.com/jaksm/icm-kit-core), vendored: commit checks, the Claude adapter (phone and cloud access, sync hooks, key revocation), the component library for pages, the graph of your base |
| `.githooks/` | runs the checks before every commit, refuses any push that is not to the encrypted remote |

## What encryption does and does not do

The repo is pushed through `git-remote-gcrypt`, so the host only ever stores an encrypted blob.
That protects you if the repository or the hosting account is stolen. It does **not** hide anything
from the AI provider: whatever the agent reads in a session is sent to the model. What the provider
may do with it is set by its data retention terms, not by this kit. Read them for the plan you are on.

## Start

Paste the setup prompt from the site into your agent. It asks a few questions to learn how
technical you are, checks what is installed, clones this template, fills the personal records in a
conversation, makes your key, and walks you through cloud access, sources, reminders and your
first routines. Setup by hand:

```bash
git clone https://github.com/jaksm/icm-kit my-icm && cd my-icm
rm -rf .git && git init -b main && git config core.hooksPath .githooks
```

Then open the folder in Claude Code and say: read `CLAUDE.md` and onboard me.

## Updates

`core/` is updated as a whole; everything else is yours and is never touched. Ask the agent to
update the system. It runs the `core-update` skill: it sees which core files you changed, reads the
migration guides between your version and the new one, and adapts your customizations instead of
overwriting them.

## Working on the kit itself

This clone has the push guard on, and the kit's own remote is a plain one. Push it with
`git -c core.hooksPath=/dev/null push`.

## Lineage

ICM is the Interpretable Context Methodology by Jake Van Clief: the folder structure is the
orchestration layer, and one agent reading the right files at the right moment does what would
otherwise take a framework.
[RinDig/Interpretable-Context-Methodology](https://github.com/RinDig/Interpretable-Context-Methodology), MIT.
His workspaces move a piece of work through stages. icm-kit applies the same layers to a base that
holds one person's knowledge and keeps growing.

MIT.
