# MÓDULO 14 — Terminal do Windows (CMD)

> **Dificuldade:** ●●○○○ · **Tempo:** 2 a 3 semanas · **Pré-requisito:** nenhum *(serve desde o Módulo 1)*

**Objetivo:** resolver pelo Prompt de Comando os problemas de todo dia no Windows — disco, rede, atualizações, programa travado, configuração — e automatizar o que se repete com scripts `.bat`.

A tela de Configurações do Windows muda de lugar a cada versão, esconde metade das informações e não deixa você repetir nada. O terminal faz o contrário: o mesmo comando funciona hoje e daqui a cinco anos, mostra o que está acontecendo de verdade e cabe num arquivo que roda sozinho.

Isto vale para qualquer pessoa que usa Windows — e vale dinheiro para quem busca a primeira vaga em **suporte técnico**, a porta de entrada mais comum para a área. No Módulo 11 você viu o terminal do Linux, que é onde os servidores moram. Este módulo é o outro lado: o computador que está na sua frente, e na mesa de quase todo cliente.

**Como ler este módulo:** todos os comandos e todas as mensagens foram conferidos no Windows 11 em português. Em outra versão ou outro idioma, o texto das mensagens muda; os comandos, não.

**Ferramentas:** o próprio Windows. Nada para instalar.

---

## Nível Básico

### Aula 14.1 — CMD, PowerShell e Terminal: quem é quem

Três nomes que as pessoas usam como se fossem a mesma coisa:

- **Prompt de Comando** (`cmd.exe`) — o interpretador clássico, que roda os arquivos `.bat`. É o assunto deste módulo.
- **PowerShell** — o sucessor, mais poderoso, que trabalha com objetos em vez de texto. Alguns diagnósticos só existem nele, e dá para chamá-lo de dentro do CMD (você vai fazer isso na Aula 14.5).
- **Terminal do Windows** — a janela com abas. Ela não interpreta nada: só hospeda o CMD, o PowerShell ou outro shell.

**Abrindo:** `Win + R`, digite `cmd` e Enter. Para confirmar onde você está:

```bat
ver
```

```txt
Microsoft Windows [versão 10.0.26200.9445]
```

Sim, o Windows 11 ainda se identifica como versão 10.0 — o que muda de uma edição para outra é o número depois dela.

**Normal ou administrador?** Metade dos comandos de manutenção mexe no sistema e exige uma janela de administrador: pesquise "cmd" no menu Iniciar e aperte `Ctrl + Shift + Enter`. Sem isso, a resposta é uma recusa:

```txt
C:\Users\voce> chkdsk C:
Acesso negado, pois você não tem privilégios suficientes ou
o disco pode estar bloqueado por outro processo.
```

| Precisa de administrador | Funciona em janela normal |
|---|---|
| `chkdsk` | `dir`, `where`, `findstr` |
| `sfc` e `DISM` | `ipconfig`, `ping`, `nslookup` |
| `fsutil volume diskfree` | `tasklist`, `systeminfo` |
| `netstat -b` | `driverquery`, `pnputil /enum-drivers` |
| | `winget`, `powercfg /batteryreport` |

Conferi cada linha dessa tabela numa janela sem privilégio.

**Regra:** abra como administrador só quando o comando pedir. Numa janela de administrador, um erro de digitação apaga o que uma janela normal não deixaria.

### Aula 14.2 — Navegar sem se perder

O CMD sempre está **dentro de uma pasta**. Ela aparece antes do `>`:

```bat
C:\Users\voce>
```

Os comandos que movem você de lugar:

```bat
cd Documentos             :: entra na pasta
cd ..                     :: sobe um nível
cd \                      :: vai para a raiz da unidade
cd /d D:\Fotos            :: troca de unidade E de pasta
cls                       :: limpa a tela
```

