document.addEventListener('DOMContentLoaded', function () {
  var btn = document.querySelector('.quarto-btn-toggle');
  if (btn) {
    btn.style.display = 'flex';
    btn.innerHTML = '&#9776;';
    btn.style.width = '36px';
    btn.style.height = '36px';
    btn.style.borderRadius = '50%';
    btn.style.alignItems = 'center';
    btn.style.justifyContent = 'center';
    btn.addEventListener('click', function (e) {
      e.preventDefault();
      e.stopPropagation();
      var hide = document.body.classList.toggle('sidebar-hidden');
      localStorage.setItem('taller-sidebar', hide ? 'hidden' : 'shown');
    });
    // Restaurar preferencia
    if (localStorage.getItem('taller-sidebar') === 'hidden') {
      document.body.classList.add('sidebar-hidden');
    }
  }
});
  }
  // Restaurar preferencia previa
  if (localStorage.getItem('taller-sidebar') === 'open') {
    document.body.classList.add('sidebar-visible');
  }
});