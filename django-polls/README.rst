======
polls
======

Polls est une appl de Django base sur le web polls. pour chaque question 
visiteurs peuvent choisir une seule reponse

demarrage rapide 
----------------
1. Ajouter "polls" de ton INSTALLED_APP settings.py comme ça::
    INSTALLED_APP = [
        ......,
        "polls"
    ]

2. Include URLconf de polls dans ton projet a l'interieur urls.py comme::
    path("polls/", include("polls.urls"))

3. lancer la commande ``python manage.py migrate)``  pour créer models de polls
4. demarrer le serveur de développement et visité http://127.0.0.1:8000/admin/
    poor les models de poll
5. visité http://127.0.0.1:8000/polls/ 