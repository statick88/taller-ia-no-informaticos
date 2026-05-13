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
print("\n=== Reorganizando en libro/ ===")
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

# Limpiar _book/ raíz (dejar solo libro/ y presentacion/)
for f in list(os.listdir(BOOK_DIR)):
    if f in ('libro', 'presentacion'):
        continue
    fp = os.path.join(BOOK_DIR, f)
    if os.path.isdir(fp):
        shutil.rmtree(fp)
    else:
        os.remove(fp)

# 4. Landing page desde repo + presentación
print("\n=== Generando landing page raíz + presentación ===")
landing_src = os.path.join(REPO_ROOT, 'index.html')
landing_dst = os.path.join(BOOK_DIR, 'index.html')
if os.path.exists(landing_src):
    shutil.copy2(landing_src, landing_dst)
    print("  ✅ _book/index.html (landing — copiada de index.html)")
else:
    print(f"  ⚠ {landing_src} no encontrado")

os.makedirs(PRESENTACION_DIR, exist_ok=True)
src = os.path.join(REPO_ROOT, 'presentacion.html')
dst = os.path.join(PRESENTACION_DIR, 'index.html')
if os.path.exists(src):
    shutil.copy2(src, dst)
    print("  ✅ presentacion/index.html")
else:
    print(f"  ⚠ presentacion.html no encontrado en {src}")

# 5b. Copiar archivos HTML de la raíz al _book/
print("\n=== Copiando archivos de la raíz al _book/ ===")
for fn in ('manual.html', 'propuesta.html', 'opencode-taller.html',
            'presentacion.html', 'presentacion-parte2.html', 'presentacion-labs.html'):
    src = os.path.join(REPO_ROOT, fn)
    dst = os.path.join(BOOK_DIR, fn)
    if os.path.exists(src):
        shutil.copy2(src, dst)
        print(f"  ✅ {fn} → _book/")
    # No mostrar warning si no existe — es optional

# 5. Reporte
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