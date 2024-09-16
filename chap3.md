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

**=> Vue en liste:**     
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

def band_list(request): 
   bands = Band.objects.all()
   return render(request,
           'listings/band_list.html', 
           {'bands': bands})
```

Le modèle d'URL lui ressemble à:
```
urlpatterns = [
   ...
   path('bands/', views.band_list),
   ...
]
```

Convention:  
Chaque chemin se termine par un slash (« / »), c'est une convention Django.      

**=> Vue détaillée:**                  
Modèle d'URL:
```
# merchex/urls.py

urlpatterns = [
…
   path('bands/', views.band_list, name='band-list'),
   path('bands/<int:band_id>/', views.band_detail),     
…
]
```
J'ai noté band_id au lieu de id pour éviter la confusion avec la fonction intégrée id de Python
**int** est le type de données que nous nous attendons à recevoir : un entier.


Vue:
```
# listings/views.py

...

def band_detail(request, band_id):
  band = Band.objects.get(id=band_id)  # nous insérons cette ligne pour obtenir le Band avec cet id
  return render(request,
          'listings/band_detail.html',
          {'band': band}) 
...
```

Template:          

Django met à notre disposition la méthode **get_genre_display** (à la place de **genre**) pour convertir les valeurs de la base de données **genre** (par exemple HH ) dans leur format d'affichage (par exemple Hip Hop ).                      
On utilise également le filtre de gabarit **yesno** sur le champ *active*, pour convertir *« True »* en *« Yes »* (et False en No).        
**official_homepage** peut être vide (c'est un champ nullable), donc nous devons d'abord vérifier qu'il existe avec une instruction if.
```
# listings/templates/listings/band_detail.html

{% extends 'listings/base.html' %}

{% block content %}

<h2>{{ band.name }}</h2>

<ul>
 <li>Genre : {{ band.get_genre_display }}</li>
 <li>Année de formation : {{ band.year_formed }}</li>
 <li>Actif : {{ band.active|yesno }}</li>
 {% if band.official_homepage %}
 <li><a href="{{ band.official_homepage }}"> {{ band.official_homepage }}</a></li>
 {% endif %}
 </ul>

<p>{{ band.biography }}</p>

{% endblock %}
```

#### Liaison vue en liste et vue détaillée      
Cela consiste par exemple à mettre à jour le modèle de la vue en liste, afin que chaque nom de groupe devienne 
un lien cliquable qui amène à la vue détaillée de ce groupe.  
A ce moment entre en jeu les *noms* des modèles d'URL via l'argument **name** (auquel on donne par exemple la valeur band-detail).
Le modèle d'url devient:     
```
# merchex/urls.py 

path('bands/<int:id>/', views.band_detail, name='band-detail')
```
Et le gabarit:   
```
# listings/templates/listings/band_list.html
…
  <li><a href="{% url 'band-detail' band.id %}">{{ band.name }}</a></li>
…
```
De même la vue détaillée du groupe doit comporter un lien vers la liste des groupes :      
On obtient.            
=> modèle d'URL            
```
# merchex/urls.py
   path('bands/', views.band_list, name='band-list'),
```

=> template                  
```
# listings/templates/listings/band_detail.html

   <p>{{ band.biography }}</p>

   <a href="{% url 'band-list' %}">Retour à tous les groupes</a>

{% endblock %}
```

**Astuce ManyToOne OneToMany:**      
A titre de rappel, un groupe peut être lié à plusieurs annonces mais une annonce concerne un seul groupe.     

Pour faire référence au groupe d'une annonce on fait simplement: `listing.band` (le champ band étant dans la définition du modèle listing).      

Inversément, on peut faire référence à la liste des annonces d'un groupe grâce à **listing_set** qui renvoie un set de listings (littéralement),      
et en pointant sur all, on les prend tous. Ca donne donc: `band.listing_set.all` et dans le cas d'une boucle avec balise de gabarit on fera:   
`{% for listing in band.listing_set.all %}`.    

















