import heapq
import copy

TROU = '0'

def chercher(val, ref):
    """ Trouve la position d'une valeur """
    for i in range(len(ref)):
        if val in ref[i]:
            return i, ref[i].index(val)

def distance_manhattan(jeu, ref):
    """ Distance de Manhattan + conflits linéaires """
    dim = len(jeu)
    dist = 0
    for i in range(dim):
        for j in range(dim):
            if jeu[i][j] != TROU:
                y_ref, x_ref = chercher(jeu[i][j], ref)
                dist += abs(i - y_ref) + abs(j - x_ref)
    return dist + conflict_pairs(jeu, ref)

def conflict_pairs(jeu, ref):
    """ Ajoute des pénalités pour les conflits linéaires """
    conflicts = 0
    dim = len(jeu)
    for i in range(dim):
        row = [jeu[i][j] for j in range(dim) if jeu[i][j] != TROU]
        conflicts += count_conflicts(row, [ref[i][j] for j in range(dim)])
        
        col = [jeu[j][i] for j in range(dim) if jeu[j][i] != TROU]
        conflicts += count_conflicts(col, [ref[j][i] for j in range(dim)])
    
    return conflicts * 2

def count_conflicts(line, correct_line):
    """ Vérifie si des tuiles se bloquent entre elles """
    conflicts = 0
    for i in range(len(line)):
        for j in range(i + 1, len(line)):
            if line[i] in correct_line and line[j] in correct_line:
                if correct_line.index(line[i]) > correct_line.index(line[j]):
                    conflicts += 1
    return conflicts

def deplacements_possibles(jeu):
    """ Renvoie les mouvements possibles """
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
    """ A* avec distance de Manhattan + conflits linéaires """
    pq = []
    heapq.heappush(pq, (distance_manhattan(jeu, ref), 0, jeu, []))
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
            f = g + 1 + distance_manhattan(new_jeu, ref)
            heapq.heappush(pq, (f, g + 1, new_jeu, new_path))

    return None