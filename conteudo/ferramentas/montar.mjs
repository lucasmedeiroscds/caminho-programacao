/*
 * Monta uma pagina HTML por tutorial, pronta para o Chrome imprimir.
 *
 * Le conteudo/tutoriais/<id>.md e escreve conteudo/build/<id>.html. As imagens
 * ficam referenciadas por caminho relativo — o Chrome abre por file:// e
 * enxerga a pasta img/ ao lado.
 *
 * Uso: node montar.mjs [id ...]     (sem argumento, monta todos)
 */
import { readFileSync, writeFileSync, mkdirSync, readdirSync, existsSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join, basename } from 'node:path';

const AQUI = dirname(fileURLToPath(import.meta.url));
const CONTEUDO = dirname(AQUI);
const FONTE = join(CONTEUDO, 'tutoriais');
const BUILD = join(CONTEUDO, 'build');

/* ------------------------------------------------------------------ texto */

const escapar = (s) =>
  String(s)
    .replaceAll('&', '&amp;')
    .replaceAll('<', '&lt;')
    .replaceAll('>', '&gt;')
    .replaceAll('"', '&quot;');

/* Prosa: `codigo` vira <code>. O texto e escapado antes, entao nada do que
   o autor escreveu consegue abrir uma tag. Os trechos de codigo sao
   guardados e trocados por uma marca que escapar() nao altera. */
const MARCA = '@@cod';

