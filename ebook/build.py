#!/usr/bin/env python3
"""Pipeline completo de build para el ebook: render, toggle, reorganiza."""
import os, shutil, glob, subprocess, sys

BOOK_DIR = "_book"
LIBRO_DIR = os.path.join(BOOK_DIR, "libro")
PRESENTACION_DIR = os.path.join(BOOK_DIR, "presentacion")
REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TOGGLE_SCRIPT = '''<script class="sidebar-toggle-script">
document.addEventListener('DOMContentLoaded', function() {
  var btn = document.querySelector('.quarto-btn-toggle');
  if (!btn) return;
  btn.style.display = 'flex';
  btn.innerHTML = '&#9776;';
  btn.style.width = '36px';
  btn.style.height = '36px';
  btn.style.borderRadius = '50%';
  btn.style.alignItems = 'center';
  btn.style.justifyContent = 'center';
  btn.addEventListener('click', function(e) {
    e.preventDefault();
    e.stopPropagation();
    var hide = document.body.classList.toggle('sidebar-hidden');
    localStorage.setItem('taller-sidebar', hide ? 'hidden' : 'shown');
  });
  if (localStorage.getItem('taller-sidebar') === 'hidden') {
    document.body.classList.add('sidebar-hidden');
  }
});
</script>'''

LANDING_HTML = '''<!DOCTYPE html>
<html lang="es">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Taller de IA para No Informáticos</title>
  <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;800&display=swap');
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: 'Inter', sans-serif;
      background: #0a0a0f;
      color: #e0e0e0;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
    }
    .container { max-width: 820px; padding: 2rem; text-align: center; }
    .emoji { font-size: 4rem; margin-bottom: 1rem; }
    h1 { font-size: 2.5rem; color: #00cc33; margin-bottom: 0.5rem; }
    .subtitle { font-size: 1.15rem; color: #888; margin-bottom: 2.5rem; line-height: 1.6; }
    .menu { display: grid; gap: 1.2rem; margin-top: 1rem; }
    .card {
      background: #12121a; border: 1px solid rgba(255,255,255,0.07);
      border-radius: 14px; padding: 1.6rem 1.8rem; text-decoration: none;
      color: inherit; transition: all 0.2s ease; display: flex; align-items: center; gap: 1.2rem;
    }
    .card:hover { border-color: #00cc33; transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,204,51,0.12); }
    .card .icon { font-size: 2.2rem; min-width: 48px; text-align: center; }
    .card .label { font-size: 1.1rem; font-weight: 600; color: #00b4e6; text-align: left; }
    .card .desc { font-size: 0.9rem; color: #777; margin-top: 0.15rem; text-align: left; }
    .footer { margin-top: 3.5rem; color: #444; font-size: 0.82rem; line-height: 1.8; }
    .footer a { color: #00b4e6; text-decoration: none; }
    .footer a:hover { color: #00cc33; }
    .badge {
      display: inline-block; background: #00cc3322; color: #00cc33;
      padding: 0.15rem 0.55rem; border-radius: 6px; font-size: 0.75rem;
      font-weight: 700; margin-left: 0.5rem; vertical-align: middle;
    }
    @media (min-width: 600px) { .menu { grid-template-columns: 1fr 1fr; } }
  </style>
</head>
<body>
  <div class="container">
    <div class="emoji">🤖</div>
    <h1>Taller de IA para No Informáticos</h1>
    <p class="subtitle">
      Guía práctica para profesionales no técnicos — Aprende a usar la IA
      <span class="badge">GRATIS</span><span class="badge">2 h</span>
    </p>
    <div class="menu">
      <a class="card" href="presentacion/index.html" target="_top">
        <div class="icon">🎤</div>
        <div><div class="label">Presentación</div><div class="desc">Slides interactivas del taller — Reveal.js</div></div>
      </a>
      <a class="card" href="libro/" target="_top">
        <div class="icon">📖</div>
        <div><div class="label">Libro Electrónico</div><div class="desc">15 capítulos + 3 apéndices — navegación completa</div></div>
      </a>
      <a class="card" href="libro/Taller-de-IA-para-No-Informáticos.pdf" download target="_blank">
        <div class="icon">📄</div>
        <div><div class="label">Descargar PDF</div><div class="desc">Formato A4 profesional — imprimir o leer offline</div></div>
      </a>
      <a class="card" href="libro/Taller-de-IA-para-No-Informáticos.epub" download target="_blank">
        <div class="icon">📱</div>
        <div><div class="label">Descargar EPUB</div><div class="desc">Compatible con Kindle, Apple Books, Kobo</div></div>
      </a>
      <a class="card" href="https://github.com/statick88/taller-ia-no-informaticos" target="_blank">
        <div class="icon">📂</div>
        <div><div class="label">Repositorio</div><div class="desc">Código fuente y materiales del taller</div></div>
      </a>
    </div>
    <div class="footer">
      <p>Diego Saavedra García — CC BY-NC-SA 4.0</p>
      <p><a href="https://github.com/statick88/taller-ia-no-informaticos">github.com/statick88/taller-ia-no-informaticos</a></p>
      <p>Última actualización: 2026-05-12</p>
    </div>
  </div>
</body>
</html>'''


