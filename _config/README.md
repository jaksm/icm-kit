# _config

Configure the factory, not the product: what `core/` reads about this ICM. `core/` is replaced
whole on update; this folder never is.

| File | Read by | Holds |
| --- | --- | --- |
| `labels.json` | `core/ui/build.py` | every string the components put on screen, in the owner's language; keys in `core/ui/primitives/labels.js` |
| `graph.json` | `core/workflows/graph` | labels of the graph page, plus `archive` (prefix of greyed out groups), `nested` (folders whose children are the groups, usually `["domains"]`) and `out` |
| `actions.json` | pages that use `icm-action` | the owner's own action catalog, when the default in `core/ui/actions.json` does not fit |

All optional. Without them everything is in English with default grouping.

## Your own changes to what core does

Never edit a file in `core/`: the next update refuses to run until the edit has a home outside it.

| What you want to change | Where it goes |
| --- | --- |
| the look of a page: `core/workflows/graph/template/graph-template.html`, `core/workflows/expenses/template/expenses-template.html`, `core/workflows/feed/template/feed-template.html` | a changed copy at `_config/overrides/<same path>`; the builder uses it instead of its own |
| the sync hooks of the adapter: `core/adapters/claude/hooks/session-start.sh`, `stop-sync.sh` | `_config/overrides/<same path>`. It takes effect only after the cloud setup script is generated again and pasted into the environment; a cached container keeps the old one for about a week |
| a rule of your own before every commit | an executable script in `_config/checks/`; the pre-commit hook runs each one after the core checks. A check that looks for a bare word also fires on the record that describes the rule, so match more than the word |
| a value a core script reads | its file here (`expenses.json`, `feed.json`, ...) or the environment variables set in `.githooks/pre-commit` |

Nothing else is read from `overrides/`. If what you need is not in this table, it is either a
contribution to icm-kit-core or a script of your own in `skills/`.
