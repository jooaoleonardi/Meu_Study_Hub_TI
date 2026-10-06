import hashlib
import itertools
import multiprocessing

HASH_ALVO = "70502ff6bb85356055ea52ff0a657afd09a52324a33734ccfb7bdedf05634925"
CARACTERES = 'abcdefghijklmnopqrstuvwxyz'
TAMANHO_STRING = 7


def gerar_combinacoes(parte_inicial, caracteres, tamanho):

    for sufixo in itertools.product(caracteres, repeat=tamanho - len(parte_inicial)):
        yield parte_inicial + ''.join(sufixo)


def encontrar_hash_parcial(parte_inicial, caracteres, tamanho, hash_alvo):

    for combinacao in gerar_combinacoes(parte_inicial, caracteres, tamanho):
        hash_gerada = hashlib.sha256(combinacao.encode()).hexdigest()
        if hash_gerada == hash_alvo:
            print(f'Palavra:{combinacao}')
            return combinacao
    return None


def encontrar_hash(hash_alvo, caracteres, tamanho):

    processos = []
    pool = multiprocessing.Pool(processes=multiprocessing.cpu_count()-1)

    tarefas = [
        (prefixo, caracteres, tamanho, hash_alvo)
        for prefixo in caracteres
    ]

    resultados = pool.starmap(encontrar_hash_parcial, tarefas)

    pool.close()
    pool.join()

    for resultado in resultados:
        if resultado:
            return resultado
    return None


if __name__ == "__main__":
    print(f"Iniciando busca para o hash alvo: {HASH_ALVO}")
    resultado = encontrar_hash(HASH_ALVO, CARACTERES, TAMANHO_STRING)

    if resultado:
        print(f"String encontrada: {resultado}")
    else:
        print("Nenhuma string encontrada que corresponda ao hash alvo.")