function prosa(texto) {
  const guardados = [];
  const marcado = String(texto).replace(/`([^`]+)`/g, (_, c) => {
    guardados.push(c);
    return `${MARCA}${guardados.length - 1}@@`;
  });
  return escapar(marcado)
    .replace(/\*(?=\S)(.+?)(?<=\S)\*/g, '<em>$1</em>')
    .replace(/@@cod(\d+)@@/g, (_, i) => `<code>${escapar(guardados[Number(i)])}</code>`);
}

/* O HTML montado fica em build/, e as capturas em tutoriais/img/. */
const caminhoImagem = (a) => '../tutoriais/' + a;

/* ------------------------------------------------------------------ leitura */

function separarCabecalho(bruto) {
  const m = bruto.match(/^---\n([\s\S]*?)\n---\n?/);
  if (!m) return [{}, bruto];
  const meta = {};
  for (const linha of m[1].split('\n')) {
    const corte = linha.indexOf(':');
    if (corte > 0) meta[linha.slice(0, corte).trim()] = linha.slice(corte + 1).trim();
  }
  return [meta, bruto.slice(m[0].length)];
}

/* Fatia o corpo em blocos. Cada bloco e {tipo, ...} e sai na ordem do texto. */
function analisar(corpo) {
  const linhas = corpo.split('\n');
  const blocos = [];
  let i = 0;

  const paragrafo = [];
  const fecharParagrafo = () => {
    if (paragrafo.length) {
      blocos.push({ tipo: 'p', texto: paragrafo.join(' ') });
      paragrafo.length = 0;
    }
  };

  while (i < linhas.length) {
    const linha = linhas[i];

    if (linha.trim() === '') {
      fecharParagrafo();
      i++;
      continue;
    }

    // cerca de codigo: ~~~arquivo nome.js | ~~~codigo | ~~~arvore
    const cerca = linha.match(/^~~~(arquivo|codigo|arvore)\s*(.*)$/);
    if (cerca) {
      fecharParagrafo();
      const corpoCod = [];
      i++;
      while (i < linhas.length && !linhas[i].startsWith('~~~')) corpoCod.push(linhas[i++]);
      i++; // pula a cerca que fecha
      blocos.push({ tipo: cerca[1], rotulo: cerca[2].trim(), codigo: corpoCod.join('\n') });
      continue;
    }

    // titulos
    const h = linha.match(/^(#{2,4})\s+(.*)$/);
    if (h) {
      fecharParagrafo();
      const nivel = h[1].length;
      if (nivel === 2) blocos.push({ tipo: 'secao', texto: h[2] });
      else if (nivel === 3) {
        const etapa = h[2].match(/^(\S+?)\.?\s+(.*)$/);
        blocos.push({ tipo: 'etapa', marca: etapa[1], texto: etapa[2] });
      } else blocos.push({ tipo: 'sub', texto: h[2] });
      i++;
      continue;
    }

    // figura: ![legenda](img/a.png img/b.png)
    const fig = linha.match(/^!\[(.*?)\]\((.+?)\)\s*$/);
    if (fig) {
      fecharParagrafo();
      blocos.push({ tipo: 'figura', legenda: fig[1], arquivos: fig[2].trim().split(/\s+/) });
      i++;
      continue;
    }

    // avisos
    const aviso = linha.match(/^!(confira|nota)\s+(.*)$/);
    if (aviso) {
      fecharParagrafo();
      blocos.push({ tipo: aviso[1], texto: aviso[2] });
      i++;
      continue;
    }

    // lead do documento
    if (linha.startsWith('> ')) {
      fecharParagrafo();
      const partes = [];
      while (i < linhas.length && linhas[i].startsWith('> ')) partes.push(linhas[i++].slice(2));
      blocos.push({ tipo: 'lead', texto: partes.join(' ') });
      continue;
    }

    // tabela
    if (linha.startsWith('|')) {
      fecharParagrafo();
      const cru = [];
      while (i < linhas.length && linhas[i].startsWith('|')) cru.push(linhas[i++]);
      const celulas = (l) =>
        l
          .replace(/^\|/, '')
          .replace(/\|$/, '')
          .split('|')
          .map((c) => c.trim());
      const cab = celulas(cru[0]);
      const corpoTab = cru.slice(2).map(celulas);
      blocos.push({ tipo: 'tabela', cab, corpo: corpoTab });
      continue;
    }

    // lista
    if (linha.startsWith('- ')) {
      fecharParagrafo();
      const itens = [];
      while (i < linhas.length && linhas[i].startsWith('- ')) itens.push(linhas[i++].slice(2));
      blocos.push({ tipo: 'lista', itens });
      continue;
    }

    paragrafo.push(linha.trim());
    i++;
  }
  fecharParagrafo();
  return blocos;
}

/* ------------------------------------------------------------------ HTML */

/* A barra vertical da secao cobre o titulo e tudo o que vem dentro dela, ate
   a proxima secao ou a proxima etapa. */
function agruparSecoes(blocos) {
  const saida = [];
  let atual = null;
  for (const b of blocos) {
    if (b.tipo === 'secao') {
      atual = { tipo: 'faixa', dentro: [b] };
      saida.push(atual);
      continue;
    }
    if (b.tipo === 'etapa') atual = null;
    if (atual) atual.dentro.push(b);
    else saida.push(b);
  }
  return saida;
}

function render(blocos) {
  const saida = [];
  for (const b of blocos) {
    switch (b.tipo) {
      case 'faixa':
        saida.push(`<section class="faixa">${render(b.dentro)}</section>`);
        break;
      case 'lead':
        saida.push(`<p class="lead">${prosa(b.texto)}</p>`);
        break;
      case 'secao':
        saida.push(`<h2>${prosa(b.texto)}</h2>`);
        break;
      case 'etapa':
        saida.push(
          `<h3 class="etapa"><span class="marca">${escapar(b.marca)}</span>` +
            `<span class="nome">${prosa(b.texto)}</span></h3>`,
        );
        break;
      case 'sub':
        saida.push(`<h4>${prosa(b.texto)}</h4>`);
        break;
      case 'p':
        saida.push(`<p>${prosa(b.texto)}</p>`);
        break;
      case 'lista':
        saida.push(`<ul>${b.itens.map((it) => `<li>${prosa(it)}</li>`).join('')}</ul>`);
        break;
      case 'arquivo':
        saida.push(
          `<figure class="codigo"><figcaption>${escapar(b.rotulo)}</figcaption>` +
            `<pre><code>${escapar(b.codigo)}</code></pre></figure>`,
        );
        break;
      case 'codigo':
        saida.push(`<figure class="codigo repetido"><pre><code>${escapar(b.codigo)}</code></pre></figure>`);
        break;
      case 'arvore':
        saida.push(`<pre class="arvore">${escapar(b.codigo)}</pre>`);
        break;
      case 'figura': {
        const imgs = b.arquivos
          .map((a) => `<img src="${escapar(caminhoImagem(a))}" alt="">`)
          .join('');
        const leg = b.legenda ? `<figcaption>${prosa(b.legenda)}</figcaption>` : '';
        const par = b.arquivos.length > 1 ? ' par' : '';
        saida.push(`<figure class="captura${par}">${imgs}${leg}</figure>`);
        break;
      }
      case 'tabela': {
        const cab = b.cab.map((c) => `<th>${prosa(c)}</th>`).join('');
        const corpo = b.corpo
          .map((l) => `<tr>${l.map((c) => `<td>${prosa(c)}</td>`).join('')}</tr>`)
          .join('');
        saida.push(`<table><thead><tr>${cab}</tr></thead><tbody>${corpo}</tbody></table>`);
        break;
      }
      case 'confira':
        saida.push(
          `<p class="confira"><b>Confira antes de seguir:</b> ${prosa(b.texto)}</p>`,
        );
        break;
      case 'nota':
        saida.push(`<p class="nota">${prosa(b.texto)}</p>`);
        break;
      default:
        break;
    }
  }
  return saida.join('\n');
}

const ESTILO = readFileSync(join(AQUI, 'impressao.css'), 'utf8');

function pagina(meta, miolo) {
  return `<!DOCTYPE html>
