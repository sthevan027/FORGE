# 🧱 Stack do Projeto — Forge

---

## 1. Linguagem principal

**Python 3.11+**

**Motivo:**

- Melhor ecossistema para IA
- Ideal para bots especializados
- Excelente para automação e orquestração
- Rápido para evoluir MVP → produto final

---

## 2. Interface (CLI)

| Ferramenta   | Uso                                      |
| ------------ | ---------------------------------------- |
| **Typer**    | Criação do CLI                           |
| **Rich**     | Logs, status, tabelas, feedback visual   |
| **InquirerPy** | Confirmações explícitas do usuário     |

- ✅ **CLI-first**
- ❌ Sem interface web
- ❌ Sem modo interativo avançado no MVP

---

## 3. Arquitetura de IA

### 🔌 LLM Adapter (camada própria)

Cada bot usa um adapter, desacoplado do provider.

**Suporte:**

- OpenAI
- Claude
- IA local (Ollama)
- Futuras IAs gratuitas

**Configuração por bot:**

```json
{
  "bot": "frontend",
  "provider": "openai"
}
```

---

## 4. Bots (módulos Python)

Cada bot é um **módulo isolado**, com:

- Responsabilidade única
- Input estruturado
- Output validável
- Sem decisão de escopo

**Bots:**

- **Engineer** — orquestrador
- **Frontend**
- **Backend**
- **DevOps**
- **QA**
- **Design** _(futuro)_

---

## 5. Orquestração e core

- Engine própria em Python
- State machine simples (JSON)
- Workflow rígido
- Validação de pré-condições por comando
- Estados persistidos localmente

---

## 6. Persistência e dados

**File system** — estrutura `.forge/`

| Extensão | Uso                    |
| -------- | ---------------------- |
| `.md`    | Planos, QA, decisões   |
| `.json`  | Estado, tarefas, configs |

- ❌ Sem banco de dados
- ❌ Sem cloud

---

## 7. Git e versionamento

- **Git nativo** (subprocess ou GitPython)
- Init repo
- **Branches padrão:** `main`, `develop`
- Commits opcionais e rastreados

---

## 8. QA e validação

- QA Bot em Python
- Validação semântica + estrutural
- Relatórios em Markdown
- QA **bloqueia** avanço no workflow

---

## 9. Segurança

- `.env` com **python-dotenv**
- Chaves locais
- Nenhuma execução automática
- Nenhum envio remoto sem comando

---

## 10. Empacotamento

- **pyproject.toml**
- Instalação via `pipx` ou `pip`
- Execução global: `forge init`

---

## 11. Estrutura do código (Forge)

```
forge/
├── forge/
│   ├── cli/
│   ├── core/
│   ├── engineer/
│   ├── bots/
│   │   ├── frontend/
│   │   ├── backend/
│   │   ├── devops/
│   │   └── qa/
│   ├── llm/
│   ├── state/
│   ├── git/
│   └── utils/
├── pyproject.toml
└── README.md
```

---

## 12. Regra de stack (travada)

> Se não reforça **processo**, **controle** ou **engenharia**, não entra na stack.

✅ Stack definida, coerente e pronta para execução.

---

## Documentos do projeto

| Documento | Conteúdo |
| --------- | -------- |
| [Ideia do projeto - Forge](Ideia%20do%20projeto%20-%20Forge.md) | Conceito e diferencial |
| [Escopo do projeto](Escopo%20do%20projeto.md) | Visão v1.0 e bots |
| [MVP inicial - Forge v0.1](MVP%20inicial%20-%20Forge%20v0.1.md) | Escopo do MVP (comandos e componentes) |
| [Cronograma Geral](Cronograma%20Geral.md) | Fases e prazos |
