# Issues do Cronograma — Forge (para GitHub)

Use este arquivo para criar as issues no repositório **Forge**. Se o repo ainda não existir, crie em https://github.com/new (ex.: `sthevan027/Forge`).

---

## Como criar

1. Abra o repositório no GitHub.
2. Vá em **Issues** → **New issue**.
3. Para cada bloco abaixo: copie **Title** e **Body** (tudo entre os traços) na issue.

**Sugestão de labels:** `cronograma`, `fase-0`, `fase-1`, etc. (crie se quiser).

---

## Issue 1 — Fase 0

**Title:**
```
[Cronograma] Fase 0 — Preparação (Semana 1)
```

**Body:**
```
**Objetivo:** base sólida antes de codar

- [x] Fechar escopo (feito)
- [x] Fechar stack (feito)
- [ ] Estruturar repositório
- [ ] Setup Python + CLI base
- [ ] Definir padrão de logs e estado

📅 **Semana 1**
```

---

## Issue 2 — Fase 1 (MVP v0.1)

**Title:**
```
[Cronograma] Fase 1 — MVP v0.1 core funcional (Semanas 2–7)
```

**Body:**
```
**Objetivo:** provar o conceito

### Semana 2
- [ ] `forge init`
- [ ] Estrutura `.forge/` (context, plans, tasks, qa, decisions, logs, config)
- [ ] Config + estado inicial
- [ ] Logs básicos

### Semana 3
- [ ] **Engenheiro IA:** leitura de briefing
- [ ] Geração de plano (escopo, arquitetura, cronograma)
- [ ] Comando `forge plan`
- [ ] Persistência de planos

### Semana 4
- [ ] Aprovação de plano
- [ ] `forge approve plan`
- [ ] Controle de estado (state machine)
- [ ] Validações de fluxo (pré-condições por comando)

### Semana 5
- [ ] **Dev Bot** (fullstack provisório)
- [ ] `forge dev run`
- [ ] Geração de código simples
- [ ] Organização de output em `.forge/`

### Semana 6
- [ ] **QA Bot** básico
- [ ] `forge qa run`
- [ ] Relatório de QA em Markdown
- [ ] Bloqueio de avanço quando reprovado

### Semana 7
- [ ] `forge engineer review` — revisão final e decisão de avanço/correção
- [ ] Ajustes de integração
- [ ] `forge status` + `forge logs`
- [ ] Testes ponta a ponta do workflow

📦 **Entrega:** Forge MVP v0.1 funcional (CLI)
📅 **Semanas 2–7**
```

---

## Issue 3 — Fase 2 (Hardening)

**Title:**
```
[Cronograma] Fase 2 — Hardening do core v0.2 (Semanas 8–10)
```

**Body:**
```
**Objetivo:** deixar o Forge utilizável no dia a dia

### Semana 8
- [ ] Melhorar state machine (transições, pré-condições)
- [ ] Melhorar logs (níveis, contexto, persistência)

### Semana 9
- [ ] Melhorar tratamento de erros e mensagens ao usuário
- [ ] Refinar prompts do Engenheiro e do Dev Bot

### Semana 10
- [ ] Melhorar UX do terminal (Rich: tabelas, status, feedback)
- [ ] Testes manuais com projetos reais
- [ ] Ajustes a partir do uso

📅 **Semanas 8–10**
```

---

## Issue 4 — Fase 3 (Especialização)

**Title:**
```
[Cronograma] Fase 3 — Especialização de bots v0.5 (Semanas 11–14)
```

**Body:**
```
**Objetivo:** sair do dev genérico

### Semana 11
- [ ] Separar Dev Bot em **Frontend Bot** (módulo e responsabilidades)
- [ ] Ajuste do Engenheiro IA para distribuir tarefas frontend

### Semana 12
- [ ] **Backend Bot** (módulo e responsabilidades)
- [ ] Engenheiro IA passa a distribuir tarefas frontend e backend

### Semana 13
- [ ] Novos comandos: `forge frontend run`, `forge backend run`
- [ ] Persistência em `.forge/frontend/` e `.forge/backend/`
- [ ] Integração no workflow

### Semana 14
- [ ] QA adaptado por camada (validação frontend vs backend)
- [ ] Relatórios e critérios por tipo de entrega
- [ ] Revisão e estabilização da Fase 3

📅 **Semanas 11–14**
```

---

## Issue 5 — Fase 4 (DevOps)

**Title:**
```
[Cronograma] Fase 4 — DevOps e processo real v0.8 (Semanas 15–17)
```

**Body:**
```
**Objetivo:** engenharia completa

### Semana 15
- [ ] **DevOps Bot** dedicado (módulo, responsabilidades)
- [ ] Comando `forge devops run`
- [ ] Integração no planejamento do Engenheiro

### Semana 16
- [ ] Git workflow completo (init, branches, estratégia)
- [ ] Validação de ambientes (local, preparação para deploy)
- [ ] Preparação de deploy (sem automação total)

### Semana 17
- [ ] QA mais rigoroso (DevOps + código)
- [ ] Documentação interna do fluxo DevOps
- [ ] Estabilização da Fase 4

📅 **Semanas 15–17**
```

---

## Issue 6 — Fase 5 (v1.0)

**Title:**
```
[Cronograma] Fase 5 — Produto final v1.0 (Semanas 18–21)
```

**Body:**
```
**Objetivo:** Forge completo

### Semana 18
- [ ] **Design Bot** (opcional): módulo, wireframes/UI, integração com workflow
- [ ] Comando `forge design run` (se mantido no escopo)

### Semana 19
- [ ] Prompts maduros (todos os bots)
- [ ] Ajustes de qualidade e consistência das saídas

### Semana 20
- [ ] Documentação oficial (README, uso, comandos, exemplos)
- [ ] Templates de projeto (estrutura base recomendada)

### Semana 21
- [ ] Estabilização geral
- [ ] Testes finais e polish
- [ ] Entrega v1.0

📅 **Semanas 18–21**
```

---

## Resumo

| Issue | Fase | Semanas |
| ----- | ----- | ------- |
| 1 | Fase 0 — Preparação | 1 |
| 2 | Fase 1 — MVP v0.1 | 2–7 |
| 3 | Fase 2 — Hardening v0.2 | 8–10 |
| 4 | Fase 3 — Especialização v0.5 | 11–14 |
| 5 | Fase 4 — DevOps v0.8 | 15–17 |
| 6 | Fase 5 — Produto final v1.0 | 18–21 |

**Tempo total:** ~21 semanas (~5 meses)
