#!/usr/bin/env python3
"""Post-procesa el ebook: inyecta toggle sidebar y reorganiza estructura."""
import os, shutil, glob

BOOK_DIR = "_book"
LIBRO_DIR = os.path.join(BOOK_DIR, "libro")
PRESENTACION_DIR = os.path.join(BOOK_DIR, "presentacion")

# Crear directorios
os.makedirs(LIBRO_DIR, exist_ok=True)
os.makedirs(PRESENTACION_DIR, exist_ok=True)

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
    var open = document.body.classList.toggle('sidebar-visible');
    localStorage.setItem('taller-sidebar', open ? 'open' : 'closed');
  });
  if (localStorage.getItem('taller-sidebar') === 'open') {
    document.body.classList.add('sidebar-visible');
  }
});
</script>'''

print("=== Inyectando toggle-sidebar en HTMLs ===")
for html_path in sorted(glob.glob(os.path.join(BOOK_DIR, "*.html"))):
    fname = os.path.basename(html_path)
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    if 'sidebar-toggle-script' in content:
        print(f"  ⏭ {fname} (ya procesado)")
        continue
    if '</body>' in content:
        content = content.replace('</body>', f'  {TOGGLE_SCRIPT}\n\n</body>')
        with open(html_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"  ✅ {fname}")
    else:
        print(f"  ⚠ {fname} (sin </body>)")

print("\n=== Reorganizando estructura ===")

# Mover HTMLs a libro/
for f in glob.glob(os.path.join(BOOK_DIR, "*.html")):
    shutil.move(f, LIBRO_DIR)

# Mover assets a libro/
for subdir in ['images', 'site_libs']:
    src = os.path.join(BOOK_DIR, subdir)
    if os.path.exists(src):
        shutil.move(src, LIBRO_DIR)

for fname in ['styles.css', 'search.json', 'robots.txt', 'sitemap.xml']:
    src = os.path.join(BOOK_DIR, fname)
    if os.path.exists(src):
        shutil.move(src, LIBRO_DIR)

# Mover PDF y EPUB a libro/
for ext in ['*.pdf', '*.epub']:
    for f in glob.glob(os.path.join(BOOK_DIR, ext)):
        shutil.move(f, LIBRO_DIR)

# Copiar presentación
presentacion_src = os.path.join(LIBRO_DIR, 'presentacion.html')
if os.path.exists(presentacion_src):
    shutil.copy2(presentacion_src, PRESENTACION_DIR)

# Listar resultado
total = len(glob.glob(os.path.join(LIBRO_DIR, "**/*"), recursive=True))
print(f"Total archivos en libro/: {total}")

sizes = glob.glob(os.path.join(LIBRO_DIR, "Taller*.*"))
for s in sizes:
    sz = os.path.getsize(s)
    print(f"  {os.path.basename(s)}: {sz/1024:.0f} KB")

print("\n✅ Post-procesamiento completado")