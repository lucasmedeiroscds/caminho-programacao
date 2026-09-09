# Caminho da Programação

Portal de aprendizado gerado a partir do guia `CAMINHO_DA_PROGRAMACAO.md` — do zero ao
avançado, passando por Lógica, HTML, CSS, JavaScript, Python, C e C++.

**No ar:** https://lucasmedeiroscds.github.io/caminho-programacao/

## O que tem dentro

| | |
|---|---|
| 8 módulos, 84 aulas | Lógica → HTML → CSS → JS → Python → C → C++ → Fundamentos |
| 12 exercícios | os do Módulo 0, para fazer no papel antes do editor |
| 14 projetos | com requisitos e critério de aprovação destacados |
| 48 itens de checklist | os portões de saída de cada módulo |
| 40 questões | 5 por módulo, sobre as armadilhas que o próprio material sinaliza |

Além disso: busca por `Ctrl + K`, tema claro/escuro, barra de progresso de leitura,
índice lateral por aula e certificado imprimível ao fechar todos os módulos.

## Como funciona

`index.html` é um arquivo único e autossuficiente. Não tem build, não tem dependência,
não tem servidor — abre com duplo clique e funciona offline. As únicas requisições
externas são as fontes do Google Fonts.

O progresso de cada leitor fica no `localStorage` do navegador dele. Quem abre o link
tem o próprio avanço, ninguém enxerga o de ninguém, e não existe login. O reverso da
moeda: o progresso não atravessa de um aparelho para outro.

## Como atualizar

O HTML é gerado, não editado à mão. O conteúdo sai do markdown original por um parser
em Node que fatia o documento em módulos, aulas, exercícios, projetos e checklists, e
renderiza cada bloco com realce de sintaxe próprio.

Para publicar uma alteração, substitua o `index.html` e faça o push — o GitHub Pages
republica sozinho a partir da branch `main`.
