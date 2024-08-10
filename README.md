**Initialisation du projet** 
                
`django-admin startproject stockexchange` => pour initialiser un projet django (nommé ici *stockexchange*)       
Cette commande d'initialisation crée le projet et à l'intérieur du répertoire il y a 3 éléments:
- un fichier sqlite3 (qui est la bdd par défaut de django)
- un fichier manage.py qui sera très utile par la suite
- un répertoire de même nom que le parent *stockexchange* et qui sera notre app de base ?? (l'app principale?) 

Par la suite on se déplace dans le projet nouvellement créé en faisant       
`cd .\stockexchange\`      
On peut constater la création des 3 éléments

`python3 .\manage.py runserver` => lance le serveur django  
`python3 .\manage.py migrate`    => pour appliquer les migrations générées automatiquement

L'application de ces migrations nous charge la bdd sqlite3 

Ayant le serveur et une bdd, on peut créer une app django, on l'appellera listings
`python3 .\manage.py startapp listings` 

Ensuite on peut ajouter l'application *listings* dans la liste des applications
Concrètement, il s'agit d'ajouter *listings* dans le fichier **settings.py** du répertoire *stockexchange*
