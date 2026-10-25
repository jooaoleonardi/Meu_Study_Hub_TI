# Como contribuir com o Meu Study Hub TI

Obrigado pelo interesse! Este repositório é o portfólio acadêmico e profissional de João Vitor Leonardi (Ciência da Computação, UniCEUB). Sugestões, correções e revisões são bem-vindas.

## Antes de começar

- Leia o [README](README.md) e os guias em [`docs/`](docs/) (`PADRONIZACAO.md`, `FLUXO_DE_TRABALHO.md` e `GUIA_GIT.md`).
- Para mudanças grandes, abra uma **Issue** antes e descreva o que pretende fazer.
- Para vulnerabilidades, **não** abra Issue pública. Siga o [SECURITY.md](SECURITY.md).

## Fluxo de trabalho

```bash
# 1. Atualize a main
git switch main && git pull

# 2. Crie uma branch curta e descritiva
git switch -c feat/nome-curto

# 3. Faça commits pequenos e frequentes
git commit -m "docs(readme): explica a estrutura de pastas"

# 4. Envie a branch
git push -u origin feat/nome-curto
```

5. Abra um **Pull Request** para a `main`, referenciando a Issue (`Closes #N`).
6. Preencha o checklist do template do PR.
7. Após a revisão e o merge, a `main` é publicada automaticamente no GitHub Pages.

A `main` é protegida: não se faz push direto nela.

## Padrão de commits

Formato: `tipo(escopo): descrição`, em português, no imperativo, com até 72 caracteres.

| Tipo | Quando usar |
|---|---|
| `feat` | nova funcionalidade ou novo conteúdo no portfólio |
| `fix` | correção de erro ou link quebrado |
| `docs` | mudança só em documentação |
| `style` | formatação ou visual, sem mudar o comportamento |
| `refactor` | reorganização sem mudar o resultado |
| `test` | testes e validações |
| `chore` | tarefas de manutenção |

Exemplos: `feat(projetos): adiciona projeto de forca bruta em hash` · `fix(site): corrige link da página Entregas`

## Padrão de pastas e arquivos

- Pastas numeradas (`01_`, `02_`...), sem acentos e sem espaços, com `_` como separador.
- Um `README.md` em cada pasta.
- Arquivos de disciplina: `disciplina_tipo_tema.extensao` (ex.: `bootcampI_atividade01_study_hub.pdf`).
- Novos projetos e resumos partem dos modelos em [`_templates/`](_templates/).

## Versionamento

Usamos [Versionamento Semântico](https://semver.org/lang/pt-BR/) e [Keep a Changelog](https://keepachangelog.com/pt-BR/). Toda mudança relevante entra no [CHANGELOG.md](CHANGELOG.md).

## Regras de segurança

- Nunca envie senhas, tokens, chaves de API ou arquivos `.env`.
- Não inclua dados pessoais de terceiros nem documentos pessoais.
- Dúvidas sobre algo sensível: pergunte antes de enviar.
