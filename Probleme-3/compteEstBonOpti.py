import random

cpt = 0
memo = {}
nb_redondance = 0

def trouveExpr(v, valeurs):
    global cpt, nb_redondance
    cpt += 1

    valeurs_tuple = tuple(sorted(valeurs))

    if (v, valeurs_tuple) in memo:
        nb_redondance += 1  
        return memo[(v, valeurs_tuple)]

    if len(valeurs) == 1:
        if v == valeurs[0]:
            result = (True, str(v))
            memo[(v, valeurs_tuple)] = result 
            return result
        else:
            result = (False, "")
            memo[(v, valeurs_tuple)] = result 
            return result
    else:
        if v in valeurs:
            result = (True, str(v))
            memo[(v, valeurs_tuple)] = result 
            return result
        else:
            for x in valeurs:
                valeurs2 = valeurs[:]
                valeurs2.remove(x)

                (t, ch) = trouveExpr(v + x, valeurs2)
                if t:
                    result = (t, ch + " - " + str(x))
                    memo[(v, valeurs_tuple)] = result 
                    return result

                
                if v >= x:
                    (t, ch) = trouveExpr(v - x, valeurs2)
                    if t:
                        result = (t, str(x) + " + (" + ch + ") ")
                        memo[(v, valeurs_tuple)] = result 
                        return result

                
                if v <= x:
                    (t, ch) = trouveExpr(x - v, valeurs2)
                    if t:
                        result = (t, str(x) + " + (" + ch + ") ")
                        memo[(v, valeurs_tuple)] = result  
                        return result

                
                if v >= x and v % x == 0:
                    (t, ch) = trouveExpr(v // x, valeurs2)
                    if t:
                        result = (t, "(" + ch + ") * " + str(x))
                        memo[(v, valeurs_tuple)] = result  
                        return result

                
                if v <= x and x % v == 0:
                    (t, ch) = trouveExpr(x // v, valeurs2)
                    if t:
                        result = (t, str(x) + " / (" + ch + ") ")
                        memo[(v, valeurs_tuple)] = result  
                        return result

                
                (t, ch) = trouveExpr(v * x, valeurs2)
                if t:
                    result = (t, "(" + ch + ") / " + str(x))
                    memo[(v, valeurs_tuple)] = result 
                    return result

            
            result = (False, "")
            memo[(v, valeurs_tuple)] = result  
            return result


NBNOMBRES = 6
nombres = []
operateurs = ['+', '-', '*', '/']
operandes = list(range(1, 11)) + list(range(1, 11)) + [25, 50, 75, 100]

cible = 563
nombres = [3, 25, 2, 10, 9, 2]
#for i in range(NBNOMBRES) :
#    nombres.append(operandes[random.randint(0,len(operandes)-1)])
#cible = random.randint(100,999)

res = trouveExpr(cible, nombres)
print(f"Cible: {cible}, Nombres: {nombres}, Résultat: {res}, Itérations: {cpt}, Redondances évitées: {nb_redondance}")


if res[0] == False:
    for i in range(cible):
        print("Écart", i)
        res = trouveExpr(cible + i, nombres)
        if res[0] == True:
            print(f"Cible: {cible}, Cible + {i}, Nombres: {nombres}, Résultat: {res}, Itérations: {cpt}, Redondances évitées: {nb_redondance}")
            break
        res = trouveExpr(cible - i, nombres)
        if res[0] == True:
            print(f"Cible: {cible}, Cible - {i}, Nombres: {nombres}, Résultat: {res}, Itérations: {cpt}, Redondances évitées: {nb_redondance}")
            break
