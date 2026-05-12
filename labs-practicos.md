# Labs Prácticos — Taller de IA para No Informáticos

## 5 Labs para dominar OpenCode en 2 horas

---

## LAB 1: Instalación y Verificación (15 minutos)

### Objetivo
Instalar OpenCode y verificar que funciona correctamente.

### Paso 1: Verificar instalación de npm/Node.js

Abre tu terminal (PowerShell en Windows, Terminal en Mac/Linux):

```bash
# Verificar que Node.js está instalado
node --version

# Verificar que npm está instalado
npm --version
```

**Deberías ver algo como:** `v20.x.x` y `10.x.x`

### Paso 2: Instalar OpenCode

```bash
# Instalar globalmente
npm install -g opencode-ai

# O si prefieres con permisos de administrador (Linux)
sudo npm install -g opencode-ai
```

### Paso 3: Verificar instalación

```bash
# Verificar versión instalada
opencode --version

# Verificar que responde
opencode --help
```

**Resultado esperado:** Verás el número de versión y ayuda.

### Paso 4: Primeros comandos

```bash
# Ver configuración actual
opencode config list

# Ver plugins instalados
opencode plugins list

# Ver agentes disponibles
opencode agents list
```

### ✅ Checklist de verificación
- [ ] `opencode --version` muestra versión
- [ ] `opencode --help` muestra ayuda
- [ ] Sin errores de permisos

### 📸 Entregable
Captura de pantalla mostrando `opencode --version` exitoso.

---

## LAB 2: Configuración de Perfil Personal (20 minutos)

### Objetivo
Crear tu archivo AGENTS.md con tu información profesional.

### Paso 1: Crear directorio de configuración

```bash
# Crear estructura de directorios
mkdir -p ~/.config/opencode
```

### Paso 2: Crear tu AGENTS.md

Crea el archivo `~/.config/opencode/AGENTS.md` con este contenido:

```markdown
# Mi Perfil Profesional

## Quién soy

[Tu nombre completo]
[Tu profesión]
[Tu industria o sector]
[Años de experiencia]

## Sobre mi trabajo

[Describe brevemente qué haces]
[Qué tipo de proyectos manejas]
[Herramientas que usas actualmente]

## Objetivos con IA

- [Objetivo 1: qué quieres lograr]
- [Objetivo 2: segunda prioridad]
- [Objetivo 3: tercera prioridad]

## Cómo prefiero trabajar

**Tono:** Formal / Casual / Profesional pero cercano
**Idioma:** Español latino / Español / Inglés
**Nivel de detalle:** Resumen / Equilibrado / Detallado
**Formato preferido:** Listas / Párrafos / Ambos

## Restricciones importantes

- [Restricción 1, ej: "No usar jerga técnica"]
- [Restricción 2, ej: "Responder en máximo 3 párrafos"]

## Projetos actuales

1. [Proyecto 1 con breve descripción]
2. [Proyecto 2 con breve descripción]

## Recursos útiles

- [Enlace a recursos relevantes para tu trabajo]
```

### Paso 3: Template específico por profesión

#### Si eres Educator/Docente:

```markdown
# Perfil: Educator

## Quién soy
[Nombre]
Profesora/Profesor de [materia]
[Nivel: primaria, secundaria, universidad]

## Especialización
- [Materia 1]
- [Materia 2]
- [Metodología si aplica]

## Recursos que uso
- [Plataforma educativa]
- [Libro de texto]
- [Herramientas digitales]

## Mis estudiantes
- Edad/Nivel: [X]-[Y] años
- Cantidad promedio: [X] estudiantes
```

#### Si eres Administrador:

```markdown
# Perfil: Administrador

## Quién soy
[Nombre]
[Cargo: Gerente, Director, Coordinador, etc.]
[Sector: Retail, Servicios, Manufactura, etc.]

## Responsabilidades principales
1. [Responsabilidad 1]
2. [Responsabilidad 2]
3. [Responsabilidad 3]

## Métricas que manejo
- [KPI 1: ej: "Ventas mensuales"]
- [KPI 2: ej: "Rotación de inventario"]
- [KPI 3: ej: "Satisfacción de clientes"]

## Herramientas actuales
- [ERP/Sistema principal]
- [Hojas de cálculo]
- [Software de comunicación]
```

#### Si eres Marketing:

