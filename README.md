# Prototype-django

Dit project is een Django-webapplicatie waarmee geregistreerde gebruikers artikelen kunnen maken, bekijken en beheren. Het project maakt gebruik van het Django-framework en heeft basisfunctionaliteiten zoals gebruikersauthenticatie, artikelbeheer en een administratief dashboard.

Naast deze basisfunctionaliteiten biedt de applicatie ook een gebruikersactiviteitstijdlijn en een statistiekenpagina waar gebruikers hun artikelstatistieken kunnen bekijken, zoals het aantal gemaakte artikelen en ontvangen likes.


## Projectstructuur

De applicatie bestaat uit een enkele app, articles, die de functionaliteiten voor artikelbeheer biedt. Binnen de articles app worden verschillende modellen, views, forms en templates gebruikt om de gebruiker een volledige ervaring te bieden.

 **Belangrijke componenten**:

- Models: De Article, Comment, en UserActivity modellen worden gebruikt voor het opslaan van artikelen, reacties en gebruikersactiviteiten.
- Views: Function-based views (FBVs) voor het beheren van artikelen, zoals toevoegen, bewerken, en verwijderen van artikelen.
- Templates: HTML-pagina's die worden gerenderd voor elke view, met de nadruk op het weergeven van artikelen, het weergeven van een tijdlijn, en het tonen van statistieken.
- Statistieken en grafieken: Een statistiekenpagina die gebruikersinformatie visualiseert met behulp van Chart.js.

### Functionaliteiten

 **Gebruikersauthenticatie**:
-  Inloggen en registreren van gebruikers.
-  Alleen geregistreerde gebruikers kunnen artikelen toevoegen, bewerken en verwijderen.

 **Artikelen**:
- Toevoegen, bewerken en verwijderen van artikelen door de auteur.
- Overzicht van alle artikelen in een bibliotheek.
- Mogelijkheid om artikelen te liken.
- Bekijken van artikelgegevens via een detailpagina.

 **Activiteitenlogboek (Tijdlijn)**: 
 - De tijdlijn toont gebruikersactiviteiten zoals aangemaakte artikelen en het aantal ontvangen likes.
 - Dit biedt gebruikers inzicht in hun activiteit binnen de applicatie.

**Statistieken:**: 
 - Gebruikers kunnen hun persoonlijke statistieken bekijken, zoals het totaal aantal aangemaakte artikelen, het totaal aantal ontvangen likes en het populairste artikel.
 - De statistieken worden visueel weergegeven met behulp van Chart.js voor een overzichtelijke en intuïtieve gebruikerservaring.

 **Admin Interface:**
 - Beheerders kunnen via de Django admin-interface artikelen en gebruikers beheren.

 ### Sources
- Django Framework Documentatie(https://docs.djangoproject.com/en/5.1/) : voor gedetailleerde uitleg over modellen, views, templates, gebruikersauthenticatie, en hoe je applicaties 
  kunt structureren.
- W3Schools(https://www.w3schools.com/django/index.php): voor de syntax en basics van Django te leren
- charts.js(https://www.ag-grid.com/charts/?gad_source=1&gclid=Cj0KCQjwgrO4BhC2ARIsAKQ7zUlR7-D2SrCtn_b_7I07pC4OjuszOr4dUL2136PaqpcKgREfYyPgxqsaAthlEALw_wcB): toevoeging van grafieken 
  bij de statistieken.
- __str__ method(https://www.educative.io/answers/what-is-the-str-method-in-python): uitleg over deze methode en waarom deze relevant is.
- Stack Overflow(https://stackoverflow.com/questions/70226396/get-data-from-django-database) : vragen over data,views,...
- W3Schools(https://stackoverflow.com/questions/70226396/get-data-from-django-database) : deployment voor django met AWS Elastic Beanstalk(outdated)
