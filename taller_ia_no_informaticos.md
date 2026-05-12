# Taller de IA para No Informáticos

## Manual del Participante — 2 Horas Virtual Gratis

---

## ¿Qué aprenderás en 2 horas?

Este taller gratuito te enseñará a usar herramientas de inteligencia artificial para aumentar tu productividad profesional, sin necesidad de saber programar. No necesitas conocimientos técnicos previos.

Al finalizar, podrás:

- Usar Opencode para tareas profesionales
- Personalizar tu asistente de IA con tu perfil
- Instalar habilidades (skills) adicionales
- Conectar extensiones (MCP)
- Elegir la mejor herramienta para tu trabajo

**Duración**: 2 horas | **Modalidad**: Virtual en vivo | **Costo**: Totalmente gratis

---

## Requisitos previos

Antes del taller, prepara en tu computadora:

1. **Cuenta de Google** — Para NotebookLM (gratis)
2. **Editor de texto** — Bloc de notas (Windows) o TextEdit (Mac)
3. **Navegador actualizado** — Chrome, Firefox o Edge
4. **Conexión a internet** — Estable

No necesitas instalar nada antes del taller. Lo haremos juntos durante la primera media hora.

---

## Estructura del Taller

### Hora 1: Fundamentos y Configuración

| Tiempo | Tema | Actividad |
|--------|------|-----------|
| 0:00 - 0:15 | Bienvenida e introducción | Presentación del taller y objetivos |
| 0:15 - 0:30 | El ecosistema de IA en 2026 | Overview de herramientas disponibles |
| 0:30 - 0:45 | Instalación de Opencode | Práctica: instalar y verificar |
| 0:45 - 1:00 | Tu primer contacto con la IA | Práctica: primera conversación |

### Hora 2: Personalización y Extensiones

| Tiempo | Tema | Actividad |
|--------|------|-----------|
| 1:00 - 1:20 | Perfiles personalizados (agents.md) | Práctica: crear tu perfil |
| 1:20 - 1:40 | Skills y extensiones | Práctica: explorar skills |
| 1:40 - 1:55 | Comparativa de herramientas | Análisis: Copilot, Gemini, Ollama |
| 1:55 - 2:00 | Cierre y siguientes pasos | Resumen y recursos |

---

## Capítulo 1: El Ecosistema de IA

### ¿Qué es un asistente de IA?

Un asistente de IA es como un coworker virtual que puede ayudarte con tareas intelectuales: escribir, investigar, analizar, resumir y muchas cosas más. No es una persona, pero actúa como un copiloto inteligente que trabaja contigo.

A diferencia de los motores de búsqueda tradicionales, un asistente de IA entiende el contexto de tu pregunta y puede mantener una conversación para profundizar en lo que necesitas. Puede recordar información de conversaciones anteriores y adaptarse a tu estilo de trabajo.

### Las principales herramientas en 2026

**Asistentes de código**:
- **Copilot** (Microsoft/GitHub): Integrado en Visual Studio Code, ideal para quienes ya ProgRaman.Tiene autocompletado inteligente y puede generar código, pero está enfocado en programación.
- **Kilo Code**: Asistente especializado en generación de código seguro. Fuerte en proyectos grandes y documentación automática.
- **Codex** (OpenAI): Capacidad técnica profunda, puede ejecutar código y automatizar el sistema. Más difícil de configurar para principiantes.

**Frameworks de asistencia**:
- **Opencode**: Framework versátil con memoria persistente, personalización profunda y sistemas de skills. Funciona bien para múltiples tareas, no solo código.
- **Claude Code** (Anthropic): Potente pero más complejo de configurar. Requiere más conocimiento técnico.

**Modelos locales**:
- **Ollama**: Ejecuta modelos de IA en tu computadora sin internet. Ideal para datos sensibles o conectividad limitada.
- **LM Studio**: Interfaz gráfica para modelos locales. Más fácil de usar que Ollama para quienes no usan terminal.

