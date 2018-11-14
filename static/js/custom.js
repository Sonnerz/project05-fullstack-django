$(document).ready(function () {

    //#region set form fields to readonly - New bug
    $("#id_published_date").prop("readonly", true);
    $("#id_cost_per_hour").prop("readonly", true);
    //#endregion



    //#region show/hide donate form - Feature details page
    $(".donate_feature_button").click(function () {
        $('#donate_feature_form').show()

        $('html, body').animate({
            scrollTop: $("#donate_feature_form").offset().top - 50
        }, 'slow');
    });
    $(".donate_feature_cancel").click(function () {
        $('#donate_feature_form').hide()
    });
    //#endregion



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
