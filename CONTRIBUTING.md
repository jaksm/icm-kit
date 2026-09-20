# Working on the kit

Three repos, one product:

| Repo | Holds |
| --- | --- |
| [icm-kit](https://github.com/jaksm/icm-kit) | the template a new ICM is cloned from, this landing page and these docs |
| [icm-kit-core](https://github.com/jaksm/icm-kit-core) | everything vendored into `core/`: checks, adapters, setup, the workflow catalog, migrations |
| [icm-ui](https://github.com/jaksm/icm-ui) | the component library for pages, vendored into core by `sync-ui.sh` |

Never edit `core/` here: change icm-kit-core, then `<icm-kit-core>/install.sh <this clone>`.

This clone has the push guard on and the kit's own remote is a plain one, so push it with
`git -c core.hooksPath=/dev/null push`.

After changing `setup-prompt.md` or `docs/providers.md`, run `python3 site/build.py`; the commit
hook refuses a landing page that is stale. Numbers in `docs/providers.md` come from the provider's
own pages only, each with its link and the date it was checked.

Everything is English, names no person and no personal data, and nothing outside `core/adapters/`
names a harness.
