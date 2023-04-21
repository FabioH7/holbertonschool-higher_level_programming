$.ajax({
  url: 'https://hellosalut.stefanbohacek.dev/?lang=fr',
  type: 'GET',
  dataType: 'json',
}).done(function (json) {
  $('#hello').append(json.hello);
});
