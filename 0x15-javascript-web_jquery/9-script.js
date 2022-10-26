$(function () {
  $('body').ready(() => {
    $.getJSON('https://stefanbohacek.com/hellosalut/?lang=fr', (r) => {
      $('DIV#hello').text(`${r.hello}`);
    });
    // $.ajax({
    //   type: 'GET',
    //   url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    //   // dataType: "json",
    //   headers: {
    //     "Access-Control-Allow-Origin": "*",
    //     'Access-Control-Allow-Headers': 'x-requested-with'
    //   },
    //   success: (r) => {
    //     $('DIV#hello').text(`${r.hello}`);
    //   }
    // })
    // $.ajax({
    //   type: 'GET',
    //   url: 'https://fourtonfish.com/hellosalut/?lang=fr',
    //   crossDomain: true,
    //   // dataType: "json",
    //   headers: {
    //     "Access-Control-Allow-Origin": "*",
    //     "Access-Control-Allow-Headers": "x-requested-with"
    //   },
    // }).done((data) => console.log(data))
  });
});
