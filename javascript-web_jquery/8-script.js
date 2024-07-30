const url = 'https://swapi-api.hbtn.io/api/films/?format=json';

function update () {
  $.get(url, (data) => {
    data.results.forEach((movie) => {
      $('#list_movies').append('<li>' + movie.title + '</li>');
    });
  });
}

$(document).ready(update);
