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