**Herramientas integradas**:
- **Gemini** (Google): Integrado con Sheets, Docs y Drive.Excelente si usas el ecosistema de Google.
- **Amp**: Automatización de flujo de trabajo. Permite encadenar acciones.

### ¿Cuál deberías elegir?

| Si necesitas... | Te recomiendo... |
|-----------------|-----------------|
| Programar y usar VS Code | Copilot |
| Flexibility sin programar | Opencode |
| Privacy total de datos | Ollama |
| Usar el ecosistema Google | Gemini |
| Solo análisis básico | NotebookLM |

---

## Capítulo 2: Instalación de Opencode

### ¿Por qué Opencode?

Opencode es un framework de asistencia de IA que funciona como un copiloto inteligente para cualquier tarea profesional. A diferencia de herramientas especializadas en código, Opencode puede ayudarte con escritura, investigación, análisis y muchas otras tareas.

Sus principales ventajas son:

- **Memoria persistente**: Remember lo que has trabajado antes, incluso entre sesiones
- **Sistema de perfiles**: Se adapta a tu industry y preferencias
- **Skills modulares**: Extiende sus capacidades según lo que necesites
- **MCPs**: Se conecta con servicios externos

### Instalación en Windows

Abre el símbolo del sistema (busca "PowerShell" en el menú inicio) y escribe:

```
npm install -g opencode-cli
```

Verifica que instaló correctamente:

```
opencode --version
```

Si ves un número de versión, ¡felicidades! Ya está instalado.

### Instalación en Mac

Abre la aplicación Terminal (está en Aplicaciones > Utilerías) y escribe:

```
npm install -g opencode-cli
```

Verifica la instalación:

```
opencode --version
```

### Instalación en Linux

Abre tu terminal preferred y ejecuta:

```
sudo npm install -g opencode-cli
```

Verifica con:

```
opencode --version
```

### ¿Qué hacer si no funciona?

Error común: "npm no se reconoce". solutions:

- En Windows: Busca "Node.js" en Google y descárgalo para instalar
- En Mac: Instala Homebrew (busca "brew install node" en Google) y luego Node
- En Linux: Verifica que tienes Node.js instalado con `node --version`

Autre error: "Permiso denegado". Solution: Agrega `sudo` antes del comando en Linux o Mac.

---

## Capítulo 3: Tu Primer Contacto con la IA

### Iniciar tu primera conversación

Una vez instalado Opencode, escribe en tu terminal:

```
opencode
```

Verás un mensaje de bienvenida. Ahora puedes escribirle lo que necesites.

### Ejemplo 1: Presentación básica

Escríbele:

```
Hola, me llamo [tu nombre] y trabajo en [tu industria]. Me gustaría que me ayudaras con tareas de [tu trabajo específico].
```

Opencode te responderá y te hará preguntas para entender mejor cómo ayudarte.

### Ejemplo 2: Pedir ayuda con una tarea

Escríbele:

```
Tengo que escribir un informe sobre [tu tema]. ¿Puedes ayudarme a estructurarlo?
```

Recibirás una guía sobre cómo organizar tu trabajo.

### Ejemplo 3: Hacer una pregunta

Escríbele:

```
¿Cómo podría usar herramientas de IA para mejorar mi productividad en [tu área de trabajo]?
```

Recibirás sugerencias específicas para tu contexto.

### Ejemplo 4: Investigación básica

Escríbele:

```
Busca información sobre [tu tema de interés]
```

Opencode buscará en fuentes confiables y te presentará un resumen.

---

## Capítulo 4: Perfiles Personalizados

### ¿Qué es agents.md?

El archivo agents.md es como una tarjeta de presentación para tu asistente de IA. Le dice quién eres, qué necesitas y cómo prefieres trabajar. Es el centro de la personalización.

Sin este archivo, Opencode te ayuda de manera general. Con él, se adapta a tu contexto profesional específico.

### Estructura básica del archivo

Crea un archivo llamado `agents.md` en tu carpeta de proyecto o en tu carpeta personal. Su contenido básico:

