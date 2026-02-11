# 📌 Escopo do Produto Final — Forge (v1.0)

---

## 1. Visão geral

**Forge** é uma plataforma CLI em Python que simula e orquestra um **time completo de engenharia de software**, composto por IAs especialistas por área, coordenadas por um **Engenheiro de Software IA**.

O Forge executa projetos de software com:

- Planejamento real
- Especialização técnica
- Validação contínua
- Controle humano total
- Rastreabilidade completa

---

## 2. Conceito central

> **Forge não usa um dev genérico. Forge trabalha com especialistas.**

Cada etapa do projeto é executada por um **bot especialista**, como em um time profissional real.

---

## 3. Arquitetura do time de IA (produto final)

### 👷 Engenheiro de Software IA (core)

**Responsável por:**

- Interpretar briefing
- Definir escopo, arquitetura e stack
- Criar cronograma e roadmap
- Quebrar o projeto em tarefas
- Distribuir tarefas para os bots corretos
- Revisar entregas
- Decidir próximos passos
- Interagir com o usuário para aprovações

- ❌ **Não escreve código diretamente.**

---

### 🎨 Design Bot (UX/UI)

**Responsável por:**

- Criar fluxo de navegação
- Criar telas e layouts
- Gerar wireframes e UI final
- Preparar estrutura visual para desenvolvimento

_(Integrável com Figma / templates no futuro)_

---

### 💻 Frontend Bot

**Responsável por:**

- Implementar UI
- Criar componentes
- Gerenciar estado
- Aplicar acessibilidade e boas práticas
- Respeitar design aprovado

---

### 🧠 Backend Bot

**Responsável por:**

- Criar APIs
- Definir regras de negócio
- Modelar banco de dados
- Garantir segurança e performance

---

### ⚙️ DevOps Bot

**Responsável por:**

- Criar e organizar repositório Git
- Definir estratégia de branches
- Configurar ambientes
- Preparar pipelines
- Validar builds e deploys

---

### 🧪 QA Bot

**Responsável por:**

- Validar funcionalidades
- Testar fluxos
- Identificar falhas
- Garantir critérios de aceite
- Bloquear avanço se necessário

---

## 4. CLI Forge (produto final)

**Comandos evoluídos (visão final):**

| Comando                 | Uso              |
| ----------------------- | ---------------- |
| `forge init`            | Inicializa       |
| `forge plan`            | Planejamento     |
| `forge approve plan`    | Aprova plano     |
| `forge design run`      | Design Bot       |
| `forge frontend run`    | Frontend Bot     |
| `forge backend run`     | Backend Bot      |
| `forge devops run`      | DevOps Bot       |
| `forge qa run`          | QA Bot           |
| `forge engineer review` | Revisão          |
| `forge status`          | Status           |
| `forge logs`            | Logs             |

- **CLI permanece o único meio de interação.**

---

## 5. Workflow final (produto completo)

1. Usuário cria projeto
2. Engenheiro cria planejamento
3. Usuário aprova planejamento
4. Design Bot cria UX/UI
5. Usuário aprova design
6. Frontend / Backend executam tarefas
7. DevOps prepara ambiente
8. QA valida entregas
9. Engenheiro revisa
10. **Usuário aprova ou solicita ajustes**

> **Nada avança sem aprovação.**

---

## 6. Persistência e auditoria

**Estrutura `.forge/` expandida:**

```
.forge/
├── context/
├── plans/
├── design/
├── frontend/
├── backend/
├── devops/
├── qa/
├── decisions/
├── logs/
└── config/
```

---

## 7. IA e integrações

**Múltiplas IAs:**

- OpenAI
- Claude
- IA local

- Seleção por bot
- Configuração manual
- Possibilidade de fallback futuro

---

## 8. Controle do usuário

O usuário:

- Aprova todas as etapas
- Pode intervir em qualquer momento
- Pode editar outputs
- Pode reprovar entregas
- Mantém **controle absoluto** do projeto

---

## 9. Fora do escopo (mesmo no produto final)

O Forge **não** terá:

- Interface web como canal obrigatório
- Execução automática sem aprovação do usuário
- Código gerado sem registro
- IA sem logs ou rastreabilidade
- Decisões sem auditoria

---

## 10. Filosofia final do produto

> **Forge** é um sistema de **engenharia assistida por IA**, não um gerador automático de software.
>
> Ele ensina, organiza, valida e executa — **sempre com o humano no controle.**

---

## 11. Relação MVP vs produto final

| Versão           | Bots                          |
| ---------------- | ----------------------------- |
| **MVP v0.1**     | 1 Dev Bot provisório (fullstack) |
| **Produto v1.0** | Bots especialistas por área   |

A visão final não muda; só a **profundidade da implementação**.

---

## Documentos do projeto

| Documento | Conteúdo |
| --------- | -------- |
| [Ideia do projeto - Forge](Ideia%20do%20projeto%20-%20Forge.md) | Conceito e diferencial |
| [MVP inicial - Forge v0.1](MVP%20inicial%20-%20Forge%20v0.1.md) | Escopo da primeira entrega (v0.1) |
| [Stack do projeto](Stack%20do%20projeto.md) | Tecnologias e arquitetura |
| [Cronograma Geral](Cronograma%20Geral.md) | Fases e prazos |

---

🔒 Produto final atualizado, coerente e fiel à ideia original.
