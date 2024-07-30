let new_header = 'New Header!!!';

$(document).ready(function() {
  $('#update_header').click(() => { $('header').text(new_header); });
});
