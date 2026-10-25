# Guia do VS Code

Como abrir, rodar e editar o Study Hub no Visual Studio Code com o mesmo ambiente em qualquer máquina. A configuração fica versionada em [`.vscode/`](../.vscode/).

## 1. Clonar e abrir

```bash
git clone https://github.com/jooaoleonardi/Meu_Study_Hub_TI.git
cd Meu_Study_Hub_TI
code .
```

Ao abrir a pasta, o VS Code oferece instalar as **extensões recomendadas**. Aceite. A lista está em `.vscode/extensions.json`.

## 2. Extensões recomendadas

| Extensão | Para que serve |
|---|---|
| Live Server | Abre o site local (`index.html`) com recarga automática |
| Prettier | Formata HTML, CSS e JavaScript |
| markdownlint | Aponta erros de estilo nos arquivos `.md` |
| Code Spell Checker + pacote pt-BR | Corrige a ortografia em português e inglês |
| GitLens | Mostra o histórico e o autor de cada linha |
| GitHub Pull Requests | Cria e revisa Pull Requests sem sair do editor |
| Python | Projetos práticos em Python (ex.: força bruta em hash) |

## 3. Rodar o site localmente

1. Abra `index.html`.
2. Clique em **Go Live** (canto inferior direito) ou use o comando `Live Server: Open with Live Server`.
3. O navegador abre em `http://127.0.0.1:5500`. Salvou o arquivo, a página recarrega.

O site é HTML, CSS e JavaScript puros, sem etapa de build.

## 4. Configurações compartilhadas (`.vscode/settings.json`)

- UTF-8, fim de linha `\n`, remoção de espaços no fim das linhas e uma linha final em branco.
- Indentação de 2 espaços (4 em Python).
- Formatação automática ao salvar **desligada**, para não gerar diffs enormes em arquivos já existentes. Para formatar, use `Shift + Option + F` (Mac) ou `Shift + Alt + F` (Windows).
- Git: fetch automático e sem confirmação de sincronização.
- Corretor ortográfico em `pt-BR` e `en`.

O `.gitignore` versiona só `settings.json` e `extensions.json`. Qualquer outro arquivo em `.vscode/` fica local.

## 5. Fluxo de Git no VS Code

1. Barra lateral **Controle de Código-Fonte** (`Ctrl+Shift+G`).
2. Crie uma branch: paleta de comandos (`Cmd/Ctrl+Shift+P`) → `Git: Create Branch`.
3. Escreva a mensagem no padrão `tipo(escopo): descrição` (veja o [CONTRIBUTING](../CONTRIBUTING.md)) e confirme.
4. `Publish Branch` e, com a extensão do GitHub, `Create Pull Request`.
5. Após o merge: `Git: Checkout to... main` e `Git: Pull`.

## 6. Segurança no editor

- Nunca salve senhas, tokens ou arquivos `.env` no workspace.
- Antes de cada commit, confira a lista de arquivos alterados.
- Mantenha ativo o **push protection** do GitHub (veja o [SECURITY](../SECURITY.md)).
