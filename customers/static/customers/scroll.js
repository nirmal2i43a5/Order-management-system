// $(document).ready(function(){
//     $(window).scroll(function () {
//            if ($(this).scrollTop() > 50) {
//                $('#back-to-top').fadeIn();
//            } else {
//                $('#back-to-top').fadeOut();
//            }
//        });
//        // scroll body to 0px on click
//        $('#back-to-top').click(function () {
//            $('#back-to-top').tooltip('hide');
//            $('body,html').animate({
//                scrollTop: 0
//            }, 800);
//            return false;
//        });
       
//        $('#back-to-top').tooltip('show');

// });

// -------------------------------------------------------------------
// https://www.templatemonster.com/blog/back-to-top-button-css-jquery/
jQuery(document).ready(function() {
  
    var btn = $('#back-to-top');
  
    $(window).scroll(function() {
      if ($(window).scrollTop() > 300) {
        btn.addClass('show');
      } else {
        btn.removeClass('show');
      }
    });
  
    btn.on('click', function(e) {
      e.preventDefault();
      $('html, body').animate({scrollTop:0}, '300');
    });
  
  });



  function scrollToBottom() {
    window.scrollTo(0,700);
  }

