#!/usr/bin/env bash
# Post-procesa los HTML del ebook para inyectar el toggle del sidebar
# y reorganiza la estructura para GitHub Pages

set -e

BOOK_DIR="_book"

echo "=== Inyectando toggle-sidebar en todos los HTML ==="

for htmlfile in "$BOOK_DIR"/*.html; do
  if [ -f "$htmlfile" ]; then
    # Solo procesar si aún no tiene el toggle
    if ! grep -q "sidebar-toggle-script" "$htmlfile"; then
      # Inyectar script antes de </body>
      sed -i '' '/<\/body>/i\
<script class="sidebar-toggle-script">\n\
document.addEventListener("DOMContentLoaded", function() {\n\
  var btn = document.querySelector(".quarto-btn-toggle");\n\
  if (!btn) return;\n\
  btn.style.display = "flex";\n\
  btn.innerHTML = "☰";\n\
  btn.addEventListener("click", function(e) {\n\
    e.preventDefault();\n\
    e.stopPropagation();\n\
    var open = document.body.classList.toggle("sidebar-visible");\n\
    localStorage.setItem("taller-sidebar", open ? "open" : "closed");\n\
  });\n\
  if (localStorage.getItem("taller-sidebar") === "open") {\n\
    document.body.classList.add("sidebar-visible");\n\
  }\n\
});\n\
</script>' "$htmlfile"
      echo "  ✅ $(basename "$htmlfile")"
    else
      echo "  ⏭ $(basename "$htmlfile") (ya procesado)"
    fi
  fi
done

echo ""
echo "=== Reorganizando estructura ==="
cd "$BOOK_DIR"

# Crear estructura
mkdir -p libro presentacion

# Mover HTMLs del libro
for f in *.html; do
  if [ -f "$f" ]; then
    mv "$f" libro/
  fi
done

# Mover assets
mv styles.css images search.json robots.txt sitemap.xml libro/ 2>/dev/null || true
mv site_libs libro/ 2>/dev/null || true

# Mover PDF y EPUB
mv *.pdf libro/ 2>/dev/null || true
mv *.epub libro/ 2>/dev/null || true

# Copiar presentación
cp libro/presentacion.html presentacion/ 2>/dev/null || true

echo "=== Estructura final ==="
find . -type f | wc -l
echo "archivos totales"

echo ""
echo "=== Tamaños ==="
ls -lh libro/Taller-de-IA*.* 2>/dev/null

echo ""
echo "✅ Post-procesamiento completado"