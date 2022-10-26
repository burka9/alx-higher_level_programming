const translate = () => {
  const lang = $('INPUT#language_code').val();

  $.get(`https://www.fourtonfish.com/hellosalut/hello/lang=${lang}`, data => {
    $('DIV#hello').text(data.hello);
  });
};

$(window).read(() => {
  $('INPUT#btn_translate').click(translate);
  $('INPUT#btn_translate').keypress(event => {
    if (event.which === 13) translate();
  });
});
