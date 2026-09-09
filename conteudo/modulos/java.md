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