O `/d` não é enfeite: a ajuda do próprio `cd` explica que é a chave para **alterar a unidade atual**, além da pasta. Para sair do `C:` e ir para uma pasta do `D:`, use `cd /d`.

Para ver o que existe:

```bat
dir                       :: arquivos e pastas daqui
dir /a                    :: inclui os ocultos
dir /o-s                  :: ordena por tamanho, maior primeiro
dir /s /b *.pdf           :: todos os PDFs daqui para dentro, só o caminho
```

Três atalhos que economizam horas:

- `Tab` completa o nome da pasta ou arquivo. Aperte de novo para a próxima opção.
- `↑` e `↓` percorrem os comandos já digitados.
- `F7` abre a lista do histórico da janela.

**Espaço no nome pede aspas.** Veja o que acontece sem elas:

```bat
mkdir minha pasta
```

Isso **não** cria "minha pasta". Cria duas pastas, `minha` e `pasta` — conferi. O CMD separa argumentos por espaço, e `mkdir` aceita vários de uma vez. Com aspas, sai uma pasta só:

```bat
mkdir "minha pasta"
```

Na dúvida, ponha aspas em todo caminho. Elas nunca atrapalham.

### Aula 14.3 — Arquivos e pastas

```bat
mkdir projetos                    :: cria pasta
copy nota.txt backup.txt          :: copia
move nota.txt projetos            :: move
ren nota.txt anotacao.txt         :: renomeia
type anotacao.txt                 :: mostra o conteúdo
type log-grande.txt | more        :: mostra de tela em tela (espaço avança)
```

Curingas valem em quase todo comando: `*` é "qualquer coisa" e `?` é "um caractere".

```bat
copy *.jpg D:\Fotos               :: todas as imagens JPG
dir relatorio-2026-??.xlsx        :: relatorio-2026-01 até relatorio-2026-12
```

Apagar:

```bat
del anotacao.txt                  :: apaga um arquivo
del *.tmp                         :: apaga todos os .tmp da pasta
rmdir /s /q pasta-velha           :: apaga a pasta e tudo dentro, sem perguntar
```

**Cuidado: `del` e `rmdir` não passam pela Lixeira.** Conferi contando os itens da Lixeira antes e depois de apagar um arquivo com `del`: o arquivo sumiu, e a contagem ficou igual. Não existe `Ctrl + Z` no terminal. Antes de um `del` com curinga, rode o mesmo padrão com `dir` e leia a lista:

```bat
dir *.tmp          :: primeiro, veja o que casa
del *.tmp          :: só depois, apague
```

### Aula 14.4 — Ajuda, busca e redirecionamento

**Todo comando explica a si mesmo** com `/?`:

```bat
robocopy /?
```

É a documentação oficial, no seu idioma, na versão exata do seu Windows. Consulte antes de procurar na internet.

**Onde está esse programa?** `where` responde qual arquivo roda quando você digita um nome:

```bat
where notepad
```

```txt
C:\Windows\System32\notepad.exe
C:\Windows\notepad.exe
C:\Users\voce\AppData\Local\Microsoft\WindowsApps\notepad.exe
```

Quando aparece mais de um, vale o primeiro. É assim que se descobre um mistério comum: num Windows sem Python instalado, `where python` encontra um arquivo em `WindowsApps` — um atalho da Microsoft Store — e digitar `python` só mostra um aviso sugerindo instalar pela loja. O comando "existe", mas o Python não.

**Procurar texto dentro de arquivos:**

```bat
findstr /i "erro" app.log               :: linhas com "erro", ignorando maiúscula
findstr /s /i "senha" *.txt             :: em todos os .txt, daqui para dentro
find /c /v "" lista.txt                 :: conta as linhas do arquivo
```

**Redirecionamento** — mandar a saída para outro lugar:

