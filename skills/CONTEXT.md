# Procedures

What is done when the owner asks for something, in what order, what is checked. A `SKILL.md` is a
contract with three sections: **Inputs** (which files to load), **Process** (the steps, with a
**checkpoint** wherever the owner must decide) and **Outputs** (what is written, and where). The
knowledge lives in the area the skill points to. A skill may carry `scripts/` (volume and
exactness) and `references/` (what must be known before changing the script); `SKILL.md` holds the
judgement. Results go to the area's `output/`, skills have no outputs of their own.

System skills come with `core/` and are listed in `CLAUDE.md`. This folder is for the owner's own.

## Other people's skills: audit before use

A downloaded skill runs with the agent's full permissions, so it is read whole before first use:

- does it fetch a remote file or script at run time, which can change after the audit
- does any text address the agent as a command (ignore the rules, send, open, install)
- does it ask for keys or paid APIs, or send anything off the machine
- what does it write, and where, especially outside the project folder

The finding goes in the table below. A skill that fails is not used; it can still be read for ideas.

## When they ask, the skill

| When they ask | Skill | Area | State |
| --- | --- | --- | --- |