```markdown
# Perfil: Marketing

## Quién soy
[Nombre]
[Rol: Coordinador, Manager, Director]
[Tipo: Digital, Tradicional, Producto]

## Canales que manejo
- [ ] Instagram
- [ ] LinkedIn
- [ ] Facebook
- [ ] TikTok
- [ ] Email
- [ ] Website

## Especialización
- [ ] Estrategia de contenido
- [ ] Publicidad pagada
- [ ] SEO
- [ ] Email marketing
- [ ] Análisis de datos

## Mi audiencia
[Describe tu cliente ideal]
```

### Paso 4: Integrar con OpenCode

```bash
# Reiniciar OpenCode para cargar el nuevo perfil
opencode

# Dentro de OpenCode, verificar que reconoce tu perfil
/config
```

### ✅ Checklist de verificación
- [ ] Archivo `~/.config/opencode/AGENTS.md` existe
- [ ] Contiene tu información real
- [ ] Tono y formato reflejados
- [ ] OpenCode lo reconoce

### 📸 Entregable
Captura de tu AGENTS.md personalizado.

---

## LAB 3: Tu Primer Agente Especializado (25 minutos)

### Objetivo
Crear un agente personalizado para tu caso de uso específico.

### Paso 1: Crear directorio de agentes

```bash
mkdir -p ~/.config/opencode/agents
```

### Paso 2: Template de Agente

Crea `~/.config/opencode/agents/mi-agente.md`:

```markdown
---
name: mi-agente
description: "Trigger: [keyword1], [keyword2], [keyword3]. [Descripción breve]"
mode: subagent
permission:
  edit: allow
  bash: deny
  webfetch: allow
---

# Eres [describe quién es el agente]

## Tu rol

[Describe el rol específico]

## Áreas de expertise

1. [Área 1]
2. [Área 2]
3. [Área 3]

## Cómo comunicas

**Tono:** [Formal/Casual/Profesional]
**Estilo:** [Descriptivo/Técnico/Ejemplos]
**Idioma:** [Español/English/Ambos]

## Metodología de trabajo

### Para [tipo de tarea 1]
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

### Para [tipo de tarea 2]
1. [Paso 1]
2. [Paso 2]

## Formatos de entrega

### Documento largo
```
[Título]

## Resumen
[Breve resumen]

## Contenido principal
[Detalle]

## Conclusión
[Resumen final]
```

### Respuesta corta
```
[Punto principal]
[Explicación breve]
[Ejemplo si aplica]
```

## Restricciones

- ❌ [Nunca hacer esto]
- ❌ [Nunca hacer aquello]
- ✅ [Siempre hacer esto]

## Frases típicas de cierre

- "Quedo a su disposición para cualquier duda"
- "¿Hay algo más en lo que pueda ayudarle?"
- "Será un placer ampliar esta información"
```

### Paso 3: Agentes por profesión

#### Agente para Educator:

```markdown
---
name: educator
description: "Trigger: lesson, class, teaching, student, education. Asistente para educadores y docentes"
mode: subagent
permission:
  edit: allow
  bash: deny
  webfetch: allow
---

# Eres un asistente para educadores

## Tu expertise

- Diseño curricular y planes de clase
- Creación de evaluaciones y rúbricas
- Estrategias didácticas
- Adaptación para diferentes estilos de aprendizaje
- Recursos educativos

## Tipos de contenido que generas

### Plan de Clase
```
PLAN DE CLASE

Título: [Tema]
Duración: [X] minutos
Curso: [Grado/Nivel]
Objetivo: [Objetivo de aprendizaje]

MATERIALES:
- [Material 1]
- [Material 2]

DESARROLLO:
1. Inicio ([X] min): [Actividad]
2. Desarrollo ([X] min): [Actividad]
3. Cierre ([X] min): [Actividad]

EVALUACIÓN:
[Tipo de evaluación]
[Rúbrica si aplica]
```

### Evaluación
```
EVALUACIÓN

Curso: [Grado/Nivel]
Materia: [Nombre]
Fecha: [Fecha]
Duración: [X] minutos

INSTRUCCIONES:
[Instrucciones claras]

PREGUNTAS:

I. [Tipo: opción múltiple, desarrollo, etc.]
[Puntaje]

II. [Siguiente pregunta]
[Puntaje]

CUADRO DE RESPUESTAS
1. [Opciones]
2.
3.
```

### Rúbrica
```
RÚBRICA DE EVALUACIÓN

Criterio | Excelente (4) | Bueno (3) | Suficiente (2) | Insuficiente (1)
---------|---------------|-----------|----------------|-----------------
[Criterio 1] | [Desc] | [Desc] | [Desc] | [Desc]
[Criterio 2] | [Desc] | [Desc] | [Desc] | [Desc]
```
```

#### Agente para Administrador:

