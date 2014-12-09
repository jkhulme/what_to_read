$(function() {
  $("#purchase_link").on("click",function(e) {
    e.preventDefault(); // cancel the link itself
    $.post(this.href,function(data) {
      $("#someContainer").html(data);
    });
  });
});
