import random
import csv

# Méthode sans mémorisation
def trouveExpr_v1(v, valeurs):
    cpt = 0
    def recursive(v, valeurs):
        nonlocal cpt
        cpt += 1
        if len(valeurs) == 1:     
            if v == valeurs[0]: 
                return (True, str(v))
            else: 
                return (False, "")
        else:
            if v in valeurs:
                return (True, str(v))
            else:
                for x in valeurs:
                    valeurs2 = valeurs[:]
                    valeurs2.remove(x)

                    (t, ch) = recursive(v + x, valeurs2)
                    if t: return (t, ch + " - " + str(x))

                    if v >= x: 
                        (t, ch) = recursive(v - x, valeurs2)
                        if t: return (t, str(x) + " + (" + ch + ") ")

                    if v <= x: 
                        (t, ch) = recursive(x - v, valeurs2)
                        if t: return (t, str(x) + " + (" + ch + ") ")

                    if v >= x and v % x == 0: 
                        (t, ch) = recursive(v // x, valeurs2)
                        if t: return (t, "(" + ch + ") * " + str(x))

                    if v <= x and x % v == 0: 
                        (t, ch) = recursive(x // v, valeurs2)
                        if t: return (t, str(x) + " / (" + ch + ") ")

                    (t, ch) = recursive(v * x, valeurs2)
                    if t: return (t, "(" + ch + ") / " + str(x))

                return (False, "")
    return recursive(v, valeurs), cpt

# Méthode avec mémorisation
def trouveExpr_v2(v, valeurs):
    cpt = 0
    memo = {}
    def recursive(v, valeurs):
        nonlocal cpt
        cpt += 1
        valeurs_tuple = tuple(sorted(valeurs))
        if (v, valeurs_tuple) in memo:
            return memo[(v, valeurs_tuple)]
        
        if len(valeurs) == 1:
            if v == valeurs[0]:
                return (True, str(v))
            else:
                return (False, "")
        else:
            if v in valeurs:
                return (True, str(v))
            else:
                for x in valeurs:
                    valeurs2 = valeurs[:]
                    valeurs2.remove(x)

                    (t, ch) = recursive(v + x, valeurs2)
                    if t:
                        result = ch + " - " + str(x)
                        memo[(v, valeurs_tuple)] = (t, result)
                        return (t, result)

                    if v >= x:
                        (t, ch) = recursive(v - x, valeurs2)
                        if t:
                            result = str(x) + " + (" + ch + ") "
                            memo[(v, valeurs_tuple)] = (t, result)
                            return (t, result)

                    if v <= x:
                        (t, ch) = recursive(x - v, valeurs2)
                        if t:
                            result = str(x) + " + (" + ch + ") "
                            memo[(v, valeurs_tuple)] = (t, result)
                            return (t, result)

                    if v >= x and v % x == 0:
                        (t, ch) = recursive(v // x, valeurs2)
                        if t:
                            result = "(" + ch + ") * " + str(x)
                            memo[(v, valeurs_tuple)] = (t, result)
                            return (t, result)

                    if v <= x and x % v == 0:
                        (t, ch) = recursive(x // v, valeurs2)
                        if t:
                            result = str(x) + " / (" + ch + ") "
                            memo[(v, valeurs_tuple)] = (t, result)
                            return (t, result)

                    (t, ch) = recursive(v * x, valeurs2)
                    if t:
                        result = "(" + ch + ") / " + str(x)
                        memo[(v, valeurs_tuple)] = (t, result)
                        return (t, result)

        memo[(v, valeurs_tuple)] = (False, "")
        return (False, "")

    return recursive(v, valeurs), cpt


def compare_iterations():
    NBNOMBRES = 6
    operandes = list(range(1, 11)) + list(range(1, 11)) + [25, 50, 75, 100]
    
    with open("./Probleme-3/comparaison_iterations.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Cible", "Nombres", "Iterations_Prog1", "Resultat_v1", "Iterations_Prog2", "Resultat_v2", "Division_Iterations"])
        
        for _ in range(1000): #1000 tests
            nombres = [operandes[random.randint(0, len(operandes) - 1)] for _ in range(NBNOMBRES)]
            cible = random.randint(100, 999)

            res_v1, iterations_programme1 = trouveExpr_v1(cible, nombres)
            res_v1 = res_v1[0]
            
            res_v2, iterations_programme2 = trouveExpr_v2(cible, nombres)
            res_v2 = res_v2[0]

            div_Moy = iterations_programme1 / iterations_programme2

            writer.writerow([cible, nombres, iterations_programme1, res_v1, iterations_programme2, res_v2, div_Moy])


compare_iterations()
