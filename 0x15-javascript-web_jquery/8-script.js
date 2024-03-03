$(document).ready(() => {
  $.get('https://swapi-api.alx-tools.com/api/films/?format=json', (data) => {
    const movies = data.results;
    const ul = $('#list_movies');
    movies.forEach((movie) => {
      ul.append(`<li>${movie.title}</li>`);
    });
  });
});
