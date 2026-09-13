"""
Executa cada trecho dos laboratórios "Qual é a saída?" e compara com a
resposta cadastrada em conteudo/pratica/labs.json.

Nenhuma resposta entra no portal sem ter rodado: se o trecho não produzir
exatamente a saída que o aluno vai precisar digitar, este script falha. Um
trecho numa linguagem sem compilador nesta máquina também falha — "não deu
para conferir" nunca vira "conferido".

Uso: python verificar-saidas.py            (confere tudo)
     python verificar-saidas.py --mostrar  (imprime a saída real de cada trecho)
"""
import json
import os
import shutil
import sqlite3
import subprocess
import sys
import tempfile
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[2]
LABS = RAIZ / "conteudo" / "pratica" / "labs.json"


def normalizar(texto: str) -> str:
    """A mesma regra do portal (função normalizarSaida no index.html).

    Espaço no fim da linha e linhas vazias no fim não contam. Espaço no começo
    e no meio da linha contam — em `git status --short` eles são a resposta.
    """
    linhas = texto.replace("\r\n", "\n").replace("\r", "\n").split("\n")
    return "\n".join(l.rstrip() for l in linhas).rstrip("\n")


def rodar_python(preludio: str, codigo: str) -> str:
    env = dict(os.environ, PYTHONIOENCODING="utf-8", PYTHONHASHSEED="0")
    r = subprocess.run(
        [sys.executable, "-c", f"{preludio}\n{codigo}"],
        capture_output=True, text=True, encoding="utf-8", env=env, timeout=30,
    )
    if r.returncode != 0:
        raise RuntimeError(r.stderr.strip().splitlines()[-1])
    return r.stdout


def rodar_sql(preludio: str, codigo: str) -> str:
    """Imprime como o sqlite3 do terminal: colunas com |, NULL vazio."""
    con = sqlite3.connect(":memory:")
    try:
        con.executescript(preludio)
        linhas = con.execute(codigo).fetchall()
    finally:
        con.close()
    return "\n".join("|".join("" if v is None else str(v) for v in l) for l in linhas)


def rodar_bash(preludio: str, codigo: str) -> str:
    bash = shutil.which("bash")
    if not bash:
        raise FileNotFoundError("bash")
    with tempfile.TemporaryDirectory() as pasta:
        # Um HOME vazio e o idioma fixo: sem isso a configuração global do Git
        # e a tradução das mensagens entrariam na saída.
        env = dict(os.environ, HOME=pasta, LC_ALL="C", LANG="C",
                   GIT_CONFIG_NOSYSTEM="1", GIT_CONFIG_GLOBAL=os.devnull)
        r = subprocess.run(
            [bash, "-c", f"{preludio}\n{codigo}"],
            cwd=pasta, capture_output=True, text=True, encoding="utf-8",
            env=env, timeout=60,
        )
    return r.stdout


EXECUTORES = {"python": rodar_python, "sql": rodar_sql, "bash": rodar_bash}


def main() -> int:
    mostrar = "--mostrar" in sys.argv
    labs = json.loads(LABS.read_text(encoding="utf-8"))
    total = falhas = 0

    for mod, lista in labs.items():
        for lab in lista:
            if lab["tipo"] != "saida":
                continue
            for i, item in enumerate(lab["itens"], 1):
                total += 1
                rotulo = f"m{mod} {lab['id']} #{i} ({item['ling']})"
                executor = EXECUTORES.get(item["ling"])
                try:
                    if executor is None:
                        raise FileNotFoundError(f"sem executor para {item['ling']}")
                    real = normalizar(executor(lab.get("preludio", ""), item["codigo"]))
                except Exception as e:  # noqa: BLE001 — qualquer falha reprova
                    falhas += 1
                    print(f"  NÃO CONFERIDO  {rotulo}: {e}")
                    continue

                esperado = normalizar(item["saida"])
                if mostrar:
                    print(f"--- {rotulo}\n{real}")
                if real != esperado:
                    falhas += 1
                    print(f"  DIVERGE  {rotulo}\n    cadastrado: {esperado!r}\n    real:       {real!r}")
                elif not mostrar:
                    print(f"  ok  {rotulo}")

    print(f"\n{total - falhas}/{total} trechos conferidos por execução")
    return 1 if falhas else 0


if __name__ == "__main__":
    sys.exit(main())
