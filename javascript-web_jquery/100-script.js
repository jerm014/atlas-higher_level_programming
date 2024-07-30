function makeRed() {
  if (document.readyState === 'complete') {
    const style = document.createElement('style');
    style.innerHTML = 'header { color: red; }';
    document.head.appendChild(style);
  }
}

document.onreadystatechange = makeRed;
