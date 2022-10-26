$(function () {
  function getTranslation () {
    const input = $('INPUT#language_code').val();
    if (input.length === 2) {
      $.getJSON(`https://stefanbohacek.com/hellosalut/?lang=${input}`, (r) => {
        $('DIV#hello').text(`${r.hello}`);
      });
    }
  }
  $('body').ready(() => {
    $('INPUT#btn_translate').click(() => {
      getTranslation();
    });

    $('INPUT#language_code').focus(() => {
      $(document).keyup(function (event) {
        if (event.which === 13) {
          getTranslation();
        }
      });
    });
  });
});
