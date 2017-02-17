$(".brighten").click(function() {
  window.location = $(this).find("a").attr("href");
  return false;
});

$(".demo-card-wide").hover(
    function() {
        $(this).toggleClass('mdl-shadow--8dp').toggleClass('mdl-shadow--2dp');

    }
);

var notification = document.querySelector('.mdl-js-snackbar');

var validateDetails = function() {
  var bookname = $('#bookname');
  var authorname = $('#authorname');
  var coverUrl = $('#coverurl');
  var description = $('#description');
  var category = $('#category');

  if (bookname.val() == "") {
    notification.MaterialSnackbar.showSnackbar(
      {
        message: "Book name Can't  Empty!"
      }
    );
    bookname.focus();
    return false;
  }
  else if (authorname.val() == "") {
    notification.MaterialSnackbar.showSnackbar(
      {
        message: "Author Name also required :)"
      }
    );
    authorname.focus();
    return false;
  }
  else if (coverUrl.val() == "") {
    notification.MaterialSnackbar.showSnackbar(
      {
        message: "Cover Image Url also Required!"
      }
    );
    coverUrl.focus();
    return false;
  }
  else if (description.val() == "") {
    notification.MaterialSnackbar.showSnackbar(
      {
        message: "Please provide some description of book!"
      }
    );
    description.focus();
    return false;
  }
  else if (category.val() == "") {
    notification.MaterialSnackbar.showSnackbar(
      {
        message: "Please Select Book Genre!"
      }
    );
    return false;
  }

  $('#newBook').submit();

};
