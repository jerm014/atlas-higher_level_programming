function add() { $('UL.my_list').append('<li>Item</li>'); }

function remove() { $('UL.my_list li').last().remove(); }

function clear() { $('UL.my_list').empty(); }

function loader() {
  if (document.readyState === 'complete') {
      $('DIV#add_item').click(add);
      $('DIV#remove_item').click(remove);
      $('DIV#clear_list').click(clear);
  }
}

document.onreadystatechange = loader;
