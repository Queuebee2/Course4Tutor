# Project overzicht

## Deadlines
- onderzoeksverslag 1 week na tutor op **11 juni** (zelfde dag als IPV)
- applicatie en technische documentatie op **14 juni**


## Uitleg over Azure
We gebruiken Azure om de site te runnen. Je komt op de Azure pagina door portal.azure.com in je search balk typen.
1. Ga dan naar *Dashboard*.
2. Klik op *hannl-hlo-bi1a1-app*. (Dit is de applicatie van klas 1 groep 1)
3. In het *Deployment Center*  kan je de repo zien die op dat moment wordt gebruikt.

## Overig
De file die je door middel van Azure wil runnen moet *App.py* heten.

## Uitleg over Jinja
Door middel van Jinja kan je zelf makkelijk een template maken.
Bij Jinja kan je elementen uit een bestaand html file gebruiken voor andere html files.
Dit kan door bijvoorbeeld
```Jinja
# maak een block die je ook op een andere html file wil gebruiken
{% block content %} 
{% endblock %}
# met endblock sluit je het block

# om dit block uit "eenhoorn.html" te gebruiken
# in je andere file
{% extends "eenhoorn.html" %}

# Als je niks wil overwriten, dan is denk ik include handiger
# Met extend kan je blocken vervangen
```

Voor meer uitleg verwijs ik onder andere naar de site:
- [Flask uitleg](https://flask-navigation.readthedocs.io/en/latest/)
