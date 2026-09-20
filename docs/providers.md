# Providers: what they keep, and which subscription

icm-kit is provider agnostic by design: everything specific to a harness lives in
`core/adapters/<name>/`. **One adapter exists today, for Claude Code.** This record is the canonical
source for the landing page (`site/build.py` copies the marked blocks), so a fact is changed here and
nowhere else.

No prices are written here on purpose. They change, and a stale price is worse than a link.

## What each provider keeps

Checked 2026-09-20, on the provider's own pages only. Terms change: open the link before you rely on a line.

<!-- site:retention -->
| Provider | Used to train models | What is kept, and how long | The setting |
| --- | --- | --- | --- |
| Anthropic (Claude, Claude Code, cloud sessions) | only if you allow it; you are asked to choose | 30 days if you do not allow model improvement, up to 5 years if you do; content flagged for a policy violation up to 2 years. [Claude Code data usage](https://code.claude.com/docs/en/data-usage), [How long do you store my data?](https://privacy.claude.com/en/articles/10023548-how-long-do-you-store-my-data) | [claude.ai/settings/data-privacy-controls](https://claude.ai/settings/data-privacy-controls) |
| OpenAI (ChatGPT, Codex on a personal plan) | yes by default, with an opt-out that also covers Codex | chats stay until you delete them; a deleted chat is scheduled for permanent deletion within 30 days, with exceptions. [Chat and file retention](https://help.openai.com/en/articles/8983778-chat-and-file-retention-policies-in-chatgpt) | Settings, Data Controls, "Improve the model for everyone": [Data Controls FAQ](https://help.openai.com/en/articles/7730893-data-controls-faq) |
| Google Antigravity (individual) | yes by default, and people at Google may review interactions | no retention period is stated in the terms or the FAQ. [Terms](https://antigravity.google/terms) | an opt-out in the Settings panel: [FAQ](https://antigravity.google/docs/faq) |
| Ollama, run locally | no | nothing leaves your computer: "We don't see your prompts or data when you run locally." Its cloud models are a different product with different terms. [FAQ](https://docs.ollama.com/faq) | none needed |
<!-- /site:retention -->

## Which subscription

<!-- site:plans -->
| Provider | Works with icm-kit today | Which plan | Prices |
| --- | --- | --- | --- |
| Claude | **yes**: Claude Code on your computer, cloud sessions and the mobile app | the entry paid plan is enough to start; it includes Claude Code and cloud sessions, which the free plan does not. Move up when you hit the limits, not before | [claude.com/pricing](https://claude.com/pricing) |
| ChatGPT with Codex | adapter planned | Codex is included in the personal plans, with limits that grow by plan | [chatgpt.com/pricing](https://chatgpt.com/pricing) |
| Google Antigravity | adapter planned | there is a free individual tier; the Google AI plans raise the limits | [antigravity.google/pricing](https://antigravity.google/pricing) |
| Ollama and other local models | untested | free software; the cost is the computer. It is the one setup where the provider question goes away | [ollama.com](https://ollama.com) |
<!-- /site:plans -->

## The maintainer's opinion

Experience of one person using these daily through 2026, not a benchmark. It will age.

<!-- site:opinion -->
**Claude**, entry paid plan: the best place to start, and excellent for people who are not technical. To my eye it has the smartest models available today, and an ICM lives on judgement more than on volume.
**Codex**, entry paid plan: more usage for the same money, and in my experience drastically less clever.
**Antigravity**, a mid-priced plan: a lot more usage and a very fast model, and the weakest judgement of the three.
**Ollama and local models**: I have not tested them with the kit. They are worth watching, because they solve the privacy question outright.
<!-- /site:opinion -->

## Checking this record again

With every release, and before the repos go public: open every link above, read the sentence it
supports, and change the date. If a page no longer says it, the line goes or is rewritten; nothing
here is kept on memory. Anything that could not be confirmed on the provider's own page is written
as not stated, never guessed.
