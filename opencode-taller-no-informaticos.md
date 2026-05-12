# Taller OpenCode para No Informáticos

## Guía Completa 2026

> **Objetivo**: Capacitar a profesionales no técnicos en el uso de OpenCode como asistente de IA para potenciar su productividad diaria.

---

## 📋 Tabla de Contenidos

1. [¿Qué es OpenCode?](#1-qué-es-opencode)
2. [Instalación](#2-instalación)
3. [Configuración Básica](#3-configuración-básica)
4. [Sistema de Agentes](#4-sistema-de-agentes)
5. [AGENTS.md - Personalización](#5-agentsmd---personalización)
6. [MCP - Extensiones](#6-mcp---extensiones)
7. [Skills - Habilidades](#7-skills---habilidades)
8. [Casos de Uso por Profesión](#8-casos-de-uso-por-profesión)
9. [Ejercicios Prácticos](#9-ejercicios-prácticos)

---

## 1. ¿Qué es OpenCode?

### Definición Simple

OpenCode es un **asistente de inteligencia artificial de código abierto** que funciona en tu terminal, escritorio o IDE. A diferencia de ChatGPT o Claude Chat, OpenCode está diseñado específicamente para:

- ✅ **Trabajar con archivos y código** en tu computadora
- ✅ **Ejecutar comandos** del sistema
- ✅ **Conectarse a herramientas externas** (GitHub, Jira, Notion)
- ✅ **Recordar contexto** de tus proyectos
- ✅ **Automatizar tareas repetitivas**

### Estadísticas (2026)

| Métrica | Valor |
|---------|-------|
| GitHub Stars | 150,000+ |
| Desarrolladores mensuales | 6.5 millones |
| Contribuidores | 850+ |
| Proveedores de modelos IA | 75+ |

### ¿Por qué es Relevante para No Informáticos?

Aunque su nombre dice "code" (código), OpenCode puede ayudarte con:

- 📝 **Redactar documentos** profesionales
- 📊 **Analizar datos** en hojas de cálculo
- ✉️ **Redactar correos** y mensajes
- 📋 **Gestionar proyectos** (integración con Jira, Notion)
- 🔍 **Investigar** temas en la web
- 📁 **Organizar archivos** automáticamente

---

## 2. Instalación

### Método 1: Script de Instalación (Recomendado)

Este es el método más rápido y funciona en **todos los sistemas operativos**.

#### Paso a Paso

```bash
# 1. Abrir la terminal
# En macOS: Cmd + Espacio → "Terminal"
# En Windows: Win + X → "Terminal" (o usar WSL)
# En Linux: Ctrl + Alt + T

# 2. Ejecutar el script de instalación
curl -fsSL https://opencode.ai/install | bash

# 3. Verificar la instalación
opencode --version
```

#### Opciones de Personalización

```bash
# Instalar en un directorio personalizado
OPENCODE_INSTALL_DIR=/usr/local/bin curl -fsSL https://opencode.ai/install | bash

# Usar directorio XDG estándar
XDG_BIN_DIR=$HOME/.local/bin curl -fsSL https://opencode.ai/install | bash
```

### Método 2: npm (Gestor de Paquetes Node.js)

```bash
# Requiere Node.js 18+ instalado
npm install -g opencode-ai

# O usando otros gestores
bun add -g opencode-ai    # Bun
pnpm add -g opencode-ai   # pnpm
yarn global add opencode-ai # Yarn
```

### Método 3: Homebrew (macOS/Linux)

```bash
# Añadir el tap oficial
brew tap anomalyco/tap/opencode

# Instalar
brew install opencode

# Verificar
opencode --version
```

### Método 4: Aplicación de Escritorio (Beta)

Para quienes prefieren **no usar la terminal**:

#### macOS

```bash
# Usando Homebrew
brew install --cask opencode-desktop
```

#### Windows

Descarga directa desde: [opencode.ai/download](https://opencode.ai/download)

#### Linux

- **.deb** para Debian/Ubuntu
- **.rpm** para Fedora/RHEL
- **AppImage** para distribuciones universales

### Método 5: Scoop (Windows)

```bash
scoop install opencode
```

### Comparativa de Métodos

| Método | Dificultad | Recomendado para |
|--------|------------|-----------------|
| Script curl | ⭐ Fácil | 90% de usuarios |
| npm | ⭐⭐ Media | Desarrolladores |
| Homebrew | ⭐ Fácil | macOS/Linux |
| Desktop App | ⭐ Fácil | No técnicos |
| Scoop | ⭐⭐ Media | Windows power users |

---

## 3. Configuración Básica

### Estructura de Archivos de Configuración

```
MiCarpetaProyecto/
├── opencode.json           # Configuración del proyecto
├── AGENTS.md               # Reglas específicas del proyecto
└── .opencode/
    ├── agents/             # Agentes personalizados
    │   └── mi-agente.md
    ├── skills/             # Habilidades personalizadas
    │   └── mi-skill/
    │       └── SKILL.md
    └── commands/           # Comandos personalizados
        └── mi-comando.md

~/.config/opencode/         # Configuración global del usuario
├── opencode.json
├── AGENTS.md
├── agents/
├── skills/
└── commands/
```

### Configuración Inicial con `/init`

```bash
# Ejecutar dentro de tu carpeta de proyecto
opencode /init

# Esto analizará tu proyecto y creará un AGENTS.md automáticamente
```

### Configurar tu Primera API Key

#### Opción A: Variables de Entorno (Recomendado)

```bash
# Añadir a ~/.zshrc (macOS/Linux)
echo 'export OPENAI_API_KEY="sk-tu-clave-aqui"' >> ~/.zshrc
source ~/.zshrc

# Añadir a ~/.bashrc (Linux)
echo 'export OPENAI_API_KEY="sk-tu-clave-aqui"' >> ~/.bashrc
source ~/.bashrc
```

#### Opción B: Usando el Comando `/connect`

```bash
opencode
# Dentro de OpenCode ejecutar:
/connect
# Seleccionar proveedor (OpenAI, Anthropic, etc.)
# Seguir instrucciones de autenticación
```

### opencode.json Mínimo

Crea `~/.config/opencode/opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "provider": "openai",
  "model": "gpt-4o",
  "theme": "opencode",
  "permission": {
    "edit": "ask",
    "bash": "ask",
    "webfetch": "allow"
  }
}
```

---

## 4. Sistema de Agentes

### ¿Qué es un Agente?

Un **agente** es una configuración específica que define:

- 🎯 **Qué puede hacer** el asistente
- 🔒 **Qué permisos tiene** (leer, escribir, ejecutar comandos)
- 🧠 **Cómo piensa** (prompt personalizado)
- 🛠️ **Qué herramientas usa** (MCP, skills)

### Agentes Integrados

OpenCode viene con agentes predefinidos:

| Agente | Propósito | Permisos |
|--------|-----------|----------|
| `@plan` | Planificación y análisis (NO hace cambios) | Solo lectura |
| `@code` | Implementación de código | Lectura + Escritura |
| `@explore` | Explorar y entender proyectos | Solo lectura |
| `@scout` | Investigar documentación externa | Web |
| `@general` | Tareas generales | Todo |

### Usar un Agente Específico

```bash
# Ejecutar con un agente específico
opencode @plan "Analiza la estructura de este proyecto"

# O dentro de OpenCode
@plan Analiza la estructura de este proyecto
```

### Crear un Agente Personalizado

#### Paso 1: Crear el archivo del agente

Crea `~/.config/opencode/agents/redactor.md`:

```markdown
---
description: Asistente de redacción profesional
mode: subagent
permission:
  edit: allow
  bash: deny
  webfetch: allow
---

# Eres un redactor profesional

Tu rol es ayudar con:
- Escritura de correos electrónicos formales
- Redacción de informes y documentos
- Revisión gramatical y ortográfica
- Estilo profesional latinoamerican

## Reglas de Escritura

1. Usar español latinoamerican formal
2. Tono respetuoso pero cercano
3. Oraciones claras y directas
4. Evitar anglicismos innecesarios
5. Incluir frases de transición

## Formato de Documentos

- Títulos: Mayúsculas iniciales
- Listas: Guiones (no números)
- Cierre: "Quedo atento/a a sus comentarios"
```

#### Paso 2: Usar el agente

```bash
@redactor Redacta un correo formal solicitando una reunión de seguimiento
```

### Ejemplo: Agente para Marketing

`~/.config/opencode/agents/marketing.md`:

```markdown
---
description: Asistente de marketing y redes sociales
mode: subagent
permission:
  edit: allow
  bash: deny
  webfetch: allow
---

# Eres un consultor de marketing digital

Experto en:
- Marketing digital para Latinoamérica
- Redes sociales (Instagram, LinkedIn, TikTok)
- Email marketing
- Creación de contenido

## Voz de Marca

- Tono: Profesional pero accesible
- Idioma: Español latinoamerican
- Formato: Adaptable a cada plataforma

## Plataforma-Specífico

### LinkedIn
- Posts de 150-300 palabras
- Incluir call-to-action
- Usar emojis con moderación

### Instagram
- Captions de 125-150 caracteres
- Hashtags relevantes (#negocios, #emprendimiento)
- Incluir línea de acción

### Correos
- Asunto: Claro y conciso
- Cuerpo: Máximo 3 párrafos
- CTA visible
```

---

## 5. AGENTS.md - Personalización

### ¿Qué es AGENTS.md?

`AGENTS.md` es un archivo especial que le dice a OpenCode **cómo comportarse** en tu proyecto o de forma global.

### Ubicaciones y Prioridad

```
1. ./AGENTS.md                    → Reglas del proyecto actual (PRIORIDAD ALTA)
2. ./packages/*/AGENTS.md        → Reglas por paquete
3. ~/.config/opencode/AGENTS.md   → Reglas globales del usuario (MEDIA)
4. ~/.claude/CLAUDE.md           → Compatibilidad con Claude Code (BAJA)
```

> **Nota**: Si existe `AGENTS.md`, se ignora `CLAUDE.md`. Si existe `~/.config/opencode/AGENTS.md`, se ignora `~/.claude/CLAUDE.md`.

### Ejemplo Completo para No Técnicos

#### Proyecto: Gestión de Redes Sociales

Crea `AGENTS.md` en tu proyecto:

```markdown
# Proyecto: Gestión de Redes Sociales - Empresa XYZ

## Contexto del Negocio

Somos una pyme ecuatoriana dedicada a [describir negocio].
Nuestra audiencia objetivo son emprendedores y pequeños negocios.
Presencia en: Instagram, LinkedIn, Facebook.

## Estilo de Comunicación

- Tono: Profesional pero cercano, inspira confianza
- Idioma: Español latinoamerican (Ecuador)
--No usar: Argot excesivo, anglicismos innecesarios
- Sí usar: Frases cortas, verbos de acción, números específicos

## Tipos de Contenido

1. Educativo: Tips y consejos prácticos
2. Inspiracional: Frases motivacionales del día
3. Promocional: Productos/servicios destacados
4. Interactivo: Encuestas, preguntas a la audiencia

## Calendario de Publicación

- Lunes: Tip de la semana
- Miércoles: Producto destacado
- Viernes: Contenido motivacional
- Sábados: Interactivo (stories)

## Hashtags por Categoría

### Negocio
#emprendimiento #pyme #negocios #empresa # Ecuador

### Motivación
#lunesdemotivación #exito #logros #crecimiento

### Producto
#[nombredemarca] #[categoría]

## Restricciones Importantes

- NO publicar contenido político o religioso
- NO usar imágenes con texto excesivo
- SIEMPRE incluir alt text en imágenes
- VERIFICAR horarios: 9:00-11:00 y 18:00-20:00 (hora Ecuador)

## Proceso de Aprobación

Antes de publicar:
1. Revisión de ortografía
2. Verificar hashtags (máximo 15)
3. Adjuntar imagen/recurso
4. Esperar confirmación antes de publicar
```

### Ejemplo: Agente de Atendimento al Cliente

```markdown
# Sistema de Atención al Cliente - Soporte Técnico

## Tu Rol

Eres un agente de soporte técnico especializado.
Tu objetivo es resolver problemas de forma eficiente y amable.

## Principios de Atención

1. **Escuchar primero**: Entender el problema antes de solución
2. **Ser empático**: "Entiendo su frustración"
3. **Ser claro**: Explicaciones simples, sin jerga técnica
4. **Ser paciente**: Preguntar hasta entender completamente

## Tipos de Consultas y Respuestas

### Consulta de Horarios
" Nuestros horarios de atención son:
- Lunes a Viernes: 8:00 a 18:00
- Sábados: 9:00 a 13:00
- Domingos: Cerrado

¿Hay algo más en lo que pueda ayudarle?"

### Consulta de Precios
"A continuación le presento nuestros precios:
[Producto A]: $XX.XX
[Producto B]: $XX.XX

¿Le gustaría más información sobre algún producto?"

### Consulta Técnica
"Para resolver su problema, necesito verificar algunos datos:
1. ¿Qué dispositivo está usando?
2. ¿Desde cuándo ocurre el problema?
3. ¿Ha intentado algún paso de solución?

Mientras tanto, puede consultar nuestra guía de problemas comunes en [enlace]."

## Firmas de Cierre

"¿Hay algo más en lo que pueda ayudarle?"
"Quedo atento/a a sus comentarios"
"Fue un placer atenderle"
```

### Configurar Instrucciones Externas

Para proyectos grandes, puedes separar las reglas en múltiples archivos.

#### `opencode.json`:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "instructions": [
    "docs/estilo-comunicacion.md",
    "docs/procesos.md",
    "~/mis-reglas/tono-redes.md"
  ]
}
```

---

## 6. MCP - Extensiones

### ¿Qué es MCP?

MCP (Model Context Protocol) es como un **cable USB para IA**. Permite que OpenCode se conecte a herramientas externas como:

- 📁 Google Drive / OneDrive
- 📋 Notion / Jira / Trello
- 📧 Gmail / Outlook
- 🐙 GitHub / GitLab
- 🗄️ Bases de datos
- 🌐 Navegadores web

### Instalar un Servidor MCP

#### Paso a Paso con `opencode mcp add`

```bash
opencode mcp add
# Seguir las instrucciones interactivas
```

### MCPs Recomendados para No Técnicos

#### 1. GitHub MCP (Para gestionar repositorios)

```bash
# Configuración
opencode mcp add
# Nombre: github
# Tipo: Local
# Comando: npx
# Args: -y @modelcontextprotocol/server-github
# Variables: GITHUB_PERSONAL_ACCESS_TOKEN=tu_token
```

```json
// En opencode.json
{
  "mcp": {
    "github": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "environment": {
        "GITHUB_PERSONAL_ACCESS_TOKEN": "{file:~/.config/opencode/.secrets/github-token}"
      }
    }
  }
}
```

#### 2. Notion MCP (Gestión de notas y documentos)

```bash
# 1. Crear integración en notion.so/my-integrations
# 2. Compartir las páginas con la integración
# 3. Configurar:
opencode mcp add
# Nombre: notion
# Comando: npx
# Args: -y notion-mcp-server
# Variables: NOTION_API_KEY=secret_tu_key
```

```json
{
  "mcp": {
    "notion": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "notion-mcp-server"],
      "environment": {
        "NOTION_API_KEY": "secret_tu_api_key"
      }
    }
  }
}
```

#### 3. Gmail MCP (Gestión de correo)

```bash
# Requiere OAuth de Google
opencode mcp add
# Nombre: gmail
# Comando: npx
# Args: -y @modelcontextprotocol/server-gmail
```

#### 4. Playwright MCP (Automatización de navegador)

```bash
# Para automatizar tareas web
opencode mcp add
# Nombre: browser
# Comando: npx
# Args: -y @modelcontextprotocol/server-playwright
```

#### 5. Slack MCP (Comunicación de equipo)

```bash
# Integración con Slack
opencode mcp add
# Nombre: slack
# Comando: npx
# Args: -y @modelcontextprotocol/server-slack
# Variables: SLACK_BOT_TOKEN=xoxb-tu-token
```

### MCPs Populares Adicionales

| MCP | Propósito | Dificultad |
|-----|-----------|------------|
| **Context7** | Buscar documentación de librerías | ⭐ Fácil |
| **Sentry** | Monitoreo de errores | ⭐⭐ Media |
| **Figma** | Revisión de diseños | ⭐ Fácil |
| **n8n** | Automatización de workflows | ⭐⭐ Media |
| **Filesystem** | Acceso a archivos local | ⭐ Fácil |
| **PostgreSQL** | Consultas a bases de datos | ⭐⭐⭐ Alta |

### Ejemplo: Configurar Context7 (Documentación)

```json
{
  "mcp": {
    "context7": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@context7/mcp-server"]
    }
  }
}
```

### Permisos por Agente para MCP

```json
{
  "agent": {
    "redactor": {
      "permission": {
        "tool": {
          "notion_*": "allow",
          "gmail_*": "allow",
          "github_*": "deny"
        }
      }
    }
  }
}
```

---

## 7. Skills - Habilidades

### ¿Qué es un Skill?

Un **skill** es un conjunto de instrucciones reutilizables que el agente puede cargar cuando lo necesite. Es como un "plugin" de comportamiento.

### Estructura de un Skill

```
.opencode/skills/
└── nombre-del-skill/
    └── SKILL.md          # Obligatorio
    ├── archivo1.md       # Opcional
    └── archivo2.md       # Opcional
```

### SKILL.md - Formato Obligatorio

```markdown
---
name: nombre-del-skill
description: Descripción clara de qué hace este skill (1-1024 caracteres)
license: MIT              # Opcional
compatibility: opencode   # Opcional
metadata:                # Opcional
  audiencia: desarrolladores
  categoria: frontend
---

# Contenido del Skill

Aquí van las instrucciones detalladas...
```

### Reglas de Nomenclatura

| Regla | Correcto | Incorrecto |
|-------|---------|------------|
| Minúsculas | `mi-skill` | `MiSkill` |
| Guiones simples | `redaccion-pro` | `redaccion__pro` |
| Sin guiones al inicio/final | `mi-skill` | `-mi-skill` |
| Máximo 64 caracteres | ✓ | ✗ |

### Ejemplo de Skill: Redacción de Correos

`.opencode/skills/redaccion-correos/SKILL.md`:

```markdown
---
name: redaccion-correos
description: Plantillas y guía para redactar correos profesionales efectivos
compatibility: opencode
metadata:
  idioma: español-latino
  tono: profesional
---

# Skill: Redacción de Correos Profesionales

## Estructura Obligatoria

Todo correo debe seguir esta estructura:

1. **Saludo** (1 línea)
2. **Cuerpo** (máximo 3 párrafos)
3. **Cierre** (1 línea)
4. **Firma** (nombre + cargo + contacto)

## Plantillas

### Solicitud de Reunión

```
Asunto: Solicitud de reunión - [Tema]

Estimado/a [Nombre],

Me dirijo a usted para solicitar una reunión con el fin de discutir [tema].

¿Sería posible coordinar una reunión [fecha/hora]? Quedo a su disposición para adaptarme a su agenda.

Quedo atento/a a su confirmación.

Saludos cordiales,
[Tu nombre]
[Cargo]
[Contacto]
```

### Respuesta a Queja

```
Asunto: Re: [Asunto original]

Estimado/a [Nombre],

Agradezco profundamente su Retroalimentación. Tomamos muy en serio este tipo de comentarios.

[Explicar acciones tomadas o que se tomarán]

¿Hay algo adicional que pueda hacer para resolver esta situación?

Atentamente,
[Tu nombre]
```

### Seguimiento

```
Asunto: Seguimiento - [Asunto previo]

Estimado/a [Nombre],

Espero que se encuentre bien. Me permito dar seguimiento a nuestra conversación del [fecha].

[Estado actual o próxima acción]

Quedo a su disposición para cualquier duda.

Saludos,
[Tu nombre]
```

## Frases de Cierre

- "Quedo atento/a a sus comentarios"
- "A la espera de su confirmación"
- "Será un placer ampliar la información"
- "Agradezco de antemano su atención"

## Errores Comunes a Evitar

❌ "Hola buenos días" (genérico)
✅ "Buenos días, estimado Juan"

❌ "Le escribo para..." (directo pero poco cálido)
✅ "Espero que se encuentre bien. Le escribo porque..."

❌ "No dude en contactarme" (pasivo)
✅ "Estoy a su disposición en [canal específico]"
```

### Ejemplo de Skill: Gestión de Proyectos

`.opencode/skills/gestion-proyectos/SKILL.md`:

```markdown
---
name: gestion-proyectos
description: Metodología y plantillas para gestión de proyectos ágiles
compatibility: opencode
metadata:
  metodologia: agile
  region: latinoamerica
---

# Skill: Gestión de Proyectos Ágiles

## Principios Fundamentales

1. **Iteraciones cortas**: 1-2 semanas
2. **Entregas frecuentes**: Valor incremental
3. **Retroalimentación**: Del cliente y del equipo
4. **Adaptación**: Cambiar según necesidad

## Estructura de Historia de Usuario

```
COMO: [tipo de usuario]
QUIERO: [acción específica]
PARA: [beneficio/valor]
```

### Ejemplo

```
COMO: Jefe de ventas
QUIERO: Ver un dashboard con métricas semanales
PARA: Tomar decisiones informadas rápidamente
```

## Criterios de Aceptación

Toda historia debe tener:

```
DADO QUE: [contexto previo]
CUANDO: [acción del usuario]
ENTONCES: [resultado esperado]
```

## Tipos de Reuniones

### Daily Standup (15 min)
- ¿Qué hice ayer?
- ¿Qué haré hoy?
- ¿Qué me bloquea?

### Sprint Planning (1-2 hrs)
1. Seleccionar historias del backlog
2. Estimar esfuerzo (puntos de historia)
3. Asignar responsable

### Sprint Review (1 hr)
1. Demostrar funcionalidades completadas
2. Recoger Retroalimentación
3. Actualizar backlog

### Retrospectiva (1 hr)
1. ¿Qué salió bien?
2. ¿Qué puede mejorar?
3. Plan de acción

## Formato de Reporte Semanal

```
REPORTE SEMANAL - [Semana X]

## Avances de la Semana
- [Tarea 1]: Estado | Evidencia
- [Tarea 2]: Estado | Evidencia

## Próxima Semana
- [Tarea 1]: Objetivo
- [Tarea 2]: Objetivo

## Bloqueantes
- Ninguno / [Bloqueante 1]

## Métricas
- Velocidad del equipo: X puntos
- Tareas completadas: X/Y
- Deuda técnica identificada: X horas
```

## Definition of Done (DoD)

- [ ] Código revisado
- [ ] Pruebas unitarias pasando
- [ ] Documentación actualizada
- [ ] Aprobación del Product Owner
- [ ] Desplegado a entorno de pruebas
```

### Habilitar/Deshabilitar Skills por Agente

```json
// En opencode.json
{
  "permission": {
    "skill": {
      "*": "allow",
      "internal-*": "deny",
      "experimental-*": "ask"
    }
  }
}
```

### Skill Predeterminado: GitHub Operations

```markdown
---
name: github-ops
description: Operaciones comunes con GitHub CLI
compatibility: opencode
---

# GitHub Operations Skill

## Comandos Esenciales

### Navegación
```bash
gh repo list                    # Listar repositorios
gh repo view                    # Ver repo actual
gh browse                       # Abrir repo en navegador
```

### Issues
```bash
gh issue list                   # Listar issues
gh issue create                 # Crear issue
gh issue view 123               # Ver issue específico
gh issue close 123              # Cerrar issue
```

### Pull Requests
```bash
gh pr list                      # Listar PRs
gh pr create                    # Crear PR
gh pr view 123                  # Ver PR
gh pr merge 123                 # Mergear PR
```

### Releases
```bash
gh release list                 # Listar releases
gh release create v1.0.0        # Crear release
```

## Flujo de Trabajo Recomendado

1. `gh issue create` → Crear issue
2. `gh branch create` → Crear rama
3. Trabajar en el código
4. `gh pr create` → Crear PR
5. `gh pr review` → Revisar
6. `gh pr merge` → Mergear
```

---

## 8. Casos de Uso por Profesión

### 📊 Para Administradores de Empresas

#### Tareas Comunes
- Redactar reportes ejecutivos
- Preparar presentaciones
- Resumir documentos largos
- Traducir comunicaciones

#### Configuración Recomendada

```bash
# Crear estructura
mkdir -p ~/.config/opencode/skills/administracion
```

`.opencode/skills/administracion/SKILL.md`:

```markdown
---
name: administracion
description: Habilidades para administración de empresas y gestión documental
---

# Administracion Skill

## Tipos de Documentos

### Reporte Ejecutivo
- Máximo 2 páginas
- Resumen ejecutivo al inicio
- Datos cuantificables
- Conclusiones y recomendaciones

### Minuta de Reunión
```
FECHA: [fecha]
ASISTENTES: [lista]
OBJETIVO: [propósito]

DESARROLLO:
- Punto 1: [discusión]
- Punto 2: [discusión]

ACUERDOS:
- [Acuerdo 1] → Responsable: [nombre] → Fecha: [fecha]

PRÓXIMA REUNIÓN: [fecha]
```

### Carta Comercial
- Encabezado con datos de empresa
- Referencia (su carta, fecha)
- Cuerpo (máximo 1 página)
- Cierre formal

## Análisis Financiero Básico

### Calcular Indicadores

```
Margen de Ganancia = (Ganancia / Ingresos) × 100
Punto de Equilibrio = Costos Fijos / (Precio - Costo Variable)
ROI = ((Ganancia - Inversión) / Inversión) × 100
```

## Tiempo Estimado

- Reporte ejecutivo: 30-60 minutos
- Carta comercial: 10-15 minutos
- Minuta de reunión: 15-20 minutos
- Presentación (10 slides): 45-60 minutos
```

### 🎨 Para Diseñadores Gráficos

#### Tareas Comunes
- Escribir briefs de proyectos
- Documentar decisiones de diseño
- Preparar presentaciones para clientes
- Crear documentación de marca

#### Configuración Recomendada

```markdown
# .opencode/agents/disenador.md
---
description: Asistente especializado para diseñadores gráficos
mode: subagent
permission:
  edit: allow
  bash: deny
---

# Eres un asistente de diseño gráfico

## Áreas de Expertise

1. Diseño de marca
2. Diseño editorial
3. Diseño UI/UX
4. Fotografía y composición
5. Tipografía

## Brief de Proyecto

```
PROYECTO: [Nombre]
CLIENTE: [Empresa]
CONTACTO: [Nombre - Email]

## 1. Objetivos de Comunicación
[Qué quiere transmitir el cliente]

## 2. Público Objetivo
[Quién debe recibir el mensaje]

## 3. Competencia
[Otras marcas en el mismo espacio]

## 4. Entregables
- [ ] Logo principal
- [ ] Variaciones de color
- [ ] Tipografía seleccionada
- [ ] Paleta de colores
- [ ] Manual de marca

## 5. Restricciones
- [Presupuesto]
- [Plazos]
- [Materiales existentes]
```

## Presentación para Cliente

```
1. INTRODUCCIÓN (1 slide)
   - Resumen del proyecto
   - Metodología usada

2. EXPLORACIÓN (3-5 slides)
   - Direcciones exploradas
   - Razón de descarte

3. DIRECCIÓN ELEGIDA (5-10 slides)
   - Solución presentada
   - Detalles de cada elemento
   - Versatilidad

4. APLICACIONES (3-5 slides)
   - Ejemplos de uso real

5. CIERRE (1 slide)
   - Próximos pasos
   - Contacto
```
```

### 📱 Para Community Managers

#### Tareas Comunes
- Crear calendarios de contenido
- Redactar posts para diferentes plataformas
- Responder preguntas frecuentes
- Analizar métricas
- Crear respuestas a comentarios

#### Configuración Recomendada

```markdown
# .opencode/skills/social-media/SKILL.md
---
name: social-media
description: Gestión de redes sociales y creación de contenido digital
---

# Social Media Skill

## Calendario de Contenido Semanal

| Día | Tipo | Plataforma | Hora |
|-----|------|------------|------|
| Lunes | Educativo | LinkedIn + IG | 9:00 |
| Martes | Producto | Facebook | 10:00 |
| Miércoles | Interactivo | Stories | 12:00 |
| Jueves | Testimonial | IG + TikTok | 18:00 |
| Viernes | Motivacional | Todas | 17:00 |
| Sábado | Detrás de cámaras | Stories | 10:00 |
| Domingo | Inspiracional | Twitter | 19:00 |

## Fórmulas de Posts

### Post Educativo
```
HOOK (primeros 2 segundos):
¿Te pasó que...? / 3 errores que... / El secreto que...

CUERPO:
- Punto 1: [Dato o consejo]
- Punto 2: [Dato o consejo]
- Punto 3: [Dato o consejo]

CTA:
¿Cuál es tu experiencia? Cuéntame en comentarios 👇
```

### Post de Producto/Servicio
```
BENEFICIO PRINCIPAL en primera línea.

Historia breve (2-3 líneas):
[Cómo ayudar antes/después]

Características clave:
✓ [Característica 1]
✓ [Característica 2]
✓ [Característica 3]

CTA: Link en bio / DM / Comentarios
```

### Testimonial
```
📣 LO QUE DICEN NUESTROS CLIENTES

"[Quote del cliente]"

- [Nombre], [Cargo/Empresa]

¿Conoces a alguien que necesite esto? Etiquétalo 👇
```

## Hashtags por Categoría

### Ecuador
#Ecuador #Quito #Guayaquil #Cuenca #negocioseu

### Marketing
#marketingdigital #redessociales #marcaspersonal #contentcreator

### Negocio
#emprendimiento #pyme #startup #negocios #empresa

## Métricas a Monitorear

| Métrica | Meta Mensual |
|---------|--------------|
| Seguidores nuevos | +10% |
| Engagement rate | >3% |
| Alcance | +20% vs mes anterior |
| Clics en link | >500 |
| Mensajes recibidos | >100 |
```

### 📧 Para Asistentes Ejecutivos

#### Tareas Comunes
- Agendar reuniones
- Preparar agendas
- Redactar comunicaciones
- Gestionar correspondence
- Preparar viajes

#### Configuración Recomendada

```markdown
# .opencode/skills/asistente-ejecutivo/SKILL.md
---
name: asistente-ejecutivo
description: Habilidades para asistentes ejecutivos y coordinación administrativa
---

# Asistente Ejecutivo Skill

## Gestión de Reuniones

### Formato de Agenda

```
REUNIÓN: [Nombre]
FECHA: [Fecha] | HORA: [Hora]
UBICACIÓN: [Sala/Físico/Zoom]
DURACIÓN ESTIMADA: [X] minutos

PARTICIPANTES:
1. [Nombre] - [Rol]
2. [Nombre] - [Rol]

AGENDA:
1. [Tema] ([X] min) - Responsable: [Nombre]
2. [Tema] ([X] min) - Responsable: [Nombre]

PREPARADO POR: [Tu nombre]
ULTIMA ACTUALIZACIÓN: [Fecha]
```

### Confirmación de Reunión

```
Asunto: Confirmación - [Nombre reunión] - [Fecha]

Estimado/a [Nombre],

Me permito confirmar los detalles de nuestra reunión:

📅 Fecha: [Fecha]
🕐 Hora: [Hora]
📍 Ubicación: [Lugar/Link]
⏱️ Duración: [X] minutos

Agenda adjunta para su revisión.

Quedo atento/a a cualquier ajuste.

Saludos,
[Tu nombre]
```

### Seguimiento Post-Reunión

```
ASISTENTES: [Lista]
FECHA: [Fecha]

ACUERDOS:
1. [Acción] → Responsable: [Nombre] → Fecha límite: [Fecha]
2. [Acción] → Responsable: [Nombre] → Fecha límite: [Fecha]

PRÓXIMA REUNIÓN: [Fecha] (si aplica)

Nota: [Información adicional relevante]
```

## Gestión de Viajes

### Checklist de Viaje

```
□ Boletos de avión/trayecto confirmados
□ Reservación de hotel verificada
□ Transportación del aeropuerto confirmada
□ Agenda de reuniones/reuniones preparada
□ Presentaciones/documents listos
□ Tarjeta de presentación física
□ Dispositivo chargé y funcional
□ Adaptadores de corriente (si aplica)
□ Dinero local/divisas
□ Documentos de viaje (pasaporte, visa)
□ Confirmación de seguro de viaje
□ Itinerario compartido con [contacto de emergencia]
□ Oficina/notas de fuera de oficina preparadas
□ Respaldos de documentos importantes
□ Contactos importantes localizables
```

## Correspondence Templates

### Fuera de Oficina

```
Asunto: Fuera de oficina - [Tu nombre]

Estimados/as,

Me encuentro fuera de oficina desde [fecha] hasta [fecha] con acceso limitado al correo.

Para asuntos urgentes, comuníquese con:
[Nombre de backup]: [Contacto]
[Email]: [Email de backup]

Respondré sus mensajes a mi regreso.

Saludos,
[Tu nombre]
```

### Gestión de Prioridades

Clasificación Eisenhower:

| Urgente + Importante | No Urgente + Importante |
|---------------------|------------------------|
| Hacer inmediatamente | Planificar para después |
| Crisis | Construcción de relaciones |
| Plazos límite | Desarrollo profesional |
| Emergencias | |

| Urgente + No Importante | No Urgente + No Importante |
|------------------------|---------------------------|
| Delegar si es posible | Eliminar |
| Llamadas no necesarias | Redundancias |
| Reuniones innecesarias | Tiempo desperdiciado |
```

---

## 9. Ejercicios Prácticos

### Ejercicio 1: Instalación y Configuración (15 minutos)

**Objetivo**: Instalar OpenCode y configurar tu primera API key.

```bash
# 1. Verificar instalación
opencode --version

# 2. Ejecutar configuración inicial
opencode /init

# 3. Configurar tu proveedor de IA preferido
# Seguir las instrucciones en pantalla
```

**Entregable**: Captura de pantalla de `opencode --version` funcionando.

### Ejercicio 2: Crear tu Primer AGENTS.md (20 minutos)

**Objetivo**: Crear un archivo AGENTS.md personalizado para tu profesión.

```markdown
# Mi AGENTS.md Personal

## Sobre Mí
[Tu nombre]
[Tu profesión]
[Años de experiencia]

## Mi Estilo de Comunicación
- Tono: [Formal/Casual/Neutro]
- Idioma: Español [latinoamerican/Español]
- Preferencias: [，有什么具体要求]

## Projetos Actuales
- Projeto 1: [Descripción]
- Projeto 2: [Descripción]

## Herramientas que Uso
- [Herramienta 1]
- [Herramienta 2]
- [Herramienta 3]

## Preferencias de Respuesta
- Longitud: [Corta/Detallada]
- Formato: [Listas/Párrafos/Ambos]
```

**Entregable**: Archivo `AGENTS.md` guardado en `~/.config/opencode/`.

### Ejercicio 3: Crear un Skill Personalizado (30 minutos)

**Objetivo**: Crear un skill para una tarea recurrente de tu trabajo.

```bash
# 1. Crear estructura de carpetas
mkdir -p ~/.config/opencode/skills/mi-tarea
```

**Template**:

```markdown
---
name: mi-tarea
description: [Descripción de qué hace este skill]
---

# Mi Task Skill

## Cuándo Usar Este Skill
- [Escenario 1]
- [Escenario 2]

## Proceso Paso a Paso

1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

## Template/Plantilla

```
[TU TEMPLATE AQUÍ]
```

## Checklist de Verificación
- [ ] [Verificación 1]
- [ ] [Verificación 2]
- [ ] [Verificación 3]
```

**Entregable**: Skill funcional guardado en `~/.config/opencode/skills/`.

### Ejercicio 4: Configurar un MCP (25 minutos)

**Objetivo**: Conectar OpenCode con una herramienta que uses frecuentemente.

**Opciones**:

1. **Notion** (Notas y documentación)
2. **GitHub** (Gestión de código/proyectos)
3. **Gmail** (Correo electrónico)
4. **Slack** (Comunicación de equipo)

**Pasos**:

```bash
# 1. Obtener API key del servicio
# [Instrucciones específicas del servicio]

# 2. Añadir MCP
opencode mcp add

# 3. Seguir las instrucciones interactivas

# 4. Verificar conexión
opencode mcp list
```

**Entregable**: Captura de pantalla de MCP configurado y funcionando.

### Ejercicio 5: Crear un Agente Especializado (30 minutos)

**Objetivo**: Crear un agente personalizado para un caso de uso específico.

```markdown
# Template de Agente

## 1. Define el Propósito
[Qué hará este agente]

## 2. Define los Permisos
[Qué puede y no puede hacer]

## 3. Escribe el Prompt del Sistema
```

**Ejemplo Completado**:

```markdown
---
description: Asistente de atención al cliente para restaurante
mode: subagent
permission:
  edit: allow
  bash: deny
  webfetch: deny
---

# Eres un asistente de reservas para [Nombre del Restaurante]

## Información del Restaurante
- Ubicación: [Dirección]
- Horarios: [Horario]
- Teléfono: [Teléfono]
- Capacidad: [X] personas

## Servicios Ofrecidos
- Reservaciones
- Eventos privados
- Delivery
- Recoger en local

## FAQs Frecuentes

### ¿Aceptan reservaciones?
"Sí, aceptamos reservaciones. Puede hacerlas por [canales]"

### ¿Cuál es el dress code?
"Para [nombre], vestimos casual elegante"

### ¿Tienen opciones vegetarianas/veganas?
"Sí, contamos con un [X]% del menú dedicado a opciones..."

## Proceso de Reservación
1. Solicitar: Nombre, fecha, hora, número de personas, ocasión
2. Confirmar disponibilidad
3. Solicitar teléfono de contacto
4. Confirmar reservación
5. Enviar recordatorio 24hrs antes
```

**Entregable**: Archivo de agente guardado en `~/.config/opencode/agents/`.

---

## 📚 Recursos Adicionales

### Documentación Oficial
- [docs.opencode.ai](https://dev.opencode.ai/docs)
- [opencode.ai/download](https://opencode.ai/download)

### Comunidad
- GitHub: github.com/anomalyco/opencode
- Discord: OpenCode Community

### MCP Servers Populares
- [Awesome MCP Servers](https://github.com/wong2/awesome-mcp-servers)
- [MCP Server Directory](https://mcp-awesome.com)

### Skills Compartidos
- Repositorio público de skills en GitHub

---

## ✅ Checklist de Verificación del Taller

Al finalizar el taller, deberías poder:

- [ ] Instalar OpenCode en tu computadora
- [ ] Configurar al menos un proveedor de IA
- [ ] Crear un archivo AGENTS.md personalizado
- [ ] Crear un skill para tu profesión
- [ ] Configurar al menos un MCP
- [ ] Crear un agente especializado
- [ ] Ejecutar una tarea práctica con OpenCode

---

## 🔧 Comandos Rápidos de Referencia

```bash
# Instalación
curl -fsSL https://opencode.ai/install | bash

# Verificación
opencode --version

# Inicialización
opencode /init

# Conexión de proveedor
opencode /connect

# Gestión de MCPs
opencode mcp add       # Añadir MCP
opencode mcp list      # Listar MCPs
opencode mcp ls        # Alias

# Gestión de Agentes
opencode agent create  # Crear agente

# Ayuda
opencode --help
```

---

## 📞 Soporte

¿Necesitas ayuda?

1. **Documentación**: [docs.opencode.ai](https://dev.opencode.ai/docs)
2. **Discord**: Pregunta en la comunidad
3. **GitHub Issues**: Para reportar bugs

---

*Documento creado para el Taller de OpenCode - 2026*
*Dirigido a profesionales no informáticos de América Latina*
