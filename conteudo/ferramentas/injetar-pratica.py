"""
Leva conteudo/pratica/*.json para dentro do index.html.

O gerador original do portal se perdeu, mas os dados continuam num único
objeto — window.DADOS — dentro do index.html. Este script troca só os campos
que têm fonte em conteudo/pratica/ (laboratórios, avaliações e oficinas) e
regrava o objeto no mesmo formato, então o resto do arquivo fica intacto byte
a byte.

Antes de gravar, confere cada laboratório "Qual é a saída?" executando os
trechos (verificar-saidas.py). Se algum não bater, nada é gravado.

Uso: python injetar-pratica.py
"""
import importlib.util
import json
import re
import sys
from pathlib import Path

AQUI = Path(__file__).resolve().parent
RAIZ = AQUI.parents[1]
INDEX = RAIZ / "index.html"
PRATICA = RAIZ / "conteudo" / "pratica"

TIPOS = {"js", "html", "css", "guiado", "saida"}


def ler(nome: str):
    return json.loads((PRATICA / nome).read_text(encoding="utf-8"))


def serializar(dados) -> str:
    """O formato do gerador original: JSON compacto, acentos crus, e só
    `</script` escapado — senão o navegador fecharia a tag no meio dos dados."""
    texto = json.dumps(dados, separators=(",", ":"), ensure_ascii=False)
    return re.sub(r"</(script)", lambda m: "<\\/" + m.group(1), texto, flags=re.I)


def validar(modulos, labs) -> list[str]:
    erros = []
    por_num = {str(m["num"]): m for m in modulos}
    vistos = set()
    for chave, lista in labs.items():
        m = por_num.get(chave)
        if m is None:
            erros.append(f"labs.json cita o módulo {chave}, que não existe")
            continue
        aulas = {a["id"] for a in m["aulas"]}
        for lab in lista:
            onde = f"{lab.get('id')} (módulo {chave})"
            if lab["id"] in vistos:
                erros.append(f"id repetido: {onde}")
            vistos.add(lab["id"])
            if lab["tipo"] not in TIPOS:
                erros.append(f"tipo desconhecido '{lab['tipo']}' em {onde}")
            if lab.get("aula") and lab["aula"] not in aulas:
                erros.append(f"{onde} aponta para a aula {lab['aula']}, que não existe no módulo")
            if lab["tipo"] == "saida":
                for i, item in enumerate(lab.get("itens") or [], 1):
                    faltam = {"ling", "codigo", "saida", "porque"} - item.keys()
                    if faltam:
                        erros.append(f"{onde}, trecho {i}: faltam {sorted(faltam)}")
                if not lab.get("itens"):
                    erros.append(f"{onde} não tem trechos")
            elif lab["tipo"] != "guiado" and not lab.get("testes"):
                erros.append(f"{onde} não tem testes")
    return erros


def main() -> int:
    # newline="" preserva o CRLF do arquivo em qualquer sistema.
    with open(INDEX, encoding="utf-8", newline="") as f:
        html = f.read()
    inicio = re.search(r"window\.DADOS=", html).end()
    dados, tamanho = json.JSONDecoder().raw_decode(html[inicio:])
    original = html[inicio:inicio + tamanho]

    if serializar(dados) != original:
        print("O window.DADOS atual não sai igual ao ser regravado — o formato mudou. Nada foi gravado.")
        return 1

    labs, avaliacoes, oficinas = ler("labs.json"), ler("avaliacoes.json"), ler("oficinas.json")

    erros = validar(dados["modulos"], labs)
    if erros:
        print("Problemas em conteudo/pratica/labs.json:")
        print("\n".join(f"  - {e}" for e in erros))
        return 1

    spec = importlib.util.spec_from_file_location("verificar", AQUI / "verificar-saidas.py")
    verificar = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(verificar)
    if verificar.main() != 0:
        print("Há saídas que não conferem. Nada foi gravado.")
        return 1

    antes = sum(len(m["labs"]) for m in dados["modulos"])
    for m in dados["modulos"]:
        m["labs"] = labs.get(str(m["num"]), [])
        m["avaliacao"] = avaliacoes.get(str(m["num"]), m.get("avaliacao"))
    dados["oficinas"] = oficinas
    depois = sum(len(m["labs"]) for m in dados["modulos"])

    novo = html[:inicio] + serializar(dados) + html[inicio + tamanho:]
    if novo == html:
        print("\nindex.html já estava em dia.")
        return 0
    with open(INDEX, "w", encoding="utf-8", newline="") as f:
        f.write(novo)
    print(f"\nindex.html atualizado: {antes} → {depois} laboratórios")
    return 0


if __name__ == "__main__":
    sys.exit(main())
