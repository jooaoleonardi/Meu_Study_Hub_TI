# Política de Segurança

## Versões com suporte

O portfólio publicado em GitHub Pages corresponde sempre à branch `main`. Apenas a versão mais recente (a tag mais nova) recebe correções.

| Versão | Suporte |
|---|---|
| Última tag (`v2.x`) | Sim |
| Versões anteriores | Não |

## Como reportar uma vulnerabilidade

**Não abra uma Issue pública.** Use um destes canais:

1. **Relato privado no GitHub (preferido):** aba **Security → Report a vulnerability** neste repositório.
2. **E-mail:** jooao.leonardi@gmail.com, com o assunto `[SEGURANÇA] Meu Study Hub TI`.

Inclua, se possível: a descrição do problema, o endereço ou arquivo afetado, os passos para reproduzir e o impacto que você enxerga.

## O que esperar

- Confirmação de recebimento em até **5 dias úteis**.
- Avaliação e retorno sobre a correção em até **15 dias**.
- Crédito pelo relato no CHANGELOG, se você quiser.

## Escopo

Este é um site estático (HTML, CSS e JavaScript) sem login, banco de dados ou formulários. Têm relevância:

- exposição acidental de segredos, tokens ou dados pessoais no repositório;
- links ou scripts maliciosos em páginas do site;
- dependências com falhas conhecidas nos projetos práticos (ex.: Python).

Fora de escopo: falhas da própria plataforma GitHub ou GitHub Pages (reporte ao GitHub) e ataques de negação de serviço.

## Boas práticas adotadas no repositório

- Autenticação em dois fatores na conta do dono.
- Branch `main` protegida (Pull Request obrigatório, sem force-push).
- Secret scanning e push protection ativos.
- Dependabot alerts ativos.
- HTTPS obrigatório no GitHub Pages.
- `.gitignore` cobrindo `.env`, chaves e arquivos locais.
