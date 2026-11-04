"""
Reconstroi a fonte de um tutorial a partir do PDF que o portal imprimiu.

O layout do portal e regular o bastante para ser lido de volta: a fonte diz se
o trecho e codigo (Consolas) ou prosa (Arial), o tamanho do corpo diz o papel
da linha e o x diz o recuo. Este script devolve o Markdown de autoria.

Rode isto so contra um PDF impresso pelo portal antigo. Um PDF ja gerado a
partir de conteudo/tutoriais/ nao volta igual: extrair dele sobrescreve a
fonte boa com uma copia degradada.

Uso: python extrair.py pdf/of-markdown.pdf conteudo/tutoriais
"""
import os
import re
import sys

from pypdf import PdfReader
from pypdf.generic import ContentStream

# ------------------------------------------------------------------ estilos
# Tamanhos medidos nos PDFs prontos. Variam um pouco de um documento para
# outro, entao toda comparacao passa por perto().
TITULO = 36.0
LEAD = 15.3
ETAPA_TIT = 22.7
ETAPA_NUM = 16.0      # Consolas negrito
SUBTITULO = 14.7      # subtitulo da etapa (leve) e sub-heading (negrito)
CORPO = 14.0
SECAO = 13.3          # caixa alta, e o aviso "Confira antes de seguir"
TAB_CEL = 13.1
LEGENDA = 12.0
TAB_CAB = 11.3        # Arial negrito

TOL = 0.45

# O portal imprime cada pagina num espaco de 1000 unidades de texto.
PAGINA_TEXTO = 1000.0

EXT_ARQUIVO = r'html|css|js|mjs|py|json|md|txt|sql|env|example|cfg|toml|ini'
RE_ROTULO = re.compile(r'^[\w.\-/]+\.(?:' + EXT_ARQUIVO + r')\b')


def perto(a, b, tol=TOL):
    return abs(a - b) <= tol


# ------------------------------------------------------------------ leitura


def ler_pedacos(caminho):
    """[(pagina, y, x, fonte, tamanho, texto)] na ordem em que foram pintados."""
    r = PdfReader(caminho)
    out = []
    for n, pag in enumerate(r.pages):
        buf = []

        def v(text, cm, tm, fd, fs, _b=buf):
            # trechos so de espaco carregam o recuo do codigo: nao descartar
            if not text.strip(chr(10)):
                return
            nome = (fd.get('/BaseFont', '?') if fd else '?').split('+')[-1]
            _b.append((round(tm[5], 1), round(tm[4], 1), nome, round(fs, 1), text))

        pag.extract_text(visitor_text=v)
        for y, x, nome, fs, t in buf:
            out.append((n, y, x, nome, fs, t))
    return out


def agrupar_linhas(pedacos):
    """Junta os pedacos que dividem a mesma linha de base."""
    linhas = []
    for pag, y, x, nome, fs, t in pedacos:
        for L in linhas:
            if L['pag'] == pag and abs(L['y'] - y) < 1.5:
                L['run'].append((x, nome, fs, t))
                break
        else:
            linhas.append({'pag': pag, 'y': y, 'run': [(x, nome, fs, t)]})
    for L in linhas:
        L['run'].sort(key=lambda p: p[0])
        L['x'] = L['run'][0][0]
        L['fs'] = max(p[2] for p in L['run'])
        L['mono'] = all('Consolas' in p[1] for p in L['run'])
        L['misto'] = any('Consolas' in p[1] for p in L['run'])
        L['bold'] = any('Bold' in p[1] for p in L['run'])
        L['txt'] = ''.join(p[3] for p in L['run']).rstrip(chr(10))
        L['figura'] = None
    linhas.sort(key=lambda L: (L['pag'], L['y']))
    return linhas


def imagens_posicionadas(caminho):
    """Figuras na ordem do fluxo. Duas no mesmo topo sao uma figura lado a lado."""
    r = PdfReader(caminho)
    achadas = []
    ordem = 0
    for n, pag in enumerate(r.pages):
        rec = pag.get('/Resources', {})
        xo = rec.get('/XObject', {}) if rec else {}
        nomes = {k for k in xo.keys() if xo[k].get('/Subtype') == '/Image'} if xo else set()
        if not nomes:
            continue
        altura = float(pag.mediabox.height)
        escala = PAGINA_TEXTO / altura
        cs = ContentStream(pag.get_contents(), r)
        ctm = [1, 0, 0, 1, 0, 0]
        pilha = []
        for ops, op in cs.operations:
            if op == b'q':
                pilha.append(list(ctm))
            elif op == b'Q':
                if pilha:
                    ctm = pilha.pop()
            elif op == b'cm':
                a, b, c, d, e, f = [float(v) for v in ops]
                A, B, C, D, E, F = ctm
                ctm = [a * A + b * C, a * B + b * D,
                       c * A + d * C, c * B + d * D,
                       e * A + f * C + E, e * B + f * D + F]
            elif op == b'Do' and str(ops[0]) in nomes:
                ordem += 1
                topo = (altura - (ctm[5] + ctm[3])) * escala + n * PAGINA_TEXTO
                achadas.append({'y': topo, 'pag': n, 'x': ctm[4], 'n': ordem,
                                'obj': xo[str(ops[0])]})
    figuras = []
    for im in sorted(achadas, key=lambda i: (i['y'], i['x'])):
        if figuras and abs(figuras[-1]['y'] - im['y']) < 4:
            figuras[-1]['ns'].append(im['n'])
            figuras[-1]['objs'].append(im['obj'])
        else:
            figuras.append({'y': im['y'], 'pag': im['pag'],
                            'ns': [im['n']], 'objs': [im['obj']]})
    return figuras


