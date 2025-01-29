import copy

TROU = '0'

def chercher(val, ref):
    """ Trouve la position d'une valeur """
    for i in range(len(ref)):
        if val in ref[i]:
            return i, ref[i].index(val)

def distance_manhattan(jeu, ref):
    """ Heuristique : distance de Manhattan """
    dim = len(jeu)
    return sum(
        abs(i - chercher(jeu[i][j], ref)[0]) + abs(j - chercher(jeu[i][j], ref)[1])
        for i in range(dim) for j in range(dim) if jeu[i][j] != TROU
    )

def deplacements_possibles(jeu):
    """ Renvoie les mouvements possibles """
    dim = len(jeu)
    mt, nt = chercher(TROU, jeu)
    moves = []
    if mt > 0: moves.append((-1, 0))  # Haut
    if mt < dim - 1: moves.append((1, 0))  # Bas
    if nt > 0: moves.append((0, -1))  # Gauche
    if nt < dim - 1: moves.append((0, 1))  # Droite
    return moves

def appliquer_mouvement(jeu, move):
    """ Applique un mouvement """
    mt, nt = chercher(TROU, jeu)
    new_mt, new_nt = mt + move[0], nt + move[1]
    new_jeu = copy.deepcopy(jeu)
    new_jeu[mt][nt], new_jeu[new_mt][new_nt] = new_jeu[new_mt][new_nt], new_jeu[mt][nt]
    return new_jeu

def ida_star_recursive(jeu, ref, g, bound, path):
    """ Recherche récursive pour IDA* """
    f = g + distance_manhattan(jeu, ref)
    if f > bound:
        return f
    if jeu == ref:
        return path
    
    min_cost = float("inf")
    for move in deplacements_possibles(jeu):
        new_jeu = appliquer_mouvement(jeu, move)
        new_path = path + [move]
        t = ida_star_recursive(new_jeu, ref, g + 1, bound, new_path)
        if isinstance(t, list):
            return t
        if t < min_cost:
            min_cost = t
    return min_cost

def solve_taquin(jeu, ref):
    """ IDA* """
    bound = distance_manhattan(jeu, ref)
    while True:
        t = ida_star_recursive(jeu, ref, 0, bound, [])
        if isinstance(t, list):
            return t
        bound = t