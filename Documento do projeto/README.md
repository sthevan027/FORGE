# 📁 Documentos do Projeto Forge

Documentação do projeto **Forge** — CLI que orquestra um time de IAs para construir software com processo, validação e controle humano.

---

## Como os documentos se alinham

| Documento | O que define | Relação com os outros |
| --------- | ------------- | ----------------------- |
| **[Ideia do projeto - Forge](Ideia%20do%20projeto%20-%20Forge.md)** | Conceito, diferencial e slogan | Base; tudo deriva daqui |
| **[Escopo do projeto](Escopo%20do%20projeto.md)** | Produto final v1.0: bots especialistas, workflow completo, CLI | Visão de destino |
| **[MVP inicial - Forge v0.1](MVP%20inicial%20-%20Forge%20v0.1.md)** | Primeira entrega: 1 Dev Bot, Engenheiro, QA, comandos mínimos | Subconjunto do Escopo; prova o conceito |
| **[Stack do projeto](Stack%20do%20projeto.md)** | Python, CLI (Typer/Rich/InquirerPy), IA, estrutura `.forge/` e do código | Suporta Ideia, MVP e Escopo |
| **[Cronograma Geral](Cronograma%20Geral.md)** | Fases 0→5, prazos (MVP em ~7 sem, v1.0 em ~21 sem) | Ordena a execução do MVP e do Escopo |

---

## Ideias comuns (alinhadas em todos)

- **CLI-first** — sem interface web; terminal como único canal.
- **Engenheiro IA** orquestra e planeja; **não escreve código**; distribui para os bots.
- **Aprovação obrigatória** — nenhuma etapa avança sem o usuário aprovar.
- **MVP v0.1** = 1 Dev Bot fullstack provisório; **v1.0** = bots especialistas (Frontend, Backend, DevOps, QA, Design opcional).
- **Git** com branches `main` e `develop`; **QA** pode bloquear avanço.
- **Rastreabilidade** — logs, estado em `.forge/`, nada automático sem registro.

Cada documento tem no final a seção **Documentos do projeto** com links para os demais.