```markdown
---
name: admin
description: "Trigger: report, analysis, meeting, planning, admin. Asistente para administradores"
mode: subagent
permission:
  edit: allow
  bash: deny
  webfetch: allow
---

# Eres un asistente administrativo

## Tu expertise

- Reportes ejecutivos
- Análisis de datos
- Minutas de reunión
- Planificación
- Presentaciones ejecutivas

## Tipos de documentos

### Reporte Ejecutivo
```
REPORTE EJECUTIVO

Fecha: [Fecha]
Preparado por: [Tu nombre]
Para: [Audiencia objetivo]

RESUMEN EJECUTIVO
[2-3 oraciones del punto más importante]

HALLAZGOS PRINCIPALES
1. [HECHO]: [IMPLICACIÓN]
2. [HECHO]: [IMPLICACIÓN]

ANÁLISIS
[Análisis de 2-3 párrafos]

RECOMENDACIONES
1. [Recomendación 1] → Impacto: [Alto/Medio/Bajo]
2. [Recomendación 2] → Impacto: [Alto/Medio/Bajo]

PRÓXIMOS PASOS
- [ ] [Acción 1] - Fecha límite: [Fecha]
- [ ] [Acción 2] - Fecha límite: [Fecha]
```

### Minuta de Reunión
```
MINUTA DE REUNIÓN

Fecha: [Fecha]
Hora: [Hora inicio] - [Hora fin]
Lugar/Virtual: [Ubicación/Plataforma]
Asistentes: [Lista de nombres]
Ausentes: [Lista si aplica]

OBJETIVO: [Propósito de la reunión]

AGENDA:
1. [Tema 1] - [Responsable] - [Duración]
2. [Tema 2] - [Responsable] - [Duración]

DESARROLLO:

1. [Tema 1]
   Discusión: [Resumen de puntos discutidos]
   Acuerdos: [Lista de acuerdos]
   
2. [Tema 2]
   Discusión: [Resumen]
   Acuerdos: [Lista]

ACUERDOS GENERALES
| Acuerdo | Responsable | Fecha límite |
|---------|-------------|---------------|
| [Acuerdo 1] | [Nombre] | [Fecha] |
| [Acuerdo 2] | [Nombre] | [Fecha] |

PRÓXIMA REUNIÓN
Fecha: [Fecha si está definida]
```

### Checklist de Verificación
- [ ] Agente creado en `~/.config/opencode/agents/`
- [ ] Archivo .md con frontmatter correcto
- [ ] Descripción con keywords específicas
- [ ] Permissions configuradas

---

## LAB 4: Conectar Extensiones MCP (20 minutos)

### Objetivo
Conectar OpenCode con herramientas externas que uses.

### Paso 1: Instalar Context7 (Documentación)

Context7 permite buscar documentación actualizada de librerías.

```bash
# Añadir MCP de Context7
opencode mcp add

# Seleccionar:
# Nombre: context7
# Tipo: Remote
# URL: https://mcp.context7.com/mcp

# O manualmente editar ~/.config/opencode/mcp.json
```

Configuración manual en `~/.config/opencode/mcp.json`:

```json
{
  "mcp": {
    "context7": {
      "type": "remote",
      "url": "https://mcp.context7.com/mcp",
      "enabled": true
    }
  }
}
```

### Paso 2: Configurar GitHub MCP (Opcional)

```bash
# Añadir GitHub MCP
opencode mcp add

# Seleccionar:
# Nombre: github
# Tipo: Local
# Comando: npx
# Args: -y @modelcontextprotocol/server-github
```

### Paso 3: Verificar MCPs instalados

```bash
# Listar MCPs activos
opencode mcp list

# Ver detalles
opencode mcp ls
```

### Paso 4: Usar Context7

```bash
opencode

# Dentro de OpenCode:
@general Buscame la documentación actualizada de React para hacer un formulario con validación
```

### MCPs recomendados por profesión

| Profesión | MCP recomendado |
|-----------|----------------|
| Educator | NotebookLM, Context7 |
| Administrador | GitHub, Jira |
| Marketing | Slack, Notion |
| Programador | GitHub, PostgreSQL |
| Legal | Notion, Filesystem |
| Investigador | NotebookLM, ArXiv |

### ✅ Checklist de verificación
- [ ] Al menos 1 MCP instalado
- [ ] `opencode mcp list` muestra el MCP
- [ ] El MCP responde correctamente

### 📸 Entregable
Captura de `opencode mcp list` mostrando tu MCP instalado.

---

## LAB 5: Caso Práctico End-to-End (30 minutos)

### Objetivo
Completar una tarea real usando todo lo aprendido.

### Escenario: Educator

**Contexto:** Eres profesor/a de historia y mañana tienes una clase sobre la Revolución Francesa. Necesitas preparar el material en 30 minutos.

**Tarea:** Usando OpenCode, prepara:
1. Plan de clase (90 minutos)
2. Presentación de 10 slides
3. Evaluación de 5 preguntas

### Instrucciones paso a paso

#### 1. Abre OpenCode

```bash
opencode
```

#### 2. Carga tu perfil

```
/load @agents/educator
```

#### 3. Genera el plan de clase

```
Necesito un plan de clase de 90 minutos sobre la Revolución Francesa para estudiantes de 4to año de bachillerato.

