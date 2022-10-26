$(function () {
  $('DIV#toggle_header').click(() => {
    if ($('header').hasClass('red')) { $('header').addClass('green').removeClass('red'); } else { $('header').addClass('red').removeClass('green'); }
  });
});
