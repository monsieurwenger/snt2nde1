

<h1> Les secrets du Markdown </h1>


Le Markdown est un langage d'édition de texte très simple à utiliser pour les néophytes.

Il suffit de taper le texte pour qu'ils s'affiche.  Certains caractères spéciaux sont réservés à exprimer des modifications du texte :

## Mise en forme basique


Les techniques de base pour mettre en forme le texte sont :

### Texte en italique

On entoure le texte d'étoiles `*` :    `Le mot *penché*` s'affichera comme Le mot *penché*


### Texte en gras

On entoure le texte de **deux** étoiles de part et d'autre `**` :    `Le mot **gras**` s'affichera comme Le mot **gras**

### Texte en gras et italique 

On entoure le texte de **trois** étoiles `***` :    `Les mots ***gras et penché***` s'affichera comme Les mots ***gras et penché***

### Texte brut

Pour afficher du code, ou encore si l'on veut utiliser une étoile (ou autre caractère interprété par Markdown), on entoure le texte de `` ` `` :   `` La bibliothèque est `numpy` `` s'affichera comme La bibliothèque est `numpy` 

Pour afficher plusieurs lignes de code, on utilise `` ``` `` de part et d'autre du texte. On peut même spécifier le langage pour donner des couleurs :

Par exemple, 


    ```python
      def carre(n):
          return n*n
    ```

Donnera :

```python
  def carre(n):
      return n*n
```

## Mise en page

### Titres

On emploie des `#` pour afficher des éléments sous forme de titres (texte plus gros):

```
# Chapitre
## Partie
### Sous-partie
```

Donnera 

# Chapitre
## Partie
### Sous-partie

### Barre horizontale

Ecrire `***` sur une ligne vide tracera une barre horizontale qui ressemble à ceci :

***

### Tableau


    | Colonne 1 | Colonne 2 | Colonne 3 |
    |-----------|-----------|-----------|
    | cellule 1 | cellule 2 | cellule 3 |
    |   autre cellule        | Encore une | Cellule 6 |
    | | |  |


Donnera 
| Colonne 1 | Colonne 2 | Colonne 3 |
|-----------|-----------|-----------|
| cellule 1 | cellule 2 | cellule 3 |
|   autre cellule        | Encore une | Cellule 6 |
| | |  |



## Liens et fichiers externes

### Lien

La syntaxe `[Texte Lien](https://www.adressedusite.com)` Donnera : [Texte Lien](https://www.adressedusite.com)

### Image externe


    ![texte alternatif de l'image](https://www.radiofrance.fr/s3/cruiser-production/2019/04/438690ea-e271-4c98-9a13-c08fa8297f53/870x489_000_par2192549.webp)

Donnera

![texte alternatif de l'image](https://www.radiofrance.fr/s3/cruiser-production/2019/04/438690ea-e271-4c98-9a13-c08fa8297f53/870x489_000_par2192549.webp)

## Ressources


Il existe de nombreux tutoriels de Markdown en français. La plupart des informations présentes sur cette page proviennent de [ce site](https://documentation-snds.health-data-hub.fr/contribuer/guide_contribution/tutoriel_markdown.html)
