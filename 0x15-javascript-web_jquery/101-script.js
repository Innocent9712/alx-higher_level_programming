$(function () {
  $('body').ready(() => {
    $('DIV#add_item').click(() => {
      $('UL.my_list').append($('<li></li>').text('Item'));
    });

    $('DIV#remove_item').click(() => {
      const itemList = $('UL.my_list li');
      if (itemList.length > 0) {
        itemList[itemList.length - 1].remove();
      }
    });

    $('DIV#clear_list').click(() => {
      $('UL.my_list').empty();
    });
  });
});
