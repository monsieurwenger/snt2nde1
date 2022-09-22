# Initiation au Python

## Qu'est ce qu'un langage de programmation ?

Un langage de programmation permet de donner des instructions plus ou moins complexes à une machine pour qu'elle effectue ce qu'on désire.

Même si vous n'avez jamais programmé sur ordinateur, vous avez déjà utilisé des langages de programmation sans le savoir : rentrer un calcul dans une calculatrice est une manière (rudimentaire) de donner des instructions à une machine.

Vous avez aussi fait du Scratch au collège, c'est une manière visuelle de donner des instructions à une machine.

Le Python est un langage de programmation, mais qui s'exprime sous la forme d'un texte, et non pas d'images (ou d'une série d'appuis sur des touches). Cela permet sa transmission et sa sauvegarde simple.

Le python est un des langages de programmations les plus intuitifs et qui a la syntaxe la moins lourde.

## Installer python

Python est normalement déjà installé sur votre ordinateur.

Pour s'en assurez, ouvrez une ligne de commande (en exécutant cmd.exe) et essayez de taper "python" (On appuye toujours sur "Entrée" après avoir rentré une ligne de commande). 

un texte qui ressemble à ceci devrait s'afficher

    Python 3.8.10 (default, Jun 22 2022, 20:18:18) 
    [GCC 9.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>> 


Quelles différences avec le texte précédent observez-vous dans ce qui s'affiche sur votre ordinateur ?  .........................................................................................................................................................................................................................................................................................................................................................................................................................................................

Si python n'est pas installé sur votre ordinateur, vous pouvez 
- essayer de l'installer vous-même (Cela ne devrait pas marcher), en téléchargeant le programme https://www.python.org/downloads/ 
- Demander à M. Bensussan pendant ses heures de permanence informatique

Pendant le reste de la séance, vous pouvez employer un éditeur en ligne sur https://www.programiz.com/python-programming/online-compiler/


## Installer Jupyter

Jupyter est un format qui permet d'afficher des calculs de manière plus sympathique, notamment d'afficher en même temps le code et le résultat de son exécution.

Pour installer jupyter sur votre ordinateur, il faut taper (Là encore, il n'est pas sûr que ça marche sur votre ordinateur)  dans la ligne de commande :

    pip install notebook

Une fois l'installation effectuée, vous pouvez taper toujours dans une ligne de commande :

    jupyter-notebook
    
Dans l'impossibilité d'utiliser Jupyter, on utilisera tout simplement la console, c'est à dire l'interface qui s'affiche quand on tape python dans une ligne de commande, ou le site de python en ligne cité plus haut.

## Afficher du texte dans python :

Par défaut, la console (et le Jupyter Notebook) affichent la valeur renvoyée par la dernière ligne qui apparaît dans le code :
Ecrire `"Bonjour"` dans ces deux environnements affichera "Bonjour"

Pour le site de python en ligne (ou un programme dans un fichier, que nous verrons la prochaine fois), il faut entourer le texte à afficher de `print` :

`print("Bonjour")`


## Premières opérations dans python

On veut effectuer l'opération  `5+3` dans python

Pour cela, tapez 5+3 dans la console. Vous devriez voir afficher le résultat 8. 


Vous pouvez essayez avec d'autres nombres, et aussi en rajoutant des espaces dans le texte :  Que donne `5 + 3` ? Que donne `5+   3` ?


Dans python, il existe de nombreuses opérations qui permettent de mettre en jeu deux nombres. Certaines sont intuitives comme le +, d'autres un peu moins :

Que font les opérations suivantes ?      Donner ce qu'effectue l'ordinateur en langage mathématiques, puis donner le nom de l'opération :

|Instruction | En langage maths | Nom de l'opération |
|----------|------------|----------|
`5 + 3`| 5 + 3 = 8| Addition|
`5 - 3`| ||
`5 * 3`| ||
`5 / 3`| ||
`5 ** 3`|||
`5 // 3`|||
`5 % 3`|||
`5 ^ 3`|||


## Manipuler du texte

Pour utiliser du texte dans python, il faut l'entourer de `"` ou de `'`.  

Que fait l'opération + sur du texte ? 

|Instruction | Résultat | Nom de l'opération |
|----------|------------|----------|
`"2nde" + "1"`| ||

### Imprimer du texte

Comme écrit plus haut, la commande pour demander à python d'afficher du texte est la fonction `print`.

Si je veux afficher mon prénom, j'écrirai :  ..................................................................


### Demander du texte à l'utilisateur du programme 

Pour demander à l'utilisateur du programme d'entrer une information au clavier, et pouvoir l'utiliser dans python, on utilise la fonction `input()`

Par exemple, l'instruction `print(input("Entrez le texte à Afficher"))` demandera à l'utilisateur d'entrer le texte qui s'affichera, puis l'imprimera.


A votre avis, que fait cette ligne de commande : `print("Votre prénom est " + input("Quel est votre prénom"))`?  .........................................................................................................................................................................................................................................................................................................................................................................................................................................................

Exécutez là et vérifiez que vous avez vu juste.




