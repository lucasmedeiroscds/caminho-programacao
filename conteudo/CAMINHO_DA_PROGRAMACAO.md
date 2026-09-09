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

**Sobre JavaScript vir antes de Python:** os dois têm dificuldade parecida. Coloquei JS primeiro porque ele dá continuidade ao HTML/CSS — você faz a página que acabou de construir *fazer coisas*, e isso segura a motivação nas primeiras semanas, que é quando a maioria desiste. Se em algum momento o JavaScript te frustrar demais, pode inverter: faça Python primeiro e volte pro JS depois. A lógica é a mesma, só muda o vestido.

**Sobre Java entrar entre Python e C:** Java é o degrau que falta entre as duas. Ele te obriga a declarar tipo, como o C vai obrigar, mas continua limpando a memória por você, como o Python faz — então você paga só metade do preço de cada vez. É também a linguagem com mais vagas de back-end no Brasil, o que torna esta a segunda parada de empregabilidade do caminho.

**Sobre C vir depois de tudo:** muita escola começa por C. Funciona, mas é cruel com iniciante — você passa três semanas lutando com ponteiro sem nunca ter visto um programa seu funcionar. Deixando C para depois, quando você já sabe programar, ele deixa de ser um obstáculo e vira o que realmente é: a explicação de *por que* as outras linguagens funcionam.

---

## Cronograma para 4–7 horas por semana

Com o seu ritmo, o caminho completo leva de **17 a 21 meses**. Parece muito, mas veja onde você já está empregável:

| Fase | Módulos | Tempo | O que você já consegue |
|------|---------|-------|------------------------|
| Fase 1 | 0, 1, 2 | ~3 meses | Montar sites estáticos. Já dá freela pequeno |
| Fase 2 | 3 (JS) | ~4 meses | **Ponto de empregabilidade.** Vaga júnior de front-end |
| Fase 3 | 4 (Python) | ~3 meses | Back-end, automação, dados. Dobra seu leque de vagas |
| Fase 4 | 5 (Java) | ~3 meses | **Segundo ponto de empregabilidade.** Vaga júnior de back-end |
| Fase 5 | 6, 7 (C/C++) | ~5 meses | Base sólida. Diferencial em entrevista técnica |

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

Mesma coisa que o exemplo acima, escrito de forma compacta. As três partes estão todas na primeira linha.

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

**async/await** — a mesma coisa, escrita de forma legível:

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

Esta é a terceira linguagem de sintaxe parecida que você vê — JavaScript, C e Java compartilham as chaves, o ponto e vírgula e o `for`. A novidade aqui não é a sintaxe, é a **disciplina**: tudo tem tipo declarado, tudo vive dentro de uma classe, e o compilador não deixa passar.

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

Repare que são **duas etapas**, como no C. Mas o `javac` não gera código de máquina: gera *bytecode*, uma linguagem intermediária que a **JVM** (Java Virtual Machine) executa. É daí que vem o slogan antigo *"escreva uma vez, rode em qualquer lugar"* — o mesmo `.class` roda no Windows, no Linux e no Mac sem recompilar, porque cada sistema tem sua própria JVM.

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

Igual ao que você já viu em C e JavaScript, com duas adições modernas:

```java
if (idade >= 18) { } else if (idade >= 16) { } else { }

String status = idade >= 18 ? "adulto" : "menor";       // ternário

for (int i = 0; i < 5; i++) { }

int[] numeros = {1, 2, 3};
for (int n : numeros) { }          // for-each: percorre sem índice

while (condicao) { }
do { } while (condicao);
```

**Switch moderno** (Java 14+) — sem `break`, sem cair no caso seguinte:

```java
String tipo = switch (dia) {
    case "sábado", "domingo" -> "Fim de semana";
    case "sexta" -> "Quase lá";
    default -> "Dia útil";
};
```

Compare com o switch antigo, onde esquecer o `break` fazia a execução escorrer para o próximo caso — bug clássico que a seta `->` eliminou de vez.

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

Este é o conceito de **passagem por valor vs. passagem por referência**. Quando você entender isso, você vai entender de uma vez por que em JavaScript modificar um objeto dentro de uma função afeta o original mas modificar um número não afeta. É a mesma coisa, escondida.

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

# MÓDULO 8 — O que atravessa todas as linguagens

> Estude em paralelo aos módulos, não depois. Marquei em qual módulo faz sentido começar cada um.

Linguagem é vocabulário. O que segue é gramática — e é o que decide se você é programador ou digitador de sintaxe.

## 8.1 — Git e GitHub *(comece junto com o Módulo 1)*

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

## 8.2 — Estruturas de dados *(comece no Módulo 4, aprofunde no 6)*

| Estrutura | Para que serve | Custo de busca |
|-----------|----------------|----------------|
| Array | Acesso por posição | O(1) por índice, O(n) por valor |
| Lista ligada | Inserção/remoção frequente | O(n) |
| Pilha (LIFO) | Desfazer, chamadas de função | O(n) |
| Fila (FIFO) | Processamento em ordem | O(n) |
| Tabela hash | Busca por chave | O(1) em média |
| Árvore binária de busca | Dados ordenados | O(log n) |
| Grafo | Relações, rotas, redes | Depende |

## 8.3 — Algoritmos e complexidade *(Módulo 4 em diante)*

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

## 8.4 — Banco de dados *(Módulo 4 em diante)*

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

## 8.5 — Como a web funciona *(Módulo 3 em diante)*

- Cliente e servidor; o que roda em cada um
- HTTP: métodos GET, POST, PUT, DELETE
- Códigos de status: 200, 201, 301, 400, 401, 403, 404, 500
- JSON como formato de troca
- API REST: recursos e endpoints
- Autenticação: sessão, token, JWT
- DNS e como o navegador acha o servidor

## 8.6 — Boas práticas *(sempre)*

- **DRY** (*Don't Repeat Yourself*): copiou e colou código? Vira função.
- **KISS** (*Keep It Simple*): a solução esperta que ninguém entende é pior que a óbvia.
- **YAGNI** (*You Aren't Gonna Need It*): não construa para um futuro imaginário.
- **Nomes claros**: `calcularImpostoRenda()` vale mais que qualquer comentário.
- **Comente o porquê, não o quê**: o código já diz o que faz. Escreva por que faz assim.
- **Commits pequenos e frequentes**, com mensagem que descreve a mudança.

## 8.7 — Testes *(Módulo 4 em diante)*

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

## 8.8 — Terminal e ambiente *(Módulo 1 em diante)*

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
MÓDULO 8 — Fundamentos     paralelo   —       o que realmente importa
```

Três coisas para levar daqui:

1. **Consistência bate intensidade.** Uma hora por dia, cinco dias por semana, derruba oito horas de sábado.
2. **Projeto terminado é a única prova.** Ninguém contrata por horas assistidas.
3. **Travar é o processo, não uma falha nele.** Quem programa há dez anos ainda passa uma tarde inteira num bug bobo. A diferença é que já sabe que isso passa.

Comece hoje pelo Módulo 0. No papel.
