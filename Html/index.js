const btnMobile = document.getElementById('btn-mobile');

function toggleMenu(event) {
  if (event.type === 'touchstart') event.preventDefault();
  const nav = document.getElementById('nav');
  nav.classList.toggle('active');
  const active = nav.classList.contains('active');
  event.currentTarget.setAttribute('aria-expanded', active);
  if (active) {
    event.currentTarget.setAttribute('aria-label', 'Fechar Menu');
  } else {
    event.currentTarget.setAttribute('aria-label', 'Abrir Menu');
  }
}
btnMobile.addEventListener('click', toggleMenu);
btnMobile.addEventListener('touchstart', toggleMenu);

$(document).ready(function() {
  $('.link-ancla').click(function(e) {
    e.preventDefault();
    
    var target = $(this).attr('href');
    var scrollToPosition = $(target).offset().top;
    
    $('html, body').animate({
      scrollTop: scrollToPosition  - 100
    }, 300);
  });
});

function toggleVisibility(button) {
  var divLaranja = document.querySelector('.indice-conteudo');
  var LaranjaHeader = document.querySelector('.indice-header');
  var buttonCollor = document.querySelector('#indice_button');

  divLaranja.classList.toggle('highlight');
  LaranjaHeader.classList.toggle('highlight');
  buttonCollor.classList.toggle('highlight');
  button.textContent = divLaranja.classList.contains('highlight') ? 'mostrar' : 'ocultar';
}

window.onload = function () {
  var button = document.querySelector('.laranja button');
  button.addEventListener('click', function () {
      toggleVisibility(this);
  });
};

function scrollToTop() {
    $('html, body').animate({
        scrollTop: 0
    }, 500);
}