```bat
dir > lista.txt              :: escreve no arquivo (SOBRESCREVE)
dir >> lista.txt             :: acrescenta ao fim
comando 2> erros.txt         :: só as mensagens de erro
comando > tudo.txt 2>&1      :: saída e erros no mesmo arquivo
comando 2>nul                :: joga os erros fora
dir | findstr ".pdf"         :: a saída de um vira a entrada do outro
ipconfig | clip              :: copia a saída para a área de transferência
```

Existem **dois canais**: a saída normal e a de erro. `>` só leva a normal. Medi com um `dir` de uma pasta inexistente: com `>`, a mensagem "Arquivo não encontrado" continuou aparecendo na tela, e o arquivo ficou com 228 bytes; com `> arquivo 2>&1`, a tela ficou limpa e o arquivo, com 253 — os 25 bytes a mais são a mensagem de erro.

É por isso que um script "salvando o log" às vezes salva tudo, menos o erro que você queria ver.

---

## Nível Intermediário

### Aula 14.5 — Disco: espaço, saúde e erros

**"O disco está cheio?"** — a última linha do `dir` responde, sem privilégio nenhum:

```bat
dir C:\
```

```txt
               1 arquivo(s)         12.288 bytes
              14 pasta(s)   386.416.197.632 bytes disponíveis
```

**"O disco está morrendo?"** — aqui existe uma armadilha de tutorial velho. Durante anos a resposta foi `wmic diskdrive get status`. **O WMIC não vem mais no Windows 11 atual**: no computador em que este módulo foi testado, `where wmic` não encontra nada. O substituto é um comando do PowerShell, que o CMD chama sem problema:

```bat
powershell -NoProfile -Command "Get-PhysicalDisk | Select-Object FriendlyName,MediaType,HealthStatus,OperationalStatus"
```

```txt
FriendlyName                   MediaType HealthStatus OperationalStatus
------------                   --------- ------------ -----------------
WDC PC SN530 SDBPNPZ-512G      SSD       Healthy      OK
```

`Healthy` e `OK` é o que se quer ver. Qualquer outra coisa — `Warning`, `Unhealthy` — significa: **faça backup hoje**, antes de qualquer outro diagnóstico.

**"O sistema de arquivos tem erro?"** — `chkdsk`, em janela de administrador:

```bat
chkdsk C:                 :: só verifica e relata, não mexe em nada
chkdsk C: /scan           :: verifica com o volume em uso
chkdsk C: /f              :: corrige erros do sistema de arquivos
chkdsk C: /r              :: /f + procura setores defeituosos (demorado)
```

Com `/f` na unidade do Windows, o disco está em uso e não dá para corrigir agora: o `chkdsk` pergunta se pode agendar a verificação para o próximo reinício.

**Cuidado:** `chkdsk /r` num disco com defeito físico pode levar horas e forçar ainda mais um disco que está falhando. Se o `Get-PhysicalDisk` já acusou problema, copie seus arquivos **antes**.

### Aula 14.6 — Windows corrompido: DISM e SFC

Sintomas: aplicativos do próprio Windows que não abrem, atualizações que falham sempre no mesmo ponto, telas azuis sem motivo aparente. Os dois comandos abaixo comparam os arquivos do sistema com cópias íntegras e consertam o que estiver diferente. Ambos exigem administrador — sem ele, o `sfc` recusa, e o `DISM` responde com o erro 740.

A ordem importa:

```bat
DISM /Online /Cleanup-Image /ScanHealth
DISM /Online /Cleanup-Image /RestoreHealth
sfc /scannow
```

- `DISM ... /ScanHealth` verifica a **imagem** do Windows — o estoque de onde os arquivos saem.
- `DISM ... /RestoreHealth` conserta essa imagem, baixando o que faltar pelo Windows Update. Precisa de internet e pode parar um tempo em alguma porcentagem; deixe terminar.
- `sfc /scannow` verifica os **arquivos em uso** e substitui os corrompidos usando a imagem.

