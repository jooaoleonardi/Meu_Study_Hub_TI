# Guia de Git deste Repositório

Os comandos efetivamente usados no dia a dia do Study Hub. Não é um curso de
Git — é a referência rápida para não travar na hora de commitar.

---

## Configuração inicial (uma vez só)

```bash
git config --global user.name "Joao Leonardi"
git config --global user.email "jooao.leonardi@gmail.com"
```

## Clonar o repositório em outra máquina

```bash
git clone https://github.com/jooaoleonardi/Meu_Study_Hub_TI.git
cd Meu_Study_Hub_TI
```

---

## Ciclo do dia a dia

```bash
# 1. Ver o que mudou
git status

# 2. Adicionar tudo o que mudou
git add -A

# 3. Commitar com mensagem padronizada
git commit -m "docs(seguranca): adiciona resumo de criptografia"

# 4. Enviar para o GitHub
git push
```

### Adicionar apenas um arquivo específico

```bash
git add 02_Disciplinas_Atuais/Seguranca_Digital/Anotacoes_e_Resumos/arquivo.md
```

---

## Situações comuns

### Esqueci de incluir um arquivo no último commit

```bash
git add arquivo_esquecido.md
git commit --amend --no-edit
```

> Use apenas se ainda **não** tiver feito push.

### Errei a mensagem do último commit

```bash
git commit --amend -m "docs(seguranca): mensagem corrigida"
```

### Quero desfazer alterações não commitadas de um arquivo

```bash
git restore nome_do_arquivo.md
```

### Ver o histórico de forma resumida

```bash
git log --oneline --graph --decorate
```

### O push foi rejeitado porque há mudanças no GitHub

```bash
git pull --rebase
git push
```

---

## Autenticação

O GitHub não aceita mais senha de conta no push. As opções são:

| Método | Como funciona |
|---|---|
| **Token pessoal** | Gerar em *Settings → Developer settings → Personal access tokens*. Usar o token no lugar da senha. |
| **Navegador** | Na primeira autenticação o Git abre o navegador para autorizar. É o caminho mais simples no macOS. |
| **Chave SSH** | Configuração única, sem senha depois. Recomendado a médio prazo. |

> **Nunca** commite um token dentro do repositório. Se isso acontecer, revogue o
> token imediatamente — considerá-lo comprometido é a única postura segura.

---

## Glossário mínimo

| Termo | Significado |
|---|---|
| **repositório** | A pasta do projeto versionada pelo Git |
| **commit** | Um ponto salvo no histórico, com mensagem descritiva |
| **branch** | Uma linha de desenvolvimento. Aqui usamos apenas `main` |
| **remote / origin** | O endereço do repositório no GitHub |
| **push** | Enviar commits locais para o GitHub |
| **pull** | Trazer commits do GitHub para a máquina local |
| **.gitkeep** | Arquivo vazio usado para versionar pastas vazias, já que o Git só rastreia arquivos |
