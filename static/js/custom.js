$(document).ready(function () {

    // #region ENABLE BS TOOLTIP

    $('[data-toggle="tooltip"]').tooltip();

    // #endregion

    // #region NEW BUG :: SET FORM FIELDS TO READONLY

    $("#id_published_date").prop("readonly", true);
    $("#id_cost_per_hour").prop("readonly", true);

    // #endregion


    // #region PASSWORD RESET :: RESET EMAIL INPUT LENGTH

    $('#id_email').attr('size', 60);

    // #endregion


    // #region FEATURE DETAILS :: SHOW/HIDE DONATE FORM

    $(".donate_feature_button").click(function () {
        $('#donate_feature_form').show();

        $('html, body').animate({
            scrollTop: $("#donate_feature_form").offset().top - 50
        }, 'slow');
    });
    $(".donate_feature_cancel").click(function () {
        $('#donate_feature_form').hide();
    });

    // #endregion


    // #region NAVBAR LINK :: ADD CLASS TO ACTIVE LINK

    var current_path = $(location).attr('pathname');
    if (current_path == "/accounts/profile/") {
        $("#profile-nav-link").addClass("active-link text-success");
    }
    else if (current_path == "/blog/") {
        $("#blog-nav-link").addClass("active-link text-primary");
    }

    // #endregion


    // #region BUG/FEATURE FILTER :: ALIGN BUTTON WITH SELECT

    $("#bugfilter").append("<button type='submit'>Search</button>");
    $("#bugfilter select").addClass("custom-select");
    $("#bugfilter button").addClass("btn btn-primary ");

    // #endregion


    // #region CLOSE MESSAGE DIV
    $('.close-message').on('click', function (c) {
        $('.messages-wrapper').fadeOut('slow', function (c) {
            $('.messages-wrapper').remove();
        });
    });
    // #endregion


}); // close document.ready


// #region GO BACK TO PREVIOUS PAGE

function goPrev() {
    window.history.back();
}

// #endregion


// #region SMOOTH SCROLLING

(function ($) {
    "use strict"; // Start of use strict

    // Smooth scrolling using jQuery easing
    $('a.js-scroll-trigger[href*="#"]:not([href="#"])').click(function () {
        if (location.pathname.replace(/^\//, '') == this.pathname.replace(/^\//, '') && location.hostname == this.hostname) {
            var target = $(this.hash);
            target = target.length ? target : $('[name=' + this.hash.slice(1) + ']');
            if (target.length) {
                $('html, body').animate({
                    scrollTop: (target.offset().top - 70)
                }, 1000, "easeInOutExpo");
                return false;
            }
        }
    });

    // Closes responsive menu when a scroll trigger link is clicked
    $('.js-scroll-trigger').click(function () {
        $('.navbar-collapse').collapse('hide');
    });

    // Activate scrollspy to add active class to navbar items on scroll
    $('body').scrollspy({
        target: '#mainNav',
        offset: 100
    });

})(jQuery);


// #endregion