**Por que DISM primeiro:** o `sfc` repara a partir da imagem. Se a imagem também estiver corrompida, ele "conserta" copiando o defeito. Consertar o estoque antes de repor as peças.

Se o `sfc` disser que encontrou arquivos corrompidos e não conseguiu reparar alguns, o detalhe fica em `C:\Windows\Logs\CBS\CBS.log`. Rode o `sfc /scannow` de novo depois de reiniciar: é comum a segunda passada terminar o que a primeira começou.

### Aula 14.7 — Atualizações: programas, drivers e o Windows

**Programas: `winget`**, o gerenciador de pacotes que já vem no Windows 11:

```bat
winget upgrade                              :: lista o que tem atualização
winget upgrade --id Mozilla.Firefox         :: atualiza um programa
winget upgrade --all                        :: atualiza tudo que ele reconhece
winget search 7zip                          :: procura um programa
winget install --id 7zip.7zip               :: instala
winget list                                 :: tudo que está instalado
```

Sem argumentos, `winget upgrade` só **mostra** as atualizações disponíveis — é seguro rodar a qualquer momento. Algumas opções úteis, todas conferidas na ajuda do comando:

| Opção | O que faz |
|---|---|
| `--include-unknown` | inclui programas cuja versão instalada o winget não consegue determinar |
| `--silent` | pede instalação sem janelas |
| `--accept-package-agreements` | aceita as licenças dos pacotes sem perguntar |

**Atenção ao `--accept-package-agreements`:** ele aceita contratos de licença em seu nome. Num script de empresa isso é decidido uma vez, por quem pode decidir; no seu computador, leia pelo menos na primeira vez. Na primeira execução, o winget também pede para aceitar os termos das fontes de pacotes.

Use o `--id` exato, que aparece no `winget search`. Pelo nome, uma busca pode casar com mais de um programa.

**Drivers:**

```bat
driverquery                          :: drivers carregados, com a data
pnputil /enum-drivers                :: drivers de terceiros instalados
pnputil /enum-devices /problem       :: dispositivos com problema
```

O `pnputil /enum-drivers` mostra, para cada driver, o provedor, a classe e a versão:

```txt
Nome Publicado:     oem39.inf
Nome Original:      acerairplanemodecontroller.inf
Nome do Provedor:   Acer Incorporated
Nome da Classe:     HIDClass
Versão do Driver:   09/26/2025 1.0.0.14
```

O `/problem` é o atalho para "por que esse dispositivo não funciona": lista só o que está com erro, sem abrir o Gerenciador de Dispositivos. Quando está tudo certo, a resposta é "Nenhum dispositivo foi encontrado no sistema." — que assusta, mas quer dizer "nenhum dispositivo **com problema**".

**O Windows Update em si** não tem um comando próprio no CMD para verificar e instalar. Os que aparecem em tutoriais antigos, como `wuauclt /detectnow`, não fazem mais isso no Windows 10 e 11. O caminho honesto é abrir a tela certa direto:

```bat
start ms-settings:windowsupdate
```

### Aula 14.8 — Rede: "a internet caiu"

Um problema de rede sempre está em uma de quatro camadas. O diagnóstico é descer por elas, **nesta ordem**:

**1. Tenho endereço?**

```bat
ipconfig
```

Procure a linha `Endereço IPv4` e a linha `Gateway Padrão` do adaptador que você usa. Se o IPv4 começa com `169.254`, o computador não recebeu endereço do roteador: o problema está entre você e o roteador — cabo, Wi-Fi, o próprio roteador.

```bat
ipconfig /release          :: devolve o endereço
ipconfig /renew            :: pede um novo ao roteador
ipconfig /all              :: tudo: DNS, MAC, DHCP
```

**2. Alcanço o roteador?** `ping` no endereço do `Gateway Padrão`:

```bat
ping 192.168.0.1
```

**3. Alcanço a internet?** `ping` num endereço IP público, sem depender de nome:

```bat
ping -n 2 1.1.1.1
```

