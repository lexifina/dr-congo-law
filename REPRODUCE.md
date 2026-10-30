# How this repository was made (DR Congo)

This file is written by the build on 2026-10-30, the day the source data was retrieved.

## Sources

| Source | Address | Retrieved | Licence |
| --- | --- | --- | --- |
| Journal officiel PDFs hosted by Leganet (leganet.be, formerly leganet.cd) | <https://www.leganet.be/JO.htm> | 2026-10-28 | Official texts; Leganet states no licence. |
| Journal officiel de la RDC (journalofficiel.cd), Textes phares: Constitution | <https://journalofficiel.cd/textes-phares/constitution> | 2026-10-29 | Official text; the site states no licence. |
| Journal officiel de la RDC (journalofficiel.cd), Textes phares: codes en vigueur | <https://journalofficiel.cd/textes-phares/codes-en-vigueur> | 2026-10-30 | Official text; the site states no licence. |
| Leganet (leganet.be): copy of the J.O. numéro spécial du 12 mars 2024 | <https://www.leganet.be/Legislation/JO/2024/JOS%2012.03.2024.Code.de.procedure.penale.LEGANET.2024.pdf> | 2026-10-30 | Official text; Leganet states no licence. |
| Journal officiel, numéro spécial du 25 octobre 2002 (Code du travail), hosted by Leganet | <https://www.leganet.be/Legislation/DroitSocial/Code_travail.pdf> | 2026-10-30 | Official text; Leganet states no licence. |
| Leganet (leganet.be): HTML edition of Loi n° 015/2002 | <https://www.leganet.be/Legislation/DroitSocial/Code%20du%20travail.%20loi.2002.htm> | 2026-10-30 | Leganet states no licence. |

Every word of law in this repository comes from these sources. Lexifina reads them and records each act's dated versions, and the laws that made each change, in one corpus file. This repository is built from that file.

## What is in it

| Act | Title | Versions | Span |
| --- | --- | ---: | --- |
| `constitution` | Constitution de la République Démocratique du Congo du 18 février 2006 | 3 | 2006-02-18 to 2011-02-05 |
| `code-procedure-penale` | Décret du 6 août 1959 portant Code de procédure pénale | 1 | 2024-03-12 to 2024-03-12 |
| `code-du-travail` | Loi n° 015/2002 du 16 octobre 2002 portant Code du travail | 1 | 2002-10-16 to 2002-10-16 |

The build made 5 commits:

| Commits | Kind |
| ---: | --- |
| 3 | first version of an act |
| 1 | one law on its in-force day |
| 1 | changes no amendment note explains, credited to the publisher |

Other counts:
- 0 commits on the branch `futur`: laws not yet in force on 2026-10-30.
- 0 commits dated 1 January 1970: in force before 1970, with the real day in their `In-force` trailer.
- 15 laws in the record.
- 8 tags.

## Dates

Each commit is dated at noon (Africa/Kinshasa) on the day the change took effect. The other dates, enacted and published, are trailers.

When a law gives no date of its own, the default rule applies: No general rule is used: each act here states its own entry into force (Constitution art. 229; Loi n° 11/002 art. 3: on promulgation). https://www.leganet.be/Legislation/JO/2006/JO.18.02.2006.pdf

## How the history is built

`tools/build.py` turns the corpus into this history in one pass: one commit per law, on the day it took effect. The same corpus always gives the same commit hashes. `tools/check_repo.py` reads every version back from git and compares it with the corpus. `tools/on.py` shows the law as it stood on any date. The corpus format is described in `tools/SCHEMA.md`.

- Corpus: sha256 `6bb3f9cf6b113f0238580bab3011b90770cbc2820dcb866ca6971140faf3a192` (832104 bytes).
- Builder blob hashes (`git hash-object`): `build.py` `a4faa25af85facb64b956b372f6b528aafdd7ec1`, `check.py` `3d00541d258745461ab52b1b0cb4e1716a27a95d`, `on.py` `644a6c0857fbcc72562032b58d57aa113fee0641`.
- Python 3.12.10; git version 2.46.0.windows.1.

## Checks

5 versions of 3 acts read back from git on the day each took effect and on the day before: 0 mismatches. Trailers: 0 commits whose trailers git cannot parse. Health: 0 merge commits on main, 0 commit dates that go backwards, 0 commits dated after the build.

