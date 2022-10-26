$(function () {
  $.get('https://swapi-api.hbtn.io/api/films/?format=json', (r) => {
    for (let i = 0; i < r.results.length; i++) {
      $('UL#list_movies').append($('<li><li>').text(`${r.results[i].title}`));
    }
  });
});