```txt
Disparando 1.1.1.1 com 32 bytes de dados:
Resposta de 1.1.1.1: bytes=32 tempo=17ms TTL=52
Resposta de 1.1.1.1: bytes=32 tempo=18ms TTL=52

Estatísticas do Ping para 1.1.1.1:
    Pacotes: Enviados = 2, Recebidos = 2, Perdidos = 0 (0% de perda),
```

**4. Os nomes funcionam?**

```bat
nslookup example.com
```

```txt
Servidor:  one.one.one.one
Address:  1.1.1.1

Nome:    example.com
```

Com isso, os sintomas se separam sozinhos:

| O que acontece | Onde está o problema | O que tentar |
|---|---|---|
| IPv4 começa com `169.254` | entre o computador e o roteador | cabo, Wi-Fi, `ipconfig /renew`, reiniciar o roteador |
| Roteador responde, `1.1.1.1` não | o roteador não chega à internet | reiniciar o roteador, ligar para o provedor |
| `ping 1.1.1.1` responde, sites não abrem | DNS | `ipconfig /flushdns`, trocar o DNS |
| Um site só não abre | o site | nada no seu computador |

`ipconfig /flushdns` limpa o cache de nomes que o Windows guarda. Resolve o caso clássico de um site que mudou de servidor e só no seu computador continua apontando para o endereço velho.

**Quem está usando a rede?**

```bat
netstat -ano | findstr LISTENING        :: portas abertas esperando conexão, com o PID
tasklist /FI "PID eq 4312"              :: qual programa é aquele PID
```

A última coluna do `netstat -ano` é o número do processo (PID); o `tasklist` traduz o número em nome. O `netstat -b`, que mostraria o nome direto, responde "A operação solicitada requer elevação" numa janela normal.

---

## Nível Avançado

### Aula 14.9 — Processos travados, desligamento e bateria

**O que está rodando:**

```bat
tasklist
tasklist /FI "IMAGENAME eq explorer.exe"
```

```txt
Nome da imagem            Identifi Nome da sessão       Sessão# Uso de memór
========================= ======== ================ =========== ============
explorer.exe                 10932 Console                    4    466.484 K
```

**Encerrar o que travou:**

```bat
taskkill /IM notepad.exe            :: pede para fechar, pelo nome
taskkill /IM notepad.exe /F         :: força — o programa não tem chance de salvar
taskkill /PID 10932 /F              :: pelo número
taskkill /IM chrome.exe /T /F       :: o processo e todos os filhos dele
```

Tente sem `/F` primeiro. Encerrar à força é puxar o fio da tomada do programa: o que não foi salvo se perde.

**Informações da máquina:**

```bat
systeminfo | findstr /B /C:"Nome do sistema operacional" /C:"Versão do sistema operacional"
```

O `findstr` filtra pelo começo da linha, e os rótulos são os do Windows em português — num Windows em inglês, seriam `OS Name` e `OS Version`. Os mesmos dados que o suporte pede por telefone, sem abrir cinco telas.

**Desligar e reiniciar com hora marcada:**

```bat
shutdown /s /t 3600        :: desliga daqui a uma hora
shutdown /r /t 0           :: reinicia agora
shutdown /a                :: cancela o desligamento agendado
```

`/t` é em segundos. Se não houver nada agendado, o `/a` avisa: "Não foi possível anular o desligamento do sistema porque o sistema não estava sendo desligado."

**Saúde da bateria** (notebook):

```bat
powercfg /batteryreport /output "%USERPROFILE%\Desktop\bateria.html"
```

Gera uma página com a capacidade de fábrica e a capacidade atual da bateria, e o uso dos últimos dias. Abra o arquivo no navegador. Mesmo com o Windows em português, o relatório sai em inglês: procure `DESIGN CAPACITY` (de fábrica) e `FULL CHARGE CAPACITY` (a carga completa de hoje). Quando a capacidade atual está bem abaixo da de fábrica, não é o Windows gastando mais: é a bateria envelhecendo.

