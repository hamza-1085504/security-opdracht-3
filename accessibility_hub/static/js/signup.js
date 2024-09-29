
$(document).ready(function() {
    $("#supervisor_div").hide();

    $("#supervisor").change(function() {
        if ($(this).val() === 'ja') {
            $("#supervisor_div").fadeIn();
        } else {
            $("#supervisor_div").fadeOut();
        }
    });

    $("#birthday").change(function() {
        var geboortedatum = new Date($(this).val());
        var vandaag = new Date();
        var leeftijd = vandaag.getFullYear() - geboortedatum.getFullYear();
        var maandVerschil = vandaag.getMonth() - geboortedatum.getMonth();
        
        if (maandVerschil < 0 || (maandVerschil === 0 && vandaag.getDate() < geboortedatum.getDate())) {
            age--;
        }
        
        if (leeftijd < 18) {
            $("#supervisor_div").fadeIn();
            $("#supervisor_div_btn_hide").fadeOut();
            $("#supervisorName").prop("required", true);
            $("#email_supervisor").prop("required", true);
            $("#phonenumber_supervisor").prop("required", true);
            
        } else {
            $("#supervisor_div").fadeOut();
            $("#supervisor_div_btn_hide").fadeIn();
            $("#supervisorName").prop("required", false);
            $("#email_supervisor").prop("required", false);
            $("#phonenumber_supervisor").prop("required", false);
        }
    });
});