// Write a JavaScript script that fetches the character name from this URL: https://swapi-api.hbtn.io/api/people/5/?format=json

$(function () {
  $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function (data, textStatus) {
    if (textStatus === 'success') {
      $('#character').text(data.name);
    }
  });
});
