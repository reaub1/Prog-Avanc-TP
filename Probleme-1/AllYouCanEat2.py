# k est le nombre d'élèves ingénieurs 
k = 2
# n est le nombre maximum d'assiettes
n = 1

# Compteur global pour suivre le nombre total d'assiettes consommées
plats_consommees = 0

# Si k >= log2(n), écrivez un algorithme en O(log2(n)) repas.
# Si k < log2(n), écrivez un algorithme en O(k + n / (2k - 1)) repas.
# Si k = 2, écrivez un algorithme en O(n1/2) repas

def find_critical_dishes(n, k):
    if k >= (n).bit_length():
        return find_dichotomie(n) -1
    elif k < (n).bit_length():
        return find_sequentiel(n, k)
    elif k == 2:
        return find_bloc(n)


def survives(x):
    global plats_consommees
    plats_consommees += x  
    return x <= n


def find_dichotomie(n):
    left, right = 1, n
    while left <= right:
        mid = (left + right) // 2
        if survives(mid):
            left = mid + 1
        else:
            right = mid - 1
    return left

def find_sequentiel(n, k):
    step = max(1, n // k)
    last_survived = 0
    for i in range(1, n + 1, step):
        if not survives(i):
            break
        last_survived = i
    for i in range(last_survived + 1, min(last_survived + step, n + 1)):
        if not survives(i):
            return i
    return n

def find_bloc(n):
    step = int(n ** 0.5)
    last_survived = 0
    for i in range(1, n + 1, step):
        if not survives(i):
            break
        last_survived = i
    for i in range(last_survived + 1, min(last_survived + step, n + 1)):
        if not survives(i):
            return i
    return n

resultat_print = "PAS LE BON NOMBRE TROUVEE"
resultat = find_critical_dishes(n, k)
if(n == resultat):
    resultat_print = "BON NOMBRE TROUVEE"

print("--------------------------------------------------------------")
print("Résultat : " + resultat_print)
print("Nombre maximum d'assiettes mageable par ingénieur à trouver : " + str(n))
print("Nombre maximum d'assiettes mangeables trouvés : " + str(resultat))
print("Nombre total d'assiettes consommées : " + str(plats_consommees))
print("Nombres d'élèves ingénieurs : " + str(k))
print("--------------------------------------------------------------")