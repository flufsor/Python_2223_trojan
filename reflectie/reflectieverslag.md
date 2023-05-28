# Reflectieverslag Trojan agent worker
*Tom Goedemé* / 2CSC2

## Security opmerking
Omdat de trojan een bepaalde rechten nodig heeft op github is de token niet ingevuld in code op de repository.
De apitoken is meegeleverd met de zip van dit project in het token bestand, dit bestand is niet meegeleverd in de repository.


## Inleiding
Dit semester hebben we een project gedaan waarbij we een trojan moesten maken in python.
Deze trojan moest een aantal functies hebben en deze moesten in modules worden opgedeeld.
Deze modules moesten dan dynamisch kunnen worden gedownload en uitgevoerd.
De modules repository is [Modules repo](https://github.com/flufsor/Python_2223_trojan_modules)

## Functies
De Trojan agent worker heeft de volgende functies:
- Dynamisch modules downloaden en uitvoeren
- Per host modules
- Achtergrondafbeelding veranderen
- Ransomware simulatie met een folder te scannen en deze bestanden te encrypteren als ook een ransomnote achterlaten
- Screenshots nemen
- Sshkey's zoeken en stelen

## Trojan
De trojan zal op regelmatige tijd de gitrepository polsen op een nieuwe revisie van de modules. Indien er een nieuwe revisie is zal deze gedownload worden en indien nodig gestart worden. De modules kunnen door per host ingesteld worden, dit wordt per hostname gedefinieerd in de "config.json" file die ook in de repository zit.

Er zal bij het starten van de trojan een host object worden gemaakt dat details bevat van de host die de trojan draaid, hiermee kan er dynamisch bepaald worden hoe modules bepaalde acties moeten ondernemen afhankelijk van bijvoorbeeld het besturingssysteem.

De data die tijdens het draaien van de trojan wordt gegenereerd zal in een json object per host worden opgeslagen in de data folder in de repository. De data van vorige scans zal elke keer worden geappend aan het json object en dan opnieuw worden opgeslagen met de bijkomende data.

## Modules

### Achtergrondafbeelding veranderen
Deze module zal de achtergrondafbeelding van de host veranderen naar een afbeelding die wordt gedownload, deze url is een variablen in de module en dus eenvoudig te veranderen.

Omdat het veranderen van de achtergrondafbeelding anders werkt per besturingssysteem is er een functie die de juiste commando's zal uitvoeren afhankelijk van het besturingssysteem.

Bij het loggen van de module zullen we de status raporteren van het veranderen van de achtergrondafbeelding.

### Ransomware simulatie
Voor deze module is er een folder die wordt gescand op bestanden die worden geencrypteerd, er wordt een voorbeeldfolder meegeleverd met een aantal bestanden die worden geencrypteerd. De folder die wordt gescand is een variablen in de module en dus eenvoudig te veranderen.

De encryptie gebeurd met een meegeleverde publieke sleutel die mee in de repository zit, de private sleutel is niet meegeleverd en dus kan de encryptie niet ongedaan worden gemaakt.

Bij het loggen van de module zal er gerapporteerd worden welke bestanden er geencrypteerd zijn als ook het aantal bestanden.
De module verwijdert de originele bestanden niet, dit is voor simulatie doeleinden.

### Screenshots nemen
Deze module zal screenshots nemen van de host, deze screenshots worden in de data folder opgeslagen.
De screenshosts worden opgeslagen als PNG-bestanden met een lichte compressie, de bestandsnaam is een samenstelling van de hostname en een timestamp.

Bij het loggen van de module zal de screenshot worden opgeslaan en zal de bestandsnaam en de timestamp worden gerapporteerd.

### Sshkey's zoeken en stelen
De module zal zoeken naar sshkey paren en deze bij het loggen van de functie opslaan in het data json object.
Er zal bij het opslaan van de sshkey's gekeken worden of de key al in het json object zit, indien dit het geval is zal de key niet worden toegevoegd.

## Ervaren problemen
Het moeilijkste van het project vond ik het feit dat het opdelen van dit project.
Hiermee bedoel ik dan niet enkel hoe ik de trojan en de modules van elkaar ga scheiden, maar ook hoe ik dit best in 1 repository ga steken.

Voor het oplossen van het probleem van alles in 1 repo te forceren heb ik voor 2 repo's gegaan.
- Deze repo bevat de trojan en het reflectieverslag
- [Modules repo](https://github.com/flufsor/Python_2223_trojan_modules)

Om de git repository voor de modules te kunnen laten pushen is er een wachtwoord.
Maar omdat dit ook mijn persoonlijke github account is, wil ik dit niet in de repository steken.
Hiervoor een oplossing zoeken was niet eenvoudig, maar uiteindelijk heb ik een oplossing gevonden waar ik me het meest kan achter zetten.
De oplossing is om de apitoken mee te leveren met de zip van het project, dit is niet ideaal, maar het is de beste oplossing die ik heb gevonden.