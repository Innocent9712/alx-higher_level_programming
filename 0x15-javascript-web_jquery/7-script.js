$(function () {
  $.get('https://swapi-api.hbtn.io/api/people/5/?format=json', (r) => {
    $('#character').text(`${r.name}`);
  });
});