# ------------------------------------------------------------------ prosa


def com_crases(run):
    """Prosa marcada: Consolas vira `codigo` e o italico vira *enfase*."""
    partes = []
    for x, nome, fs, t in run:
        t = t.rstrip(chr(10))
        if 'Consolas' in nome:
            miolo = t.strip()
            if miolo:
                # o portal poe um respiro em volta do codigo; ele fica fora
                # da marca, senao as palavras vizinhas grudam
                antes = ' ' if t[:1].isspace() else ''
                depois = ' ' if t[-1:].isspace() else ''
                partes.append(antes + '`' + miolo + '`' + depois)
        elif 'Italic' in nome or 'Oblique' in nome:
            miolo = t.strip()
            if miolo:
                # o espaco que sobrou fica fora da marca, senao ela nao fecha
                antes = ' ' if t[:1].isspace() else ''
                depois = ' ' if t[-1:].isspace() else ''
                partes.append(antes + '*' + miolo + '*' + depois)
        else:
            partes.append(t)
    s = ''.join(partes)
    s = s.replace('``', '').replace('**', '')   # marcas coladas por quebra de run
    s = re.sub(r'[ \t]+', ' ', s)
    # o respiro do codigo virou espaco na extracao; antes de pontuacao ele
    # nao existia na tela — quem o desenha de volta e o padding do CSS
    s = re.sub(r'`\s+([,.;:!?)\]])', r'`\1', s)
    return s.strip()


# ------------------------------------------------------------------ codigo


def e_rotulo(L, prox):
    """Nome de arquivo isolado logo acima de um bloco de codigo."""
    if not L['mono'] or len(L['run']) != 1:
        return False
    txt = L['txt'].strip()
    if not RE_ROTULO.match(txt):
        return False
    # o rotulo fica mais a esquerda e destacado do bloco que anuncia
    return prox is not None and prox['mono'] and prox['y'] - L['y'] > 25


def juntar_codigo(linhas, i):
    """Consome um bloco de codigo. Linha em branco vem do salto no y."""
    corpo = []
    passo = None
    ant = None
    base = linhas[i]['fs']
    while i < len(linhas):
        L = linhas[i]
        prox = linhas[i + 1] if i + 1 < len(linhas) else None
        if not L['mono'] or not perto(L['fs'], base, 0.6):
            break
        if e_rotulo(L, prox):
            break
        if ant is not None and L['pag'] == linhas[i - 1]['pag']:
            salto = L['y'] - ant
            if passo is None and salto > 0:
                passo = salto
            if passo and salto > passo * 1.6:
                corpo.extend([''] * round(salto / passo - 1))
        corpo.append(L['txt'])
        ant = L['y']
        i += 1
    while corpo and not corpo[-1].strip():
        corpo.pop()
    return corpo, i


def e_arvore(corpo):
    return any(('├──' in l or '└──' in l or '│' in l) for l in corpo)


# ------------------------------------------------------------------ tabelas


def cortes_de_coluna(run_cab):
    xs = [run_cab[0][0]]
    for k in range(1, len(run_cab)):
        if run_cab[k][0] - run_cab[k - 1][0] > 40:
            xs.append(run_cab[k][0])
    return xs


def celulas(run, cortes):
    cols = [[] for _ in cortes]
    for p in run:
        alvo = 0
        for k, c in enumerate(cortes):
            if p[0] >= c - 2:
                alvo = k
        cols[alvo].append(p)
    return [com_crases(c) for c in cols]


# ------------------------------------------------------------------ extracao


