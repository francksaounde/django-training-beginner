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

*******************************************************************************************

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

***Le modèle par défaut admin***:                 
Quand nous créons le projet par le CLI de django, par défaut il y a création d'un modèle avec le chemin admin/.     
Ce modèle par défaut servira au paramétrage (on en parlera ultérieurement)               
En résumé, lorsqu'une URL correspond à un modèle d'URL, le déroulement passe à l'étape suivante :          
La demande HTTP est transmise à la vue spécifiée.          



                    




















