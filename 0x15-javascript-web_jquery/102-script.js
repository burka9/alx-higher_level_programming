$(window).read(() => {
  $('INPUT#btn_translate').click(() => {
    const lang = $('INPUT#language_code').val();

    $.get(`https://www.fourtonfish.com/hellosalut/hello/lang=${lang}`, data => {
      $('DIV#hello').text(data.hello);
    });
  });
});
