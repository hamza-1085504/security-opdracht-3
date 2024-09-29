# Accessibility Hub API

Voor het toevoegen van onderzoeken en organisaties hebben wij gewerkt met een API, hieronder zal ik uitleggen hoe de API kan bereiken en hoe dit werkt.

# Installatie Postman

De makkelijkste manier om de API te bereiken is door Postman te gebruiken dat kan op de volgende website: https://www.postman.com/downloads/ <br/>
Als je de tootl hebt gedownload kan je deze gaan gebruiken.

# Organisatie aanmaken

Om een organisatie aan te maken ga je naar de volgende URL: ```http://127.0.0.1:8000/organisaties/register/``` en zet de methode op ```POST``` <br/>
Ga naar het tabje ```Body``` en klik hier op ```raw``` <br/>
Gebruik nu het volgende format: <br/>
```
{
    "bedrijfsnaam": "",
    "email": "",
    "password": "",
    "first_name": "",
    "last_name": ""
}
```
Vul de lege haakjes in met de gewenste gegevens en klik daarna op ```Send``` <br/>
Bij response zie je nu de response van de applicatie en als alles goed is ingevuld kan je bij het medewerkers portal de organisatie zien. <br/>

<b>Tip: Vul een eigen e-mailadres in dan kan je de e-mail functie testen als je de organisatie goedkeurt of afkeurt ook bij het keuren van een onderzoek krijg je een mailtje in je inbox.</b>

# Onderzoek aanmaken

Om een onderzoek aan te maken ga je naar de volgende URL: ```http://127.0.0.1:8000/organisaties/onderzoek/``` en zet de methode op ```POST``` <br/>
Ga naar het tabje ```Body``` en klik hier op ```raw``` <br/>
Gebruik nu het volgende format: <br/>
```
{
    "titel": "",
    "beschikbaar": ,
    "beschrijving": "",
    "startdatum": "",
    "einddatum": "",
    "type_onderzoek": "",
    "locatie": "",
    "met_beloning": ,
    "doelgroep_leeftijd_van": ,
    "doelgroep_leeftijd_tot": ,
    "doelgroep_beperking": "",
    "token": ""
}
```
Vul de lege haakjes in met de gewenste gegevens en klik daarna op ```Send``` <br/>
Bij response zie je nu de response van de applicatie en als alles goed is ingevuld kan je bij het medewerkers portal het onderzoek zien. <br/>

# Vraag aanmaken

Om een vraag toe te voegen aan een onderzoek ga je naar de volgende URL: ```http://127.0.0.1:8000/organisaties/vraag/``` en zet de methode op ```POST``` <br/>
Ga naar het tabje ```Body``` en klik hier op ```raw``` <br/>
Gebruik nu het volgende format: <br/>
```
{
    "vraagtitel": "",
    "categorie": "",
    "beschrijving": "",
    "onderzoek_titel": "",
    "token": ""
}
```
Vul de lege haakjes in met de gewenste gegevens en klik daarna op ```Send``` <br/>
Bij response zie je nu de response van de applicatie en als alles goed is ingevuld kan je bij het medewerkers portal het onderzoek aanklikken en de vraag zien die is toegevoegd aan het onderzoek. <br/>
