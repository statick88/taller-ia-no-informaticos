# Estructura OpenCode - Guía Completa

## Arquitectura OpenCode

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        OPENCODE.AI                                    │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   ┌─────────────┐    ┌─────────────┐    ┌─────────────┐             │
│   │ opencode.json│    │ AGENTS.md  │    │ mcp.json   │             │
│   │ Agentes     │    │ Perfil     │    │ Extensions  │             │
│   │ Skills      │    │ Context    │    │ Tools      │             │
│   │ Permisos    │    │ Rules      │    │             │             │
│   └─────────────┘    └─────────────┘    └─────────────┘             │
│                                                                     │
│   ┌─────────────────────────────────────────────────────────┐       │
│   │                    DIRECTORIES                           │       │
│   │                                                         │       │
│   │  ~/.config/opencode/                                   │       │
│   │  ├── opencode.json       → Agentes y configuración    │       │
│   │  ├── AGENTS.md           → Perfil principal            │       │
│   │  ├── mcp.json            → MCP servers                   │       │
│   │  ├── skills/             → Skills del usuario          │       │
│   │  │   └── mi-skill/                                   │       │
│   │  │       └── SKILL.md                                 │       │
│   │  ├── agents/             → Agentes personalizados       │       │
│   │  │   └── mi-agente.md                                │       │
│   │  ├── prompts/            → Prompts de agentes         │       │
│   │  └── skill-libraries/    → Librerías de skills       │       │
│   │                                                         │       │
│   └─────────────────────────────────────────────────────────┘       │
└─────────────────────────────────────────────────────────────────────────────┘
```

---

## 1. opencode.json - Estructura Completa

```json
{
  "$schema": "https://opencode.ai/config.json",
  
  // Modelo por defecto
  "model": "opencode/minimax-m2.5-free",
  
  // Plugins instalados
  "plugin": [
    "opentmux",
    "opencode-ghostty-notify",
    "opencode-skills-collection@latest"
  ],
  
  // Proveedores de IA (locales o remotos)
  "provider": {
    "ollama": {
      "name": "Ollama (Local)",
      "api": "openai",
      "options": {
        "baseURL": "http://127.0.0.1:11434/v1",
        "apiKey": "ollama"
      },
      "models": {
        "llama3.2:3b": {
          "id": "llama3.2:3b",
          "name": "Llama 3.2 3B"
        }
      }
    },
    "lmstudio": {
      "name": "LM Studio (Local)",
      "api": "openai",
      "options": {
        "baseURL": "http://127.0.0.1:1234/v1",
        "apiKey": "lm-studio"
      },
      "models": {
        "qwen3.5-35b": {
          "id": "qwen3.5-35b-a3b",
          "name": "Qwen 3.5 35B"
        }
      }
    }
  },
  
  // Sistema de agentes
  "agent": {
    // Agente primario (carga por defecto)
    "developer": {
      "description": "FullStack Developer + SDD Orchestrator — React, Next.js, TypeScript, Python",
      "mode": "primary",
      "model": "opencode/minimax-m2.5-free",
      
      // Prompt inline (alternativa a archivo)
      "prompt": "You are a senior fullstack developer...",
      
      // Skills activados para este agente
      "skills": [
        "react-19",
        "nextjs-15",
        "typescript",
        "tailwind-4",
        "sdd-apply",
        "sdd-spec",
        "sdd-design",
        "software-security"
      ],
      
      // Herramientas disponibles
      "tools": {
        "bash": true,
        "read": true,
        "write": true,
        "edit": true,
        "glob": true,
        "grep": true,
        "delegate": true,
        "mcp": true
      },
      
      // Permisos especiales
      "permission": {
        "task": {
          "*": "deny",
          "sdd-apply": "allow",
          "sdd-spec": "allow"
        }
      }
    },
    
    // Agente secundario
    "security-researcher": {
      "description": "Trigger: security, pentest, vuln, hacker, ctf. Security researcher — Pentesting, CVE research, Bug Bounty",
      "mode": "all",
      "model": "opencode/minimax-m2.5-free",
      "prompt": "You are a security researcher...",
      
      "skills": [
        "pentest-methodology",
        "pentest-web",
        "xss-hunter",
        "sqli-hunter",
        "cyber-intelligence"
      ],
      
      "tools": {
        "bash": true,
        "read": true,
        "write": true,
        "websearch": true,
        "webfetch": true
      }
    },
    
    // Sub-agente (ejecuta tareas específicas)
    "sdd-apply": {
      "description": "Implement SDD tasks from specs",
      "hidden": true,
      "mode": "subagent",
      "model": "opencode/minimax-m2.5-free",
      
      // Prompt desde archivo externo
      "prompt": "{file:/ruta/a/sdd-apply.md}",
      
      "skills": [
        "software-security",
        "code-review"
      ],
      
      "tools": {
        "bash": true,
        "read": true,
        "write": true,
        "edit": true
      }
    }
  },
  
  // MCP Servers (extensiones de capacidades)
  "mcp": {
    "context7": {
      "enabled": true,
      "type": "remote",
      "url": "https://mcp.context7.com/mcp"
    },
    
    "notebooklm": {
      "enabled": true,
      "type": "local",
      "command": ["notebooklm-mcp"],
      "timeout": 300000
    },
    
    "github": {
      "type": "local",
      "command": ["npx", "-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "your-token-here"
      }
    }
  },
  
  // Permisos globales
  "permission": {
    "bash": {
      "*": "allow",
      "sudo *": "ask",
      "git push": "ask",
      "rm *": "ask"
    },
    "read": {
      "*": "allow",
      "**/.env": "deny",
      "**/.env.*": "deny",
      "**/.ssh/**": "deny"
    }
  },
  
  // Configuración experimental
  "experimental": {
    "mcp_timeout": 300000
  }
}
```

---

## 2. AGENTS.md - Perfil de Usuario

```markdown
# Diego Saavedra García — AGENTS.md

