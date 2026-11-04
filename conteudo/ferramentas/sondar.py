"""Dump linha a linha de um PDF com fonte, tamanho e posicao."""
import sys
from pypdf import PdfReader

alvo = sys.argv[1]
pags = [int(x) for x in sys.argv[2].split('-')] if len(sys.argv) > 2 else [1, 3]

r = PdfReader(alvo)
for npag in range(pags[0] - 1, min(pags[-1], len(r.pages))):
    pedacos = []

    def v(text, cm, tm, fd, fs, _p=pedacos):
        if not text.strip('\n'):
            return
        nome = (fd.get('/BaseFont', '?') if fd else '?').split('+')[-1]
        _p.append((round(tm[5], 1), round(tm[4], 1), nome, round(fs, 1), text))

    r.pages[npag].extract_text(visitor_text=v)
    print(f'\n{"="*78}\nPAGINA {npag+1}\n{"="*78}')
    # agrupa por linha (mesmo y, tolerancia 1.5)
    linhas = []
    for y, x, nome, fs, t in pedacos:
        for L in linhas:
            if abs(L[0] - y) < 1.5:
                L[1].append((x, nome, fs, t))
                break
        else:
            linhas.append([y, [(x, nome, fs, t)]])
    for y, ps in sorted(linhas, key=lambda L: L[0]):
        ps.sort()
        fontes = {p[1] for p in ps}
        tam = max(p[2] for p in ps)
        txt = ''.join(p[3] for p in ps).rstrip('\n')
        marca = 'C' if all('Consolas' in f for f in fontes) else ('m' if any('Consolas' in f for f in fontes) else '.')
        bold = 'B' if any('Bold' in f for f in fontes) else ' '
        print(f'y={y:6.1f} x={ps[0][0]:6.1f} {marca}{bold} {tam:5.1f} | {txt}')
