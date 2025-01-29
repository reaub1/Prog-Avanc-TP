import random
from solver_astar import solve_taquin, appliquer_mouvement  
import time


TROU = '0'
dim = 0

def afficheJeu(jeu):
    """ Affiche la grille du taquin """
    for l in jeu:
        print(" ".join(l))
    print()

def initTaquin(nf):
    """ Initialise le taquin depuis un fichier """
    with open(nf, "r") as f:
        lignes = f.readlines()
    
    global dim
    dim = len(lignes) // 2
    jeu, ref = [], []
    
    for l in lignes[:dim]:
        jeu.append(l.split())
    for l in lignes[dim:]:
        ref.append(l.split())
    
    return jeu, ref

def chercher(val, ref):
    """ Trouve la position (ligne, colonne) d'une valeur dans la grille """
    for i in range(len(ref)):
        if val in ref[i]:
            return i, ref[i].index(val)

def est_solvable(jeu, ref):
    """ Vérifie si le taquin est solvable """
    valeurs = {val: i+1 for i, val in enumerate(sum(ref, [])) if val != TROU}
    flatten = [valeurs[val] for row in jeu for val in row if val != TROU]

    # Calcul des inversions
    inversions = sum(1 for i in range(len(flatten)) for j in range(i + 1, len(flatten)) if flatten[i] > flatten[j])

    # Trouver la position du trou en comptant depuis le haut
    trou_y, _ = chercher(TROU, jeu)
    trou_y += 1  # 1 = première ligne

    # Vérification de la parité correcte
    return (inversions % 2 == 0) if (dim % 2 == 1) else ((inversions + trou_y) % 2 == 0)

# === Programme Principal ===
jeu, ref = initTaquin("taquin4.txt")
afficheJeu(jeu)

if not est_solvable(jeu, ref):
    print("Ce taquin n'est pas résoluble !")
    exit(1)
else:
    print("Ce taquin est résoluble !")

solution = solve_taquin(jeu, ref)

if solution:
    # Traduire les mouvements en texte
    move_names = {
        (-1, 0): "Haut",
        (1, 0): "Bas",
        (0, -1): "Gauche",
        (0, 1): "Droite"
    }
    moves_text = [move_names[move] for move in solution]

    print("\n🚀 Solution trouvée en", len(solution), "mouvements.")

    # === Afficher l'évolution du taquin pas à pas ===
    print("\nAffichage de la résolution pas à pas :")

    for step, move in enumerate(solution, start=1):
        print(f"\n Étape {step} : {move_names[move]}")
        jeu = appliquer_mouvement(jeu, move)
        afficheJeu(jeu)
        input("Appuyez sur Entrée pour continuer...")

    print("\nTaquin résolu ! ")
else:
    print("Aucune solution trouvée.")