## Identity

**Diego Medardo Saavedra García** — Full Stack Developer (10+ yrs) | Docente Universitario (6+ yrs, 100+ students) | MSc Ciberseguridad UCM (2024-present) | Investigador

> El desarrollador pasa a ser el DIRECTOR DEL PROCESO. La IA ejecuta, el humano valida.

---

## Perfiles Disponibles

| Perfil | Descripción | Especialidad |
|--------|-------------|-------------|
| **statick** | Senior Architect & Researcher | Full Stack, arquitectura moderna, SDD, mentoring |
| **gentle-orchestrator** | COORDINATOR | SDD orchestration, multi-agent coordination |
| **facilitator** | Facilitator/Teacher | Course creation, mentoring |

---

## Stack Técnico

```
Frontend:     React, Next.js, TypeScript, Tailwind
Mobile:       React Native, Expo, Flutter
Backend:      Python (FastAPI), Node.js, Django
Database:     PostgreSQL, MongoDB, Redis
Cloud:        AWS, GCP, Docker, Kubernetes
Security:     Pentesting, CTF, Bug Bounty, CVE research
AI/LLM:       OpenAI, Claude, Local models (Ollama, LM Studio)
```

---

## SDD Workflow

Spec-Driven Development con gates:

```
HU → [Refine] → [Close Decisions] → HITL Approval → Tasks → Apply → Verify → Archive
                                              ↓
                                    QA + Security + Design gates
```

### Fases SDD

| Fase | Agente | Gate |
|------|--------|------|
| HU | explore | - |
| Refine | sdd-spec | Spec |
| Design | sdd-design | Design |
| HITL | humano | APPROVAL |
| Apply | sdd-apply | - |
| Verify | qa-engineer | QA |

---

## Reglas de Comportamiento

- **NUNCA** hacer commit sin tests passing
- **SIEMPRE** seguir TypeScript strict mode
- **RESPETAR** Clean Architecture
- **USAR** Conventional Commits
- **MANTENER** secrets fuera del código

---

## Preferences

- pnpm como package manager
- Dark mode por defecto
- JetBrains Mono / Fira Code para código
- RevealJS para presentaciones
- Notion para documentación
```

---

## 3. SKILL.md - Estructura de Skills

```markdown
---
name: mi-skill
description: "Trigger: mi-skill, keyword1, keyword2. Descripción breve de qué hace este skill."
disable-model-invocation: true
user-invocable: false
license: MIT
metadata:
  author: tu-nombre
  version: "1.0"
  delegate_only: true
