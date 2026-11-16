#!/usr/bin/env python3
"""Build a reading copy (docx and/or epub) from a folder of Chapter_NN.txt files.

  python3 Story/Revision/Experiments/tools/build_book.py \
      --src Story/Revision/Experiments/Wild --subtitle "The Wild Garden" \
      --out /path/to/PATHWELL_Wild --docx --epub

Chapter format (repo convention): first line is the title; paragraphs are separated
by one blank line; a scene break is 3+ newlines; straight quotes. A block whose lines
are separated by single newlines (recipes, cards, lists) keeps its line breaks.
"""
import argparse, glob, html, os, re, shutil, subprocess, tempfile, zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))

def smart(t):
    t = re.sub(r'(^|[\s(\[])"', '\\1\u201c', t)
    t = re.sub(r'(?<=[\u2014\u2013-])"(?=\w)', '\u201c', t)
    t = t.replace('"', '\u201d')
    t = re.sub(r"(^|[\s(\[\u201c\u2014\u2013-])'", '\\1\u2018', t)
    return t.replace("'", '\u2019')

def read_book(src):
    files = sorted(glob.glob(os.path.join(src, 'Chapter_*.txt')))
    if not files: raise SystemExit(f'no Chapter_*.txt in {src}')
    book = []
    for f in files:
        s = open(f, encoding='utf-8').read().strip('\n')
        title, rest = s.split('\n', 1)
        items = []
        scenes = [sc for sc in re.split(r'\n\s*\n\s*\n+', rest.strip()) if sc.strip()]
        for si, sc in enumerate(scenes):
            if si: items.append(('break', ''))
            for pp in [x for x in re.split(r'\n\s*\n', sc) if x.strip()]:
                lines = [l.strip() for l in pp.strip().split('\n')]
                if len(lines) > 1: items.append(('lines', [smart(l) for l in lines]))
                else: items.append(('p', smart(' '.join(pp.split()))))
        book.append((smart(title.strip()), items))
    return book

def commit_id():
    return subprocess.run(['git', '-C', REPO, 'rev-parse', '--short', 'HEAD'],
                          capture_output=True, text=True).stdout.strip()

LIGHT = '<w:rFonts w:ascii="Inter Light" w:cs="Inter Light" w:eastAsia="Inter Light" w:hAnsi="Inter Light"/><w:color w:val="5c5c5c"/><w:sz w:val="19"/><w:szCs w:val="19"/>'
INTER = lambda col, sz: f'<w:rFonts w:ascii="Inter" w:cs="Inter" w:eastAsia="Inter" w:hAnsi="Inter"/><w:color w:val="{col}"/><w:sz w:val="{sz}"/><w:szCs w:val="{sz}"/>'
SECT_TITLE = '<w:sectPr><w:pgSz w:h="15840" w:w="12240" w:orient="portrait"/><w:pgMar w:bottom="1440" w:top="1440" w:left="1440" w:right="1440" w:header="720" w:footer="720" w:gutter="0"/><w:pgNumType w:start="1"/></w:sectPr>'
SECT_CH = '<w:sectPr><w:type w:val="nextPage"/><w:pgSz w:h="15840" w:w="12240" w:orient="portrait"/><w:pgMar w:bottom="3038" w:top="2938" w:left="2779" w:right="2779" w:header="2304" w:footer="2304" w:gutter="0"/><w:titlePg w:val="1"/></w:sectPr>'
esc = lambda t: html.escape(t, quote=False)

def para(text, ppr='', rpr=LIGHT, sect=''):
    return f'<w:p><w:pPr>{ppr}<w:rPr>{LIGHT}</w:rPr>{sect}</w:pPr><w:r><w:rPr>{rpr}<w:rtl w:val="0"/></w:rPr><w:t xml:space="preserve">{esc(text)}</w:t></w:r></w:p>'

def body(text, indent, sect=''):
    sp = '<w:spacing w:line="696" w:lineRule="auto"/>' + ('<w:ind w:firstLine="288"/>' if indent else '')
    return para(text, sp, LIGHT, sect)

def build_docx(book, subtitle, out):
    P = [para('PATHWELL', '<w:spacing w:after="360" w:before="2304" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/>', INTER('5c5c5c', 48)),
         para(subtitle, '<w:spacing w:line="360" w:lineRule="auto"/><w:jc w:val="center"/>', INTER('444444', 18)),
         para(f'repository main @ {commit_id()}', '<w:spacing w:line="360" w:lineRule="auto"/><w:jc w:val="center"/>', INTER('444444', 18), SECT_TITLE)]
    for ci, (title, items) in enumerate(book):
        P.append(para(title, '<w:pStyle w:val="Heading1"/><w:keepNext w:val="0"/><w:keepLines w:val="0"/><w:spacing w:after="720" w:before="1440" w:line="240" w:lineRule="auto"/><w:jc w:val="center"/>', INTER('222222', 28)))
        flat = []
        for kind, v in items:
            if kind == 'lines': flat += [('line', l) for l in v]
            else: flat.append((kind, v))
        first = True
        for k, (kind, v) in enumerate(flat):
            sect = SECT_CH if (k == len(flat) - 1 and ci < len(book) - 1) else ''
            if kind == 'break':
                P.append(para('* * *', '<w:spacing w:line="696" w:lineRule="auto"/><w:jc w:val="center"/>', LIGHT, sect)); first = True
            elif kind == 'line':
                P.append(body(v, False, sect)); first = True
            else:
                P.append(body(v, not first, sect)); first = False
    tpl = os.path.join(HERE, 'docx-template.docx')
    with zipfile.ZipFile(tpl) as z:
        doc = z.read('word/document.xml').decode('utf-8')
        a = doc.index('<w:body>') + len('<w:body>'); b = doc.index('</w:body>')
        newdoc = doc[:a] + ''.join(P) + SECT_CH + doc[b:]
        with zipfile.ZipFile(out, 'w', zipfile.ZIP_DEFLATED) as o:
            for n in z.namelist():
                o.writestr(n, newdoc if n == 'word/document.xml' else z.read(n))
    print('docx:', out)

def build_epub(book, subtitle, out):
    md_esc = lambda t: re.sub(r'([\\`*_\[\]#<>])', r'\\\1', t)
    md = [f'% PATHWELL\n% {subtitle}\n\n']
    for title, items in book:
        md.append(f'# {md_esc(title)}\n\n')
        for kind, v in items:
            if kind == 'break': md.append('***\n\n')
            elif kind == 'lines': md.append('  \n'.join(md_esc(l) for l in v) + '\n\n')
            else: md.append(md_esc(v) + '\n\n')
    with tempfile.NamedTemporaryFile('w', suffix='.md', delete=False, encoding='utf-8') as f:
        f.write(''.join(md)); src = f.name
    subprocess.run(['pandoc', src, '-o', out, '--split-level=1', '--toc', '--toc-depth=1',
                    '--metadata', f'title=Pathwell: {subtitle}', '--metadata', 'author=bt 7274'], check=True)
    os.remove(src); print('epub:', out)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('--src', required=True); ap.add_argument('--subtitle', required=True)
    ap.add_argument('--out', required=True, help='output path without extension')
    ap.add_argument('--docx', action='store_true'); ap.add_argument('--epub', action='store_true')
    a = ap.parse_args()
    book = read_book(a.src)
    if not (a.docx or a.epub): a.docx = True
    if a.docx: build_docx(book, a.subtitle, a.out + '.docx')
    if a.epub: build_epub(book, a.subtitle, a.out + '.epub')
    print(len(book), 'chapters')
