# Changelog

Todas as mudanças relevantes do Study Hub ficam registradas aqui.

O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e as
versões seguem o [versionamento semântico](https://semver.org/lang/pt-BR/). Cada
versão corresponde a uma tag Git (`git tag -n` lista todas).

## [2.0] — 2026-10-25

### Adicionado

- Política de segurança (`SECURITY.md`) e guia de contribuição (`CONTRIBUTING.md`).
- `CODEOWNERS` e template de Pull Request em `.github/`.
- Proteção da branch `main`, secret scanning, push protection e Dependabot alerts.
- Plano de Implantação do PortfolioHUB com apoio do Google Gemini (entrega final do Bootcamp I).

### Alterado

- Rodapé e terminal do topo passam a mostrar a versão 2.0.
- Página **Versionamento** passa a listar as versões 1.3 e 2.0.

### Corrigido

- Tags `v1.2` e `v1.3` criadas conforme o histórico deste changelog.

## [1.3] — 2026-10-17

### Adicionado

- Site em várias páginas, com menu entre elas e a página atual destacada.
- Página **Sobre** (trajetória, projeto SAE, motivação, formação e idiomas) e página **Carreira**
  (áreas de interesse, metas por horizonte, stack e certificações).
- Página **Projetos**: problema, solução, decisões, validação e aprendizados de cada projeto,
  critérios de entrada no portfólio e como adicionar um novo projeto.
- Página **Disciplinas**: as cinco disciplinas do módulo, estrutura fixa de pastas, padrão de nomes
  e rotina de estudo versionada.
- Página **Versionamento**: histórico de versões, convenção de commits, ciclo de Git, tags e
  checklist antes de cada commit.
- Página **Entregas**: vídeo de apresentação incorporado, requisitos do desafio com a evidência de cada um,
  fases do Bootcamp I e critérios de avaliação.
- Seção "Explore o portfólio" na página inicial, página 404, `sitemap.xml` e `robots.txt`.

### Alterado

- Rodapé e terminal do topo passam a mostrar a versão 1.3.

## [1.2] — 2026-10-17

### Adicionado

- Barra de progresso de leitura, botão de voltar ao topo e entrada suave das seções
  (desativada com `prefers-reduced-motion`).
- Bloco de competências na seção Sobre e botão "Ver projetos" no topo.
- Link para as tags de versão na Fase 2 das entregas.
- Metadados para compartilhamento (Open Graph, Twitter, `theme-color`) e dados estruturados.
- Estilos de impressão.

### Alterado

- Rodapé e terminal do topo passam a mostrar a versão 1.2.

## [1.1] — 2026-10-06

### Adicionado

- Projeto [Força Bruta em Hash SHA-256](03_Projetos_e_Certificados/Projetos_Praticos/forca_bruta_hash/)
  na seção Projetos da página.

### Alterado

- Rodapé e terminal do topo da página passam a mostrar a versão 1.1.

## [1.0] — 2026-10-06

Primeira versão do portfólio publicada com GitHub Pages.

### Adicionado

- Página do portfólio (`index.html`, `assets/css/style.css`, `assets/js/main.js`)
  com perfil, estrutura do Study Hub, disciplinas, projetos, entregas e contato.
- Tema claro/escuro, layout responsivo e menu mobile.
- Documentação do projeto em
  [`03_Projetos_e_Certificados/Projetos_Praticos/portfolio_github_pages/`](03_Projetos_e_Certificados/Projetos_Praticos/portfolio_github_pages/).
- Este changelog.

### Corrigido

- README do Bootcamp I renderizado como bloco de código por causa de indentação.
- Referência à foto de perfil, que ainda não existe, sinalizada como pendente.

## [0.1] — 2026-09-13

Fase 1: arquitetura inicial do Study Hub.

### Adicionado

- Estrutura de pastas `01_` a `04_`, `_templates/` e `docs/`.
- README principal, perfil acadêmico, objetivos de carreira e stack.
- Padronização de nomes e commits, fluxo de trabalho e guia de Git.

[1.1]: https://github.com/jooaoleonardi/Meu_Study_Hub_TI/releases/tag/v1.1
[1.0]: https://github.com/jooaoleonardi/Meu_Study_Hub_TI/releases/tag/v1.0
[0.1]: https://github.com/jooaoleonardi/Meu_Study_Hub_TI/releases/tag/v0.1