def run(cmd):
    print(f"\n  $ {cmd}")
    r = subprocess.run(cmd, shell=True, capture_output=True)
    if r.stdout:
        print(r.stdout.decode(), end="")
    if r.returncode != 0:
        if r.stderr:
            print(r.stderr.decode(), end="", file=sys.stderr)
        print(f"  ❌ FAILED (exit {r.returncode})")
        sys.exit(r.returncode)


# ============================================
# MAIN
# ============================================
print("=" * 60)
print("  🚀 Build completo del ebook")
print("=" * 60)
shutil.rmtree(BOOK_DIR, ignore_errors=True)

# 1. Render HTML + PDF + EPUB
print("\n📝 Renderizando todos los formatos (HTML + PDF + EPUB)...")
run("quarto render")
print("✅ Render completado")

# 2. Inyectar toggle en todos los HTMLs del _book raíz
print("\n=== Inyectando toggle-sidebar ===")
count = 0
for fp in sorted(glob.glob(os.path.join(BOOK_DIR, "**/*.html"), recursive=True)):
    if '/libro/' in fp:
        continue
    with open(fp, 'r', encoding='utf-8') as f:
        c = f.read()
    if 'sidebar-toggle-script' in c:
        continue
    if '</body>' in c:
        c = c.replace('</body>', f'  {TOGGLE_SCRIPT}\n\n</body>')
        with open(fp, 'w', encoding='utf-8') as f:
            f.write(c)
        print(f"  ✅ {os.path.basename(fp)}")
        count += 1
if count == 0:
    print("  (ya procesado)")

# 3. Crear libro/ y mover todo
print("\n=== Reorganizando en librom/ ===")
os.makedirs(LIBRO_DIR, exist_ok=True)

for fp in glob.glob(os.path.join(BOOK_DIR, "*.html")):
    shutil.move(fp, LIBRO_DIR)
print("  ✅ HTMLs → libro/")

for subdir in ('images', 'site_libs'):
    src = os.path.join(BOOK_DIR, subdir)
    if os.path.exists(src):
        shutil.move(src, LIBRO_DIR)
        print(f"  ✅ {subdir}/ → libro/")

for fn in ('styles.css', 'search.json', 'robots.txt', 'sitemap.xml'):
    src = os.path.join(BOOK_DIR, fn)
    if os.path.exists(src):
        shutil.move(src, LIBRO_DIR)
        print(f"  ✅ {fn} → libro/")

for ext in ('*.pdf', '*.epub'):
    for fp in glob.glob(os.path.join(BOOK_DIR, ext)):
        shutil.move(fp, LIBRO_DIR)
        print(f"  ✅ {os.path.basename(fp)} → libro/")

# Limpiar _book/ raíz
for f in list(os.listdir(BOOK_DIR)):
    if f in ('libro', 'presentacion'):
        continue
    fp = os.path.join(BOOK_DIR, f)
    if os.path.isdir(fp):
        shutil.rmtree(fp)
    else:
        os.remove(fp)

# 4. Generar landing page raíz en _book/
print("\n=== Generando landing page raíz ===")
with open(os.path.join(BOOK_DIR, 'index.html'), 'w', encoding='utf-8') as f:
    f.write(LANDING_HTML)
print("  ✅ _book/index.html (landing)")

# 5. Copiar presentación
os.makedirs(PRESENTACION_DIR, exist_ok=True)
src = os.path.join(REPO_ROOT, 'presentacion.html')
dst = os.path.join(PRESENTACION_DIR, 'index.html')
if os.path.exists(src):
    shutil.copy2(src, dst)
    print("  ✅ presentacion/index.html")
else:
    print(f"  ⚠ presentacion.html no encontrado en {src}")

# 6. Reporte
print("\n" + "=" * 60)
print("  ✅ BUILD COMPLETADO EXITOSAMENTE")
print("=" * 60)
total = len(list(glob.glob(os.path.join(LIBRO_DIR, "**/*"), recursive=True)))
print(f"\nTotal archivos en libro/: {total}")
for fn in sorted(glob.glob(os.path.join(LIBRO_DIR, "Taller*.*"))):
    sz = os.path.getsize(fn)
    print(f"  📦 {os.path.basename(fn)}: {sz//1024} KB")

print("\n📁 Estructura final de _book/:")
for root, dirs, files in os.walk(BOOK_DIR):
    level = root.replace(BOOK_DIR, "").count(os.sep)
    indent = "  " * level
    print(f"{indent}📁 {os.path.basename(root)}/")
    for fn in sorted(files):
        sz = os.path.getsize(os.path.join(root, fn))
        unit = "KB" if sz >= 1024 else "B"
        val = sz // 1024 if unit == "KB" else sz
        print(f"{indent}  📄 {fn} ({val} {unit})")