<html lang="pt-BR">
<head>
<meta charset="UTF-8">
<title>${escapar(meta.titulo || meta.id)}</title>
<style>
${ESTILO}
</style>
</head>
<body>
<header class="capa">
  <h1>${escapar(meta.titulo || meta.id)}</h1>
  <p class="kicker">${escapar(meta.kicker || '')}</p>
</header>
${miolo}
<footer class="rodape">${escapar(meta.rodape || '')}</footer>
</body>
</html>
`;
}

/* ------------------------------------------------------------------ main */

const pedidos = process.argv.slice(2);
const alvos = readdirSync(FONTE)
  .filter((f) => f.endsWith('.md'))
  .map((f) => basename(f, '.md'))
  .filter((id) => pedidos.length === 0 || pedidos.includes(id));

if (!alvos.length) {
  console.error('Nenhum tutorial encontrado em', FONTE);
  process.exit(1);
}

mkdirSync(BUILD, { recursive: true });

let faltando = 0;
for (const id of alvos) {
  const bruto = readFileSync(join(FONTE, id + '.md'), 'utf8');
  const [meta, corpo] = separarCabecalho(bruto);
  meta.id = meta.id || id;
  const blocos = analisar(corpo);

  for (const b of blocos) {
    if (b.tipo !== 'figura') continue;
    for (const a of b.arquivos) {
      if (!existsSync(join(FONTE, a))) {
        console.error(`  ${id}: imagem ausente — ${a}`);
        faltando++;
      }
    }
  }

  writeFileSync(join(BUILD, id + '.html'), pagina(meta, render(agruparSecoes(blocos))));
  const etapas = blocos.filter((b) => b.tipo === 'etapa').length;
  console.log(`  ok   ${id.padEnd(18)} ${String(blocos.length).padStart(4)} blocos, ${etapas} etapas`);
}

console.log(`\n${alvos.length} paginas em conteudo/build/`);
if (faltando) {
  console.error(`${faltando} imagens ausentes`);
  process.exit(1);
}
