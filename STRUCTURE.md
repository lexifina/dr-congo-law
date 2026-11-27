# Structure

| Dossier | Contenu |
| --- | --- |
| `constitution/` | La Constitution du 18 février 2006, révisée par la Loi n° 11/002 du 20 janvier 2011 |
| `codes/<code>/` | Les codes : `codes/code-du-travail/`, `codes/code-de-procedure-penale/`, ... |
| `lois/<année>/<numéro>-<objet>/` | Lois et lois organiques, par année et numéro, p. ex. `lois/2023/23-049-portant-autorisation-de-la-prorogation-de-l-etat/` |
| `ordonnances-lois/<année>/...`, `decrets-lois/<année>/...` | Ordonnances-lois et décrets-lois |
| `ordonnances/<année>/...`, `decrets/<année>/...` | Ordonnances du Président de la République et décrets du Premier ministre |
| `arretes/<année>/<date>-<objet>/` | Arrêtés ministériels, interministériels et autres, par date (leurs numéros sont trop longs pour un nom de dossier) |
| `edits-provinciaux/<année>/...`, `arretes-provinciaux/<année>/<date>-<objet>/` | Édits des assemblées provinciales et arrêtés des gouverneurs de province |
| `ohada/<acte-uniforme>/` | Actes uniformes de l'OHADA en vigueur en RDC (depuis le 12 septembre 2012, date d'entrée en vigueur du Traité pour la RDC, ou depuis leur propre entrée en vigueur) |

Chaque dossier d'acte contient un fichier par article (`art-001.md` ; `art-034-bis.md` pour l'article 34 bis),
`preambule.md` (exposé des motifs, visas) et un `README.md`. Aucun dossier ne dépasse 1 000 entrées.

## Dates

Chaque version est un commit daté de 12 h 00 (Africa/Kinshasa, UTC+1) le jour de son entrée en vigueur, que répète
le trailer `In-force:`. `In-force-basis:` dit d'où vient ce jour, d'après la clause d'entrée en vigueur de l'acte :

- `promulgation` / `signature` : l'acte entre en vigueur à la date de sa promulgation ou de sa signature, soit la
  date de l'acte ;
- `publication` : à la date de sa publication au Journal officiel, dont la date est donnée par Leganet ;
- `publication+Nd` : N jours après cette publication ;
- `fixed-date` : le jour que nomme le texte.

Les actes sans clause, ou dont le jour ne peut être fixé à partir de la source, sont mis de côté. Avant 1970 (que
git ne peut dater), le commit est daté du 1er janvier 1970 et le vrai jour est dans `In-force:`. Aucune date de ce
dépôt n'est le jour où nous avons téléchargé quoi que ce soit.

## Sources

Le Journal officiel (journalofficiel.cd) pour la Constitution et les premiers codes ; Leganet (leganet.be, autrefois
leganet.cd, site associatif de l'ASBL PPDS) pour les autres actes, marqués `Source-status: secondary copy (Leganet ...)` ;
le site du Journal officiel pour les actes marqués `Source-status: official (Journal officiel ...)` ; le Journal officiel de
l'OHADA (ohada.org) pour `ohada/`. Une loi sans clause d'entrée en vigueur entre en vigueur trente jours après sa
publication au Journal officiel (Constitution, art. 142) : `In-force-basis: publication+30d (Constitution, art. 142)`.
