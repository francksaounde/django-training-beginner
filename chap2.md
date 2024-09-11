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

On a par exemple la définition suivante:      
```
# listings/models.py  (d'après le cours d'origine cette ligne indique le chemin vers le fichier courant)

from django.core.validators import MaxValueValidator, MinValueValidator
...
    class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    genre = models.fields.CharField(max_length=50)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField(
      validators=[MinValueValidator(1900), MaxValueValidator(2021)]
      )
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True)
```

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
  Pour ce user l'email n'est pas obligatoire, mais il est conseillé de renseigner un password pour pouvoir se connecter par la suite à `http://127.0.0.1:8000/admin/`.      

  => on déclare dans le fichier `admin.py` qu'on veut gérer le modèle en spécifique dans le site d'administration de Django.
C'est fait via la commande: `admin.site.register(Band)`, *Band* désigne le nom du modèle.
L'utilisation de ce site d'admin permet de bien comprendre ce que signifie `blank=True`.
Pour consulter un modèle particulier enregistré sur le site d'admin par la commande précédente, on accède à l'url:
`http://127.0.0.1:8000/admin/listings/band/ ` ou plus généralement `http://127.0.0.1:8000/admin/<nom-application>/<nom-du-modèle>/ `
                                         
Le site d'administration est une interface back-end prévue pour les devs mais surtout les admins, pour effectuer facilement des tests et 
les opérations CRUD (donc sans passer par le shell Django notamment). Pour les end-users ce sera une interface front-end et il faudra souvent faire des personnalisés de formulaires.

=> Petite personnalisation qu'on peut faire pour un modèle:           
Le bout de code ci-après (ajouté dans models.py) permet d'afficher les noms des modèles(ici Band) dans la vue en liste de l'interface d'administration:           
```
class Band(models.Model):
   def __str__(self):
    return f'{self.name}'
```
Pour avoir plus de détail, on peut afficher plus de colonnes dans la vue en liste (de l'interface d'admin).  
Pour cela il suffit d'ajouter dans `admin.py` une classe qui hérite de `admin.ModelAdmin` et qui définit l'attribut de classe variable `list_display`.
Cette classe qui hérite de `admin.ModelAdmin` est souvent notée <nom-du-modèle>-suivi-de-Admin, ça nous donne par exemple: `BandAdmin` pour la classe Band.      
`list_display` est un tuple formé des noms des champs du modèle qu'on veut voir affichés dans la vue en liste (de l'interface d'admin).       
Après la définition de la classe on l'enregistre sur le site d'administration par convention avec le modèle dont elle gère l'affichage.      
On a donc la définition suivante:
```
class BandAdmin(admin.ModelAdmin):
list_display = ('name', 'year_formed', 'genre') # liste les champs que nous voulons sur l'affichage de la liste

admin.site.register(Band, BandAdmin) 
```

### Relation Many-to-one, One-to-Many avec champ ForeignKey (clé étrangère)
Il s'agit simplement des relations de type un-à-plusieurs de la modélisation des données.
Considérons le cas où un article ne peut pas être lié à la fois à deux groupes (Band) différents.
On a donc une relation 1 à plusieurs et la clé du groupe va migrer vers l'article. L'ajout de cette clé dans la table article (annonce) se fait par la ligne:   
```
class Listing(models.Model):
   band = models.ForeignKey(Band, null=True, on_delete=models.SET_NULL)
```
Cette référence permet d'obtenir par des requêtes le groupe de d'importe quelle annonce (ou article) en faisant `listing.band`.    
On passe trois arguments à `ForeignKey`:
- le modèle auquel on veut se rattacher: `Band`;
- `null=True`: signifie que le groupe n'existe pas (autrement dit, il n'ya pas de  groupe associé) => cela permet de créer les annonces(articles) même si elles ne sont pas directement liées à un groupe;
-  L'argument `on_delete` signifie que le groupe associé est supprimé => cela permet de définir la stratégie à suivre lorsque les objets `Band` sont supprimés.
 Il existe de multiples options pour cela, par exemple:           
- définir le champ band comme ****null**** en utilisant `models.SET_NULL`,
- définir le champ band à sa ****valeur par défaut**** en utilisant `models.SET_DEFAULT`,
- ****supprimer**** l'objet Listing en utilisant `models.CASCADE`,
- et d'autres paramètres plus complexes décrits dans la documentation de Django.
  Dans notre cas, on a choisi `models.SET_NULL` car on ne veut pas supprimer l'objet `Listing` si un `Band` est supprimé.

  Par la suite, il faut ajouter l'objet `Listing` au site d'administration en faisant `admin.site.register(Listing, ListingAdmin)`                

  ****Nota:**** Une fois les modifs effectuées ne pas oublier d'appliquer les migrations et relancer le serveur (`python3 .\manage.py runserver`)

  Astuce: Pour voir les groupes associés (liés) aux articles, il suffit d'ajouter le champ `band` au `ListingAdmin`dans `admin.py`
  ```
  class ListingAdmin(admin.ModelAdmin):
  list_display = ('title', 'band')  
  ```

### Quelques spécificités de la migration          

**Annulation de migration**       
On se place dans le cas où on a fait des migrations dont on veut annuler les changements, on a deux stratégies principales:

- Si les modifications non souhaitées n'ont pas été partagées avec d'autres utilisateurs (sur un repo git et pullé par les autres devs par exemple),
  on peut annuler la migration localement (simple *rollback*), puis la supprimer pour revenir à la migration précédente.
  Pour cela on commence par repérer la migration "fâcheuse" (celle qu'on veut supprimer) en affichant la liste des migrations
  grâce à la commande: `python manage.py showmigrations`.
  Une fois la migration repérée (dans notre cas pratique il s'agit de: `0006_band_like_new`), on repère aussi la migration précédente (`0005_listing_band`).
  Ensuite on annule la migration fâcheuse en faisant le rollback à proprement parler (ce rollback me fait penser au `git reset --hard` avec git):
  ```
  python manage.py migrate <nom-application>.<nom-migration-précédente>	
  ```
  On peut vérifier que la migration fâcheuse n'a pas été appliquée en affichant de nouveau les migrations par `python manage.py showmigrations`.
  On peut constater que la migration `listings.0006_band_like_new` apparaît sans **[X]** à côté ce qui signifie qu'elle n'a pas été exécutée.
  Enfin on supprime (le fichier de) la migration fâcheuse en faisant: `rm listings/migrations/0006_band_like_new.py `
  

- Si les changements ont été partagés, il est préférable de créer une nouvelle migration qui annule les changements de la migration non désirée.
La nuance ici est qu'il ne s'agit pas d'un rollback (comme précédemment). Il est plutôt question de modifier le code manuellement pour revenir à l'état
antérieur à la modification.
Dans notre cas par exemple il faut supprimer la ligne problématique, et par la suite créer et exécuter une nouvelle migration.
Donc la migration problématique n'est pas supprimée (elle est justement visible dans l'historique), mais la nouvelle migration fait une modification qui met le code à l'état souhaité.
Cette option est choisie car les autres dev ayant fait des pull, on ne peut pas leur demander d'aller chacun faire un rollback...

**Fusion de migration conflictuelles**       

Parfois en travaillant sur un projet avec d'autres dev, on risque d’être confronté à des migrations conflictuelles. 
Si ces migrations concernent des champs ou des modèles différents, on peut les fusionner par `python manage.py makemigrations --merge` 
sinon, il faut les supprimer et créer de nouvelles migrations à la place.




