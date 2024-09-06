# Django training beginner (based on openclassrooms)

### Initialisation du projet         
                
`django-admin startproject stockexchange` => pour initialiser un projet django (nommé ici *stockexchange*)       
Cette commande d'initialisation crée un répertoire pour le projet et à l'intérieur du répertoire il y a 3 éléments:
- un fichier sqlite3 (qui est la bdd par défaut de django)
- un fichier manage.py qui est un utilitaire plus spécifique au projet par rapport à django-admin (qui est plus générique)     
- un répertoire de même nom que le parent *stockexchange* et qui sera notre répertoire de projet *(une sorte de tour de contrôle qui contient des fichiers de configuration pour l'ensemble du projet)*

Par la suite on se déplace dans le projet nouvellement créé en faisant       
`cd .\stockexchange\`      
On peut constater la création des 3 éléments...                 

*Commandes pour le lancement du serveur et l'application des migrations:*               

`python3 .\manage.py runserver` => lance le serveur django  
`python3 .\manage.py migrate`    => pour appliquer à la bdd les migrations générées automatiquement    

L'application de ces migrations nous charge la bdd sqlite3           

`Dans Django, une application est une sous-section du projet entier`         

Ayant le serveur et une bdd, on peut créer une app django, on l'appellera listings (pour indiquer qu'elle gère la liste des marchandises)             
`python3 .\manage.py startapp listings` 

Ensuite on peut ajouter l'application *listings* dans la liste des applications.
Concrètement, il s'agit d'ajouter *listings* dans le fichier **settings.py** du répertoire *stockexchange*.
On ajoute donc la chaine de caractères  *"listings"*  dans la liste (au sens python) *INSTALLED_APPS*                

***Résumé sur l'initialisation***                            
Lorsque nous démarrons un nouveau projet Django, 
- Nous installons la dernière version de Django avec `pip install django`
- Nous générons notre code de de base
- Initialisons notre base de données
- Et démarrons le serveur de développement à l'aide de l'utilitaire de ligne de commande de Django.                 

Nous vérifions que tout fonctionne comme il se doit en naviguant vers le front-end du site à l'adresse `http://127.0.0.1:8000/`

***************************************************************************************************************************************************

### Première vue Django                           
Une vue a pour fonction de répondre à la visite d'un utilisateur sur le site en renvoyant une page que l’utilisateur peut voir.    
Elle prend en paramètre un *objet HttpRequest* et retourne un *objet HttpResponse*.    
- Par convention l'objet HttpRequest est appelé "request" sans précision sur son type. Cet objet contient des attributs utiles liés à la requête de l'user.   
Il sera étudié plus en détail ultérieurement.
- Le contenu de l'objet HttpResponse dépend du type d'application. Dans cette partie du cours, nous mettrons du HTML dans nos réponses.        
Pour mettre en place notre vue, il faut créer un un modèle d'URL et de le lier au code de notre vue.         
La vue associée doit être définie dans views.py de stockexchange.             
Ainsi quand l'user va rechercher l'url le code de la vue associé sera exécuté.          
Le modèle d'url est créé dans le fichier urls.py de notre tour de contrôle stockexchange.   
La variable `urlpatterns` contient la liste des modèles d'url.          
Le modèle d'url est défini grâce à la fonction path qui prend en paramètre un chemin et la vue correspondante à exécuter.      

***Attention***     
Lorsqu'on ajoute un chemin à un modèle d'URL, il ne faut jamais mettre le slash de tête.   
Par exemple dans le cas de notre première vue on a mis `hello/` et non `/hello/`.

Si on inclue un slash (de tête), le modèle d'URL ne sera pas reconnu et la page ne se chargera pas.    
Django affichera un avertissement dans le terminal.

***Le modèle d'url par défaut admin***:                 
Quand nous créons le projet par le CLI de django, par défaut il y a création d'un modèle avec le chemin admin/.     
Ce modèle par défaut servira au paramétrage (on en parlera ultérieurement)               
En résumé, lorsqu'une URL correspond à un modèle d'URL, le déroulement passe à l'étape suivante :          
La demande HTTP est transmise à la vue spécifiée.          

-------------------------------------------------------------------------------------------------------------------------------------------------

### Modèle Django        

Il nous servira à afficher les données dans nos pages.                    
Grâce à l'ORM on passe des classes aux tables de façon implicite.                     

Pour chaque entité pour laquelle nous voulons stocker des données, nous créons un modèle pour représenter cette entité.               
Un modèle définit les caractéristiques que nous voulons stocker à propos d'une entité particulière.         

***Différences modèle et classe***             
Un modèle tout comme une classe permet de définir les caractéristiques des entités.    
En outre, dans les frameworks MVC et MVT en général, un modèle est également capable de stocker (ou de `"persister"`) ses données dans une base de données pour une utilisation ultérieure.     
Cela contraste avec les classes et objets ordinaires, dont les données existent temporairement : par exemple seulement pendant l'exécution de l'application.           
De même, les « caractéristiques » des classes Python sont appelées attributs/propriétés, mais lorsqu'un modèle enregistre un attribut dans la base de données, il s'agit d'un champ.    

Un des avantages de l'utilisation d'un framework comme Django est que toutes les fonctionnalités de persistance des données dans une base de données ont été pré-écrites. Tout ce qui reste à faire au développeur est de faire au modèle hériter de la classe `models.Model` de Django. Le modèle hérite ensuite de toutes les méthodes (comportements) nécessaires pour effectuer des opérations telles que la sélection et l'insertion de données dans une base de données.

***Définition du modèle***    
Les types de données sont préfixés par `models.fields`, par exemple models.fields.CharField qui stocke des données de type caractère/texte/chaîne

Les classes Python ont généralement un constructeur : la méthode `__init__`, où nous utilisons les arguments passés pour définir les valeurs des *attributs d'instance*.            
Avec les modèles Django, les choses se font différemment. Le framework examine les champs du modèle (que nous définissons comme des *attributs de classe*), puis crée le constructeur pour nous.              

*****Quelques rappels:*****    
- clé primaire : un identifiant unique pour chaque ligne de la table.          
- Schéma : structure d'une base de données, en termes de tables et de colonnes

La commande `python manage.py makemigrations` va générer les scripts SQL et la commande `python manage.py migrate` va les exécuter sur notre bdd.               
La commande `makemigrations` scanne le fichier models.py et fait le différentiel entre les deux états: ancien et nouveau,    
puis génère les migrations pour que la bdd soit à jour avec le nouveau modèle.              

****Utilisation du shell django****: Le shell de Django est simplement un shell Python ordinaire qui exécute votre application Django. Il permet d'essayer du code en temps réel.       
Pour ouvrir le shell faire la commande `python manage.py shell`.          
_Nota:_ Le code d'un module/fichier Python peut être exécuté de nombreuses fois tandis que le code tapé dans le shell Django n'est exécuté qu'une seule fois, puis oublié (puisqu'il n'est pas stocké quelque part). Mais ses effets sont bien entendu permanents quand ils sont stockés via la méthode save.           
La méthode `save` permet de stocker l'objet en bdd et par la même occasion de lui attribuer un id; elle est héritée de la classe de base `models.Model` (de Django) dont hérite nos modèles.              

*****Quelques requêtes sur les modèles dans le shell:*****   
On prend l'exemple de la classe _Band_ qui signifie _Groupe_ en français.          
- band = Band.objects.create(name='Foo Fighters')   => crée un objet Band (avec l'attribut name qui vaut _Foo Fighters_) et le stocke dans la bdd        
- band.save()  => stocke l'objet créé en bdd et lui affecte un attribut  (il s'agit d'un objet créé par exemple en faisant band=Band())
- Band.objects.count() => permet d'afficher le nombre d'objets Band stockés en bdd      
- Band.objects.all() => affiche la liste des objets Band existants en bdd (plus précisément il s'agit d'une structure de type QuerySet = sorte de liste Python avec d'autres spécificités)

*****Mise à jour des vues pour afficher les objets des modèles:*****            

Maintenant que les modèles ont été créés et que des instances ont été sauvegardées en bdd, on peut les afficher dans nos pages en passant par les vues.      
On récupère par exemple les instances de bdd comme dit précédemment par : `bands = Band.objects.all()`, puis dans une f-string on peut entre-accolades placer les éléments à afficher.    
Ca donne: `f"""{bands[i].name}"""` pour afficher la valeur du champ _name_ de l'objet d'indice _i_ dans le QuerySet.          
On met ce code dans une vue.               

****Petits éléments à retenir:****      
- Une migration est un ensemble d'instructions qui font passer notre base de données d'un état à un autre, par exemple en créant une nouvelle table. Nous pouvons utiliser le CLI de Django pour générer et exécuter les migrations à notre place.        
- Nous pouvons utiliser le shell de Django pour insérer de nouveaux objets dans notre base de données.
- Dans une vue, nous pouvons récupérer des objets dans la base de données et afficher leurs données dans nos pages.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Gabarit (ou template) Django      
Fichier HTML capable d'interpréter du code Python. Il peut donc recevoir des données depuis le modèle et intégrer des mécanismes comme des boucles.           

************_Rappel sur le design pattern MVT:_************
- Le modèle stocke les données
- La vue joue le rôle d'orchestrateur et récupère les données du modèle à injecter dans le bon template
- Le template se charge de l'affichage

Jusqu'ici le fait de mettre du code HTML dans la vue est un anti-pattern et on le voit bien quand ce code HTML grossit.   
En plus le `principe de responsabilité unique` est violé car la vue gère à la fois la logique (la logique renvoie à ce qui est logique, 
et en ce qui concerne la vue, celle-ci est en relation avec le métier, elle sélectionne tous les objets Band de la base de données) et 
la présentation (l'affichage -des noms des groupes...-).          
Pour résoudre le problème, on va déplacer la partie présentation vers le gabarit.          

*****Création du premier gabarit:*****       
On crée (sous le répertoire de l'application listings) un répertoire de gabarits, qu'on appelle templates. 
Sous ce répertoire templates on crée un répertoire qui porte le nom de l'application ici "listings".       
Cette nomenclature est faite pour éviter les ambiguités. Car pour la recherche de gabarits, django cherche systématiquement dans les répertoires templates.      
Donc ajouter le nom de l'application avant de mettre les fichiers HTML permet bien de faire la différence.               
Ainsi avec deux applications app1 et app2, et des fichiers temp1_app1, temp2_app1 (relatifs à app1), temp1_app2, temp2_app2 (relatifs à app2), on aura les chemins:      
- templates/app1/temp1_app1  et  templates/app1/temp2_app1 pour app1
- templates/app2/temp1_app2 et templates/app2/temp2_app2 pour app2.             
***Et donc, aucune ambiguité possible***!!!

*****Mise à jour de la vue pour la génération du gabarit*****      
Jusqu'ici la vue faisait une génération brute d'objet HttpResponse. Maintenant nous introduisons la méthode `render` qui prend un objet `HttpRequest` (nommé par convention `request`) 
et d'autres arguments et retourne un `HttpResponse`.    
***Rappel définition (technique) d'une vue:***
Une vue est un élément qui prend en entrée un objet de type HttpRequest et retourne un HttpResponse.                   

Paramètres de la méthode render:
- un objet request (de type HttpRequest)
- le chemin vers le template généré
- un dictionnaire contextuel:
Chaque clé du dictionnaire devient une variable que nous pouvons utiliser pour indexer le modèle dans le fichier de gabarits.                    
En effet, `la clé est identifiée à sa valeur`.
Par exemple la définition `{'first_band': bands[0]})` au niveau de la vue, permet d'écrire: `{{ first_band.name }}` au niveau du template.                           
Cette écriture est équivalente à l'écriture Python: `band[0].name` pour indexer le champ name du 1er groupe (indice 0) du QuerySet.              
Les _accolades doubles_ sont utilisées au niveau du gabarit pour injecter des appels au modèle via les variables passées par le dictionnaire contextuel de la vue.

Nota: Dans un code HTML valide, les gabarits de Django peuvent inclure une syntaxe avec des accolades, on l'appelle aussi *****langage de gabarits Django*****. Et 
les variables appelées entre accolades sont appelées aussi *****variables de gabarits*****         
Prenons un deuxième exemple: le dictionnaire `{'cle': bands}` donne lieu dans le gabarit aux appels `{{ cle.i.name }}` avec _i_ l'indice du groupe dans le Queryset.      
```
- {{ cle.0.name }}
- {{ cle.1.name }}
- {{ cle.2.name }}
```
Notons qu'on ne fait pas `cle[i].name` comme en Python, en effet cette dernière écriture génèrerait une erreur.   
On fera donc un appel par notation pointée.     
Dans nos exemples on récupèrera la liste des objets à travers l'écriture `bands=Band.objects.all()` et on définira le dictionnaire `{'bands': bands}`.
Dans cette écriture, la clé _bands_ est une variable muette qui peut être remplacée par n'importe quoi, 
par contre la valeur _bands_ contient bien la liste des objets récupérés précédemment.              


*****Résumé  de cette première partie sur l'introduction aux gabarits*****      
Les gabarits sont un moyen pour définir le contenu d'une page qui ne change pas.      
À l'intérieur de ces gabarits, nous insérons des variables de gabarits, qui servent d'espaces réservés pour le contenu qui change. 
Lorsque nous générons un gabarit dans une vue, nous passons un dictionnaire de contexte au gabarit et les variables de contexte sont injectées dans leurs espaces respectifs.    
En gardant la vue libre de tout code de présentation (HTML), nous pouvons limiter la responsabilité de la vue à une seule chose : 
la logique pour récupérer les données correctes de la base de données, et les injecter dans la page.        

Note sur la logique:
Dans Django le système de gabarits est un outil qui contrôle la présentation et la logique liée à la présentation. La logique fait référence aux 
boucles, embranchements (conditions)

Optimisation dans l'utilisation des listes de modèle dans un gabarit:          
Les boucles et autres instructions logiques sont entourées d'accolades et de signes de pourcentage (`{% ... %}`). Il s'agit de balises de gabarits.     
On a les balises `for`, `endfor`, ... Attention à ne pas mettre les deux points à la fin comme en Python.   
Pour le cas de la balise for, l'espace entre les balises for et endfor peut contenir du texte, du HTML et même des variables de gabarits Django.  
On va proposer une autre écriture du bloc de code:
```
- {{ cle.0.name }}
- {{ cle.1.name }}
- {{ cle.2.name }}
```
En effet, dans la réalité on peut avoir un nombre d'objets dont on ne connait pas le nombre, on peut supprimer certains, etc. Et ce code ne marchera plus.
On utilise la boucle `for` bien adaptée à l'itération sur une liste dont on ne connait pas la longueur à priori.   
```
<ul>
    {% for cle in bands %}
    <li>{{ cle.name }}</li>
    {% endfor %}
</ul>
```
Dans le bout de code ci-dessus on met la balise  `<li>` dans la boucle car on veut qu'elle se répète, tandis que la balise `<ul>` est hors de la boucle, 
car on ne veut pas sa répétition.

*****Filtre de gabarit:*****
- filtre lower (minuscule) ou upper (majuscule)
Ce filtre est utilisé de la façon suivante: `<li>{{ band.name|upper }}</li>` pour afficher en majuscules le nom du groupe.
  
- filtre length:
  Qui filtre la longueur d'une liste et donc d'un objet QuerySet.
  On a donc `{{ bands|length }}` qui affiche le nombre de groupes créés en bdd.

***Utilisation de bloc conditionnel if:***
On peut utiliser if, elif, else comme en python en faisant attention à éviter les deux points (:) de fin.
On a par exemple le code ci-après:
```
<p>
    J'ai..
    {% if bands|length < 5 %}
        peu de
    {% elif bands|length < 10 %}
        quelques
    {% else %}
        beaucoup de
    {% endif %}
        groupes préférés.
</p>
```
Qui affiche  `"J'ai quelques groupes préférés."` si la longueur de la liste vérifie `5 <= bands|length < 10`.

***En résumé***
- Les gabarits sont l'endroit où nous définissons tous les éléments de présentation d'une page ; pour une application web, c'est le HTML.

- La vue peut ainsi se concentrer sur la logique, dont la récupération des données correctes à injecter dans la page.

- Nous injectons des données dans un gabarit à l'aide de variables de gabarits.

- Nous utilisons les balises de gabarits pour les boucles, les embranchements et le formatage dans les gabarits.

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Création/Extraction d'un gabarit de base - Ajout de feuilles de style (CSS) et de fichiers statiques     

***Création de gabarit de base- les balises block et extends***                             
On applique le principe `DRY : Don't Repeat Yourself`: Tout le code HTML qui se répète est factorisé et mis dans des fichiers qu'on appellera "gabarit de base", 
et qu'on incluera dans le code grâce à la syntaxe `{% extends 'chemin-vers-le-gabarit-de-base.html' %}`.    
Ici _chemin-vers-le-template-html_ est l'argument de la balise _extends_. Le mot clé _extends_ est choisi à dessein car fait référence à l'héritage.   
Par ailleur  _chemin-vers-le-template-html_ est donné suivant la convention mentionnée plus haut (tout comme _listings/contact.html_);          
Notons qu'il est mis entre côtes.             

Le code factorisé ressemble à ceci:
```
<html>
    <head><title>Nom-de-l'application</title></head>
    <body>

        {% block content %}{% endblock content %}

    </body>
</html>
```

On met ce code dans un fichier _base.html_ par exemple.
Dans ce code on reconnait bien la structure de base d'un fichier html, à laquelle on a ajouté la ligne avec la balise de gabarit:  `{% block %}` fermée par `{% endblock %}`.               
`content` désigne ici le nom du bloc déclaré, il peut être ommis quand on n'a qu'une seule balise _block_. Notons que _content_ n'est pas mis entre côtes comme l'argument de la balise _extends_.        
La balise _block_ est une zone dans laquelle le code html propre à nos pages sera inséré.
Le principe est celui de l'héritage (d'où le mot clé _extends_). Les gabarits (contact.html, about.html, ...) hériteront du gabarit de base et auront l'apparence suivante:   
```
{% extends ''chemin-vers-le-gabarit-de-base.html'' %}

{% block content %}

<h1>Hello Django !</h1>
...
</ul>

{% endblock %}
```
Les balises `block` encadrent le code de la page. En général il faut enlever tout le html autour de la balise `body` (la balise `body` comprise) et encadrer le code restant 
par les balises  `{% block %}` et `{% endblock %}`.                    

*****Utilisation de fichiers CSS*****                                 
On crée un répertoire _static_ sous le répertoire de l'application (ici _listings_) dans lequel on mettra tout ce qui est supposé être statique durant nos développements, par exemple les fichiers CSS.   
On utilise le même principe de nomenclature que dans les sections précédentes: listings/static/listings/"nom-fichier-statique".    
Une fois le fichier défini on l'introduit par exemple dans le gabarit de base pour qu'il impacte toute l'application.    
Pour un fichier _styles.css_ on a la déclaration suivante:

```
<link rel="stylesheet" href="{% static 'listings/styles.css' %}" />
```
Où _static_ indique le répertoire qui contient le fichier _'listings/styles.css'_; en d'autres termes le chemin peut s'écrire aussi:  _'static/listings/styles.css'_.           
Pour que ça fonctionne, il reste un dernier détail, il faut ajouter la ligne `{% load static %}` en début du fichier gabarit de base (en dessous du DOCTYPE s'il y en a un ).
Cette instruction _load_ permet de _"charger la balise". Il faut penser aussi à relancer le serveur après la modification des fichiers statiques.

             
*****Petite conclusion sur Django et l'architecture MVT*****             
Chaque élément de MVT a sa place : les modèles, les vues, les gabarits et même les modèles d'URL sont tous séparés dans leurs propres fichiers.

Django est un framework monolithique. Il fournit des moteurs pour toutes les parties de l'application : moteur de gabarits pour la présentation, l'ORM pour la persistance, etc. 
Si l'on veut changer une de ces parties, il est peut-être préférable de construire une architecture MVC/T à partir des éléments de notre choix, comme Flask, SQLAlchemy, etc.

MVC/T est un style d'architecture parmi d’autres. Il est très adapté aux applications CRUD simples. Mais pour les solutions d'entreprise, on peut regarder des alternatives comme Clean Architecture.     

**********_Bonus: Le rendu côté serveur et côté client_**********                         
Le rendu côté serveur est la manière « ancienne » de générer le contenu HTML d'une page web, où chaque chargement de page implique un aller-retour relativement lent vers le serveur.
Aujourd'hui, il existe de nombreux frameworks permettant de créer des applications front-end riches dans le navigateur, 
où le HTML est généré côté client et où seule une quantité minimale de données est envoyée entre le navigateur et le serveur, ce qui donne des applications rapides comme l'éclair.
                            
Mais cela ne signifie pas que vous devez ignorer le rendu côté serveur ! C'est un bon point de départ. Et pour de nombreuses applications, 
le rendu côté serveur est une solution adéquate. Elle est simple à comprendre. Elle réduit la complexité de l'application car elle ne nécessite pas de construire une API REST. 
Et votre application peut tenir dans un seul repository, car il n'est pas nécessaire d'avoir une application frontale JavaScript distincte. 
C'est pourquoi le rendu côté serveur avec Django est idéal pour les applications de démonstration et les applications à l’interface simple.

Si les besoins de votre application évoluent par la suite, vous pouvez convertir votre projet Django et son rendu côté serveur en une API REST à l'aide du cadre Django REST.

Quelques éléments qui ressortent du quizz:     
- La balise `{% now "Y" %}` permet d'extraire l'année en cours
- Quand on fait une modification au niveau du modèle il faut toujours générer les migrations et les exécuter sinon l'appel génèrera une erreur
- Pour quitter le shell django on peut faire le classique `exit()` ou bien `Ctrl-D` (cette dernière ne marche pas pendant mes tests, peut-être ça vaut pour un Mac?)
- Pour avoir de l'aide sur les commandes _manage.py_ on peut faire `./manage.py help nom-commande` exemple `./manage.py help check`

----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

### Modèles et champs, gestion des données       

*****Types de données et arguments*****            
Django nous propose nativement plusieurs types, en voici quelques uns:            
- `models.fields.CharField(max_length=100)`  pour une chaine de caractères de longueur max égale à 100.
L'argument (ou option de champ) `max_length` est obligatoire sinon une erreur sera générée. 
-  `models.fields.IntegerField()` pour un nombre entier, par exemple pour déclarer une année (quand on n'a pas besoin du mois et du jour)
-  `models.fields.BooleanField()` pour une valeur booléenne (comme dans les cas classiques _True_ ou _False_) 
-  `models.fields.URLField()` pour une URL (exemple l'url de la page d'accueil d'un site?)

  Pour la date, on passe en argument une contrainte de type liste de validateurs à l'option `validators` pour encadrer la date 
  entre un minimum (instance de la classe `MinValueValidator`) et un maximum (instance de `MaxValueValidator`).          
  Les 2 classes de validators (`MinValueValidator` et `MaxValueValidator`) sont importées de `django.core.validators`.          

*****_Valeurs par défaut_*****:                
- `default`: pour un booléen par exemple
- `blank = True` dans le cadre des formulaires, indique que le champ du formulaire associé peut être soumis vide (zone de texte vide par exemple)
- `null = True` permet d'indiquer que le champ peut ne pas être renseigné en bdd; pour de tels champs on n'a pas en s'en faire s'il existe déjà des
enregistrements en bdd: la migration ne posera aucun souci. En effet, le champ en bdd peut avoir la valeur NULL.

*****Nota:*****     
a) Quand on ajoute un nouveau champ dans une bdd qui possède déjà des enregistrements il faut faire attention aux valeurs par défaut.
Si la valeur par défaut n'est pas valide, la migration génèrera une erreur.
Et dans le cas d'une valeur par défaut non valide, Django propose 2 options: fournir nous-mêmes une valeur par défaut (_Provide a one-off default now_),
sinon le laisser proposer la valeur par défaut qu'il veut... Une fois les migrations générées, les appliquer par `python manage.py migrate`

b) Quand on instancie un modèle les champs pour lesquels on n'a pas renseigné la valeur prennent:
- la valeur par défaut du champ si c'est un champ natif (exemple _chaîne de caractères vide_ pour un _Charfield_)
- la valeur `None` pour les autres, et *****la valeur None correspond à une valeur NULL en bdd*****.               
Par exemple l'année (qui est de type IntegerField) est à None si on instancie sans donner de valeur (`band = Band()`).             
Du coup si on fait ` band.save()`, dans le _shell_ on a une erreur liée à une contrainte d'intégrité. 


*****_Un type un peu sophistiqué: la liste de choix_*****         
Une classe qui définit une liste de choix hérite de `models.TextChoices`. 
Pour chaque choix de la liste, on ajoute une constante (donc en majuscules) qu'on associe avec une clé qui est (dans notre cas) une abréviation de la constante.   
Par exemple:

```
class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'
```

Dans notre cas pratique on nous a aussi présenté le concept de _classe imbriquée_ avec Django: une classe définie dans une autre avec laquelle très étroitement liée.        
Une fois la classe `Genre` définie, on peut déclarer un champ du modèle du type `Genre`, pour limiter la valeur du champ aux choix définis.
Ca donne: `genre = models.fields.CharField(choices=Genre.choices, max_length=5)`. En tant que champ de type `CharField`, il faut préciser la longueur maximale de la clé
d'où l'argument `max_length`. Ici on a des clés de deux caractères mais on préfère être large et réserver 5 caractères.                          

Nota: Django nomme ses tables au format _"nom-application underscore nom-modèle"_, par exemple: _listings_band_ pour désigner le modèle Band.

*****Petit résumé (qui reprend plein de choses déjà dites plus haut)*****    
- Django est livré avec différents types de champs qui correspondent à différents types de données, comme CharField ou IntegerField . 
Il existe aussi des champs plus spécifiques qui vont contraindre l'entrée, comme URLField .

- Nous pouvons définir des contraintes et des règles pour les champs en leur attribuant des options, comme max_length , null et choices .
- Nous pouvons affiner davantage les contraintes sur les champs en spécifiant des validateurs sur les champs en utilisant l'option validators .
- Lorsque nous ajoutons de nouveaux champs à un modèle, nous devons effectuer une migration pour ajouter de nouvelles colonnes à la base de données, avant de pouvoir commencer à les utiliser.
- Si nous ajoutons des champs non nuls à un modèle, nous serons invités à leur fournir une valeur par défaut initiale lors de la migration.

  -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

   ### CRUD et Administration Django

  On commence par créer un utilisateur admin par la commande: `python manage.py createsuperuser`.
  Pour ce user l'email n'est pas obligatoire, mais il est conseillé de renseigner un password pour pouvoir se connecter par la suite.

  => on déclare dans le fichier `admin.py` qu'on veut gérer le modèle en spécifique dans le site d'administration de Django.
C'est fait via la commande: `admin.site.register(Band)`, *Band* désigne le nom du modèle.
L'utilisation de ce site d'admin permet de bien comprendre ce que signifie `blank=True`.
Pour consulter un modèle particulier enregistré sur le site d'admin par la commande précédente, on accède à l'url:
`http://127.0.0.1:8000/admin/listings/band/ ` ou plus généralement `http://127.0.0.1:8000/admin/<nom-application>/<nom-du-modèle>/ `
  
Le site d'administration est une interface back-end prévue pour les devs mais surtout les admins, pour effectuer facilement des tests et 
les interfaces CRUD. Pour les end-users il faudra souvent faire des personnalisés de formulaires.

  
                    




