### Aula 14.10 — Variáveis de ambiente e atalhos de configuração

O Windows guarda caminhos e preferências em **variáveis de ambiente**:

```bat
set                          :: todas
echo %USERPROFILE%           :: a sua pasta de usuário
echo %TEMP%                  :: a pasta de temporários
echo %PATH%                  :: onde o Windows procura programas
```

Criar uma variável:

```bat
set PROJETO=C:\projetos\loja         :: vale só nesta janela
setx PROJETO C:\projetos\loja        :: fica gravada, para as próximas janelas
```

A diferença pega muita gente: a ajuda do `setx` diz que o valor fica disponível **nas próximas janelas de comando, mas não na atual**. Rodou `setx` e o `echo` mostra vazio? Feche e abra outra janela.

**Cuidado com `setx PATH "%PATH%;C:\nova"`.** Parece acrescentar uma pasta ao PATH, mas o `%PATH%` da janela é a soma do PATH do sistema com o do usuário. O `setx` grava essa soma inteira no PATH do **usuário** — duplicando tudo o que era do sistema. Para editar o PATH, use a tela certa:

```bat
rundll32 sysdm.cpl,EditEnvironmentVariables
```

**Atalhos para as telas de configuração** — mais rápido que navegar por menus:

| Comando | Abre |
|---|---|
| `start ms-settings:windowsupdate` | Windows Update |
| `start ms-settings:appsfeatures` | Aplicativos instalados |
| `start ms-settings:storagesense` | Armazenamento |
| `appwiz.cpl` | Programas e Recursos (a lista clássica) |
| `ncpa.cpl` | Conexões de rede |
| `devmgmt.msc` | Gerenciador de Dispositivos |
| `diskmgmt.msc` | Gerenciamento de Disco |
| `services.msc` | Serviços |
| `eventvwr.msc` | Visualizador de Eventos |
| `msinfo32` | Informações do Sistema |

**O que abre junto com o Windows?** O registro guarda os programas de inicialização do seu usuário, e dá para **ler** sem risco:

```bat
reg query "HKCU\Software\Microsoft\Windows\CurrentVersion\Run"
```

**Cuidado:** `reg query` só lê. `reg add` e `reg delete` alteram o registro na hora, sem confirmação e sem Lixeira. Tutorial que manda colar um `reg add` sem explicar cada parte é tutorial para fechar.

### Aula 14.11 — Scripts .bat: automatizar o que se repete

Um arquivo `.bat` é uma lista de comandos que o CMD executa em sequência. Crie `ola.bat` no Bloco de Notas:

```bat
@echo off
:: comentário: o CMD ignora a linha
echo Iniciando em %DATE% as %TIME%
set PASTA=%~dp0
echo Este script mora em %PASTA%
pause
```

- `@echo off` — sem isso, cada comando é impresso antes de rodar.
- `::` — comentário.
- `%~dp0` — a pasta onde o **script** está, com a barra no fim. Use no lugar de caminhos fixos, e o script funciona em qualquer computador.
- `pause` — espera uma tecla, para a janela não fechar antes de você ler.

**Argumentos:** `%1`, `%2`… são o que veio depois do nome do script. `backup.bat D:\` recebe `D:\` em `%1`.

**Decisões e repetição:**

```bat
if exist "%USERPROFILE%\Desktop\relatorio.txt" echo O relatório já existe

for %%f in (*.log) do echo Encontrei %%f

