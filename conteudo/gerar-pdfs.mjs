/*
 * Gera um PDF por oficina, imprimindo as paginas montadas por ferramentas/montar.mjs.
 *
 * A fonte de tudo e conteudo/tutoriais/<id>.md. Mudou o texto, roda de novo e
 * o PDF sai atualizado — o arquivo publicado nunca diverge da fonte.
 *
 * Uso: node gerar-pdfs.mjs [id ...]     (sem argumento, gera todos)
 */
import { execFileSync } from 'node:child_process';
import { readdirSync, mkdirSync, existsSync, statSync, rmSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join, basename } from 'node:path';

const AQUI = dirname(fileURLToPath(import.meta.url));
const RAIZ = dirname(AQUI);
const BUILD = join(AQUI, 'build');
const SAIDA = join(RAIZ, 'pdf');

const CHROME = [
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
].find((p) => existsSync(p));

if (!CHROME) {
  console.error('Nenhum navegador encontrado para imprimir.');
  process.exit(1);
}

// Monta o HTML antes de imprimir, para nunca imprimir uma versao velha.
const pedidos = process.argv.slice(2);
execFileSync(process.execPath, [join(AQUI, 'ferramentas', 'montar.mjs'), ...pedidos], {
  stdio: 'inherit',
});

const alvos = readdirSync(BUILD)
  .filter((f) => f.endsWith('.html'))
  .map((f) => basename(f, '.html'))
  .filter((id) => pedidos.length === 0 || pedidos.includes(id));

mkdirSync(SAIDA, { recursive: true });
const perfil = join(AQUI, 'chrome-pdf');

let ok = 0;
const falhas = [];

console.log('');
for (const id of alvos) {
  const destino = join(SAIDA, `${id}.pdf`);
  const pagina = join(BUILD, `${id}.html`).replace(/\\/g, '/');
  try {
    execFileSync(
      CHROME,
      [
        '--headless',
        '--no-sandbox',
        '--disable-gpu',
        '--no-pdf-header-footer',
        `--user-data-dir=${perfil}`,
        '--virtual-time-budget=9000',
        `--print-to-pdf=${destino}`,
        `file:///${pagina}`,
      ],
      { stdio: 'pipe', timeout: 90000 },
    );

    const kb = Math.round(statSync(destino).size / 1024);
    // Um PDF de menos de 15 KB e quase certamente uma pagina em branco.
    if (kb < 15) throw new Error(`saiu com ${kb} KB — provavelmente vazio`);
    console.log(`  ok   ${id.padEnd(18)} ${String(kb).padStart(4)} KB`);
    ok++;
  } catch (e) {
    console.error(` FALHA ${id}: ${e.message.split('\n')[0]}`);
    falhas.push(id);
  }
}

rmSync(perfil, { recursive: true, force: true });

console.log(`\n${ok}/${alvos.length} PDFs gerados em pdf/`);
if (falhas.length) process.exit(1);
