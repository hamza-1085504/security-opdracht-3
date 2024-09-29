$(document).ready(function() {
    var deskundigeIds = []; // Lijst van deskundige die toegevoegd zijn om te checken dat hij ze niet nog een keer toevoegd.

    function getRecentErvaringsdeskundigen() {
        $.ajax({
            // standaard ajax procedure
            url: '/medewerkers/get_deskundige_in_behandeling_ajax',
            type: 'GET',
            dataType: 'json',
            success: function(data) {
                $.each(data.ervaringsdeskundigen, function(index, ervaringsdeskundige){
                    if (ervaringsdeskundige.account_status === 0) { // Alleen account_status 0 (in behandeling)
                        // Controleer of de deskundige al is toegevoegd aan de tabel
                        if (!deskundigeIds.includes(ervaringsdeskundige.deskundige_id)) {
                            var row = '<tr class="clickable-row" data-href="/medewerkers/ervaringsdeskundige/' + ervaringsdeskundige.deskundige_id + '">' +
                                          '<td>' + ervaringsdeskundige.voornaam + ' ' + ervaringsdeskundige.achternaam + '</td>' +
                                          '<td>' + ervaringsdeskundige.geboortedatum + '</td>' +
                                          '<td>' + ervaringsdeskundige.email + '</td>' +
                                          '<td>' + ervaringsdeskundige.telefoonnummer + '</td>' +
                                          '<td>' + ervaringsdeskundige.soort_beperking + '</td>' +
                                          '<td>' + getStatus(ervaringsdeskundige.account_status) + '</td>' +
                                          '<td>' + ervaringsdeskundige.created_at + '</td>' +
                                      '</tr>';
                            $('#recent-ervaringsdeskundigen-table').append(row); // Voeg de rij toe aan de tabel
                            deskundigeIds.push(ervaringsdeskundige.deskundige_id); // Voeg de ID toe aan de lijst
                        }
                    }
                });
            },
            error: function(xhr, status, error) {
                console.error('Probleem met het ophalen: ', error);
            }
        });
    }

    function getStatus(statusCode) {
        if (statusCode === 0) {
            return 'In behandeling';
        } else if (statusCode === 1) {
            return 'Goedgekeurd';
        } else {
            return 'Afgekeurd';
        }
    }

    getRecentErvaringsdeskundigen();
    setInterval(getRecentErvaringsdeskundigen, 1000); // Herhaal het ophalen elke 1000 ms (1 seconde)
});
