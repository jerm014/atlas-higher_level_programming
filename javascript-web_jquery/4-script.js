function toggle() {
  if ($('header').hasClass('green')) {
    $('header').removeClass('green').addClass('red');
  } else {
    $('header').removeClass('red').addClass('green');
  }
}

$(document).ready(() => {
  $('#toggle_header').click(toggle);
});
