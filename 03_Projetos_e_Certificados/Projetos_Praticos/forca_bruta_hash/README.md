# Força Bruta em Hash SHA-256

> Busca por força bruta, paralelizada em vários núcleos, da string de 7 letras minúsculas que gera uma hash SHA-256 conhecida.

| Campo | Dado |
|---|---|
| **Status** | Concluído |
| **Período** | nov/2024 |
| **Disciplina de origem** | Atividade acadêmica da graduação em Ciência da Computação |
| **Stack** | Python 3 (`hashlib`, `itertools`, `multiprocessing`) |
| **Repositório original** | [jooaoleonardi/Forca-Bruta-Hash](https://github.com/jooaoleonardi/Forca-Bruta-Hash) |

---

## O problema

Uma função de hash como a SHA-256 é de mão única: a partir da string é fácil calcular
a hash, mas a partir da hash não há como voltar para a string. Quando o conjunto de
entradas possíveis é pequeno, porém, dá para testar todas.

O desafio foi encontrar a string de **exatamente 7 caracteres**, só com letras de
`a` a `z`, que gera esta hash:

```
70502ff6bb85356055ea52ff0a657afd09a52324a33734ccfb7bdedf05634925
```

São 26⁷ = **8.031.810.176 combinações**, de `aaaaaaa` a `zzzzzzz`. Testar uma por uma
em um único núcleo de processador leva tempo demais, e é aí que entra a paralelização.

## A solução

1. **Geração das combinações sob demanda.** `itertools.product` gera as strings uma de
   cada vez (gerador), sem guardar os 8 bilhões de candidatos na memória.
2. **Divisão do trabalho pela primeira letra.** O espaço de busca é dividido em 26
   tarefas, uma para cada letra inicial (`a??????`, `b??????`, …, `z??????`).
3. **Execução em paralelo.** Um `multiprocessing.Pool` com `núcleos − 1` processos
   distribui as 26 tarefas entre os núcleos da máquina, deixando um núcleo livre para
   o sistema.
4. **Comparação.** Cada processo calcula a SHA-256 de cada candidato e compara com a
   hash alvo. O primeiro resultado não vazio é a resposta.

```
                       ┌─ processo 1 ─ testa a??????, depois outra letra livre ─┐
hash alvo ──► Pool ────┼─ processo 2 ─ testa b??????, depois outra letra livre ─┼──► string encontrada
(26 tarefas)           └─ processo N ─ …                                       ─┘
```

## Stack e justificativa

| Tecnologia | Por que foi escolhida |
|---|---|
| `hashlib` | Implementação padrão e otimizada da SHA-256 no Python |
| `itertools.product` | Gera o produto cartesiano das letras sem ocupar memória |
| `multiprocessing` | Usa todos os núcleos de verdade, sem a limitação do GIL que afeta as threads |

## Como executar

```bash
# Pré-requisitos: Python 3.8+ (só biblioteca padrão, nada para instalar)

# A partir desta pasta (forca_bruta_hash/)

# Validação rápida com palavras de 4 letras (menos de 1 segundo)
python3 testes/validar_breakcode.py

# Busca completa de 7 letras (pode levar bastante tempo, conforme a máquina)
python3 src/breakcode.py
```

## Estrutura do projeto

```
forca_bruta_hash/
├── README.md
├── src/
│   └── breakcode.py              ← código da busca (cópia do repositório original)
└── testes/
    └── validar_breakcode.py      ← validação com palavras conhecidas
```

## Resultados

A validação gera a hash de palavras conhecidas de 4 letras (a primeira combinação,
a última e uma do meio) e confere se a busca devolve exatamente a palavra de origem:

```
[OK] hash de 'aaaaaaa' confere com o enunciado
[OK] aaaa -> aaaa (0.18s)
[OK] zzzz -> zzzz (0.16s)
[OK] java -> java (0.20s)
Todos os casos passaram.
```

A string de 7 letras não é publicada aqui, para não entregar a resposta do desafio a
quem quiser resolvê-lo.

## Próximos passos

- [ ] **Parada antecipada:** hoje `pool.starmap` espera as 26 tarefas terminarem mesmo
      depois de a string ser encontrada. Trocar por `imap_unordered` e encerrar o pool
      no primeiro acerto reduz o tempo médio.
- [ ] **Máquinas de um núcleo:** `cpu_count() - 1` vira `0` e o `Pool` falha. Usar
      `max(1, cpu_count() - 1)`.
- [ ] Remover a variável `processos`, que não é usada.
- [ ] Medir o tempo total e a taxa de hashes por segundo com 1, 2, 4 e N processos.

## Aprendizados

O projeto mostra na prática por que senhas curtas e com poucos tipos de caractere são
frágeis: com 7 letras minúsculas, um computador comum testa todas as combinações. Também
mostrou a diferença entre threads e processos no Python e como dividir um problema
grande em partes independentes para usar todos os núcleos.