Incluye:
- Objetivo de aprendizaje
- 3 actividades principales
- Recursos necesarios
- Evaluación formativa
```

#### 4. Genera la presentación

```
Basado en el plan anterior, crea una presentación de 10 slides en formato markdown.
Cada slide debe tener:
- Título
- 3-4 puntos clave
- Sugerencia visual entre paréntesis
```

#### 5. Genera la evaluación

```
Crea una evaluación de 5 preguntas:
- 2 de opción múltiple
- 1 de respuesta corta
- 1 de desarrollo
- 1 de análisis de documento

Incluye rúbrica de corrección.
```

### Escenario: Administrador

**Contexto:** Eres gerente de operaciones y necesitas presentar un informe trimestral a la junta directiva.

**Tarea:** Preparar el reporte ejecutivo completo.

### Instrucciones

```bash
opencode
```

```
/load @agents/admin
```

```
Prepara un reporte ejecutivo trimestral con:

1. Resumen ejecutivo (150 palabras)
2. Métricas clave del trimestre:
   - Ventas: $X (vs meta $Y)
   - Clientes nuevos: Z
   - Retención: W%
3. Análisis de tendencias
4. 3 principales logros
5. 2 principales desafíos
6. Plan para el próximo trimestre
7. Presupuesto solicitado

Usa formato ejecutivo profesional.
```

### Escenario: Marketing

**Contexto:** Eres coordinador de marketing y necesitas planificar el contenido de Instagram para la próxima semana.

### Instrucciones

```bash
opencode
```

```
/load @agents/marketing
```

```
Crea un calendario de contenido para Instagram para la próxima semana (7 días).

Para cada día incluye:
- Tipo de post (educativo, motivacional, producto, interactivo)
- Tema/hook
- Caption (máximo 150 caracteres)
- 5 hashtags relevantes
- Mejor hora de publicación
- Call-to-action

Considera que somos una pyme de [tu industria] en Ecuador.
```

### ✅ Checklist de verificación
- [ ] Plan de clase creado y completo
- [ ] Presentación con estructura lógica
- [ ] Evaluación con rúbrica
- [ ] Contenido exportado/guardado

### 📸 Entregable
Carpeta con:
- Plan de clase.md
- Presentacion.md
- Evaluacion.md

---

## Lab Bonus: Automatización con Skills

### Crear un skill personalizado

```bash
mkdir -p ~/.config/opencode/skills/mi-skill
```

`~/.config/opencode/skills/mi-skill/SKILL.md`:

```markdown
---
name: mi-skill
description: "Trigger: [tu keyword]. [Descripción]"
---

# Mi Skill Personal

## Cuándo usarlo
[Describe cuándo activar este skill]

## Proceso
1. [Paso 1]
2. [Paso 2]
3. [Paso 3]

## Template

```
[TU TEMPLATE AQUÍ]
```

## Checklist
- [ ] [Verificación 1]
- [ ] [Verificación 2]
```

### Usar el skill

```bash
opencode

# Activar
@general /load skills/mi-skill

# Usar
[Tu keyword]: [tarea]
```

---

## Resumen de Labs

| Lab | Tema | Duración | Entregable |
|-----|------|----------|------------|
| 1 | Instalación | 15 min | Screenshot versión |
| 2 | Perfil | 20 min | AGENTS.md personalizado |
| 3 | Agente | 25 min | 1 agente especializado |
| 4 | MCPs | 20 min | 1 MCP configurado |
| 5 | E2E | 30 min | Material completo |

**Tiempo total:** ~110 minutos (con pausa incluida)

---

## Recursos Adicionales

### Documentación
- [docs.opencode.ai](https://dev.opencode.ai/docs)
- [Awesome OpenCode](https://github.com/anomalyco/awesome-opencode)

### Comunidad
- Discord: OpenCode Community
- GitHub: anomalyco/opencode

---

*Labs creados para el Taller de IA para No Informáticos*
*Duración estimada: 2 horas incluyendo teoría*