---

> **ORCHESTRATOR GATE**: Si cargaste este skill via `skill()`, eres el ORCHESTRADOR — STOP. No ejecutes inline. Delega al sub-agente `mi-skill-executor`.

## Activation Contract

Describe cuándo se activa este skill y qué contexto necesita.

**Se activa cuando:**
- El usuario menciona "mi-skill" o keywords relacionadas
- Un agente necesita capacidades de este skill
- Se solicita específicamente via `/mi-skill`

## Hard Rules

Reglas que NUNCA se deben violar:

```markdown
- ✅ SIEMPRE verificar X antes de Y
- ✅ USAR este formato de output
- ❌ NUNCA hacer Z
- ❌ NUNCA procesar sin autorización
```

## Soft Rules

Preferencias y convenciones:

```markdown
- Preferir formato A sobre B
- Usar este estilo de naming
- Seguir esta estructura de archivos
```

## Decision Gates

| Input | Acción |
|-------|--------|
| caso-1 | Ejecutar función A |
| caso-2 | Ejecutar función B |
| default | Retornar error |

## Execution Steps

```
1. ANALYZE
   - Recibir input del usuario
   - Validar parámetros
   - Verificar precondiciones

2. EXECUTE
   - Ejecutar lógica principal
   - Manejar errores

3. OUTPUT
   - Formatear resultado
   - Guardar artifacts si necesario
   - Retornar summary
```

## Output Contract

```typescript
interface MiSkillOutput {
  status: 'success' | 'error' | 'partial';
  executive_summary: string;
  artifacts: string[];  // paths o IDs
  next_recommended: string[];
  risks: string[];
  skill_resolution: 'injected' | 'fallback-registry' | 'fallback-path' | 'none';
}
```

## Referencias

- [references/detalles.md](references/detalles.md) — documentación extendida
- [../otro-skill/SKILL.md](../otro-skill/SKILL.md) — skill relacionado
- [../../templates/plantilla.md](../../templates/plantilla.md) — plantillas
```

---

## 4. SKILL.md Completo - Ejemplo Real

```markdown
---
name: sdd-apply
description: "Trigger: sdd apply, implement tasks, execute tasks. Implement SDD tasks from specs and design."
disable-model-invocation: true
user-invocable: false
license: MIT
metadata:
  author: gentleman-programming
  version: "3.0"
  delegate_only: true
---

> **ORCHESTRATOR GATE**: Este skill es para EXECUTORS. Delega a `sdd-apply` sub-agent.

## Activation Contract

Se activa cuando:
- Orchestrator invoca `/sdd-apply [change]`
- Se necesitan implementar tareas de un cambio SDD
- Apply-progress existe para continuar

## Hard Rules

```markdown
- ✅ Follow specs + design como fuente de verdad
- ✅ Check apply-progress ANTES de empezar (continuación)
- ✅ Write tests para lógica nueva
- ✅ Run linter/typecheck/tests antes de retornar
- ✅ Save progress a apply-progress después de cada batch
- ✅ Follow strict TDD si está configurado
- ❌ NUNCA divergir del spec/design
- ❌ NUNCA dejar tests en estado failing
```

## Soft Rules

```markdown
- Usar work-unit commits
- Mantener PRs < 400 líneas si es posible
- Chained PRs para cambios grandes
- No implementar features fuera del scope
```

## Decision Gates

| Condición | Acción |
|----------|--------|
| apply-progress existe | Leer y mergear con progreso previo |
| strict_tdd: true | TDD loop: red → green → refactor |
| strict_tdd: false | Implementar → test → verify |
| cambio > 400 líneas | Solicitar chained PRs |
| delivery_strategy: auto-chain | Implementar siguiente slice |

## Execution Steps

### 1. Preparación
```
a. Leer spec desde artifact store
b. Leer design desde artifact store  
c. Buscar apply-progress (si existe)
d. Verificar strict_tdd mode
e. Resolver artifact_store mode
```

### 2. Implementación
```
a. Iterar sobre tasks
b. Para cada task:
   - Read context (1-3 files)
   - Implementar código
   - Si strict_tdd: TDD loop
   - Si no: implementar + test básico
   - Save progress
c. Batch commits por work-unit
```

