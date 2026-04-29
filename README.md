# 🔨 Forge

**Forge** é um engenheiro de software em CLI que orquestra um time de IAs especializadas para construir projetos de forma **profissional**, **auditável** e **controlada**.

> *Forge forja software com processo, não com mágica.*

---

## O que é

Forge é uma ferramenta **CLI-first** em Python que simula um time completo de engenharia de software: um **Engenheiro de Software IA** coordena bots especialistas (Frontend, Backend, DevOps, QA e, no futuro, Design). Cada etapa segue planejamento real, validação obrigatória e **aprovação humana** — nada avança sozinho.

- **Não é** um gerador automático de código.
- **É** um sistema de engenharia assistida por IA, com o humano no controle.

---

## Funcionalidades

### Core

- **Briefing → plano:** lê o que você quer e gera escopo, arquitetura e cronograma.
- **Aprovação obrigatória:** cada fase só avança depois do seu *approve*.
- **Bots especialistas:** tarefas distribuídas por área (frontend, backend, DevOps, QA).
- **QA no fluxo:** validação de código e critérios de aceite; pode bloquear o avanço.
- **Rastreabilidade:** tudo em `.forge/` (planos, tarefas, decisões, logs). Nada automático sem registro.

### Diferenciais

| Diferencial | Descrição |
| ---------- | --------- |
| **CLI-first** | Terminal como único canal; sem interface web obrigatória. |
| **Workflow de engenharia** | Processo definido, não atalhos. |
| **Engenheiro orquestra** | O Engenheiro IA planeja e coordena; não escreve código. |
| **Múltiplas IAs** | OpenAI, Claude, Ollama (local); configuração por bot. |
| **Controle total** | Você aprova, edita outputs e pode reprovar a qualquer momento. |

---

## Comandos (visão geral)

| Comando | Descrição |
| ------- | --------- |
| `forge init` | Inicializa o projeto e a estrutura `.forge/`. |
| `forge plan` | Gera o planejamento (escopo, arquitetura, cronograma). |
| `forge approve plan` | Aprova o plano para seguir ao próximo passo. |
| `forge dev run` | Executa o Dev Bot (MVP: fullstack provisório). |
| `forge frontend run` / `forge backend run` | Executam os bots especialistas (pós-MVP). |
| `forge devops run` | Executa o DevOps Bot (pós-MVP). |
| `forge qa run` | Roda a validação de QA e gera relatório. |
| `forge engineer review` | Revisão do Engenheiro e decisão de avanço/correção. |
| `forge status` | Mostra o status atual do projeto. |
| `forge logs` | Exibe logs e histórico. |

*No MVP (v0.1) existem apenas: `init`, `plan`, `approve plan`, `dev run`, `qa run`, `engineer review`, `status`, `logs`.*

---

## Workflow resumido

1. Você inicia o projeto (`forge init`).
2. O Engenheiro IA gera o plano; você aprova (`forge plan` → `forge approve plan`).
3. Bots executam tarefas (dev, frontend, backend, devops conforme o escopo).
4. QA valida; o Engenheiro revisa.
5. Você aprova ou pede ajustes. **Nada avança sem sua aprovação.**

---

## Stack

- **Linguagem:** Python 3.11+
- **CLI:** Typer, Rich, InquirerPy
- **IA:** camada de adapter própria (OpenAI, Claude, Ollama)
- **Persistência:** sistema de arquivos (`.forge/`), sem banco nem cloud obrigatória
- **Git:** branches `main` e `develop`; workflow rastreável

---

## Documentação do projeto

A documentação de escopo, MVP, stack e cronograma está em:

- [**Documento do projeto/**](Documento%20do%20projeto/) — Ideia, Escopo (v1.0), MVP (v0.1), Stack, Cronograma e índice.

---

## Instalação (previsto)

```bash
# Via pip (quando publicado)
pip install forge

# Ou via pipx (recomendado para CLIs)
pipx install forge
```

Requisito: **Python 3.11+**.

---

## Desenvolvimento local

```bash
# Na raiz do repositório
python -m venv .venv

# Windows (PowerShell)
./.venv/Scripts/Activate.ps1

pip install -U pip
pip install -e .

# Ver comandos disponíveis
forge --help

# Inicializar a estrutura .forge/ em um diretório
forge init --path .
forge status --path .
forge logs --path .
```

---

## Licença

Este projeto está sob a licença **MIT**. Veja o arquivo [LICENSE](LICENSE) para detalhes.

---

## Autor

**Sthevan Santos** — [@sthevan027](https://github.com/sthevan027)
