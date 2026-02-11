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

| Semana | Foco |
| ------ | ----- |
| **2** | `forge init` — estrutura `.forge/`, config + estado inicial, logs básicos |
| **3** | **Engenheiro IA:** leitura de briefing, geração de plano, `forge plan`, persistência de planos |
| **4** | Aprovação de plano — `forge approve plan`, controle de estado, validações de fluxo |
| **5** | **Dev Bot** (fullstack provisório) — `forge dev run`, geração de código simples, organização de output |
| **6** | **QA Bot** básico — `forge qa run`, relatório de QA, bloqueio de avanço |
| **7** | `forge engineer review`, revisão final, ajustes, `forge status` + `forge logs` |

**📦 Entrega:** Forge MVP v0.1 funcional (CLI)

---

## 🔹 Fase 2 — Hardening do core (v0.2) — 3 semanas

**Objetivo:** deixar o Forge utilizável no dia a dia

- Melhorar state machine
- Melhorar logs e erros
- Refinar prompts
- Melhorar UX do terminal
- Testes manuais com projetos reais

**📅 Semanas 8–10**

---

## 🔹 Fase 3 — Especialização de bots (v0.5) — 4 semanas

**Objetivo:** sair do dev genérico

- Separar Dev Bot em:
  - **Frontend Bot**
  - **Backend Bot**
- Ajuste do Engenheiro IA
- Novos comandos: `forge frontend run`, `forge backend run`
- QA adaptado por camada

**📅 Semanas 11–14**

---

## 🔹 Fase 4 — DevOps e processo real (v0.8) — 3 semanas

**Objetivo:** engenharia completa

- DevOps Bot dedicado
- Git workflow completo
- Validação de ambientes
- Preparação de deploy (sem automação total)
- QA mais rigoroso

**📅 Semanas 15–17**

---

## 🔹 Fase 5 — Produto final v1.0 — 4 semanas

**Objetivo:** Forge completo

- Design Bot (opcional)
- Prompts maduros
- Documentação oficial
- Templates de projeto
- Estabilização geral

**📅 Semanas 18–21**

---

## ⏱️ Tempo total

| Marco | Duração |
| ----- | ------- |
| MVP funcional | ~7 semanas |
| Produto robusto | ~14 semanas |
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
