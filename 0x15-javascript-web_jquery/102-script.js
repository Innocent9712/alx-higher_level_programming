$(function () {
  $('body').ready(() => {
    $('INPUT#btn_translate').click(() => {
      const input = $('INPUT#language_code').val();
      if (input.length === 2) {
        $.getJSON(`https://stefanbohacek.com/hellosalut/?lang=${input}`, (r) => {
          $('DIV#hello').text(`${r.hello}`);
        });
      }
    });
  });
});
