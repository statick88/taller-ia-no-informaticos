# Taller de IA para No Informáticos

## Manual del Participante

### Duración: 2 Horas | Modalidad: Virtual | Costo: Gratis

---

## ¿Qué aprenderás?

Al finalizar este taller podrás usar herramientas de inteligencia artificial para aumentar tu productividad profesional sin necesidad de saber programar. Configurarás tu propio asistente personalizado y entenderás qué herramienta usar según tu trabajo.

**Al terminar serás capaz de:**

- Usar Opencode para tareas profesionales
- Personalizar tu asistente con tu perfil
- Instalar habilidades adicionales
- Conectar extensiones
- Elegir la mejor herramienta para tu trabajo

---

## Requisitos Previos

Antes del taller prepara:

1. Cuenta de Google (para NotebookLM, gratis)
2. Editor de texto (Bloc de notas o TextEdit)
3. Navegador actualizado (Chrome, Firefox o Edge)
4. Conexión a internet estable

---

## Estructura del Taller

### Hora 1: Fundamentos y Configuración

| Tiempo | Tema |
|--------|------|
| 0:00 - 0:15 | Bienvenida e introducción |
| 0:15 - 0:30 | El ecosistema de IA en 2026 |
| 0:30 - 0:45 | Instalación de Opencode |
| 0:45 - 1:00 | Primera conversación con la IA |

### Hora 2: Personalización y Análisis

| Tiempo | Tema |
|--------|------|
| 1:00 - 1:20 | Perfiles personalizados (agents.md) |
| 1:20 - 1:40 | Skills y extensiones |
| 1:40 - 1:55 | Comparativa de herramientas |
| 1:55 - 2:00 | Cierre y siguientes pasos |

---

## 1. Fundamentos: ¿Por qué usar asistentes de IA?

### Evidencia científica

La investigación científica demuestra beneficios significativos:

#### Estudio de Repsol (2024)

La multienergética española, en colaboración con MIT Technology Review, evaluó Microsoft 365 Copilot durante 4 meses con 300 empleados:

- **Ahorro de tiempo**: 121 minutos brutos por semana por empleado (96.8 horas/año)
- **Mejora en calidad**: 16% increase en la calidad de entregables
- **Satisfacción**: 61.9% declaró que preferiría no volver a trabajar sin la herramienta
- **Perfil más benefici**: Técnicos cualificados y profesionales sénior

#### Estudio en Ecuador (El Oro, 2025)

Investigación en 900 empleados de empresas comerciales:

- **Productividad**: El uso frecuente de IA incrementa la productividad (odds ratio de 2.34)
- **Eficiencia**: 40% de reducción en duración de tareas administrativas
- **Precisión**: 72% de reducción en incidencia de errores

#### Estudio en México (2025)

Encuesta a 327 usuarios mexicanos:

- **Productividad**: 62% usa IA para incrementar productividad
- **Ahorro**: 7.02 horas semanales en promedio
- **Creatividad**: 31.5% usa IA para generar nuevas ideas
- **Motivación**: Cerca de un tercio busca innovación

#### Estudio en Universidades Latinoamericanas (2024)

Implementación de asistentes virtuales en universidades de Ecuador, Perú y Colombia:

- **Satisfacción**: Más del 75% reportó altos niveles de satisfacción
- **Docentes**: Reducción de carga administrativa
- **Estudiantes**: Retroalimentación inmediata y adaptación de contenidos

### Conclusión científica

Los estudios demuestran consistentemente que los asistentes de IA:

1. **Ahorran tiempo significativo** (2+ horas/semana)
2. **Mejoran la calidad** del trabajo realizado
3. **Aumentan la satisfacción** laboral
4. **Reducen errores** en tareas repetitivas

La IA no reemplaza al profesional, pero amplifica su capacidad.

---

## 2. El Ecosistema de IA en 2026

### ¿Qué es un asistente de IA?

Es como un compañero virtual que te ayuda con tareas intelectuales: escribir, investigar, analizar, resumir. A diferencia de los motores de búsqueda, entiende el contexto y puede mantener una conversación.

### Las principales herramientas

| Herramienta | Para qué sirve | Ventaja principal |
|------------|----------------|----------------|
| **Opencode** | Asistencia versatile | Memoria persistente y personalización |
| **Copilot** | Programación | Integrado en VS Code |
| **Gemini** | Ecosistema Google | Integrado con Sheets, Docs, Drive |
| **Ollama** | Modelos locales | Trabaja sin internet |
| **NotebookLM** | Análisis de documentos | Generación de contenido desde fuentes |

