$.ajax({
  url: 'https://swapi-api.hbtn.io/api/films/?format=json',
  type: 'GET',
  dataType: 'json',
}).done(function (json) {
  for (const movie of json.results) {
    $('#list_movies').append('<li>' + movie.title + '</li>');
  }
});
