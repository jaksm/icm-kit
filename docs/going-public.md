# Before the three repos go public

Nothing here is automatic. Each line is checked by a person, on the day.

- [ ] The maintainer's scan of all three repos for personal terms, secrets and non-English text reports 0 findings.
- [ ] `git log --format='%ae %an' | sort -u` in each repo shows only the GitHub noreply address.
- [ ] `git log -p` of each repo searched for the maintainer's personal terms: history, not only the tree.
- [ ] `LICENSE` is present in all three, and `README.md` in each links the other two.
- [ ] Every link and retention sentence in `docs/providers.md` was opened and checked that day; the date in the file is that day. It holds no prices.
- [ ] `python3 build.py --check` passes in icm-kit-site; the landing page was opened at phone width; Copy puts the exact prompt on the clipboard.
- [ ] A fresh agent, given only the public URLs, completes setup steps 01 to 03 in an empty folder.
- [ ] Order of switching: icm-ui, then icm-kit-core, then icm-kit, then icm-kit-site, so no public page links to a private one.
- [ ] GitHub Pages serves icm-kit-site; the link in `README.md` points at the Pages URL.
- [ ] Private vulnerability reporting is on for all three.
