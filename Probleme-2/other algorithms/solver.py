import heapq
import copy

TROU = '0'

def chercher(val, ref):
    """ Trouve la position (ligne, colonne) d'une valeur dans la grille """
    for i in range(len(ref)):
        if val in ref[i]:
            return i, ref[i].index(val)

def distance_manhattan(jeu, ref):
    """ Calcule la somme des distances de Manhattan pour chaque tuile """
    dim = len(jeu)
    dist = 0
    for i in range(dim):
        for j in range(dim):
            if jeu[i][j] != TROU:
                y_ref, x_ref = chercher(jeu[i][j], ref)  # Position correcte
                dist += abs(i - y_ref) + abs(j - x_ref)  # Distance de Manhattan
    return dist

def deplacements_possibles(jeu):
    """ Renvoie la liste des mouvements possibles du trou """
    dim = len(jeu)
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