set /a total=7/2
echo %total%
```

Dentro de um `.bat`, a variável do `for` leva **dois** `%` (`%%f`); digitada direto no prompt, um só. É a ajuda do `for` que avisa. E `set /a` só faz conta com inteiros: o `echo` mostra `3`.

**Deu certo ou não?** Todo comando deixa um código em `errorlevel`: `0` é sucesso, outro número é falha.

```bat
dir nao-existe >nul 2>&1
if errorlevel 1 echo O comando falhou
```

`if errorlevel 1` quer dizer "se o código for **1 ou maior**".

**As duas armadilhas que todo mundo encontra** — as duas medidas num script de teste.

A primeira: o CMD troca as `%variáveis%` pelo valor **quando lê a linha**, antes de executar qualquer coisa nela.

```bat
dir nao-existe >nul 2>&1 & echo %errorlevel%
```

Mostrou `0`, embora o `dir` tenha falhado: o `%errorlevel%` já tinha sido lido antes de o `dir` rodar. Na linha seguinte, o mesmo `echo %errorlevel%` mostrou `1`.

A segunda é a mesma regra, num lugar pior: um bloco entre parênteses é lido **inteiro de uma vez**.

```bat
set n=0
for %%i in (1 2 3) do (
  set /a n+=1
  echo %n%
)
```

Isso imprime `0`, `0`, `0` — e depois do bloco, `n` vale `3`. A conta aconteceu; o `echo` é que já estava com o valor antigo. A cura é a **expansão atrasada**, com `!` no lugar de `%`:

```bat
setlocal EnableDelayedExpansion
set n=0
for %%i in (1 2 3) do (
  set /a n+=1
  echo !n!
)
endlocal
```

Agora sai `1`, `2`, `3`.

### Aula 14.12 — Backup com robocopy e tarefas agendadas

`copy` e `xcopy` copiam; o **robocopy** é feito para backup: continua de onde parou, copia só o que mudou, e registra tudo em log.

```bat
robocopy "C:\Users\voce\Documents" "D:\Backup\Documents" /E /R:2 /W:5 /LOG:"D:\Backup\log.txt"
```

| Opção | O que faz |
|---|---|
| `/E` | copia as subpastas, inclusive as vazias |
| `/MIR` | **espelha**: deixa o destino idêntico à origem |
| `/L` | só lista o que faria — não copia nem apaga nada |
| `/R:2 /W:5` | tenta 2 vezes um arquivo com falha, esperando 5 segundos |
| `/LOG:arquivo` | grava o relatório num arquivo |
| `/XD pasta` | ignora uma pasta (ex.: `node_modules`) |

Por que mexer em `/R` e `/W`: segundo a própria ajuda do robocopy, o padrão é **1 milhão** de tentativas com **30 segundos** de espera entre elas. Um único arquivo travado por outro programa congela o backup, praticamente para sempre.

**Cuidado: `/MIR` apaga.** Espelhar significa que o que existe no destino e não existe na origem **é apagado do destino**. Se você inverter origem e destino, o backup apaga seus arquivos. Teste sempre com `/L` antes:

```bat
robocopy "C:\origem" "D:\destino" /MIR /L
```

```txt
	  *Arquivo EXTRA		      15	so-no-destino.txt
	  Novo Arquivo		      10	a.txt
