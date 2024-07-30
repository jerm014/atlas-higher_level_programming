function makeRed() {
  if (document.readyState === 'complete')
    document.querySelector('header').css('color', '#FF0000');
}

document.onreadystatechange = makeRed;
