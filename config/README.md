# config

What `core/` reads about this repo. `core/` is replaced whole on update; this folder never is.

| File | Read by | Holds |
| --- | --- | --- |
| `labels.json` | `core/ui/build.py` | every string the components put on screen, in the owner's language; keys in `core/ui/primitives/labels.js` |
| `graph.json` | `core/workflows/graph` | labels of the graph page, plus `archive` (prefix of greyed out groups), `nested` (folders whose children are the groups, usually `["domains"]`) and `out` |
| `actions.json` | pages that use `icm-action` | the owner's own action catalog, when the default in `core/ui/actions.json` does not fit |

All optional. Without them everything is in English with default grouping.
