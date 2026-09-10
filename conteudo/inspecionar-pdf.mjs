/* Compara PDFs: tamanho, como as fontes entraram e se o texto é pesquisável. */
import { readFileSync } from 'node:fs';
import { inflateSync } from 'node:zlib';

const alvos = process.argv.slice(2);
if (!alvos.length) {
  console.error('uso: node inspecionar-pdf.mjs arquivo.pdf [outro.pdf]');
  process.exit(1);
}

for (const arq of alvos) {
  const buf = readFileSync(arq);
  const s = buf.toString('latin1');

  const type3 = (s.match(/\/Subtype\s*\/Type3/g) || []).length;
  const type0 = (s.match(/\/Subtype\s*\/Type0/g) || []).length;
  const toUnicode = (s.match(/\/ToUnicode/g) || []).length;

  // Conta operadores de texto nos streams descomprimidos.
  let trechos = 0;
  let amostra = '';
  for (const m of s.matchAll(/stream\r?\n/g)) {
    const ini = m.index + m[0].length;
    const fim = s.indexOf('endstream', ini);
    if (fim < 0) continue;
    let txt;
    try {
      txt = inflateSync(Buffer.from(s.slice(ini, fim), 'latin1')).toString('latin1');
    } catch {
      continue;
    }
    const achados = txt.match(/\([^)]{4,}\)\s*Tj/g);
    if (achados) {
      trechos += achados.length;
      if (!amostra) amostra = achados[0].replace(/[^\x20-\x7E]/g, '.').slice(0, 58);
    }
  }

  console.log(arq);
  console.log(`   tamanho          : ${Math.round(buf.length / 1024)} KB`);
  console.log(`   fontes Type3     : ${type3}${type3 ? '  <- letra virou desenho vetorial' : ''}`);
  console.log(`   fontes Type0     : ${type0}${type0 ? '  <- fonte real embutida' : ''}`);
  console.log(`   mapas ToUnicode  : ${toUnicode}${toUnicode ? '  (texto pesquisável)' : '  (SEM mapa)'}`);
  console.log(`   trechos de texto : ${trechos}`);
  if (amostra) console.log(`   amostra          : ${amostra}`);
  console.log();
}