```

Na simulação, o robocopy marcou como `*Arquivo EXTRA` o arquivo que só existia no destino — ele seria apagado. Conferi também que, com `/L`, nada foi copiado nem apagado.

**O código de saída do robocopy é diferente de todo o resto.** Para ele, `1` não é erro:

| Código | Significado | Medido |
|---|---|---|
| `0` | nada para copiar, tudo já estava igual | segunda cópia seguida |
| `1` | copiou arquivos com sucesso | primeira cópia |
| `8` ou mais | houve falha | origem inexistente deu `16` |

Então, no script, a pergunta certa é "8 ou mais?":

```bat
robocopy "%ORIGEM%" "%DESTINO%" /MIR /R:2 /W:5 /LOG:"%DESTINO%\log.txt"
if errorlevel 8 (
  echo BACKUP COM FALHA. Veja o log.
  exit /b 1
)
echo Backup concluído.
```

**Agendar para rodar sozinho** — `schtasks`:

```bat
schtasks /create /tn "Backup diario" /tr "C:\scripts\backup.bat" /sc daily /st 18:00
schtasks /query /tn "Backup diario"
schtasks /run /tn "Backup diario"
schtasks /delete /tn "Backup diario"
```

`/tn` é o nome da tarefa, `/tr` o que ela executa, `/sc` a frequência e `/st` a hora de início. Rode com `/run` uma vez logo depois de criar: descobrir que o agendamento não funcionava no dia em que você precisou do backup é a pior forma de descobrir.

---

## Projetos do Módulo 14

**Projeto 1 — Kit de diagnóstico em um clique**

Um `diagnostico.bat` que, ao ser executado, gera um relatório de texto com o estado do computador — o arquivo que você mandaria para o suporte, ou que o suporte pediria para você.

**Requisitos:**
- Grava tudo num arquivo com a data no nome, na pasta do script (`%~dp0`)
- Versão do Windows e dados do `systeminfo` filtrados com `findstr`
- Espaço livre na unidade C: e a saúde do disco pelo `Get-PhysicalDisk`
- Endereço IPv4 e gateway, e o resultado de um `ping` para `1.1.1.1` e de um `nslookup`
- Lista de dispositivos com problema (`pnputil /enum-devices /problem`)
- Lista de programas com atualização disponível (`winget upgrade`)
- Mensagens de erro também vão para o relatório (`2>&1`)
- Funciona numa janela **normal**, sem administrador

**Critério de aprovação:** o script roda em outro computador sem nenhuma alteração, e o relatório gerado responde, sem você abrir mais nada: tem espaço? o disco está saudável? tem internet? o DNS funciona? algum dispositivo com erro?

**Projeto 2 — Backup automático que avisa quando falha**

Um `backup.bat` que espelha uma pasta importante para outra unidade (ou pendrive) todo dia, sozinho.

**Requisitos:**
- Origem e destino em variáveis no topo do script
- Recusa rodar se a origem não existir (`if not exist`)
- Usa `robocopy /MIR` com `/R` e `/W` baixos e log com data
- Trata o código de saída do jeito certo: falha é **8 ou mais**
- Em caso de falha, grava o aviso num arquivo `FALHA.txt` na área de trabalho
- Agendado com `schtasks` e executado uma vez com `/run` para conferir
- Um teste de restauração: apague um arquivo de teste na origem, restaure a partir do backup

**Critério de aprovação:** você mostrou o `/L` rodado antes do primeiro `/MIR`, o log de uma execução agendada, e um caso de falha provocado de propósito (origem inexistente) que gerou o `FALHA.txt`.

## Checklist de saída do Módulo 14

- [ ] Sei quando um comando precisa de janela de administrador e abro uma com `Ctrl + Shift + Enter`
- [ ] Navego por pastas e unidades com `cd /d`, uso `Tab` e ponho aspas em caminho com espaço
- [ ] Sei que `del` e `rmdir` não passam pela Lixeira, e confiro com `dir` antes de apagar com curinga
- [ ] Uso `/?` antes de procurar um comando na internet
- [ ] Separo saída e erro com `>`, `2>&1` e `2>nul`
- [ ] Verifico espaço, saúde do disco (sem WMIC) e sistema de arquivos com `chkdsk`
- [ ] Sei a ordem DISM → SFC e explico por quê
- [ ] Atualizo programas com `winget` e encontro dispositivos com problema com `pnputil`
- [ ] Diagnostico falta de internet descendo as camadas: endereço, roteador, internet, DNS
- [ ] Encerro processo travado com `taskkill` e sei o que o `/F` custa
- [ ] Explico por que `%variável%` dentro de um bloco `( )` mostra o valor antigo, e uso `!variável!`
- [ ] Testo o `robocopy /MIR` com `/L` e trato o código de saída como falha só a partir de 8
