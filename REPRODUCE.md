# How this repository was made (DR Congo)

This file is written by the build on 2026-10-28, the day the source data was retrieved. Everything below is enough to rebuild this repository hash for hash.

## Sources

| Source | Address | Retrieved | Requests | Licence |
| --- | --- | --- | ---: | --- |
| Journal officiel PDFs hosted by Leganet (leganet.be, formerly leganet.cd) | <https://www.leganet.be/JO.htm> | 2026-10-28 | 6 | Official texts; Leganet states no licence; robots.txt absent (404). |

Every response is cached by the sha256 of its URL, and the table above lists every source with its retrieval date. Lexifina keeps its fetch scripts privately; `tools/parse.py` reads only the cache and writes `corpus.json`, so the same cache always gives the same corpus.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution de la République Démocratique du Congo du 18 février 2006 | 3 | 2006-02-18 to 2011-02-05 |

The build made 3 commits:

| Commits | Kind |
| ---: | --- |
| 1 | first version of an act |
| 1 | one law on its in-force day |
| 1 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futur`: laws not yet in force on 2026-10-28.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 2 laws in the record.
- 5 tags.

## Dates

Each commit is dated at noon (Africa/Kinshasa) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: No general rule is used: each act here states its own entry into force (Constitution art. 229; Loi n° 11/002 art. 3: on promulgation). https://www.leganet.be/Legislation/JO/2006/JO.18.02.2006.pdf

## Commands, in order

```sh
# fill the cache from the sources listed above (network; Lexifina's fetch scripts are kept privately)
python -X utf8 tools/parse.py                  # cache -> corpus.json (no network)
python -X utf8 tools/build.py <folder> --repo <empty folder> --docs-date 2026-10-28
python -X utf8 tools/check_repo.py <repo> --corpus <folder>/corpus.json --write
python -X utf8 tools/build.py <folder> --repo <another empty folder> --docs-date 2026-10-28 --compare <repo>
```

In the main Lexifina repository these files live as follows:
- `fetch.py`, `parse.py` and `repo/`: in `scripts/dr-congo-law/`.
- `build.py`, `check_repo.py` (`check.py` there) and `on.py`: in `scripts/gitlaw_common/`, with the corpus format in `SCHEMA.md`.

## Exact inputs

- `corpus.json` sha256 `580a894f00f712ceeef348105f361292abf8f43d1d9f16d6bbb0c1b4d72b667d` (467929 bytes)
- Script blob hashes (`git hash-object`):

| Script | Blob |
| --- | --- |
| build.py | `2bfc4ac9df193a7be844556d7f69cdb9d93ec3f2` |
| check.py | `cd346c7ff9996d450240e3bab52bcae03b2bc865` |
| on.py | `644a6c0857fbcc72562032b58d57aa113fee0641` |
| fetch.py | `676056aa7586566a1f67f0e23c7de82034b6387c` |
| parse.py | `d2745a85cb7b7f9a823a37cdce25e0d1e6c5aebf` |

- Tools:
  - Python 3.14.0
  - git version 2.52.0.windows.1
  - curl 8.21.0 (Windows) libcurl/8.21.0 Schannel zlib/1.3.2 WinIDN WinLDAP

## Checks

3 versions of 1 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

Not yet run for this build.

These results are from the check run on the build before this one, from the same corpus.

## Decisions made by hand

- Constitution in force on 2006-02-18: art. 229, "entre en vigueur dès sa promulgation"; promulgated 18 February 2006 (JO numéro spécial).
- Loi n° 11/002 in force on 2011-01-20: its art. 3, "entre en vigueur à la date de sa promulgation"; signed 20 January 2011.
- The 2011-01-20 version is the 2006 text with the eight articles of Loi 11/002 art. 1er and the § 5 heading of art. 2 replaced by the law's own wording (JO 1 February 2011).
- The JO coordinated text of 5 February 2011 differs editorially from the promulgated wording; those differences are a separate publisher commit labelled unexplained, not credited to Loi 11/002.
- Units whose wording is identical apart from line breaks keep the earlier version's lines.
- Structural headings (titres, chapitres, sections, paragraphes) are kept in one unit, constitution/structure.
- The garbled exposé des motifs on page 1 of the JO of 1 February 2011 (broken font encoding) is not used; only the operative articles are.

## What AI did and did not do

The fetch, parse and check scripts were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above, through code that anyone can rerun.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: no model output at data-build time; parsing is rule-based (Claude Opus 5.5 wrote the scripts).
