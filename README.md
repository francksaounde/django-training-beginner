**Initialisation du projet** 
                
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

**Première vue Django**                    
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

***Modèle Django***

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

La commande `python manage.py makemigrations` va générer les scripts SQL et la commande `python manage.py migrate` va les exécuter sur notre bdd       

****Utilisation du shell django****: Le shell de Django est simplement un shell Python ordinaire qui exécute votre application Django. Il permet d'essayer du code en temps réel.       
Pour ouvrir le shell faire la commande `python manage.py shell`.          
_Nota:_ Le code d'un module/fichier Python peut être exécuté de nombreuses fois tandis que le code tapé dans le shell Django n'est exécuté qu'une seule fois, puis oublié (puisqu'il n'est pas stocké quelque part). Mais ses effets sont bien entendu permanents quand ils sont stockés via la méthode save.           
La méthode `save` permet de stocker l'objet en bdd et par la même occasion de lui attribuer un id.           

*****Quelques requêtes sur les modèles dans le shell:*****   
On prend l'exemple de la classe _Band_ qui signifie _Groupe_ en français.          
- band = Band.objects.create(name='Foo Fighters')   => crée un objet Band avec l'attribut name qui vaut _Foo Fighters_
- band.save()  => stocke l'objet créé en bdd et lui affecte un attribut
- Band.objects.count() => permet d'afficher le nombre d'objets Band créés
- Band.objects.all() => affiche la liste des objets Band existants (plus précisément il s'agit d'un QuerySet = sorte de liste Python avec d'autres spécificités)
  
                    




















