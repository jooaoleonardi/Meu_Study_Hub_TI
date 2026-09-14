#!/bin/bash
# ---------------------------------------------------------------------------
# Sobe o Study Hub para o GitHub.
#
# ANTES DE RODAR:
#   1. Acesse https://github.com/new
#   2. Repository name: Meu_Study_Hub_TI
#   3. Marque "Public"
#   4. NAO marque "Add a README file" (o repo precisa nascer vazio)
#   5. Clique em "Create repository" e copie a URL
#
# COMO RODAR (no Terminal, dentro desta pasta):
#   bash subir_no_github.sh SEU_USUARIO
# ---------------------------------------------------------------------------
set -e

USUARIO="$1"
REPO="Meu_Study_Hub_TI"

if [ -z "$USUARIO" ]; then
  echo "Uso: bash subir_no_github.sh SEU_USUARIO_DO_GITHUB"
  exit 1
fi

cd "$(dirname "$0")"

git init -q
git add -A
git -c user.name="$USUARIO" -c user.email="jooao.leonardi@gmail.com" \
    commit -q -m "Fase 1: arquitetura inicial do Study Hub"
git branch -M main
git remote remove origin 2>/dev/null || true
git remote add origin "https://github.com/$USUARIO/$REPO.git"
git push -u origin main

echo ""
echo "Pronto. Repositorio publicado em:"
echo "  https://github.com/$USUARIO/$REPO"
