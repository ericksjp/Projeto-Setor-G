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
    var windowHeight = $(window).height();
    var elementOffset = $(target).offset().top;
    var scrollToPosition = elementOffset - (windowHeight / 2);
    
    $('html, body').animate({
      scrollTop: scrollToPosition
    }, 1000);
  });
});