# Padronização do Repositório

Regras que governam nomes, estrutura e commits. Seguir isso é o que mantém o
repositório navegável depois de dez disciplinas e centenas de arquivos.

---

## 1. Nomenclatura de pastas

| Regra | Exemplo correto | Exemplo incorreto |
|---|---|---|
| Prefixo numérico nas pastas de primeiro nível | `01_Apresentacao_e_Perfil` | `Apresentacao` |
| Sem acentos ou cedilha | `Seguranca_Digital` | `Segurança_Digital` |
| Sem espaços — usar underscore | `Atividades_e_Entregas` | `Atividades e Entregas` |
| Inicial maiúscula em cada palavra | `Projeto_Integrador_IV` | `projeto_integrador_iv` |

### Por que sem acento e sem espaço

1. **URL** — acentos viram códigos ilegíveis (`Seguran%C3%A7a`) no link do GitHub.
2. **Sistemas operacionais** — a codificação de acentos difere entre macOS,
   Windows e Linux, o que quebra clones.
3. **Linha de comando** — espaços exigem aspas ou escape em todo comando.

---

## 2. Nomenclatura de arquivos

Padrão geral, tudo em minúsculas:

```
disciplina_tipo_tema.extensao
```

| Componente | Função | Exemplos |
|---|---|---|
| `disciplina` | Identifica a origem | `bootcampI`, `seguranca`, `teste` |
| `tipo` | Identifica a natureza | `atividade01`, `resumo`, `plano`, `prova` |
| `tema` | Identifica o assunto | `study_hub`, `criptografia`, `regressao` |

### Exceção: certificados

```
AAAA-MM_instituicao_nome-do-curso.pdf
```

O prefixo de data garante ordenação cronológica automática.

---

## 3. Estrutura fixa de disciplina

Toda disciplina, sem exceção:

```
Nome_Da_Disciplina/
├── README.md
├── Atividades_e_Entregas/
└── Anotacoes_e_Resumos/
```

**A separação não é burocracia.** `Atividades_e_Entregas/` é o que vale nota e
precisa ser encontrado rápido em época de prazo. `Anotacoes_e_Resumos/` é o que
gera aprendizado e é consultado no estudo. Misturar os dois torna ambos lentos
de achar.

---

## 4. Mensagens de commit

```
tipo(escopo): descricao no imperativo, sem acento, em minusculas
```

| Tipo | Quando usar | Exemplo |
|---|---|---|
| `docs` | Documentação, README, resumos | `docs(seguranca): adiciona resumo de criptografia` |
| `feat` | Nova entrega, projeto ou material | `feat(bootcamp): adiciona entrega da fase 1` |
| `fix` | Correção de conteúdo ou link | `fix(readme): corrige link da arvore de pastas` |
| `chore` | Organização e manutenção | `chore(estrutura): arquiva disciplinas do modulo 1` |

### Regras da mensagem

- **Imperativo**: "adiciona", não "adicionado" nem "adicionando".
- **Sem acento**: evita problema de codificação em terminais diferentes.
- **Até 72 caracteres** na primeira linha.
- **Uma mudança lógica por commit** — não junte três assuntos em um commit só.

---

## 5. Markdown

- Todo arquivo começa com um `#` de título único.
- Hierarquia de títulos sem pular nível (`#` → `##` → `###`).
- Tabelas para dados comparáveis; listas para enumerações.
- Links relativos entre arquivos do repositório, nunca URL absoluta interna.
- Blocos de código sempre com a linguagem declarada.

---

## 6. O que não versionar

Definido em [`../.gitignore`](../.gitignore):

- Arquivos de sistema (`.DS_Store`, `Thumbs.db`)
- Configuração de editor (`.vscode/`, `.idea/`)
- Dependências (`node_modules/`, `venv/`)
- Credenciais (`.env`) — **nunca**, sob nenhuma circunstância
- Arquivos pesados (vídeos, ISOs) — usar link externo
