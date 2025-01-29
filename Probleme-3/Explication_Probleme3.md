# Probleme 3

## Pourquoi le programme fourni (compteEstBonRec.py) effectue des calculs redondants ?

Le programme *compteEstBonRec.py* utilise une méthode itérative qui teste toutes les combinaisons de chaque valeurs fournies pour atteindre la cible. Le problème avec cette méthode est qu'elle fait plusieurs fois les même calculs sans s'en rendre compte. 

Par exempe, avec des valeurs [u, v, w, x, y, z] pour atteindre la cible A, le programme va itérer en testant toutes les combinaisons de calculs entre ces valeurs (ex. u + v, u * z). Cependant, lors de tout ses test, le programme va tester plusieurs fois le meme calcul (ex. u+v & v+u, u * z & z * u ). Ce qui va prendre un nombre important d'itération et donc énormement de temps inutile à cause de ces calculs redondants.

Mais il est possible d'optimiser cela !


## Optimisation du programme

La solution la plus logique à mettre en place pour éviter ces redondements est d'implementer un 'cache' qui stocke le résultat d'une opération avec un combinaison de valeurs. On va enregistrer les résultats des appels récursif déjà effectués, pour éviter de les recalculer.

Dans ce nouveau programme optimisé (*compteEstBonOpti.py*), on va donc utiliser un dictionnaire pour mémoriser les résultats des appels. Le dictionnaire ***memo*** va stocker les résultats des appels récursifs. La clé est un tuple *(v, valeurs_tuple)* représentant l'état actuel de la cible et des valeurs, et la valeur est le résultat de la recherche (soit *True/False* et l'expression correspondante).

Ainsi, avant d'effectuer le calcul pour une combinaison de valeurs donnée, le programme vérifie si le résultat pour cette combinaison a déjà été calculé en cherchant dans ***memo***. Si c'est le cas, il retourne immédiatement le résultat mémorisé. Et chaque fois que la fonction termine un calcul, elle mémorise le résultat dans ***memo*** pour éviter les recalculs futurs.

Grace à cette mémorisation des résultats, chaque combinaison n'est calculée qu'une seule fois, réduisant ainsi grandement le nombre d'itération du programme.

## Comparaison des programmes

Nous allons maintenant comparer les deux programmes afin de prouver l'éfficacité de l'approche avec mémorisation.

### Comparaison simple
Prenons une cible et des valeurs générées aléatoirement par le programme 1 (*compteEstBonRec.py*)

On obtient :
```
563 [3, 25, 2, 10, 9, 2] (True, '3 + (10 + (((9 + (2) ) * 2) * 25) ) ') 25169
```

Donc pour trouver 563 avec ces valeurs, le programme a trouvé 3 + (10 + (((9 + (2) ) * 2) * 25) ) en **25169** itérations.

En utilisant le programme 2 (*compteEstBonOpti.py*), en prennant la meme cible et les mêmes valeurs, on obtient :

```
Cible: 563, Nombres: [3, 25, 2, 10, 9, 2], Résultat: (True, '3 + (10 + (((9 + (2) ) * 2) * 25) ) '), Itérations: 9330, Redondances évitées: 3655
```

On a donc le même résultat, mais avec 9330 itérations, soit plus de 2,5 fois moins !


### Exemple multiple

Vous trouverez dans le dossier présent le programme *comparaison.py* qui contient les deux façon de procéder. Le programme fait 1000 tests de avec 1000 même cibles et valeurs données aux 2 programmes, il génère ensuite un fichier .csv (*comparaison_iteraitons.csv*) contenant les résultats des 1000 tests (*Cible, Valeurs, nb_itérations_P1, résultat_P1, nb_itérations_P2, résultat_P2, rapport_iteration*).

Le fichier *comparaison_iterations.xlsx* est l'interprétation des résultats avec le tableau de données, un graphique montrant le nombre d'itération de chaque programme pour chaque test et la moyenne du rapport entre le nombre d'itération. 

On observe donc qu'en moyenne, le programme optimisé permet de réduire de **4,96 fois** le nombre d'itérations !