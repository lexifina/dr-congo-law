"""The Constitution of 18 February 2006: parse the two Journal officiel texts into units.

    v1  JO numéro spécial, 18 February 2006: the Constitution as promulgated.
    v2  JO numéro spécial, 5 February 2011: "textes coordonnés" as revised by Loi n° 11/002 of 20 January 2011.
"""
from __future__ import annotations

import re

from textlib import flat, norm_chars, paragraphs, pdf_text

LEGANET = 'https://www.leganet.be/Legislation'
SRC_2006 = LEGANET + '/JO/2006/JO.18.02.2006.pdf'
SRC_2011 = LEGANET + '/JO/2011/JOS.05.02.2011.pdf'
SRC_LAW_11_002 = LEGANET + '/JO/2011/JOS.01.02.2011.pdf'

HEADER = re.compile(r'^\s*(Journal Officiel\b.*Constitution.*|\d{1,3}|_{3,}|E-mail.*|Sites?\s*:.*|www\..*)\s*$', re.I)
ART = re.compile(r'^\s*Articles?\s+(\d+)(?:er|ère)?\b\s*(.*)$')
STRUCT = re.compile(r'^\s*(TITRE|Chapitre|CHAPITRE|Section|SECTION|Paragraphe|PARAGRAPHE)\s+([0-9IVX]+(?:er|ère|e)?)\s*:?\s*(.*)$')
NOTE = re.compile(r'\((?:modifiée?|révisée?)\s+par l’article.*?\)', re.I | re.S)


def _lines(url: str) -> list[str]:
    text = norm_chars(pdf_text(url))
    lines = [l for l in text.split('\n') if not HEADER.match(l)]
    return lines


def parse(url: str) -> dict[str, dict]:
    lines = _lines(url)
    start = next(i for i, l in enumerate(lines) if l.strip().startswith('Le Sénat a proposé'))
    end = next(i for i in range(start, len(lines)) if re.match(r'^\s*(Fait à Kinshasa|Joseph KABILA)', lines[i]))
    body = lines[start:end]
    # join the annotation that follows an article or heading onto one line before splitting, then drop it
    joined = '\n'.join(body)
    joined = NOTE.sub('', joined)
    body = joined.split('\n')

    units: dict[str, dict] = {}
    structure: list[str] = []
    key, label, buf = 'formule', 'Formule de promulgation', []
    kind = 'formula'

    def flush():
        if key is None:
            return
        paras = paragraphs(buf)
        if not paras:
            return
        heading = f'# {label}'
        units[key] = {'label': label, 'kind': kind, 'text': '\n'.join([heading] + paras) + '\n'}

    i = 0
    while i < len(body):
        l = body[i]
        s = l.strip()
        m = ART.match(l)
        if s == 'PREAMBULE':
            flush()
            key, label, kind, buf = 'preambule', 'Préambule', 'preamble', []
        elif m and (m.group(2).strip() == ''):
            flush()
            n = int(m.group(1))
            key, label, kind, buf = f'art-{n:03d}', 'Article 1er' if n == 1 else f'Article {n}', 'art', []
        elif STRUCT.match(l) and len(s) < 160:
            # a heading: continuation lines are indented upper-case (TITRE) or lower-case words with no full stop
            head = s
            while i + 1 < len(body):
                nxt = body[i + 1].strip()
                if not nxt or ART.match(body[i + 1]) or STRUCT.match(body[i + 1]):
                    break
                if head.endswith(('ET', 'DE', 'DES', 'DU', 'LA', 'LE', 'ou de', 'et', 'entre le pouvoir', 'de', 'des',
                                  'du', 'la', 'le', 'du', 'et de')) or (head.isupper() and nxt.isupper()):
                    head = head + ' ' + nxt
                    i += 1
                else:
                    break
            structure.append(re.sub(r'\s+', ' ', head).replace(' :', ' :'))
        else:
            buf.append(l)
        i += 1
    flush()
    units['structure'] = {'label': 'Intitulés (titres, chapitres, sections, paragraphes)', 'kind': 'structure',
                          'text': '# Intitulés\n' + '\n'.join(_tidy_heading(h) for h in structure) + '\n'}
    return units


def _tidy_heading(h: str) -> str:
    h = re.sub(r'\s*:\s*', ' : ', h, count=1)
    return re.sub(r'\s+', ' ', h).strip()


def same(a: dict, b: dict) -> bool:
    return flat(a['text']) == flat(b['text'])


if __name__ == '__main__':
    import sys
    v1, v2 = parse(SRC_2006), parse(SRC_2011)
    print(len(v1), len(v2))
    missing = [f'art-{n:03d}' for n in range(1, 230) if f'art-{n:03d}' not in v1 or f'art-{n:03d}' not in v2]
    print('missing', missing)
    diff = [k for k in sorted(set(v1) | set(v2)) if k not in v1 or k not in v2 or not same(v1[k], v2[k])]
    print('differ', diff)
    if '-v' in sys.argv:
        import difflib
        for k in diff:
            a = v1.get(k, {}).get('text', '').splitlines()
            b = v2.get(k, {}).get('text', '').splitlines()
            print('\n'.join(difflib.unified_diff(a, b, k, k, lineterm='', n=0)))
