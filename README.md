<div align="center">

# Meu Study Hub TI

**O repositório central da minha formação em Tecnologia.**

Materiais, exercícios e projetos do curso de Ciência da Computação —
registrados de forma versionada, pública e rastreável.

`Ciência da Computação` · `Brasília – DF` · `1º Módulo`

</div>

---

## Sumário

- [Sobre este repositório](#sobre-este-repositório)
- [Quem sou eu](#quem-sou-eu)
- [Propósito](#propósito)
- [Estrutura do repositório](#estrutura-do-repositório)
- [Árvore completa](#árvore-completa)
- [Disciplinas do módulo atual](#disciplinas-do-módulo-atual)
- [Padrões e convenções](#padrões-e-convenções)
- [Como navegar](#como-navegar)
- [Roadmap do projeto](#roadmap-do-projeto)
- [Documentação de apoio](#documentação-de-apoio)
- [Contato](#contato)

---

## Sobre este repositório

O **Study Hub** é o projeto integrador do Bootcamp I: construir, desde o primeiro
módulo do curso, a arquitetura que vai abrigar toda a produção acadêmica e
profissional da graduação.

A premissa é simples: conhecimento teórico é metade da jornada. A outra metade é
conseguir **organizar a produção** e **demonstrar a evolução prática**. Este
repositório é a infraestrutura dessa segunda metade.

---

## Quem sou eu

**João Leonardi** — estudante de Ciência da Computação em Brasília, pai de três
filhos, com trajetória profissional em análise de negócios e gestão de produto.

Venho de uma carreira em que minha função sempre foi traduzir o problema das
pessoas em solução. Trabalhando com rotinas de alto volume documental, automatizei
minhas primeiras tarefas repetitivas e vi o impacto real que algumas linhas de
lógica bem pensadas têm sobre horas de trabalho humano. Foi ali que decidi migrar
para a Tecnologia de forma estruturada.

Meu objetivo é ser a ponte entre o problema de negócio e a solução técnica —
com domínio real dos dois lados.

> Perfil completo em [`01_Apresentacao_e_Perfil/`](01_Apresentacao_e_Perfil/)

---

## Propósito

Este repositório não é uma pasta de faculdade. É a **linha do tempo pública do meu
aprendizado**. Ele cumpre quatro funções:

| Função | O que resolve |
|---|---|
| **Centralização** | Todo material tem um endereço único e previsível. Nada se perde entre pastas locais, e-mails e downloads soltos. |
| **Rastreabilidade** | O histórico de commits registra consistência, frequência e evolução técnica ao longo dos semestres. |
| **Vitrine profissional** | Um link público que pode ser enviado em processo seletivo no lugar de uma promessa de currículo. |
| **Prática de ferramentas** | Git, GitHub, versionamento, Markdown e padronização desde o 1º módulo — as ferramentas que o mercado realmente usa. |

Em uma frase: **o Study Hub transforma esforço de estudo em ativo profissional
demonstrável.**

---

## Estrutura do repositório

| Pasta | Conteúdo | Quando é atualizada |
|---|---|---|
| [`01_Apresentacao_e_Perfil/`](01_Apresentacao_e_Perfil/) | Identidade, trajetória, objetivos de carreira e stack em estudo. Porta de entrada do portfólio. | A cada mudança relevante de objetivo ou competência |
| [`02_Disciplinas_Atuais/`](02_Disciplinas_Atuais/) | Uma pasta por disciplina do semestre corrente. | Semanalmente, conforme as aulas |
| [`03_Projetos_e_Certificados/`](03_Projetos_e_Certificados/) | Projetos práticos autorais e certificados obtidos. A vitrine. | A cada projeto concluído ou certificado emitido |
| [`04_Arquivo_Semestres_Anteriores/`](04_Arquivo_Semestres_Anteriores/) | Disciplinas já concluídas, arquivadas. | Ao fim de cada semestre |
| [`_templates/`](_templates/) | Modelos padronizados de resumo, atividade e projeto. | Quando um padrão evolui |
| [`docs/`](docs/) | Documentação do próprio repositório: padronização, fluxo de trabalho e apoio de Git. | Quando uma convenção muda |

---

## Árvore completa

```
Meu_Study_Hub_TI/
│
├── README.md                          ← você está aqui
├── .gitignore
├── LICENSE
│
├── 01_Apresentacao_e_Perfil/
│   ├── README.md
│   ├── perfil_academico.md            ← identificação e biografia
│   ├── objetivos_de_carreira.md       ← áreas de interesse e metas
│   ├── stack_e_ferramentas.md         ← tecnologias em estudo
│   └── assets/
│       └── foto_perfil.png
│
├── 02_Disciplinas_Atuais/
│   ├── README.md
│   │
│   ├── Bootcamp_I/
│   │   ├── README.md
│   │   ├── Atividades_e_Entregas/
│   │   └── Anotacoes_e_Resumos/
│   │
│   ├── Projeto_Integrador_IV/
│   │   ├── README.md
│   │   ├── Atividades_e_Entregas/
│   │   └── Anotacoes_e_Resumos/
│   │
│   ├── Seguranca_Digital/
│   │   ├── README.md
│   │   ├── Atividades_e_Entregas/
│   │   └── Anotacoes_e_Resumos/
│   │
│   ├── Sistemas_Tempo_Real_e_Embarcados/
│   │   ├── README.md
│   │   ├── Atividades_e_Entregas/
│   │   └── Anotacoes_e_Resumos/
│   │
│   └── Teste_e_Qualidade_de_Software/
│       ├── README.md
│       ├── Atividades_e_Entregas/
│       └── Anotacoes_e_Resumos/
│
├── 03_Projetos_e_Certificados/
│   ├── README.md
│   ├── Projetos_Praticos/
│   │   └── README.md
│   └── Certificados/
│       └── README.md
│
├── 04_Arquivo_Semestres_Anteriores/
│   └── README.md
│
├── _templates/
│   ├── README.md
│   ├── modelo_resumo.md
│   ├── modelo_atividade.md
│   └── modelo_projeto.md
│
└── docs/
    ├── PADRONIZACAO.md
    ├── FLUXO_DE_TRABALHO.md
    └── GUIA_GIT.md
```

---

## Disciplinas do módulo atual

| Pasta | Disciplina | Material versionado |
|---|---|---|
| [`Bootcamp_I/`](02_Disciplinas_Atuais/Bootcamp_I/) | Bootcamp I | Planejamento da arquitetura do Study Hub, entregas do Projeto Integrador e materiais de apoio das aulas. |
| [`Projeto_Integrador_IV/`](02_Disciplinas_Atuais/Projeto_Integrador_IV/) | Projeto Integrador IV | Documentação do projeto, levantamento de requisitos, diagramas, atas de reunião e entregas parciais. |
| [`Seguranca_Digital/`](02_Disciplinas_Atuais/Seguranca_Digital/) | Segurança Digital | Resumos das aulas, estudos de caso, checklists de boas práticas e anotações sobre vulnerabilidades conhecidas. |
| [`Sistemas_Tempo_Real_e_Embarcados/`](02_Disciplinas_Atuais/Sistemas_Tempo_Real_e_Embarcados/) | Sistemas em Tempo Real e Embarcados | Anotações técnicas, exercícios resolvidos e códigos comentados. |
| [`Teste_e_Qualidade_de_Software/`](02_Disciplinas_Atuais/Teste_e_Qualidade_de_Software/) | Teste e Qualidade de Software | Planos de teste, casos de teste, scripts de validação e relatórios de execução. |

Toda disciplina — atual ou futura — segue **o mesmo par fixo de subpastas**:

- **`Atividades_e_Entregas/`** — o que vale nota: trabalhos, provas, entregas avaliadas.
- **`Anotacoes_e_Resumos/`** — o que gera aprendizado: resumos, mapas mentais, material de estudo.

Essa repetição é proposital. Quando entrar uma disciplina nova no 2º módulo, não
há nada a decidir — a estrutura já escala sozinha.

---

## Padrões e convenções

### Nomenclatura de pastas

| Regra | Motivo |
|---|---|
| Prefixo numérico (`01_`, `02_`, `03_`, `04_`) | Força a ordem lógica de leitura, não a alfabética |
| Sem acentos, cedilhas ou espaços | Evita erro de URL, de clone entre sistemas operacionais e de linha de comando |
| Underscore (`_`) como separador | Padrão legível e seguro em qualquer ambiente |
| Palavras com inicial maiúscula | `Atividades_e_Entregas` em vez de `atividades_e_entregas` |

### Nomenclatura de arquivos

Padrão: **`disciplina_tipo_tema.extensao`** — tudo em minúsculas.

```
bootcampI_atividade01_study_hub.pdf
seguranca_resumo_criptografia_simetrica.md
teste_plano_regressao_login.md
```

### Mensagens de commit

Padrão: **`tipo(escopo): descrição no imperativo`**

```
docs(perfil): adiciona objetivos de carreira do 2o modulo
feat(bootcamp): adiciona entrega da fase 1
fix(readme): corrige link quebrado da arvore de pastas
chore(estrutura): arquiva disciplinas do semestre anterior
```

| Tipo | Uso |
|---|---|
| `docs` | Documentação, README, resumos e anotações |
| `feat` | Nova entrega, novo projeto, novo material |
| `fix` | Correção de conteúdo, link ou formatação |
| `chore` | Organização, arquivamento, manutenção da estrutura |

> Detalhamento completo em [`docs/PADRONIZACAO.md`](docs/PADRONIZACAO.md)

---

## Como navegar

**Se você é recrutador ou avaliador:**

1. Comece por [`01_Apresentacao_e_Perfil/`](01_Apresentacao_e_Perfil/) para entender quem eu sou.
2. Veja [`03_Projetos_e_Certificados/`](03_Projetos_e_Certificados/) para os entregáveis práticos.
3. Consulte o histórico de commits para ver a consistência ao longo do tempo.

**Se você é colega de curso:**

1. [`02_Disciplinas_Atuais/`](02_Disciplinas_Atuais/) tem os resumos organizados por disciplina.
2. [`_templates/`](_templates/) tem os modelos que uso — sinta-se à vontade para copiar.

---

## Roadmap do projeto

| Fase | Entrega | Status |
|---|---|---|
| **Fase 1** | Guia de Arquitetura — planejamento lógico no Google Docs + pitch em vídeo | Concluída |
| **Fase 2** | Construção física do repositório intermediário | Em andamento |
| **Fase 3** | Publicação do portfólio digital completo | Planejada |

### Metas de médio prazo

- [ ] Manter frequência de commits semanal durante todo o semestre
- [ ] Publicar ao menos 2 projetos práticos autorais em `03_Projetos_e_Certificados/`
- [ ] Documentar cada projeto com README próprio (problema, solução, stack)
- [ ] Arquivar o 1º módulo em `04_` ao fim do semestre

---

## Documentação de apoio

| Documento | Conteúdo |
|---|---|
| [`docs/PADRONIZACAO.md`](docs/PADRONIZACAO.md) | Todas as regras de nomenclatura, estrutura e commits |
| [`docs/FLUXO_DE_TRABALHO.md`](docs/FLUXO_DE_TRABALHO.md) | Rotina semanal de atualização do repositório |
| [`docs/GUIA_GIT.md`](docs/GUIA_GIT.md) | Comandos de Git usados no dia a dia deste repositório |

---

## Contato

| Canal | Endereço |
|---|---|
| E-mail | jooao.leonardi@gmail.com |
| LinkedIn | _(inserir link)_ |
| GitHub | [@jooaoleonardi](https://github.com/jooaoleonardi) |

### Links do Projeto Integrador — Fase 1

| Entregável | Link |
|---|---|
| Documento base (Google Docs) | _(inserir link público)_ |
| Pitch de apresentação (YouTube) | _(inserir link)_ |

---

<div align="center">

*Este repositório é atualizado continuamente ao longo do curso.*

</div>