def extrair(caminho, destino, exts=None):
    ident = os.path.basename(caminho).replace('.pdf', '')
    linhas = agrupar_linhas(ler_pedacos(caminho))
    for fig in imagens_posicionadas(caminho):
        linhas.append({'pag': fig['pag'], 'y': fig['y'], 'run': [], 'x': 0.0,
                       'fs': 0.0, 'mono': False, 'misto': False, 'bold': False,
                       'txt': '', 'figura': fig['ns']})
    linhas.sort(key=lambda L: (L['pag'], L['y']))

    out = []
    meta = {'id': ident}
    n_fig = 0
    i = 0
    total = len(linhas)

    while i < total:
        L = linhas[i]
        fs, x, txt = L['fs'], L['x'], L['txt']
        prox = linhas[i + 1] if i + 1 < total else None

        # ---------------------------------------------------------- figura
        if L['figura']:
            i += 1
            legenda = ''
            if i < total and perto(linhas[i]['fs'], LEGENDA, 0.3) and not linhas[i]['mono']:
                bloco = []
                while i < total and perto(linhas[i]['fs'], LEGENDA, 0.3) and not linhas[i]['mono']:
                    bloco.append(com_crases(linhas[i]['run']))
                    i += 1
                legenda = ' '.join(bloco)
            arqs = ' '.join(
                'img/%s-%d%s' % (ident, k, exts[k - 1] if exts else '.png')
                for k in L['figura'])
            n_fig += len(L['figura'])
            out.append('\n![%s](%s)' % (legenda, arqs))
            continue

        # ---------------------------------------------------------- rodape
        if txt.startswith('Caminho da Programação ·'):
            bloco = [com_crases(L['run'])]
            i += 1
            while i < total and perto(linhas[i]['fs'], fs, 0.4) and linhas[i]['mono']:
                bloco.append(com_crases(linhas[i]['run']))
                i += 1
            meta['rodape'] = ' '.join(bloco).replace('`', '')
            continue

        # ---------------------------------------------------------- cabecalho
        if perto(fs, TITULO, 1.0) and L['bold']:
            meta['titulo'] = txt.strip()
            i += 1
            continue

        if L['mono'] and x < 5 and '·' in txt and 'OFICINA' in txt.upper():
            meta['kicker'] = txt.strip()
            i += 1
            continue

        if perto(fs, LEAD, 0.5):
            bloco = []
            while i < total and perto(linhas[i]['fs'], LEAD, 0.5):
                bloco.append(com_crases(linhas[i]['run']))
                i += 1
            out.append('> ' + ' '.join(bloco))
            continue

        # ---------------------------------------------------------- etapa
        # O numero da etapa e os simbolos dos blocos finais (✓ ! →) usam a
        # mesma marca a esquerda de um titulo grande.
        if perto(fs, ETAPA_NUM, 0.5) and x < 15 and len(txt.strip()) <= 3 \
                and prox is not None and perto(prox['fs'], ETAPA_TIT, 0.7):
            marca = txt.strip()
            tit = prox['txt'].strip()
            junta = '%s. %s' % (marca, tit) if marca.isdigit() else '%s %s' % (marca, tit)
            out.append('\n### ' + junta)
            i += 2
            continue

        # ---------------------------------------------------------- codigo
        if L['mono'] and fs < 13.6:
            rotulo = None
            if e_rotulo(L, prox):
                rotulo = txt.strip()
                i += 1
            corpo, j = juntar_codigo(linhas, i)
            if corpo:
                if e_arvore(corpo):
                    out.append('\n~~~arvore\n' + '\n'.join(corpo) + '\n~~~')
                elif rotulo:
                    out.append('\n~~~arquivo %s\n' % rotulo + '\n'.join(corpo) + '\n~~~')
                else:
                    out.append('\n~~~codigo\n' + '\n'.join(corpo) + '\n~~~')
                i = j
                continue
            if rotulo:
                out.append('\n~~~arquivo %s\n~~~' % rotulo)
                continue

        # ---------------------------------------------------------- subtitulo
        if perto(fs, SUBTITULO, 0.35):
            if L['bold']:
                out.append('\n#### ' + com_crases(L['run']))
                i += 1
            else:
                bloco = []
                while i < total and perto(linhas[i]['fs'], SUBTITULO, 0.35) \
                        and not linhas[i]['bold']:
                    bloco.append(com_crases(linhas[i]['run']))
                    i += 1
                out.append(' '.join(bloco))
            continue

        # ---------------------------------------------------------- secao / aviso
        if perto(fs, SECAO, 0.3) and not L['mono']:
            bloco = [com_crases(L['run'])]
            i += 1
            while i < total and perto(linhas[i]['fs'], SECAO, 0.3) and not linhas[i]['bold']:
                bloco.append(com_crases(linhas[i]['run']))
                i += 1
            junto = ' '.join(bloco)
            sem_marca = junto.replace('`', '')
            if sem_marca.startswith('Confira antes de seguir'):
                out.append('\n!confira ' + junto.split(':', 1)[-1].strip())
            elif sem_marca.upper() == sem_marca:
                out.append('\n## ' + junto)
            else:
                out.append('\n!nota ' + junto)
            continue

        # ---------------------------------------------------------- tabela
        if L['bold'] and perto(fs, TAB_CAB, 0.3) and not L['mono']:
            cortes = cortes_de_coluna(L['run'])
            cab = celulas(L['run'], cortes)
            corpo_tab = []
            i += 1
            ant = None
            while i < total and perto(linhas[i]['fs'], TAB_CEL, 0.4):
                cel = celulas(linhas[i]['run'], cortes)
                emenda = (ant is not None and linhas[i]['pag'] == linhas[i - 1]['pag']
                          and linhas[i]['y'] - ant < 25)
                if emenda and corpo_tab:
                    for k, c in enumerate(cel):
                        if c:
                            corpo_tab[-1][k] = (corpo_tab[-1][k] + ' ' + c).strip()
                else:
                    corpo_tab.append(cel)
                ant = linhas[i]['y']
                i += 1
            out.append('\n| ' + ' | '.join(cab) + ' |')
            out.append('|' + '---|' * len(cab))
            for lt in corpo_tab:
                out.append('| ' + ' | '.join(lt) + ' |')
            continue

        # ---------------------------------------------------------- legenda solta
        if perto(fs, LEGENDA, 0.3) and not L['mono']:
            bloco = []
            while i < total and perto(linhas[i]['fs'], LEGENDA, 0.3) and not linhas[i]['mono']:
                bloco.append(com_crases(linhas[i]['run']))
                i += 1
            out.append('\n' + ' '.join(bloco))
            continue

        # ---------------------------------------------------------- corpo
        if perto(fs, CORPO, 0.4):
            lista = x > 30
            itens = [[com_crases(L['run'])]]
            ant = L['y']
            i += 1
            while i < total and perto(linhas[i]['fs'], CORPO, 0.4) \
                    and (linhas[i]['x'] > 30) == lista and not linhas[i]['figura']:
                if lista and linhas[i]['pag'] == linhas[i - 1]['pag'] \
                        and linhas[i]['y'] - ant > 24:
                    itens.append([])
                itens[-1].append(com_crases(linhas[i]['run']))
                ant = linhas[i]['y']
                i += 1
            for it in itens:
                out.append(('- ' if lista else '') + ' '.join(it))
            continue

        # ---------------------------------------------------------- sobra
        if txt.strip():
            out.append(com_crases(L['run']))
        i += 1

    os.makedirs(destino, exist_ok=True)
    cab = ['---', 'id: ' + ident]
    for k in ('titulo', 'kicker', 'rodape'):
        if k in meta:
            cab.append('%s: %s' % (k, meta[k]))
    cab.append('---\n')
    texto = '\n'.join(cab) + '\n'.join(out) + '\n'
    texto = re.sub(r'\n{3,}', '\n\n', texto)
    alvo = os.path.join(destino, ident + '.md')
    with open(alvo, 'w', encoding='utf-8', newline='\n') as f:
        f.write(texto)
    return alvo, n_fig


