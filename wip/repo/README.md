# DR Congo: law history in git

The law of the Democratic Republic of the Congo as a git history. Each provision is one file, each law gets one commit on the day it took effect, and the law that made each change is the commit's author. `git blame` names the law behind every paragraph, `git log` lists every change to an article, and `tools/en_vigueur_au.py` gives the text in force on any day.

It follows the shared design of [lexifina/global-law](https://github.com/lexifina/global-law), which places it at `cd/`.

**What is in it now**

| Folder | Act | Versions | History |
| --- | --- | ---: | --- |
| `constitution/` | Constitution de la République Démocratique du Congo du 18 février 2006 | 3 | As promulgated, in force 18 February 2006; revised by Loi n° 11/002, in force 20 January 2011 (8 articles and one heading); the Journal officiel's coordinated text of 5 February 2011 |

The per-act `README.md` in each folder lists every provision, how often it changed and when.

**Why only the Constitution.** The Journal officiel (journalofficiel.cd) is the only official source, and it is not consolidated: it sells each issue as a PDF and keeps no dated versions. The history here is rebuilt from three dated Journal officiel issues that Leganet hosts as PDFs with a text layer. The Constitution has been revised once, by Loi n° 11/002 of 20 January 2011, so three versions make its whole history. Other acts (the Code pénal, the Code de la famille) need every amending law's own Journal officiel issue, and these have not been sourced and checked yet.

## A lawyer's questions as git commands

| Question | Command |
| --- | --- |
| What did art. 71 say on 1 January 2011? | `python tools/en_vigueur_au.py 2011-01-01 constitution 71` |
| The same, with raw git (bash) | `git show $(git rev-list -1 --before="2011-01-01T23:59:59Z" main -- constitution/art-071.md):constitution/art-071.md` |
| The same, in PowerShell | `$r = git rev-list -1 --before="2011-01-01T23:59:59Z" main -- constitution/art-071.md; git show "$($r):constitution/art-071.md"` |
| Which law wrote each paragraph of art. 71? | `git blame constitution/art-071.md` |
| Every change to an article, word by word | `git log -p --word-diff constitution/art-071.md` |
| Every law in the record, in order | `git log --reverse --format="%ad %an" --date=short main` |
| Everything one law changed | `git show law/loi-11-002` (tags `law/<key>` mark each law's commit) |
| The whole Constitution on a date | `python tools/en_vigueur_au.py 2007-01-01 constitution` |
| Which law gave a provision its wording on a date | `python tools/en_vigueur_au.py --law 2012-01-01 constitution 226` |

After a rebuild, refresh tags with `git fetch --force --tags`: a plain fetch keeps stale tags.

## Dates

- Each commit is dated at **noon, Africa/Kinshasa, on the day the change took effect**. The day is also in the `In-force:` trailer, which the tools read; the signature date is the `Enacted:` trailer.
- **The Constitution fixes its own entry into force** (art. 229): it "entre en vigueur dès sa promulgation par le Président de la République". It was promulgated on 18 February 2006 ("Fait à Kinshasa, le 18 février 2006").
- **Loi n° 11/002 fixes its own too** (art. 3): it "entre en vigueur à la date de sa promulgation", 20 January 2011. It was published in the Journal officiel of 1 February 2011.
- **The coordinated text is dated 5 February 2011**, the date of the Journal officiel numéro spécial that published it. It is a publisher's text, not a law.
- `--before="YYYY-MM-DD"` alone uses your clock's time of day, so a law that took effect that day may be missed before noon. Use `T23:59:59Z` as above, or the tool.

## How it is checked

- Every version is read back from git on the day it took effect and on the day before (`tools/check_repo.py`); both must match `corpus.json`. Results are in `REPRODUCE.md`.
- **Today's text against the Journal officiel's own site:** journalofficiel.cd publishes the coordinated text of 5 February 2011 marked as in force. 901 of the 906 paragraphs of today's text appear in it word for word. The other 5 differ only where the site's own copy is broken: a closing full stop is missing before the next article, or a passage of another article is spliced in (`tools/verify_jo.py`).
- **Two copies of one issue.** Leganet holds two PDFs that both carry the heading of the Journal officiel numéro spécial of 5 February 2011, and they differ in punctuation, capitals and small words in 83 articles. The Journal officiel's site agrees with one of them (a Word export of April 2011) in 78 of those articles and with the other (a reprint made in 2012) in none, so the first is used.
- **Nothing dropped:** every paragraph of the 2006 and 2011 texts, from the promulgation formula to the last article, is in a provision file word for word; only article labels, page headers, the table of contents and the appended exposé des motifs are left out.
- The repository is rebuilt from the same data a second time and must give identical hashes.

## What "author" means

The author of a commit is the law that made the change, with an e-mail address that cannot exist, so `git blame` and `git log --author` name laws. The committer is always Lexifina.

- **The first commit** is the Constitution as promulgated, credited to the Constitution of 18 February 2006 (adopted by the referendum of 18 and 19 December 2005).
- **The 2011 revision commit** holds exactly what Loi n° 11/002 rewrote: articles 71, 110, 126, 149, 197, 198, 218 and 226 (its art. 1er), and the heading of paragraph 5 (its art. 2), in the law's own wording.
- **The 5 February 2011 commit** is the Journal officiel's coordinated text. It differs from the promulgated wording in 55 provisions, by punctuation, capitals, spelling and a few small words such as articles and conjunctions. No law made those differences, so the commit is authored by the Journal officiel and labelled "unexplained". Six of the 2011 law's articles (126, 149, 197, 198, 218 and 226) read slightly differently in the coordinated text than in the law itself, and those differences are in this commit too.
- Blame credits whole lines (one paragraph per line). Use `git log -p --word-diff` to see exactly which words each change made.

## What it does not show

- **Only the Constitution of 2006.** Earlier constitutions (1960, 1964, 1967, the transition constitution of 2003) are not in this record.
- **Headings** (Titre, Chapitre, Section, Paragraphe) are kept together in one file, `constitution/structure.md`. The promulgation formula is `constitution/formule.md`.
- **The exposé des motifs** of the Constitution and of Loi n° 11/002 is left out: it is not operative text, and page 1 of the 1 February 2011 issue has a broken font encoding.
- **No OCR.** Texts published only as scanned images are not included.

## How it is built

`tools/fetch.py` downloads each source once with curl, at no more than three requests a second per host, cached by the sha256 of its URL. `tools/parse.py` reads only the cache: `tools/textlib.py` turns the PDFs' text layer into paragraphs (poppler's `pdftotext -layout`; PyMuPDF for the two-column issue of 1 February 2011), `tools/constitution.py` splits them into articles and applies Loi n° 11/002, and parse.py writes `corpus.json`; the shared builder `tools/build.py` turns that into the commits. `REPRODUCE.md` lists every source, command, tool version and decision, and the result of the hash-for-hash rebuild.

## Sources

| Source | What it gives | Used for |
| --- | --- | --- |
| [Leganet, Journal officiel numéro spécial, 18 February 2006](https://www.leganet.be/Legislation/JO/2006/JO.18.02.2006.pdf) | The Constitution as promulgated (PDF with a text layer) | Version 1 |
| [Leganet, Journal officiel numéro spécial, 1 February 2011](https://www.leganet.be/Legislation/JO/2011/JOS.01.02.2011.pdf) | Loi n° 11/002 du 20 janvier 2011 portant révision de certains articles de la Constitution | Version 2 and its credits |
| [Leganet, Journal officiel numéro spécial, 5 February 2011](https://www.leganet.be/Legislation/Droit%20Public/Constitution.2011.pdf) | The Constitution as revised by Loi n° 11/002 (textes coordonnés) | Version 3 |
| [Journal officiel de la RDC](https://journalofficiel.cd/textes-phares/constitution) | The official gazette; its site shows the coordinated text marked in force | Checking today's text; not consolidated, no dated versions |
| [Leganet, JO/2011/JOS.05.02.2011.pdf](https://www.leganet.be/Legislation/JO/2011/JOS.05.02.2011.pdf) | A 2012 reprint of the 5 February 2011 issue | Not used: it differs from the Journal officiel's own text in 83 articles |

Research guides that cover every country: [GlobaLex](https://www.nyulawglobal.org/globalex/) and the [Law Library of Congress Guide to Law Online](https://www.loc.gov/research-centers/law-library-of-congress/researcher-resources/guide-to-law-online/).

## Licence

See [LICENSE](LICENSE). Texts: Journal officiel de la République Démocratique du Congo (official texts), from the copies hosted by Leganet (www.leganet.be), reproduced with that attribution. Lexifina's arrangement, messages, tables and tools are CC0.

This repository is not legal advice.

## En français

Ce dépôt retrace l’histoire de la Constitution de la République Démocratique du Congo du 18 février 2006 dans git : un fichier par article, un commit par loi à la date de son entrée en vigueur, et la loi qui a modifié le texte comme auteur du commit. Il contient trois versions : le texte promulgué le 18 février 2006 (Journal officiel, numéro spécial du 18 février 2006), le texte révisé par la loi n° 11/002 du 20 janvier 2011, entrée en vigueur à sa promulgation (articles 71, 110, 126, 149, 197, 198, 218 et 226, et l’intitulé du paragraphe 5), et les textes coordonnés publiés au Journal officiel du 5 février 2011, dont les différences de forme avec le texte promulgué sont attribuées au Journal officiel. Le texte actuel a été vérifié contre celui du site journalofficiel.cd. `python tools/en_vigueur_au.py 2011-01-01 constitution 71` affiche l’article 71 tel qu’il était en vigueur à cette date, et `git blame constitution/art-071.md` nomme la loi à l’origine de chaque alinéa. Ce dépôt ne constitue pas un avis juridique.
