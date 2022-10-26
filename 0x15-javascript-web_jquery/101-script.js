$(window).load(() => {
  const ul = $('ul.my_list');

  $('div#add_item').click(function () {
    ul.append('<li>Item</li>');
  });

  $('div#remove_item').click(function () {
    ul.children().last().remove();
  });

  $('div#clear_list').click(function () {
    ul.empty();
  });
});