A second build from the same corpus into an empty folder gave identical hashes for all 5 history commits and 8 tags (history tip `0bd4ffb44caad4ad22a3d0409936c211251b753d`).

## Decisions made by hand

- Constitution in force on 2006-02-18: art. 229, "entre en vigueur dès sa promulgation"; promulgated 18 February 2006 (JO numéro spécial).
- Loi n° 11/002 in force on 2011-01-20: its art. 3, "entre en vigueur à la date de sa promulgation"; signed 20 January 2011.
- The 2011-01-20 version is the 2006 text with the eight articles of Loi 11/002 art. 1er and the § 5 heading of art. 2 replaced by the law's own wording (JO 1 February 2011).
- The JO coordinated text of 5 February 2011 differs editorially from the promulgated wording; those differences are a separate publisher commit labelled unexplained, not credited to Loi 11/002.
- The 2011-02-05 version is read from Leganet's Droit Public/Constitution.2011.pdf, not from its JO/2011/JOS.05.02.2011.pdf: both carry the header of the JO numéro spécial of 5 February 2011 but differ in 83 units, and the Journal officiel's own site text agrees with the first in 78 of them and with the second (a 2012 reprint) in none.
- Checked against the Journal officiel's site text: 901 of 906 paragraphs of the 2011-02-05 version appear verbatim; the other 5 differ only where the site's own text is broken (a final full stop missing before the next article, or another article's text spliced in).
- A paragraph or heading that ends on a word such as "à", "de", "les", "au" or "cette" continues on the next line, across a blank line or page break (Constitution art. 119, 153, 200 heading, § 3 heading).
- Units whose wording is identical apart from line breaks keep the earlier version's lines.
- Structural headings (titres, chapitres, sections, paragraphes) are kept in one unit, constitution/structure.
- The garbled exposé des motifs on page 1 of the JO of 1 February 2011 (broken font encoding) is not used; only the operative articles are.
- Code de procédure pénale: one version, the Journal officiel's coordinated text (J.O. numéro spécial du 12 mars 2024, "mise à jour au 12 mars 2024"), dated 2024-03-12 and credited to the Journal officiel as the oldest version available; the twelve amending texts its own list names are recorded as earlier laws, because their own J.O. issues were not sourced.
- Code de procédure pénale: the bracketed notes after article numbers ("ajouté par …", "modifié par …") are part of the coordinated text and are kept in each article's heading line.
- Code de procédure pénale: the coordinated text's title block and list of amending texts form the unit "intitule"; chapter, section and numbered sub-headings form the unit "structure".
- Code du travail: one version, Loi n° 015/2002 as promulgated, read from the Journal officiel numéro spécial du 25 octobre 2002 and dated 2002-10-16 by its art. 334 ("entre en vigueur à la date de sa promulgation"; "Fait à Kinshasa, le 16 octobre 2002").
- Code du travail: Loi n° 16/010 du 15 juillet 2016 (arts. 1er, 6, 7, 62, 119, 121, 125, 129, 190, 216 to 219, 241 and 321 rewritten; arts. 61 bis and 61 ter added) is not applied: it enters into force thirty days after its publication in the Journal officiel, and that issue and its date were not sourced. The last version here is therefore the 2002 text, not today’s.
- Code du travail: misprints in the Journal officiel issue are kept as printed (for example art. 117 "Dute forme de drogue", art. 125 "1es établissements" and "de 19 heures à 17 heures", art. 147 "d’un(période", the formula’s "1a loi"); Leganet’s HTML edition reads differently in 44 paragraphs, all such misprints, "oe"/"œ" spellings or small words.
- Code du travail: the two-column layout is read column by column; a paragraph ends at a line ending in . ; : ! or ?, or before a list item; the signature block printed beside arts. 332 to 334 is the unit "signature".

## What AI did and did not do

The scripts that read the sources and build this repository were written by Claude Code running Claude Opus 5.5 (`claude-opus-5-5`) under Lexifina's direction.

No model wrote, translated or corrected legal text. No model runs at build time. Every word of law in this repository comes from the official sources above.

The commit messages are written by `build.py` from the source data.

Model use at data-build time:
- none: no model output at data-build time; parsing is rule-based (Claude Opus 5.5 wrote the scripts).
