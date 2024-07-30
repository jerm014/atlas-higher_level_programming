const url = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$(document).ready(function () {
  $.get(url, (data) => {
    $('#hello').text(data.hello);});
});
