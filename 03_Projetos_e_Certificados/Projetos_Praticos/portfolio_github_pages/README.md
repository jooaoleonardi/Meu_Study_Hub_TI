# Portfólio Study Hub (GitHub Pages)

> Página web estática que apresenta o Study Hub, meu perfil, disciplinas, projetos e entregas do Bootcamp I.

| Campo | Dado |
|---|---|
| **Status** | Publicado (v1.1) |
| **Período** | out/2026 |
| **Disciplina de origem** | Bootcamp I — Entrega Intermediária |
| **Stack** | HTML5, CSS3, JavaScript, Git, GitHub Pages |
| **Página publicada** | [jooaoleonardi.github.io/Meu_Study_Hub_TI](https://jooaoleonardi.github.io/Meu_Study_Hub_TI/) |

---

## O problema

O repositório organiza bem o material, mas um recrutador ou avaliador que recebe o
link precisa navegar por pastas e READMEs para entender quem eu sou e o que já
produzi. Faltava uma **porta de entrada visual**, de leitura rápida, que resumisse
o portfólio e apontasse para cada parte do repositório.

## A solução

Uma página única, publicada com GitHub Pages a partir da branch `main`, com as seções:

| Seção | Conteúdo |
|---|---|
| Sobre | Trajetória profissional e motivação para a TI |
| Study Hub | As seções do repositório, com link para cada pasta |
| Disciplinas | As disciplinas do módulo atual |
| Projetos | Os projetos práticos publicados |
| Entregas | Linha do tempo das fases do Bootcamp I, com o documento e os vídeos |
| Contato | E-mail, LinkedIn e GitHub |

Decisões de arquitetura:

- **Sem framework e sem build.** O GitHub Pages publica os arquivos exatamente como
  estão no repositório, sem dependências para instalar ou atualizar.
- **Tema claro e escuro.** Segue a preferência do sistema, com botão para alternar.
- **Responsiva.** Funciona do celular ao desktop, com menu recolhível em telas pequenas.
- **Acessível.** HTML semântico, link para pular ao conteúdo, foco visível e respeito
  a `prefers-reduced-motion`.

## Onde ficam os arquivos

O GitHub Pages só publica a partir da **raiz** do repositório ou da pasta `/docs`.
Como `/docs` já guarda a documentação do Study Hub, o site fica na raiz:

```
Meu_Study_Hub_TI/
├── index.html            ← estrutura e conteúdo da página
├── .nojekyll             ← publica os arquivos sem processamento do Jekyll
└── assets/
    ├── css/style.css     ← estilos, tokens de cor e tema escuro
    └── js/main.js        ← tema, menu mobile e destaque da seção ativa
```

Esta pasta guarda apenas a documentação do projeto.

## Stack e justificativa

| Tecnologia | Por que foi escolhida |
|---|---|
| HTML5 semântico | Estrutura clara para leitores de tela e mecanismos de busca |
| CSS3 (custom properties, grid, media queries) | Tema claro/escuro e layout responsivo sem bibliotecas |
| JavaScript puro | Três interações pequenas não justificam um framework |
| GitHub Pages | Hospedagem gratuita, integrada ao repositório e atualizada a cada push |

## Como executar

```bash
# Pré-requisitos: Git e Python 3 (ou qualquer servidor estático)

# Clonar
git clone https://github.com/jooaoleonardi/Meu_Study_Hub_TI.git
cd Meu_Study_Hub_TI

# Servir localmente e abrir http://localhost:8000
python3 -m http.server 8000
```

### Publicação

1. No GitHub: **Settings → Pages**.
2. Em **Build and deployment**, escolha **Deploy from a branch**.
3. Selecione a branch `main` e a pasta `/ (root)` e salve.
4. Em cerca de um minuto a página fica disponível no endereço indicado no topo.

Cada `git push` na `main` republica a página automaticamente.

## Versionamento

As versões seguem [versionamento semântico](https://semver.org/lang/pt-BR/) e são
marcadas com tags Git. O histórico detalhado está em [`CHANGELOG.md`](../../../CHANGELOG.md).

| Versão | O que mudou |
|---|---|
| `v1.0` | Primeira versão publicada: perfil, Study Hub, disciplinas, projetos, entregas e contato |
| `v1.1` | Adiciona o projeto Força Bruta em Hash SHA-256 à seção Projetos |

```bash
# Ver as versões
git tag -n

# Ver a página como estava em uma versão
git checkout v1.0
```

## Próximos passos

- [ ] Adicionar a foto de perfil
- [ ] Incluir o link do vídeo de apresentação da Fase 2
- [ ] Adicionar novos projetos à seção Projetos conforme forem concluídos

## Aprendizados

Publicar a página tornou concreto o ciclo completo do Git: editar no diretório de
trabalho, preparar na staging area, registrar o commit, marcar a versão com uma tag
e enviar ao GitHub, que publica o resultado sozinho.
