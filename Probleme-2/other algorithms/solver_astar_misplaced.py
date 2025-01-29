import heapq
import copy

TROU = '0'

def chercher(val, ref):
    """ Trouve la position d'une valeur """
    for i in range(len(ref)):
        if val in ref[i]:
            return i, ref[i].index(val)

def nombre_tuiles_mal_placees(jeu, ref):
    """ Heuristique : nombre de tuiles mal placées """
    dim = len(jeu)
    return sum(jeu[i][j] != ref[i][j] and jeu[i][j] != TROU for i in range(dim) for j in range(dim))

def deplacements_possibles(jeu):
    """ Renvoie les mouvements possibles du trou """
    dim = len(jeu)
    mt, nt = chercher(TROU, jeu)
    moves = []
    if mt > 0: moves.append((-1, 0))
    if mt < dim - 1: moves.append((1, 0))
    if nt > 0: moves.append((0, -1))
    if nt < dim - 1: moves.append((0, 1))
    return moves

def appliquer_mouvement(jeu, move):
    """ Applique un mouvement """
    mt, nt = chercher(TROU, jeu)
    new_mt, new_nt = mt + move[0], nt + move[1]
    new_jeu = copy.deepcopy(jeu)
    new_jeu[mt][nt], new_jeu[new_mt][new_nt] = new_jeu[new_mt][new_nt], new_jeu[mt][nt]
    return new_jeu

def solve_taquin(jeu, ref):
    """ A* avec tuiles mal placées """
    pq = []
    heapq.heappush(pq, (nombre_tuiles_mal_placees(jeu, ref), 0, jeu, []))
    visited = set()

    while pq:
        _, g, current_jeu, path = heapq.heappop(pq)
        if current_jeu == ref:
            return path
        jeu_hash = tuple(tuple(row) for row in current_jeu)
        if jeu_hash in visited:
            continue
        visited.add(jeu_hash)
        for move in deplacements_possibles(current_jeu):
            new_jeu = appliquer_mouvement(current_jeu, move)
            new_path = path + [move]
            f = g + 1 + nombre_tuiles_mal_placees(new_jeu, ref)
            heapq.heappush(pq, (f, g + 1, new_jeu, new_path))

    return None