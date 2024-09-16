### Interface CRUD


****Le flux**** dans les médias sociaux correspond à la liste des messages échangés 

Objectif => Implémenter une interface pour les opérations CRUD de l'utilisateur.
On n'a pas besoin de présenter tous les détails au user tels que les détails sur la bd, 
L'user n'a pas besoin de connaitre la structure des tables.           

On va donc développer des vues spécifiques aux besoins et donner aux users les accès à ces vues.             

Django permet de donner un accès spécifique à un user précis (authentifié) => Il fait de la gestion de droits. 

#### Vue en liste et vue détaillée

**Une vue en liste** affiche une liste de tous les objets d'un modèle avec un minimum de détails, par exemple juste le titre d’une annonce ou juste le nom du groupe ;        
**Une vue détaillée** affiche un objet avec tous ses détails et tous les champs affichés.        

=> Vue en liste:     
Dans le tuto on prend une convention d'appellation. On utilise le format **« <nom du modèle type de vue>.html »**.  
On aura donc _band_list.html_ pour la vue en liste des objets Band.          
Le code du template ressemble à:

```
# listings/templates/listings/band_list.html <= nom du fichier

{% extends 'listings/base.html' %}

{% block content %}

<h1>Groupes</h1>

<ul>
 {% for band in bands %}
  <li>{{ band.name }}</li>
 {% endfor %}
</ul>

{% endblock %}
```

Ce code permet d'afficher uniquement le champ *name* de chaque groupe.   

Le code de la vue ressemble à:
```
# listings/views.py

def band_list(request):  # renommer la fonction de vue
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html',  # pointe vers le nouveau nom de modèle
           {'bands': bands})
```

Le modèle d'URL lui ressemble à:
```
urlpatterns = [
   ...
   path('bands/', views.band_list),  # mise à jour du chemin et de la vue
   ...
]
```

Convention:  
Chaque chemin se termine par un slash (« / »), c'est une convention Django.      

=> Vue détaillée :        
Modèle d'URL:
```
# merchex/urls.py

urlpatterns = [
…
   path('bands/', views.band_list, name='band-list'),
   path('bands/<int:id>/', views.band_detail), # ajouter ce motif sous notre autre motif de groupes
…
]
```