### ¿Cuál elegir?

| Si necesitas... | Elige... |
|---------------|----------|
| Flexibilidad sin programar | Opencode |
| Programar en VS Code | Copilot |
| Usar el ecosistema Google | Gemini |
| Privacidad total de datos | Ollama |
| Solo analizar documentos | NotebookLM |

---

## 3. Instalación de Opencode

### ¿Por qué Opencode?

Framework de asistencia versatile con:

- **Memoria persistente** (recuerda conversaciones anteriores)
- **Sistema de perfiles** (se adapta a tu trabajo)
- **Skills modulares** (extiende capacidades)
- **MCPs** (se conecta con servicios externos)

### Instalación

**Windows**: Abre PowerShell y escribe:

```
npm install -g opencode-cli
```

**Mac**: Abre Terminal:

```
npm install -g opencode-cli
```

**Linux**:

```
sudo npm install -g opencode-cli
```

### Verifica instalación

```
opencode --version
```

---

## 4. Tu Primer Contacto con la IA

### Iniciar conversación

```
opencode
```

### Ejemplos de conversación

**Presenter:**

```
Hola, me llamo [tu nombre] y trabajo en [tu industria]. Ayúdame con [tu tarea].
```

**Pedir ayuda:**

```
Tengo que escribir un proyecto sobre [tema]. ¿Puedes ayudarme a estructurarlo?
```

**Investigar:**

```
Busca información sobre [tu tema de interés]
```

---

## 5. Perfiles Personalizados (agents.md)

### ¿Qué es agents.md?

Es una tarjeta de presentación para tu asistente. Le dice quién eres, qué necesitas y cómo prefieres trabajar.

### Estructura básica

```markdown
# Mi Perfil Profesional

## Quién soy
[Nombre]
[Profesión/Rol]
[Industria]

## Qué hago
[Descripción]

## Mis objetivos
- Objetivo 1
- Objetivo 2

## Cómo prefiero que me ayudes
[Estilo preferido]
[Nivel de detalle]
```

### Ejemplo: Educator

```markdown
# Mi Perfil Profesional

## Quién soy
María García
Profesora de matemáticas
Educación secundaria

## Qué hago
Clases de bachillerato.
Evaluaciones.
Tutorías.

## Mis objetivos
- Crear planes de clase efectivos
- Generar evaluaciones equilibradas
```

### Ejemplo: Administrador

```markdown
# Mi Perfil Profesional

## Quién soy
Juan Pérez
Gerente de operaciones
Sector: Retail

## Qué hago
Coordinación logística.
Gestión de inventario.
Reportes semanales.

## Mis objetivos
- Automatizar reportes
- Mejorar análisis
```

---

## 6. Casos de Uso Detallados por Profesión

### Caso 1: Educator / Docente

**Perfil**: Profesora de historia enbachillerato

**Necesidad**: Crear plan de unidad sobre la Edad Media

**Con Opencode**:

1. Configura tu perfil de educator
2. Escribe: "Crea un plan de unidad sobre la Edad Media para 3er año"
3. Recibes estructura con objetivos, contenidos, actividades
4. Pide: "Genera una evaluación con 10 preguntas"
5. Recibes preguntas con rúbrica de corrección
6. Pide: "Busca fuentes actualizadas sobre [tema específico]"

**Resultado**: Plan de unidad completo en 15 minutos vs 3 horas manual

**Herramientas útiles**:

- Opencode para generación de contenido
- NotebookLM para analizar recursos educativos

---

### Caso 2: Administrador de Empresas

**Perfil**: Gerente de recursos humanos

**Necesidad**: Elaborar informe de rotación de personal

**Con Opencode**:

1. Configura tu perfil de RRHH
2. Escribe: "Ayúdame a estructurar un informe de rotación de personal"
3. Recibes plantilla con métricas clave
4. Proporciona tus datos
5. Pide: "Análisis de las causas principales"
6. Recibes recomendaciones basadas en datos

**Resultado**: informe profesional con insights accionables

**Herramientas**:

- Opencode para estructuración
- Gemini para análisis de hojas de cálculo

---

### Caso 3: Profesional de Marketing