### 3. Verificación
```
a. Run linter
b. Run typecheck
c. Run tests
d. Report status
```

## Output Contract

```typescript
interface SddApplyOutput {
  status: 'completed' | 'in_progress' | 'blocked';
  executive_summary: string;
  
  implementation: {
    tasks_completed: number;
    tasks_total: number;
    files_changed: string[];
    lines_added: number;
    lines_removed: number;
  };
  
  quality: {
    linting: 'pass' | 'fail';
    typecheck: 'pass' | 'fail';
    tests: 'pass' | 'fail' | 'skipped';
    test_count?: { passed: number; failed: number };
  };
  
  progress: {
    batch: number;
    total_batches: number;
    next_tasks: string[];
  };
  
  blockers?: string[];
  risks?: string[];
  next_recommended: string[];
}
```

## Referencias

- [references/apply-details.md](references/apply-details.md)
- `../sdd-spec/SKILL.md`
- `../sdd-design/SKILL.md`
- `../sdd-verify/SKILL.md`
```

---

## 5. mcp.json - Configuración de MCPs

```json
{
  // MCP Server: Documentación
  "context7": {
    "enabled": true,
    "type": "remote",
    "url": "https://mcp.context7.com/mcp"
  },
  
  // MCP Server: Memoria persistente
  "engram": {
    "type": "local",
    "command": [
      "engram",
      "mcp",
      "--tools=agent"
    ]
  },
  
  // MCP Server: Google NotebookLM
  "notebooklm": {
    "enabled": true,
    "type": "local",
    "command": ["notebooklm-mcp"],
    "timeout": 300000
  },
  
  // MCP Server: GitHub Integration
  "github": {
    "type": "local",
    "command": [
      "npx",
      "-y",
      "@modelcontextprotocol/server-github"
    ],
    "env": {
      "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_TOKEN}"
    }
  },
  
  // MCP Server: Jira Integration
  "jira": {
    "type": "local",
    "command": [
      "npx",
      "-y",
      "@modelcontextprotocol/server-jira"
    ],
    "env": {
      "JIRA_HOST": "tu-dominio.atlassian.net",
      "JIRA_EMAIL": "tu@email.com",
      "JIRA_API_TOKEN": "${JIRA_API_TOKEN}"
    }
  },
  
  // MCP Server: Base de datos
  "database": {
    "type": "local",
    "command": [
      "npx",
      "-y",
      "@modelcontextprotocol/server-sqlite",
      "--db-path",
      "./data/app.db"
    ]
  },
  
  // MCP Server: Slack
  "slack": {
    "type": "local",
    "command": [
      "npx",
      "-y",
      "@modelcontextprotocol/server-slack"
    ],
    "env": {
      "SLACK_BOT_TOKEN": "${SLACK_BOT_TOKEN}",
      "SLACK_TEAM_ID": "${SLACK_TEAM_ID}"
    }
  },
  
  // MCP Server: Playwright (browser automation)
  "playwright": {
    "type": "local",
    "command": [
      "npx",
      "-y",
      "@playwright/mcp@latest"
    ]
  },
  
  // MCP Server: PayPal
  "paypal-production": {
    "type": "local",
    "command": [
      "npx",
      "-y",
      "@paypal/mcp",
      "--tools=all",
      "--access-token=${PAYPAL_ACCESS_TOKEN}",
      "--paypal-environment=PRODUCTION"
    ]
  },
  
  // MCP Server: Kali Linux (pentesting)
  "kali": {
    "type": "local",
    "command": [
      "ssh",
      "kali",
      "mcp-server",
      "--server",
      "http://localhost:5000",
      "--timeout",
      "300"
    ]
  },
  
  // MCP Server: Lexis (code search)
  "lexis": {
    "type": "local",
    "command": ["lexis", "mcp"]
  }
}
```

---

## 6. MCP.json - Template Genérico

```json
{
  "mi-mcp-server": {
    "enabled": true,
    "type": "local",
    "command": [
      "npx",
      "-y",
      "@vendor/mcp-server"
    ],
    "env": {
      "API_KEY": "${MI_API_KEY}",
      "OTHER_VAR": "valor-fijo"
    },
    "timeout": 60000
  },
  
  "mi-mcp-server-remote": {
    "enabled": false,
    "type": "remote",
    "url": "https://api.mi-servicio.com/mcp"
  }
}
```

---

## 7. Estructura de Archivos - Proyecto Completo

```
~/.config/opencode/
├── opencode.json           # Configuración principal
├── AGENTS.md              # Perfil de usuario
├── mcp.json               # MCP servers
│
├── skills/                 # Skills del usuario
│   ├── mi-skill/
│   │   ├── SKILL.md
│   │   └── references/
│   │       └── detalles.md
│   └── otro-skill/
│       └── SKILL.md
│
├── agents/                 # Agentes personalizados
│   ├── mi-agente.md
│   └── agente-seguridad.md
│
├── prompts/               # Prompts de agentes
│   └── sdd/
│       ├── sdd-apply.md
│       ├── sdd-spec.md
│       └── sdd-design.md
│
├── skill-libraries/       # Librerías de skills
│   ├── web-development/
│   │   └── react-best-practices/
│   │       └── AGENTS.md
│   └── database/
│       └── postgres-best-practices/
│           └── AGENTS.md
│
└── scripts/               # Scripts de utilidad
    ├── load-context.mjs
    ├── pin.mjs
    └── opencode-backup/
