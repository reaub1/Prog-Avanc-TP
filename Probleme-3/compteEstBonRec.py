import random

cpt=0

def trouveExpr(v, valeurs) :
    global cpt
    cpt+=1
    if len(valeurs) == 1 :     
        if (v == valeurs[0]) : 
            return (True,str(v))
        else : 
            return (False, "")
    else :
        if v in valeurs :
            return (True, str(v))
        else :
            for x in valeurs :
                valeurs2 = valeurs[:]
                valeurs2.remove(x)

                (t, ch) = trouveExpr(v+x, valeurs2)
                if t: return (t, ch + " - " + str(x))

                if (v >= x) : 
                    (t, ch) = trouveExpr(v-x, valeurs2)
                    if t : return (t, str(x)+" + (" + ch+") ")

                if (v <= x) : 
                    (t, ch) = trouveExpr(x-v, valeurs2)
                    if t : return (t, str(x)+" + (" + ch+") ")
                
                if (v >= x) and v%x == 0: 
                    (t, ch) = trouveExpr(v//x, valeurs2)
                    if t : return (t, "("+ch+") * "+str(x))

                if (v <= x) and x%v == 0: 
                    (t, ch) = trouveExpr(x//v, valeurs2)
                    if t : return (t, str(x)+" / ("+ch+") ")

                (t, ch) = trouveExpr(v*x, valeurs2)
                if t : return  (t, "("+ch+") / "+str(x))

            return(False,"")

NBNOMBRES = 6
nombres=[]
operateurs = ['+', '-', '*', '/']
operandes=list(range(1,11))+list(range(1,11))+[25,50,75,100]

cible = 813
nombres = [6, 5, 10, 9, 8, 3]

#for i in range(NBNOMBRES) :
#    nombres.append(operandes[random.randint(0,len(operandes)-1)])
#cible = random.randint(100,999)

res = trouveExpr (cible, nombres)
print(cible, nombres, res, cpt)
if (res[0]==False) :
    for i in range(cible) :
        print("écart",i)
        res = trouveExpr (cible+i, nombres)
        if (res[0]==True) : 
            print(cible, cible+i, nombres, res, cpt)
            break
        res = trouveExpr (cible-i, nombres)
        if (res[0]==True) : 
            print(cible, cible-i, nombres, res, cpt)
            break

