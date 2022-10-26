$.get('https://swapi-api.hbtn.io/api/films/?format=json', data => {
  const ul = $('ul#list_movies');

  for (let i = 0; i < data.results; i++) {
    ul.append(`<li>${data.results[i].title}</li>`);
  }
});
