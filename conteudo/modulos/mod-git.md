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
