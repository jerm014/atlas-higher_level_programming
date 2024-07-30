const url = 'https://hellosalut.stefanbohacek.dev/?lang=';
const langs = 'ar, az, be, bg, bn, bs, cs, da, de, dz, el, en, en-gb, ' +
  'en-us, es, et, fa, fi, fil, fr, he, hi, hr, hu, hy, id, is, it, ja, ' +
  'ka, kk, km, ko, lb, lo, lt, lv, mk, mn, ms, my, ne, no, pl, pt, ro, ru, ' +
  'sk, sl, sq, sr, sv, sw, th, tk, uk, vi, zh';

function getLang() {
  let lang = $('INPUT#language_code').val();
  $.get(url + lang, function(data) {
    console.log(lang + data.hello);
    console.log(data);
    if (data.code !== 'none') {
      $('DIV#hello').text(data.hello);
    } else {
      $('DIV#hello').html(
        'Language code not found <p>Supported Languages:<p>' + langs); 
    }
  });
}

function loader() {
  if (document.readyState === 'complete') {
    $('#language_code').on('keypress', function(e) {
      if (e.which === 13) getLang();
    });
    $(':button').click(getLang);
    document.onreadystatechange = None;
  }
}

document.onreadystatechange = loader;
