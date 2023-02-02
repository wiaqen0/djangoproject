$(window).scroll(function(){
    if ($(window).scrollTop() >= 300) {
        $('nav').addClass('fixed-header');
        $('.banner nav div').addClass('visible-title');
    }
    else {
        $('nav').removeClass('fixed-header');
        $('.banner nav div').removeClass('visible-title');
    }
});
$(document).on('click', 'a[href^="#menu"]', function (event) {
    event.preventDefault();

    $('html, body').animate({
        scrollTop: $($.attr(this, 'href')).offset().top
    }, 500);
});