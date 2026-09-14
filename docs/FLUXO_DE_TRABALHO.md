# Fluxo de Trabalho

A rotina que mantém o repositório vivo. Um Study Hub abandonado no segundo mês
prova o contrário do que deveria provar.

---

## Rotina semanal

| Quando | Ação |
|---|---|
| **Após cada aula** | Criar o resumo em `Anotacoes_e_Resumos/` usando o modelo |
| **Ao concluir uma entrega** | Commitar em `Atividades_e_Entregas/` e atualizar o índice do README da disciplina |
| **Sexta-feira** | Revisar pendências, commitar o que ficou e conferir se algum README ficou desatualizado |

O commit semanal é o mínimo. É ele que constrói o gráfico de contribuições —
a evidência visual de consistência.

---

## Rotina de fim de módulo

1. Revisar [`01_Apresentacao_e_Perfil/stack_e_ferramentas.md`](../01_Apresentacao_e_Perfil/stack_e_ferramentas.md) — o que saiu de "aprendendo" para "domino"?
2. Revisar [`objetivos_de_carreira.md`](../01_Apresentacao_e_Perfil/objetivos_de_carreira.md) — algum objetivo mudou?
3. Mover as disciplinas concluídas para [`04_Arquivo_Semestres_Anteriores/`](../04_Arquivo_Semestres_Anteriores/)
4. Atualizar a tabela de disciplinas no README principal
5. Commit: `chore(estrutura): encerra modulo N`

---

## Ao concluir um projeto

1. Verificar os três critérios de entrada (funciona, documentado, validado)
2. Mover para `03_Projetos_e_Certificados/Projetos_Praticos/`
3. Criar o README do projeto a partir do modelo
4. Atualizar o índice de projetos
5. Commit: `feat(projetos): adiciona projeto nome_do_projeto`

---

## Checklist antes de cada commit

- [ ] Os nomes de arquivo seguem o padrão `disciplina_tipo_tema.extensao`?
- [ ] O arquivo está na pasta correta (`Atividades` vs `Anotacoes`)?
- [ ] Algum README de índice precisa ser atualizado?
- [ ] A mensagem de commit segue `tipo(escopo): descricao`?
- [ ] Nenhuma credencial ou dado sensível está sendo commitado?

---

## Princípio geral

> Commit pequeno e frequente vale mais que commit grande e raro.

Dez commits pequenos ao longo do mês contam uma história de consistência.
Um commit gigante no fim do semestre conta uma história de correria.
