let new_header = 'New Header!!!';

$(document).ready(() => {
  $('#update_header').click(() => {
    $('header').text(new_header);});
});
