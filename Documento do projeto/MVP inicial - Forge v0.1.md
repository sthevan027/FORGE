# 🚀 MVP Inicial — Forge v0.1

---

## 🎯 Objetivo do MVP

Provar que o **workflow de engenharia orquestrada por IA em CLI** funciona, com:

- Planejamento real
- Execução controlada
- Validação obrigatória
- Controle humano total

**Nada além disso.**

---

## 🧱 Componentes do MVP

### 1️⃣ CLI Forge (funcional)

**Comandos obrigatórios:**

| Comando               | Uso                    |
| --------------------- | ---------------------- |
| `forge init`         | Inicializa projeto     |
| `forge plan`         | Gera planejamento      |
| `forge approve plan` | Aprova plano          |
| `forge dev run`      | Executa Dev Bot        |
| `forge qa run`       | Executa QA Bot         |
| `forge engineer review` | Revisão do engenheiro |
| `forge status`       | Status do projeto      |
| `forge logs`         | Logs e histórico       |

- Sem subcomandos extras
- Sem modo interativo avançado

---

### 2️⃣ Engenheiro IA (core)

**Inclui:**

- Leitura do briefing
- Criação de:
  - Escopo técnico
  - Arquitetura básica
  - Cronograma simples
- Quebra do projeto em tarefas
- Geração de prompts estruturados
- Revisão das entregas
- Decisão de avanço ou correção

- ❌ **Não escreve código.**

---

### 3️⃣ Dev Bot (provisório — fullstack)

⚠️ **Exceção do MVP**

- Executa tarefas técnicas
- Gera código inicial
- Respeita arquitetura definida
- Salva outputs organizados
- Não decide nada fora da tarefa

> Esse bot será quebrado em **frontend** / **backend** no produto final.

---

### 4️⃣ QA Bot (básico)

- Valida código gerado
- Checa estrutura, coerência e fluxo
- Aprova ou reprova
- Gera relatório em Markdown

- Sem testes automatizados complexos

---

### 5️⃣ Git essencial

- Init de repositório
- **Branches:** `main`, `develop`
- Commits opcionais
- ❌ Sem CI/CD

---

## 📁 Estrutura local do projeto (MVP)

```
.forge/
├── context/
├── plans/
├── tasks/
├── qa/
├── decisions/
├── logs/
└── config/
```

---

## 🔁 Workflow do MVP (imutável)

1. `forge init`
2. `forge plan`
3. `forge approve plan`
4. `forge dev run`
5. `forge qa run`
6. `forge engineer review`
7. **Usuário aprova ou pede ajustes**

- ❌ Nenhuma etapa pula validação

---

## 🧠 IA no MVP

- 1 provider configurável por projeto
- Seleção manual
- Sem fallback automático
- Adapters simples

---

## 🔐 Segurança e controle

- `.env` local
- Nenhuma execução automática
- Tudo logado
- Usuário aprova tudo

---

## ❌ Fora do MVP (adiado)

- Bots especialistas (frontend/backend/DevOps separados)
- Design Bot
- Figma
- Web / app
- Marketplace
- Deploy automático
- Cloud
- Colaboração

---

## ✅ Critério de sucesso do MVP

O MVP está aprovado quando:

- Cria um projeto real
- Executa o workflow completo
- Gera código organizado
- Bloqueia avanço sem aprovação
- É utilizável no terminal no dia a dia

---

## 🧠 Regra de ouro do MVP

> O MVP **não muda a ideia**. Ele apenas prova o núcleo.

---

## Documentos do projeto

| Documento | Conteúdo |
| --------- | -------- |
| [Ideia do projeto - Forge](Ideia%20do%20projeto%20-%20Forge.md) | Conceito e diferencial |
| [Escopo do projeto](Escopo%20do%20projeto.md) | Visão completa v1.0 (para onde o MVP evolui) |
| [Stack do projeto](Stack%20do%20projeto.md) | Tecnologias e arquitetura |
| [Cronograma Geral](Cronograma%20Geral.md) | Fases e prazos (MVP = Fase 1) |
