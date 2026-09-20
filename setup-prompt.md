# Setup prompt

Copy everything in the block into your coding agent, in an empty folder or your home folder.

```text
I want to set up an ICM: a knowledge base about my own life and work, as markdown files in an
encrypted git repo, that you will work in from now on. Use icm-kit.

First tell me which agent and subscription you are running as. icm-kit works with Claude Code today;
if you are something else, say so and stop, because the adapter for you does not exist yet.

Talk to me in the language I answer in. Before anything else, ask me one question at a time:
what I want this to help with in the next three months, which computer and phone I use, and
whether I have used git, a terminal and encryption keys before. From my answers, decide how much
to explain, and ask me how I like things explained.

Then:
1. Check that git is installed. If it is not, tell me how to install it and wait.
2. Ask where the ICM should live, and clone https://github.com/jaksm/icm-kit there.
3. Open core/skills/setup/SKILL.md in that folder and follow it from step 01. It keeps its state in
   _config/setup.json, so if we stop, I can come back and say "continue setup".

Rules for the whole setup: never ask me for a passphrase or a password in this conversation and
never write one to a file; I type those myself when a window asks. Install nothing and create
nothing outside my computer without asking me first, one thing at a time. When a step is done,
show me the proof, not just the claim.
```

The prompt is short on purpose. Everything else lives in the repo it clones, so the steps can
improve without this text going stale.