**Perfil**: Coordinador de marketing digital

**Necesidad**: Calendario de contenido para redes sociales

**Con Opencode**:

1. Configura perfil de marketing
2. Escribe: "Crea un calendario de contenido para Instagram para el próximo mes"
3. Recibes 30 publicaciones con temas, horarios, hashtags
4. Pide: "Analiza las redes de [competidor]"
5. Recibes análisis de competidores
6. Pide: "Genera captions para 5 publicaciones"

**Resultado**: Contenido para un mes en 30 minutos

**Herramientas**:

- Opencode para generación
- Amp para automatización

---

### Caso 4: Profesional de Salud

**Perfil**: Médico general en centro de salud

**Necesidad**: Mantenerse actualizado en protocolos

**Con Ollama + NotebookLM**:

1. Configura Ollama (trabajo offline)
2. Busca: "Protocolos actualizados diabetes tipo 2 2025"
3. En NotebookLM: Agrega artículos de revistas médicas
4. Pide: "Resume los hallazgos principales"
5. Verifica siempre con fuentes primarias

**Privacidad**: Datos de pacientes nunca dejan la institución

**Herramientas**:

- Ollama (privacidad)
- NotebookLM (análisis de papers)

---

### Caso 5: Abogado / Legal

**Perfil**: Lawyer en bufete median

**Necesidad**: Investigar precedentes judiciales

**Con Opencode**:

1. Configura perfil legal
2. Escribe: "Busca precedentes sobre [tema jurídico]"
3. Recibes casos relevantes con citas
4. Pide: "Resume los argumentos principales"
5. Verifica siempre con fuentes oficiales

**Herramientas**:

- Opencode para búsqueda
- Normas de citación profesional

---

### Caso 6: Contador / Contador Público

**Perfil**: Contador en empresa comercial

**Necesidad**: Entender nuevas regulaciones fiscales

**Con Opencode**:

1. Configura perfil contable
2. Escribe: "Explica las reformas tributarias 2025"
3. Recibes resumen en lenguaje claro
4. Pide: "¿Cómo afecta a empresas del sector retail?"
5. Recibes análisis específico

**Herramientas**:

- Opencode para explicación
- Gemini para hojas de cálculo

---

### Caso 7: Periodista / Comunicador

**Perfil**: Journalist de investigación

**Necedad**: Investigar tema complejo

**Con Opencode**:

1. Configura perfil de periodista
2. Escribe: "Investiga sobre [tema]"
3. Recibes fontes confiables
4. Pide: "Resume en 5 oraciones"
5. Pide: "¿Qué ángulos no han sido explorados?"

**Herramientas**:

- Opencode para investigación
- NotebookLM para analizar documentos

---

### Caso 8: Ingeniero (No de Software)

**Perfil**: Civil engineer en constructora

**Necesidad**: Revisar normativas de construcción

**Con Opencode**:

1. Configura perfil de ingeniería civil
2. Escribe: "¿Cuáles son los requisitos sísmicos para跳水 de concreto?"
3. Recibes norma con parámetros
4. Pide: "Busca ejemplos de aplicación"
5. Recibes casos de estudio

**Herramientas**:

- Opencode para normativa
- Búsqueda de estándares

---

### Caso 9: Arquitecto

**Perfil**: Arquitecto en estudio de diseño

**Necesidad**: Investigar tendencias sostenibles

**Con Opencode**:

1. Configura perfil de arquitectura
2. Escribe: "Tendencias en materiales sostenibles 2025"
3. Recibes lista de materiales con propiedades
4. Pide: "Proyectos Beispiel que los usen"
5. Recibes casos reales con fotos

---

### Caso 10: Investigador Académico

**Perfil**: Profesor investigador universitario

**Necesidad**: Revisión bibliográfica para artículo

**Con Opencode**:

1. Configura perfil de investigador
2. Escribe: "/busqueda_cientifica [tu tema]"
3. Recibes 20+ fuentes Q1/Q2
4. Verifica en NotebookLM
5. Pide: "Resume el estado del arte"
6. Solicita: "Genera debate entre autores"

**Resultado**: Revisión de literatura completa en horas vs semanas

---

### Caso 11: Estudiante Universitario

**Perfil**: Estudiante de maestría

**Necesidad**: Completar trabajo de investigación

**Con Opencode**:

1. Configura tu perfil de estudiante
2. Escribe: "Ayúdame a estructurar mi TFM sobre [tema]"
3. Recibes estructura IMRAD
4. Proporciona avances
5. Pide: "Revisa mi redacción"
6. Recibes correcciones

**Herramientas**:

- Opencode para estructura
- NotebookLM para estudiar

---

### Caso 12: Emprendedor / Pequeño empresario

**Perfil**: Owner de tienda online

**Necedad**: Mejorar rentabilidad

**Con Opencode**:

1. Configura perfil de negocio
2. Escribe: "Analiza mis ventas del último mes [comparte datos]"
3. Recibes análisis de patrones
4. Pide: "Recomienda productos a ordenar"
5. Pide: "Estrategia de precios"

---

## 7. Skills y Extensiones

### ¿Qué son las skills?

Aplicaciones adicionales queextienden las capacidades de Opencode.

| Skill | Para qué sirve |
|-------|------------|
| Escritura académica | Informes, documentos |
| Marketing digital | Estrategias, contenido |
| Investigación | Fuentes confiables |
| Análisis de datos | Hojas de cálculo |
| Presentaciones | Diapositivas |
| NotebookLM | Análisis profundo |

### Cómo usar

Simplemente indícale qué necesitas:

```
Necesito ayuda con [tu tarea]
```

---

## 8. MCP y Extensiones

### ¿Qué es MCP?

Protocolo que permite conexiones con herramientas externas.

**MCPs esenciales**:

| MCP | Función |
|-----|---------|
| NotebookLM | Análisis de documentos |
| Context7 | Documentación |
| Engram | Memoria persistente |

---

## 9. Análisis Comparativo

### Comparativa principal

| Característica | Copilot | Opencode | Ollama |
|---------------|---------|----------|-------|
| **Costo** | Freemium | Freemium | Gratis |
| **Curva** | Media | Baja | Media |
| **Memoria** | No | Sí | Sí |
| **Personalización** | Limitada | Profunda | Media |
| **Internet** | Sí | Sí | No |
| **Datos locales** | No | No | Sí |

### Por profesión

| Profesión | Recomendación |
|-----------|-------------|
| Educator | Opencode + NotebookLM |
| Administrador | Opencode |
| Marketing | Opencode + Amp |
| Salud | Ollama (privacidad) |
| Legal | Opencode |
| Contador | Opencode + Gemini |

---

## 10. Resumen y Próximos Pasos

### Lo que aprendiste

1. **Evidencia científica**: Los estudios demuestran beneficios reales
2. **Ecosistema IA**: Herramientas disponibles
3. **Opencode**: Instalación básica
4. **Perfiles**: Personalización con agents.md
5. **Skills**: Extensiones de capacidades
6. **Casos de uso**: 12 profesiones cubiertas

### Plan post-taller

| Semana | Acción |
|--------|--------|
| **1ra** | Personaliza tu agents.md |
| **2da** | Explora 2-3 skills |
| **3ra** | Integra en tu flujo |
| **4ta** | Comparte con colegas |

---

## Referencias Científicas

1. **Repsol (2024)**. Estudio sobre Microsoft 365 Copilot. MIT Technology Review España.
2. Márquez-Romero et al. (2025). Impacto de asistentes de IA en productividad. Revista de Finanzas (Ecuador).
3. Yaranga & Olortiga (2025). IA y productividad empresarial. Estudio bibliométrico.
4. López et al. (2025). Asistentes virtuales en educación superior. Revista EDU-INNOVA.
5. Jardón et al. (2024). Asistentes IA en universidades latinoamericanas.
6. Hidalgo Toledo (2025). Productividad y creatividad con IA en México. SciELO.

---

## Preguntas Frecuentes

**¿Necesito saber programar?** No, el taller es para profesionales sin conocimientos técnicos.

**¿Cuánto cuesta?** Opencode tiene nivel gratuito. Ollama y NotebookLM son gratuitos.

**¿Es seguro?** Para datos sensibles usa Ollama (offline). Para datos generales, las herramientas estándar son seguras.

---

## Cheatsheet

```bash
# Instalación
npm install -g opencode-cli

# Verificar
opencode --version

# Iniciar
opencode

# Skills
/skills

# Ayuda
ayúdame con [tarea]
```

---

*Material preparado para el Taller de IA para No Informáticos*
*2 Horas — Virtual — Gratis*