def salvar_imagens(caminho, destino):
    """Grava as capturas sem reconverter.

    Uma captura que ja estava em JPEG dentro do PDF continua JPEG: passar
    por PNG multiplicava por seis o peso do arquivo, desfazendo o trabalho
    que deixou os PDFs mais leves. A numeracao segue a ordem do fluxo, a
    mesma que o texto usa para citar as figuras.
    """
    ident = os.path.basename(caminho).replace('.pdf', '')
    pasta = os.path.join(destino, 'img')
    os.makedirs(pasta, exist_ok=True)

    exts = {}
    for fig in imagens_posicionadas(caminho):
        for n, obj in zip(fig['ns'], fig['objs']):
            filtro = obj.get('/Filter')
            if isinstance(filtro, list):
                filtro = filtro[-1] if filtro else None
            if filtro == '/DCTDecode':
                ext, dados = '.jpg', obj._data
            elif filtro == '/JPXDecode':
                ext, dados = '.jp2', obj._data
            else:
                # Flate guarda bitmap cru; o PNG do pypdf e o menor arquivo
                ext, dados = '.png', None
            destino_arq = os.path.join(pasta, '%s-%d%s' % (ident, n, ext))
            if dados is None:
                from pypdf.generic._image_xobject import _xobj_to_image
                _, conteudo, _ = _xobj_to_image(obj)
                dados = conteudo
            with open(destino_arq, 'wb') as f:
                f.write(dados)
            exts[n] = ext
    return [exts[k] for k in sorted(exts)]


if __name__ == '__main__':
    pdf, destino = sys.argv[1], sys.argv[2]
    exts = salvar_imagens(pdf, destino)
    alvo, figs = extrair(pdf, destino, exts)
    print('%s  figuras=%d imagens=%d' % (alvo, figs, len(exts)))