```markdown
# Mi Perfil Profesional

## Quién soy
[Tu nombre]
[Tu profesión/rol]
[Tu industria o sector]

## Qué hago actualmente
[Descripción de tu trabajo principal]
[Tipos de tareas que realizas]

## Mis objetivos
- Objetivo 1
- Objetivo 2
- Objetivo 3

## Cómo prefiero que me ayudes
[Estilo de comunicación preferido]
[Nivel de detalle deseado]
[Formatos de salida favoritos]

## Información de contexto
[Proyectos actuales]
[Clientes o usuarios atendidos]
[Prioridades inmediatas]
```

### Ejemplo: Perfil para educator

```markdown
# Mi Perfil Profesional

## Quién soy
María García
Profesora de matemáticas
Educación secundaria

## Qué hago actualmente
Doy clases de matemáticas a estudiantes de bachillerato.
Preparo materiales didácticos y evaluaciones.
Tutorías individualizadas.

## Mis objetivos
- Crear planes de clase más efectivos
- Generar evaluaciones equilibradas
- Encontrar recursos pedagógicos actualizados

## Cómo prefiero que me ayudes
- Lenguaje claro y directo
- Estructura organizada
- Ejemplos prácticos

## Información de contexto
Nivel: 3er año bachillerato
Tema actual: Álgebra básica
Necesidad inmediata: Evaluación del primer parcial
```

### Ejemplo: Perfil para administrador

```markdown
# Mi Perfil Profesional

## Quién soy
Juan Pérez
Gerente de operaciones
Sector: Retail/Ropa

## Qué hago actualmente
Coordinó logística y proveedores.
Gestión de inventario.
Reportes semanales para dirección.

## Mis objetivos
- Automatizar reportes rutinarios
- Mejorar análisis de datos básicos
- Comunicar mejor con proveedores

## Cómo prefiero que me ayudes
- Formato estructurado
- Resúmenes ejecutivos
- Listas de acción

## Información de contexto
Equipo: 5 personas
Sistema actual: Excel básico
Prioridad: Reporte mensual de ventas
```

### Ejemplo: Perfil para profesional de salud

```markdown
# Mi Perfil Profesional

## Quién soy
Dra. Carolina Mendoza
Médica general
Sector: Salud pública

## Qué hago actualmente
Consulta médica general.
Seguimiento de pacientes crónicos.
Documentación clínica.

## Mis objetivos
- Mantener actualizado el conocimiento médico
- Buscar protocolos recientes
- Organizar notas clínicas

## Cómo prefiero que me ayudes
- Fuentes científicas verificables
- Formato profesional
- Resúmenes concisos

## Información de contexto
Institución: Centro de salud urbano
Especialidad: Medicina familiar
Necesidad: Actualización sobre nuevos protocolos de diabetes
```

### Cómo usar tu perfil

Cada vez que	inicias una sesión con Opencode, puedes indicarle que use tu perfil:

```
Usando mi perfil en agents.md, ayúdame con [tu tarea]
```

O simplemente pega el contenido de tu archivo agents.md al inicio de la conversación.

---

## Capítulo 5: Skills y Extensiones

### ¿Qué son las skills?

