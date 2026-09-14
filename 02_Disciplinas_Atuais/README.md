# 02 — Disciplinas Atuais

Disciplinas do módulo corrente. Cada uma tem pasta própria, README próprio e o
mesmo par fixo de subpastas.

## Disciplinas do 1º Módulo

| Pasta | Disciplina | Por que está no Study Hub |
|---|---|---|
| [`Bootcamp_I/`](Bootcamp_I/) | Bootcamp I | Define a base de organização profissional para todo o curso. |
| [`Projeto_Integrador_IV/`](Projeto_Integrador_IV/) | Projeto Integrador IV | Concentra a aplicação prática das demais disciplinas; é a peça de portfólio mais forte do módulo. |
| [`Seguranca_Digital/`](Seguranca_Digital/) | Segurança Digital | Consolida fundamentos de segurança que devem ser aplicados em todo projeto futuro do repositório. |
| [`Sistemas_Tempo_Real_e_Embarcados/`](Sistemas_Tempo_Real_e_Embarcados/) | Sistemas em Tempo Real e Embarcados | Fortalece a base de lógica e de restrições de hardware, útil para automações e IA embarcada. |
| [`Teste_e_Qualidade_de_Software/`](Teste_e_Qualidade_de_Software/) | Teste e Qualidade de Software | Garante que os projetos publicados no portfólio tenham qualidade comprovada, e não apenas código funcionando. |

## Estrutura padrão de cada disciplina

```
Nome_Da_Disciplina/
├── README.md                  ← foco, material versionado e índice de entregas
├── Atividades_e_Entregas/     ← o que vale nota
└── Anotacoes_e_Resumos/       ← o que gera aprendizado
```

Essa estrutura é **idêntica em toda disciplina**, atual ou futura. A vantagem é
previsibilidade: quem procura uma entrega sabe exatamente onde olhar, sem
precisar explorar o repositório.

## Ciclo de vida

1. **Início do semestre** — a disciplina ganha sua pasta aqui, com README preenchido.
2. **Durante o semestre** — atividades e resumos são commitados semanalmente.
3. **Fim do semestre** — a pasta inteira migra para [`../04_Arquivo_Semestres_Anteriores/`](../04_Arquivo_Semestres_Anteriores/).

Isso mantém esta pasta sempre limpa e focada apenas no que está em curso.

## Padrão de nomes de arquivo

```
disciplina_tipo_tema.extensao
```

| Exemplo | Leitura |
|---|---|
| `bootcampI_atividade01_study_hub.pdf` | Bootcamp I, atividade 01, tema Study Hub |
| `seguranca_resumo_criptografia.md` | Segurança Digital, resumo, tema criptografia |
| `teste_plano_regressao_login.md` | Teste e Qualidade, plano de teste, tema login |
