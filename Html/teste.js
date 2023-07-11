const botoes = document.querySelectorAll('.button');
const divLaranja = document.querySelector('#laranja');

function clicouEmQualquerLugar(event) {
  if (!divLaranja.contains(event.target) && !event.target.classList.contains('button')) {
    divLaranja.classList.remove('aaa');
  }
}

botoes.forEach(function(botao) {
  botao.addEventListener('click', function() {
    divLaranja.classList.toggle('aaa');
  });
});

//document.addEventListener('click', clicouEmQualquerLugar);