Las skills son como aplicaciones adicionales que(extienden las capacidades de Opencode para tareas específicas. Vienen incluidas y se activan según lo que necesites.

Por ejemplo, hay skills para:

- Escritura científica
- Investigación bibliográfica
- Marketing
- Análisis de datos
- Creación de presentaciones

### Cómo ver las skills disponibles

En Opencode, escribe:

```
/skills
```

Verás una lista de skills instaladas con su descripción.

### Cómo activar una skill

Simplemente indícale a Opencode qué necesites:

```
Necesito ayuda con [tu tarea]
```

Opencode elegirá la skill más apropiada automáticamente.

### Skills útiles para profesionales no técnicos

| Skill | Para qué sirve |
|-------|--------------|
| Escritura académica | Informes, papers, documentos formales |
| Marketing digital | Estrategias, contenido, análisis |
| Investigación | Búsqueda en fuentes confiables |
| Análisis de datos | Interpretar hojas de cálculo |
| Presentaciones | Crear diapositivas y materiales |
| NotebookLM | Análisis profundo de documentos |

### Cómo explorar nuevas skills

Si necesitas una skill específica, pregunta:

```
¿Qué skills tienes para [tu necesidad]?
```

O busca en la documentación oficial.

---

## Capítulo 6: MCP y Extensiones

### ¿Qué es MCP?

MCP (Model Context Protocol) es un protocolo que permite a los asistentes de IA conectarse con herramientas y servicios externos. Es como un ecosistema de extensiones que amplía lo que puedes hacer.

Por ejemplo, un MCP puede permitir a tu asistente de IA:

- Conectarse a una base de datos
- Acceder a tu correo electrónico
- Interactuar con servicios web
- Trabajar con archivos locales

### MCPs comunes disponibles

| MCP | Función |
|-----|--------|
| **NotebookLM** | Análisis de documentos, generación de contenido |
| **Context7** | Documentación de librerías y frameworks |
| **Playwright** | Testing automatizado |
| **Engram** | Memoria persistente |

### ¿Necesitas configurar MCPs?

Para usuarios básicos, probablemente no. Opencode viene configurado con MCPs esenciales para comenzar.

Para usuarios avanzados que necesitan conexiones específicas:

1. Revisa la documentación de MCPs
2. Configura las credenciales necesarias
3. Prueba la conexión

### Próximos pasos con MCPs

Una vez que domines lo básico de Opencode, puedes explorar:

- Conexión a bases de datos profesionales
- Integración con herramientas empresariales
- Automatización de flujos de trabajo

---

## Capítulo 7: Análisis de Herramientas

### Copilot vs Opencode vs Ollama

| Característica | Copilot | Opencode | Ollama |
|----------------|--------|----------|-------|
| **Costo** | Freemium | Freemium | Gratis |
| **Curva de aprendizaje** | Media | Baja | Media |
| **Memoria persistente** | No | Sí | Sí |
| **Personalización** | Limitada | Profunda | Media |
| **Necesita internet** | Sí | Sí | No |
| **Datos locales** | No | No | Sí |
| **Skills** | Limitadas | Muchas | N/A |

### ¿Cuál elegir?

**Elige Copilot** si:

- Ya usas Visual Studio Code
- Principalmente programas
- Quieres autocompletado de código

**Elige Opencode** si:

- Necesitas ayuda diversa (no solo código)
- Quieres personalización profunda
- Valoras la memoria persistente

**Elige Ollama** si:

- Trabajas con datos sensibles
- No tienes internet constante
- Quieres control total de tus datos

### Comparativa por profession

| Profession | Recomendación principal | Alternativa |
|------------|-----------------------|------------|
| Educator | Opencode + NotebookLM | Copilot |
| Administrador | Opencode | Gemini |
| Marketing | Opencode + Amp | Gemini |
| Salud | Ollama (privacidad) | Opencode |
| Legal | Opencode | Copilot |
| Contabilidad | Opencode | Gemini |

---

## Casos de Uso Prácticos

### Caso 1: Educator

María es profesora de historia. Necesita crear evaluaciones y encontrar recursos actualizados.

**Con Opencode**:

1. Configura tu perfil con tu información de educator
2. Pide: "Crea una evaluación sobre la Revolución Industrial"
3. Recibes una evaluación estructurada con preguntas
4. Pide: "Busca información reciente sobre [tema]"
5. Obtienes fuentes verificables

**Herramientas útiles**:

- Opencode para generación de contenido
- NotebookLM para analizar recursos

### Caso 2: Administrador

Juan es gerente de una tienda. Necesita analizar ventas y preparar reportes.

**Con Opencode**:

1. Configura tu perfil administrativo
2. Pide: "Ayúdame a estructurar un reporte de ventas mensual"
3. Recibes una plantilla de reporte
4. Pide: "Cómo presentar datos de ventas visualmente"
5. Obtienes sugerencias de gráficos y formato

**Herramientas útiles**:

- Opencode para estructuración
- Gemini para análisis de hojas de cálculo

### Caso 3: Profesional de marketing

Sofía trabaja en marketing. Necesita crear contenido y analizar competidores.

**Con Opencode**:

1. Configura tu perfil de marketing
2. Pide: "Genera ideas para publicación en redes sociales"
3. Recibes un calendario de contenido
4. Pide: "Analiza las redes sociales de [competidor]"
5. Obtienes un análisis estructurado

**Herramientas útiles**:

- Opencode para generación
- Amp para automatización

### Caso 4: Profesional de salud

Dr. López es médico. Necesita buscar protocolos actualizados y mantener privacidad.

**Con Ollama + Opencode**:

1. Configura Ollama para trabajo offline
2. Usa modelos locales para búsqueda sensible
3. Verifica siempre con fuentes primarias
4. Mantén datos de pacientes locales

**Herramientas útiles**:

- Ollama (privacidad)
- NotebookLM (análisis de papers)

---

## Resumen y Próximos Pasos

### Lo que aprendiste

En este taller cubrimos:

1. **El ecosistema de IA**: Las principales herramientas disponibles en 2026 y para qué sirve cada una

2. **Opencode**: Instalación y verificación básica en Windows, Mac y Linux

3. **Primera interacción**: Cómo conversar con tu asistente de IA

4. **Personalización**: Cómo crear un archivo agents.md con tu perfil profesional

5. **Skills**: Cómo extender las capacidades de Opencode

6. **MCPs**: Concepto básico de extensiones

7. **Análisis comparativo**: Cuándo elegir cada herramienta

### Para continúan aprendiendo

**Recursos recomendados**:

- Documentación oficial de Opencode (busca "Opencode AI documentation")
- Guía de NotebookLM (busca "NotebookLM get started")
- Comunidad de usuarios (busca "Opencode community Discord")

**Plan de acción post-taller**:

| Semana | Qué hacer |
|--------|----------|
| **1ra semana** | Personaliza tu archivo agents.md |
| **2da semana** | Explora 2-3 skills relevantes |
| **3ra semana** | Integra una herramienta en tu flujo |
| **4ta semana** | Comparte con colegas |

### Cómo obtener ayuda

- Revisa este material nuevamente
- Pregunta a la comunidad
- Busca en la documentación oficial

---

## Preguntas Frecuentes

**¿Necesito saber programar?**

No. Este taller está diseñado específicamente para profesionales sin conocimientos técnicos. Los asistentes de IA pueden ayudarte sin que programes.

**¿Cuánto cuesta?**

Opencode tiene un nivel gratuito generoso. Ollama y NotebookLM son完全amente gratuitos. Algunos features avanzados pueden tener costo.

**¿Es seguro usar estas herramientas?**

La seguridad depende de la herramienta y de cómo la uses. Para datos sensibles, considera Ollama (trabaja offline). Para datos generales, las herramientas estándar son seguras.

**¿Puedo usar estas herramientas en mi trabajo?**

Depende de las políticas de tu empresa. Verifica con tu departamento de TI antes de usar herramientas de IA con datos corporativos.

**¿Qué hago si tengo problemas?**

Busca en la documentación oficial o pregunta en la comunidad. La mayoría de problemas tienen solución sencilla.

---

## Anexo: Cheatsheet de Comandos

### Comandos básicos de Opencode

```bash
# Instalación (primera vez)
npm install -g opencode-cli

# Verificar instalación
opencode --version

# Iniciar conversación
opencode

# Ver skills disponibles
/skills

# Pedir ayuda específica
ayúdame con [tu tarea]
```

### Tips para mejores resultados

1. **Sé específico**: Cuanto más detalles des, mejor ayudarte.

2. **Indica tu contexto**: "Trabajo en marketing, ayúdame con..."

3. **Pide formato**: "Preséntalo como lista con viñetas"

4. **Itera si es necesario**: "Eso no era exactamente, necesito..."

5. **Verifica información importante**: Especialmente datos y cifras.

---

*Material preparado para el Taller de IA para No Informáticos*
*2 Horas — Virtual — Gratis*