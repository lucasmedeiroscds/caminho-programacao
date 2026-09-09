# Caminho da Programação

Portal de aprendizado gerado a partir do guia `CAMINHO_DA_PROGRAMACAO.md` — do zero ao
avançado, passando por Lógica, HTML, CSS, JavaScript, Python, Java, C, C++, Git, SQL, Segurança, Deploy e IA.

**No ar:** https://lucasmedeiroscds.github.io/caminho-programacao/

## O que tem dentro

| | |
|---|---|
|  14 módulos, 157 aulas | Lógica → HTML → CSS → JS → Python → Java → C → C++ → Git → SQL → Segurança → Deploy → IA → Fundamentos |
| 12 exercícios | os do Módulo 0, para fazer no papel antes do editor |
| 32 projetos | com requisitos e critério de aprovação destacados |
| 106 itens de checklist | os portões de saída de cada módulo |
| 70 questões | 5 por módulo, sobre as armadilhas que o próprio material sinaliza |

A cor na borda de cada módulo indica a distância da máquina: azul para o que roda
longe dela (Lógica a Java), quente para o que encosta nela (C e C++).

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
