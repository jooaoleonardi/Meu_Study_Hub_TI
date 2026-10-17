# Changelog

Todas as mudanças relevantes do Study Hub ficam registradas aqui.

O formato segue o [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/) e as
versões seguem o [versionamento semântico](https://semver.org/lang/pt-BR/). Cada
versão corresponde a uma tag Git (`git tag -n` lista todas).

## [Não lançado]

### Adicionado

- Site em várias páginas, com menu entre elas e a página atual destacada.
- Página **Sobre** (trajetória, projeto SAE, motivação, formação e idiomas) e página **Carreira**
  (áreas de interesse, metas por horizonte, stack e certificações).
- Seção "Explore o portfólio" na página inicial, página 404, `sitemap.xml` e `robots.txt`.

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
