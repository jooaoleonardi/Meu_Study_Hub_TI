"""Validação do breakcode.py com strings curtas.

Gera a hash SHA-256 de palavras conhecidas de 4 letras e confere se a busca
por força bruta encontra exatamente a palavra de origem. Com 4 letras são
26^4 = 456.976 combinações, o que roda em menos de um segundo.

Execução (a partir da pasta forca_bruta_hash/):
    python3 testes/validar_breakcode.py
"""

import hashlib
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

import breakcode  # noqa: E402

HASH_EXEMPLO_ENUNCIADO = "e46240714b5db3a23eee60479a623efba4d633d27fe4f03c904b9e219a7fbe60"
CASOS = ["aaaa", "zzzz", "java"]  # primeira, última e uma combinação do meio


if __name__ == "__main__":
    falhas = 0

    ok = hashlib.sha256(b"aaaaaaa").hexdigest() == HASH_EXEMPLO_ENUNCIADO
    print(f"[{'OK' if ok else 'FALHA'}] hash de 'aaaaaaa' confere com o enunciado")
    falhas += not ok

    for palavra in CASOS:
        alvo = hashlib.sha256(palavra.encode()).hexdigest()
        inicio = time.time()
        encontrada = breakcode.encontrar_hash(alvo, breakcode.CARACTERES, len(palavra))
        ok = encontrada == palavra
        falhas += not ok
        print(f"[{'OK' if ok else 'FALHA'}] {palavra} -> {encontrada} ({time.time() - inicio:.2f}s)")

    print("Todos os casos passaram." if falhas == 0 else f"{falhas} caso(s) falharam.")
    sys.exit(1 if falhas else 0)
