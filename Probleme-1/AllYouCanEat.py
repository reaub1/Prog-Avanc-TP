import math

# k est le nombre d'élèves ingénieurs
k = 5
# n est le nombre maximum d'assiettes
n = 1000
# s est le seuil pour chaque élève ingénieur
s = 50
# Compteur global pour suivre le nombre total d'assiettes consommées
plats_consommees = 0
# Compteur des élèves perdus
eleves_perdus = 0

def find_critical_dishes(n, k):
    global plats_consommees, eleves_perdus
    
    plats_consommees = 0
    eleves_perdus = 0

    if k >= math.log2(n):
        print("DICHOTOMIE")
        return find_dichotomie(n)
    elif k == 2:
        print("BLOC")
        return find_bloc(n)
    elif k < math.log2(n):
        print("SEQUENTIEL")
        return find_sequentiel(n, k)

def survives(x):
    global plats_consommees
    global eleves_perdus
    plats_consommees += x

    if x >= s:
        eleves_perdus += 1
        return False
    return True

def find_dichotomie(n):
    left, right = 1, n
    result = 0

    while left <= right:
        mid = (left + right) // 2
        if survives(mid):
            result = mid + 1
            left = mid + 1 
        else:
            right = mid - 1

    return result

def find_sequentiel(n, k):
    step = max(1, n // k)
    last_survived = 0

    for i in range(step, n + 1, step):
        if not survives(i):
            break
        last_survived = i

    for i in range(last_survived + 1, min(last_survived + step, n + 1)):
        if not survives(i):
            return i
    return n 

def find_bloc(n):
    step = int(n ** 0.5)
    print("STEP : " + str(step))
    last_survived = 0

    for i in range(step, n + 1, step):
        if not survives(i):
            break
        last_survived = i 

    print(str(i))

    for y in range(last_survived + 1, (last_survived + step) + 1):
        if not survives(y):
            return y

    return n

# Trouver la valeur critique des assiettes
resultat = find_critical_dishes(n, k)

resultat_string = "PAS BON RESULTAT"

if resultat == s:
    resultat_string = "BON RESULTAT"

# Affichage des résultats
print("--------------------------------------------------------------")
print("Résultat : " + resultat_string)
print("Nombre maximum d'assiettes mangeables par ingénieur à trouver : " + str(s))
print("Nombre maximum d'assiettes mangeables trouvés : " + str(resultat))
print("Nombre total d'assiettes consommées : " + str(plats_consommees))
print("Nombre d'élèves ingénieurs perdus : " + str(eleves_perdus))
print("Nombre d'élèves ingénieurs : " + str(k))
print("--------------------------------------------------------------")