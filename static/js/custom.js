$(document).ready(function () {

    $('[data-toggle="tooltip"]').tooltip()

    // #region set form fields to readonly - New bug

    $("#id_published_date").prop("readonly", true);
    $("#id_cost_per_hour").prop("readonly", true);

    // #endregion


    // #region reset email input length

    $('#id_email').attr('size', 60);

    // #endregion


    // #region show/hide donate form - Feature details page

    $(".donate_feature_button").click(function () {
        $('#donate_feature_form').show()

        $('html, body').animate({
            scrollTop: $("#donate_feature_form").offset().top - 50
        }, 'slow');
    });
    $(".donate_feature_cancel").click(function () {
        $('#donate_feature_form').hide()
    });

    // #endregion


    // #region Add class to NAVBAR LINK depending on the page displayed  

    var current_path = $(location).attr('pathname');
    if (current_path == "/accounts/profile/") {
        $("#profile-nav-link").addClass("active-link text-success");
    }
    else if (current_path == "/blog/") {
        $("#blog-nav-link").addClass("active-link text-primary");
    }

    // #endregion


}); // close document.ready


// #region Smooth scrolling from nav

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

})(jQuery); // End of use strict


// #endregion Smooth scrolling from nav