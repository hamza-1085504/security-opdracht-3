$(document).ready(function() {
    $("#afkeur_form").hide();
    $("#terug_btn_afkeur").hide();

    var isFormHidden = true;

    $("#afkeur_btn").on("click", function() {
        if (isFormHidden) {
            $("#afkeur_form").show();
        } else {
            $("#afkeur_form").hide();
        }
        isFormHidden = !isFormHidden;
    });
});