```

---

## 8. Permisos - Seguridad

```json
{
  "permission": {
    // Permisos para bash
    "bash": {
      "*": "allow",
      "sudo *": "ask",
      "rm *": "ask",
      "rm -rf /*": "deny",
      "git push": "ask",
      "git push --force": "deny",
      "chmod 777": "ask",
      "chown": "ask"
    },
    
    // Permisos para lectura de archivos
    "read": {
      "*": "allow",
      "**/.env": "deny",
      "**/.env.*": "deny",
      "**/credentials.json": "deny",
      "**/.ssh/**": "deny",
      "**/.aws/**": "deny",
      "**/.gnupg/**": "deny",
      "**/.kube/config": "deny"
    },
    
    // Permisos para tareas específicas
    "task": {
      "sdd-apply": "allow",
      "sdd-spec": "allow",
      "sdd-design": "allow",
      "*": "ask"
    }
  }
}
```

---

## 9. Template: Nuevo Agent

```yaml
# agents/mi-agente.md

---
name: mi-agente
description: "Trigger: keyword1, keyword2, keyword3. Descripción del agente"
license: MIT
metadata:
  author: tu-nombre
  version: "1.0"
---

## Activation Contract

Load this profile when user asks for [describe qué hace].

## Hard Rules

- ✅ [Regla 1]
- ✅ [Regla 2]
- ❌ [Nunca hacer esto]

## Soft Rules

- Preferir [opción A]
- Usar [formato/estilo]

## Decision Gates

| Request | Action |
|--------|--------|
| caso-1 | usar skill X |
| caso-2 | usar skill Y |

## Execution Steps

1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

## Output Contract

Retornar:
- status
- executive_summary
- artifacts
- next_recommended
```

---

## 10. Template: Nuevo Skill

```markdown
# skills/mi-skill/SKILL.md

---
name: mi-skill
description: "Trigger: mi-skill, keyword. Descripción del skill"
disable-model-invocation: true
user-invocable: false
license: MIT
metadata:
  author: tu-nombre
  version: "1.0"
  delegate_only: true
---

> **ORCHESTRATOR GATE**: Si cargaste este skill via `skill()`, eres el ORCHESTRADOR. Delega.

## Activation Contract

[Cuándo se activa este skill]

## Hard Rules

```markdown
- ✅ [Regla 1]
- ❌ [Nunca hacer esto]
```

## Soft Rules

[Preferencias]

## Decision Gates

| Input | Action |
|-------|--------|
| caso-1 | acción A |
| caso-2 | acción B |

## Execution Steps

1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

## Output Contract

```typescript
interface MiSkillOutput {
  status: 'success' | 'error';
  executive_summary: string;
  artifacts: string[];
  next_recommended: string[];
  risks: string[];
}
```

## Referencias

- [references/detalles.md](references/detalles.md)
- [../otro-skill/SKILL.md](../otro-skill/SKILL.md)
```
