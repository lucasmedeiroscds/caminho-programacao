/*
 * Gera um PDF por oficina, imprimindo a própria página do portal.
 *
 * Usa a folha de impressão do portal, então o arquivo nunca diverge do que
 * está na tela: mudou o conteúdo, roda de novo e os 20 saem atualizados.
 *
 * Uso: node gerar-pdfs.mjs
 */
import { execFileSync } from 'node:child_process';
import { readFileSync, mkdirSync, existsSync, statSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import { dirname, join } from 'node:path';

const AQUI = dirname(fileURLToPath(import.meta.url));
const SAIDA = join(AQUI, 'pdf');

const CHROME = [
  'C:/Program Files/Google/Chrome/Application/chrome.exe',
  'C:/Program Files (x86)/Microsoft/Edge/Application/msedge.exe',
].find((p) => existsSync(p));

if (!CHROME) {
  console.error('Nenhum navegador encontrado para imprimir.');
  process.exit(1);
}

const oficinas = JSON.parse(readFileSync(join(AQUI, 'oficinas.json'), 'utf8'));
mkdirSync(SAIDA, { recursive: true });

const portal = join(AQUI, 'portal.html').replace(/\\/g, '/');
const perfil = join(AQUI, 'chrome-pdf');

let ok = 0;
const falhas = [];

for (const o of oficinas) {
  const destino = join(SAIDA, `${o.id}.pdf`);
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
        `file:///${portal}#/oficina/${o.id}`,
      ],
      { stdio: 'pipe', timeout: 90000 },
    );

    const kb = Math.round(statSync(destino).size / 1024);
    // Um PDF de menos de 15 KB é quase certamente uma página em branco.
    if (kb < 15) throw new Error(`saiu com ${kb} KB — provavelmente vazio`);
    console.log(`  ok   ${o.id.padEnd(18)} ${String(kb).padStart(4)} KB`);
    ok++;
  } catch (e) {
    console.error(` FALHA ${o.id}: ${e.message.split('\n')[0]}`);
    falhas.push(o.id);
  }
}

console.log(`\n${ok}/${oficinas.length} PDFs gerados em pdf/`);
if (falhas.length) process.exit(1);
