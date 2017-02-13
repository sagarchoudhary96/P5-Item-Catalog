$(".brighten").click(function() {
  window.location = $(this).find("a").attr("href"); 
  return false;
});

$(".demo-card-wide").hover(
    function() {
        $(this).toggleClass('mdl-shadow--8dp').toggleClass('mdl-shadow--2dp');

    }
);