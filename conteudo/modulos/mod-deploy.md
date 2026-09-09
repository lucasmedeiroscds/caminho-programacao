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
