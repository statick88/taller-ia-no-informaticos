# 📚 Taller de IA para No Informáticos

**Guía práctica completa** — Domina Opencode, NotebookLM y la Inteligencia Artificial sin saber programar.

> 🎯 **2 horas** | 🌐 **Virtual** | 🆓 **100% Gratis**
> Por **Diego Saavedra García** — CC BY-NC-SA 4.0

---

## 📖 Contenidos

### Ebook (HTML, PDF, EPUB)

El ebook completo está disponible en 3 formatos dentro de `ebook/_book/libro/`:

| Formato | Descripción | Enlace |
|---------|-------------|--------|
| 🌐 **HTML** | Navegación interactiva con buscador | [Abrir ebook](ebook/_book/libro/index.html) |
| 📄 **PDF** | Formato A4 profesional (scrbook) | [Descargar PDF](ebook/_book/libro/Taller-de-IA-para-No-Informáticos.pdf) |
| 📱 **EPUB** | Compatible con Kindle, Apple Books | [Descargar EPUB](ebook/_book/libro/Taller-de-IA-para-No-Informáticos.epub) |

### 🌐 Sitio web desplegado

> **Nota:** Requiere activar GitHub Pages en Settings → Pages → Source: GitHub Actions

- **Landing page:** `https://statick88.github.io/taller-ia-no-informaticos/`
- **Libro:** `.../libro/index.html`
- **Presentación:** `.../presentacion/`

### 📑 Capítulos

| # | Capítulo | Temas |
|---|----------|-------|
| 1 | 🤖 Introducción | Fundamentos, evidencia científica, requisitos |
| 2 | 🔧 OpenCode a fondo | Arquitectura, características, ventajas |
| 3 | ⚙️ Instalación | Windows, macOS, Linux |
| 4 | 👤 Perfiles personalizados | Agentes.md, JSON, configuración |
| 5 | 🧩 Skills y MCP | Extensiones, protocolo, habilidades |
| 6 | 🔍 NotebookLM | Análisis de documentos, fuentes |
| 7 | 🏢 Casos de uso | 12 profesiones con ejemplos reales |
| 8 | 🖥️ OpenCode Avanzado | Prompts, autenticación, funciones |
| 9 | 🤝 Trabajo en equipo | Agentes, colaboración, seguridad |
| 10 | 🧠 IA Generativa | Modelos, comparativas, mejores prácticas |
| 11 | 📊 Comparativa | Herramientas vs profesión vs presupuesto |
| 12 | 🚀 Próximos pasos | Plan de acción 4 semanas |

**+ 3 Apéndices:** Cheatsheet, FAQ, Gentleman AI

---

## 🎯 ¿Qué aprenderás?

- ✅ Usar **OpenCode** para tareas profesionales
- ✅ **Personalizar tu asistente** con perfiles personalizados
- ✅ Instalar **habilidades adicionales** (Skills)
- ✅ Conectar **extensiones** (MCP)
- ✅ Crear **agentes especializados**
- ✅ Elegir la **mejor herramienta** para cada trabajo
- ✅ Aplicar todo en **5 labs prácticos**

---

## 🏗️ Estructura del proyecto

```
.
├── index.html                          # Landing page estática
├── presentacion.html                   # Slides (Reveal.js)
├── propuesta.md                        # Propuesta del taller
├── manual.md                           # Manual del participante
├── ebook/                              # Fuente y build del ebook
│   ├── _quarto.yml                    # Configuración Quarto
│   ├── styles.css                     # CSS profesional dark
│   ├── toggle-sidebar.js              # Toggle sidebar (JS)
│   ├── post_process.py                # Post-procesamiento (legacy)
│   ├── build.py                       # Pipeline completo de build
│   ├── _book/                         # Build generado
│   │   ├── index.html                # Landing page raíz del sitio
│   │   ├── libro/                    # Contenido del ebook
│   │   │   ├── index.html            # Capítulo 1
│   │   │   ├── intro.html
│   │   │   ├── fundamentos.html
│   │   │   ├── opencode.html
│   │   │   ├── instalacion.html
│   │   │   ├── perfiles.html
│   │   │   ├── mcp-skills.html
│   │   │   ├── casos-uso.html
│   │   │   ├── labs.html
│   │   │   ├── comparativa.html
│   │   │   ├── proximos-pasos.html
│   │   │   ├── referencias.html
│   │   │   ├── apendice-cheatsheet.html
│   │   │   ├── apendice-faq.html
│   │   │   ├── apendice-gentle-ai.html
│   │   │   ├── styles.css            # CSS (con toggle inyectado)
│   │   │   ├── search.json           # Búsqueda offline
│   │   │   ├── robots.txt
│   │   │   ├── sitemap.xml
│   │   │   ├── Taller-de-IA-para-No-Informáticos.pdf
│   │   │   ├── Taller-de-IA-para-No-Informáticos.epub
│   │   │   ├── images/               # Assets del ebook
│   │   │   └── site_libs/            # Dependencias JS/CSS
│   │   └── presentacion/            # Slides desplegadas
│   │       └── index.html
│   └── images/
│       └── taller-ia-cover.svg       # Cover del ebook
├── .github/workflows/deploy.yml       # Pipeline CI/CD (GitHub Actions)
└── materiales/                        # Recursos adicionales
    ├── labs/labs-practicos.md
    ├── ejemplos/ejemplos-agentes.md
    ├── estructura/estructura-opencode.md
    └── pdf/
```

---

## 🚀 Cómo usar este material

### Para participantes
1. Abrir el ebook en HTML: `ebook/_book/libro/index.html`
2. O leer el manual: `manual.md`
3. Descargar el PDF para referencia offline

### Para facilitadores
1. Abrir `presentacion.html` en navegador para las slides
2. Usar `materiales/labs/labs-practicos.md` para las actividades
3. El ebook tiene 5 labs integrados con instrucciones paso a paso

### Para contribuidores
- Editar archivos `.qmd` en `ebook/`
- Ejecutar `python3 ebook/build.py` para reconstruir todo (HTML + PDF + EPUB + deploy structure)
- Push automáticamente despliega vía GitHub Actions

---

## 🔧 Requisitos del entorno

| Herramienta | Versión | Uso |
|------------|---------|-----|
| [Quarto](https://quarto.org/) | 1.9.37+ | Renderizado del ebook |
| Python 3.10+ | — | Post-procesamiento |
| Git | — | Control de versiones |

---

## 🤝 Contribución

Las contribuciones son bienvenidas. Si deseas:
- **Reportar errores** → Abre un Issue
- **Sugerir mejoras** → Abre un Discussion
- **Contenido adicional** → Fork + Pull Request

---

## 📄 Licencia

Este material está licenciado bajo [Creative Commons BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/).

Puedes compartir y adaptar el material para uso **no comercial**, manteniendo la atribución y compartiendo bajo la misma licencia.

---

*Última actualización: Mayo 2026*
*[Diego Saavedra García](https://github.com/statick88) — [OpenCode Community](https://github.com/statick88/taller-ia-no-informaticos)*