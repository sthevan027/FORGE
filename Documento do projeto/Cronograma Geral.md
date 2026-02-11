# 🗓️ Cronograma Geral — Forge

---

## 🔹 Fase 0 — Preparação (1 semana)

**Objetivo:** base sólida antes de codar

- Fechar escopo (✅ feito)
- Fechar stack (✅ feito)
- Estruturar repositório
- Setup Python + CLI base
- Definir padrão de logs e estado

**📅 Semana 1**

---

## 🔹 Fase 1 — MVP v0.1 (core funcional)

**Objetivo:** provar o conceito

### Semana 2

- `forge init`
- Estrutura `.forge/` (context, plans, tasks, qa, decisions, logs, config)
- Config + estado inicial
- Logs básicos

### Semana 3

- **Engenheiro IA:**
  - Leitura de briefing
  - Geração de plano (escopo, arquitetura, cronograma)
  - Comando `forge plan`
  - Persistência de planos

### Semana 4

- Aprovação de plano
- `forge approve plan`
- Controle de estado (state machine)
- Validações de fluxo (pré-condições por comando)

### Semana 5

- **Dev Bot** (fullstack provisório)
- `forge dev run`
- Geração de código simples
- Organização de output em `.forge/`

### Semana 6

- **QA Bot** básico
- `forge qa run`
- Relatório de QA em Markdown
- Bloqueio de avanço quando reprovado

### Semana 7

- `forge engineer review` — revisão final e decisão de avanço/correção
- Ajustes de integração
- `forge status` + `forge logs`
- Testes ponta a ponta do workflow

**📦 Entrega:** Forge MVP v0.1 funcional (CLI)

**📅 Semanas 2–7**

---

## 🔹 Fase 2 — Hardening do core (v0.2) — 3 semanas

**Objetivo:** deixar o Forge utilizável no dia a dia

### Semana 8

- Melhorar state machine (transições, pré-condições)
- Melhorar logs (níveis, contexto, persistência)

### Semana 9

- Melhorar tratamento de erros e mensagens ao usuário
- Refinar prompts do Engenheiro e do Dev Bot

### Semana 10

- Melhorar UX do terminal (Rich: tabelas, status, feedback)
- Testes manuais com projetos reais
- Ajustes a partir do uso

**📅 Semanas 8–10**

---

## 🔹 Fase 3 — Especialização de bots (v0.5) — 4 semanas

**Objetivo:** sair do dev genérico

### Semana 11

- Separar Dev Bot em **Frontend Bot** (módulo e responsabilidades)
- Ajuste do Engenheiro IA para distribuir tarefas frontend

### Semana 12

- **Backend Bot** (módulo e responsabilidades)
- Engenheiro IA passa a distribuir tarefas frontend e backend

### Semana 13

- Novos comandos: `forge frontend run`, `forge backend run`
- Persistência em `.forge/frontend/` e `.forge/backend/`
- Integração no workflow

### Semana 14

- QA adaptado por camada (validação frontend vs backend)
- Relatórios e critérios por tipo de entrega
- Revisão e estabilização da Fase 3

**📅 Semanas 11–14**

---

## 🔹 Fase 4 — DevOps e processo real (v0.8) — 3 semanas

**Objetivo:** engenharia completa

### Semana 15

- **DevOps Bot** dedicado (módulo, responsabilidades)
- Comando `forge devops run`
- Integração no planejamento do Engenheiro

### Semana 16

- Git workflow completo (init, branches, estratégia)
- Validação de ambientes (local, preparação para deploy)
- Preparação de deploy (sem automação total)

### Semana 17

- QA mais rigoroso (DevOps + código)
- Documentação interna do fluxo DevOps
- Estabilização da Fase 4

**📅 Semanas 15–17**

---

## 🔹 Fase 5 — Produto final v1.0 — 4 semanas

**Objetivo:** Forge completo

### Semana 18

- **Design Bot** (opcional): módulo, wireframes/UI, integração com workflow
- Comando `forge design run` (se mantido no escopo)

### Semana 19

- Prompts maduros (todos os bots)
- Ajustes de qualidade e consistência das saídas

### Semana 20

- Documentação oficial (README, uso, comandos, exemplos)
- Templates de projeto (estrutura base recomendada)

### Semana 21

- Estabilização geral
- Testes finais e polish
- Entrega v1.0

**📅 Semanas 18–21**

---

## ⏱️ Tempo total

| Marco | Duração |
| ----- | ------- |
| MVP funcional (v0.1) | ~7 semanas |
| Produto robusto (até v0.8) | ~17 semanas |
| Produto final (v1.0) | ~21 semanas (~5 meses) |

---

## 🧠 Leitura estratégica

- **MVP rápido** → valida ideia
- **Evolução contínua** → sem reescrita
- Cronograma respeita realidade solo

---

## Documentos do projeto

| Documento | Conteúdo |
| --------- | -------- |
| [Ideia do projeto - Forge](Ideia%20do%20projeto%20-%20Forge.md) | Conceito e diferencial |
| [Escopo do projeto](Escopo%20do%20projeto.md) | Visão v1.0 (Fase 5) |
| [MVP inicial - Forge v0.1](MVP%20inicial%20-%20Forge%20v0.1.md) | Escopo da Fase 1 |
| [Stack do projeto](Stack%20do%20projeto.md) | Tecnologias e arquitetura |
