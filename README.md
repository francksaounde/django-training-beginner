**Initialisation du projet** 
                
`django-admin startproject stockexchange` => pour initialiser un projet django (nommé ici *stockexchange*)       
Cette commande d'initialisation crée le projet et à l'intérieur du répertoire il y a 3 éléments:
- un fichier sqlite3 (qui est la bdd par défaut de django)
- un fichier manage.py qui est un utilitaire plus spécifique au projet par rapport à django-admin qui lui est plus générique     
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
On ajoute donc la chaine de caractères  *"listings"*  dans la liste python *INSTALLED_APPS*                

***En résumé***                            
Lorsque nous démarrons un nouveau projet Django, 
- Nous installons la dernière version de Django avec `pip install django`
- Nous générons notre code de de base
- Initialisons notre base de données
- Et démarrons le serveur de développement à l'aide de l'utilitaire de ligne de commande de Django.                 

Nous vérifions que tout fonctionne comme il se doit en naviguant vers le front-end du site à l'adresse `http://127.0.0.1:8000/`
