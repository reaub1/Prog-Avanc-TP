import random
import heapq
import copy

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

def distance_manhattan(jeu, ref):
    """ Calcule la somme des distances de Manhattan pour chaque tuile """
    dist = 0
    for i in range(dim):
        for j in range(dim):
            if jeu[i][j] != TROU:
                y_ref, x_ref = chercher(jeu[i][j], ref)  # Position correcte
                dist += abs(i - y_ref) + abs(j - x_ref)  # Distance de Manhattan
    return dist

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

def deplacements_possibles(jeu):
    """ Renvoie la liste des mouvements possibles du trou """
    mt, nt = chercher(TROU, jeu)
    moves = []
    if mt > 0:
        moves.append((-1, 0))  # Haut
    if mt < dim - 1:
        moves.append((1, 0))  # Bas
    if nt > 0:
        moves.append((0, -1))  # Gauche
    if nt < dim - 1:
        moves.append((0, 1))  # Droite
    return moves

def appliquer_mouvement(jeu, move):
    """ Applique un mouvement au trou et retourne la nouvelle configuration """
    mt, nt = chercher(TROU, jeu)
    new_mt, new_nt = mt + move[0], nt + move[1]
    new_jeu = copy.deepcopy(jeu)
    new_jeu[mt][nt], new_jeu[new_mt][new_nt] = new_jeu[new_mt][new_nt], new_jeu[mt][nt]
    return new_jeu

def solve_taquin(jeu, ref):
    """ Algorithme A* pour résoudre le taquin """
    pq = []  # File de priorité
    heapq.heappush(pq, (distance_manhattan(jeu, ref), 0, jeu, []))  # (f(n), g(n), état, chemin)
    visited = set()

    while pq:
        _, g, current_jeu, path = heapq.heappop(pq)

        if current_jeu == ref:  # Si on a trouvé la solution
            return path

        # Générer un hash de la grille pour éviter de revisiter les mêmes états
        jeu_hash = tuple(tuple(row) for row in current_jeu)
        if jeu_hash in visited:
            continue
        visited.add(jeu_hash)

        for move in deplacements_possibles(current_jeu):
            new_jeu = appliquer_mouvement(current_jeu, move)
            new_path = path + [move]
            f = g + 1 + distance_manhattan(new_jeu, ref)  # f(n) = g(n) + h(n)
            heapq.heappush(pq, (f, g + 1, new_jeu, new_path))

    return None  # Si aucune solution trouvée

# === Programme Principal ===
jeu, ref = initTaquin("taquin4.txt")
afficheJeu(jeu)

if not est_solvable(jeu, ref):
    print("❌ Ce taquin n'est pas résoluble !")
    exit(1)
else:
    print("✅ Ce taquin est résoluble !")

solution = solve_taquin(jeu, ref)

if solution:
    print("\n🚀 Solution trouvée en", len(solution), "mouvements.")
    print("🧩 Séquence des déplacements :", solution)
else:
    print("❌ Aucune solution trouvée.")