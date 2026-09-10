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
