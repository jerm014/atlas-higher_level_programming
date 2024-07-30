const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

function element(el, text) {
  const element = document.createElement(el);
  element.innerHTML = text;
  return element;
}

function update () {
  $.get(url, (data) => {
    data.results.forEach((movie) => {
      $('#list_movies').append(element('LI', movie.title));
    });
  });
}

$(document).ready(update);
