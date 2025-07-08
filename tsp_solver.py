from itertools import combinations
import matplotlib.pyplot as plt
import sys

def tsp_dp(distances):
    n = len(distances)
    
    memo = {} # memo: {(ensemble_de_villes_visitees, derniere_ville): (distance, chemin)} , dictionnaire
    
    # Étape 1: Initialisation (de la ville 0 à chaque ville i)
    for i in range(1, n):
        memo[(frozenset([i]), i)] = (distances[0][i], [0, i])
    
    # Étape 2: Résoudre pour des sous-ensembles de plus en plus grands
    for subset_size in range(2, n):
        for subset in combinations(range(1, n), subset_size):
            subset = frozenset(subset)
            for m in subset:
                # Trouver le chemin minimal pour arriver à m
                min_dist = sys.maxsize
                min_path = []
                
                for k in subset:
                    if k == m:
                        continue
                    dist, path = memo[(subset - {m}, k)]
                    new_dist = dist + distances[k][m]
                    if new_dist < min_dist:
                        min_dist = new_dist
                        min_path = path + [m]
                
                memo[(subset, m)] = (min_dist, min_path)
    
    # Étape 3: Trouver le chemin complet (retour à l'origine)
    full_set = frozenset(range(1, n))
    min_dist = sys.maxsize
    best_path = []
    
    for m in range(1, n):
        dist, path = memo[(full_set, m)]
        total_dist = dist + distances[m][0]
        if total_dist < min_dist:
            min_dist = total_dist
            best_path = path + [0]
    
    return min_dist, best_path

def plot_solution(coords, path):
    plt.figure(figsize=(10, 6))
    
   
    x, y = zip(*coords)
    plt.scatter(x, y, c='red', s=200, zorder=2)
    
  
    for i, (xi, yi) in enumerate(coords):
        plt.annotate(i, (xi, yi), xytext=(0, 10), 
                    textcoords='offset points', ha='center')
    
    
    path_coords = [coords[i] for i in path]
    px, py = zip(*path_coords)
    plt.plot(px, py, 'b-', linewidth=2, alpha=0.6, zorder=1)
    
    
    plt.title("Solution optimale du Voyageur de Commerce", fontsize=14)
    plt.xlabel("Coordonnée X", fontsize=12)
    plt.ylabel("Coordonnée Y", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()

# Exemple avec 4 villes
villes = [
    (0, 0),   # Ville 0 de depart
    (2, 3),   # Ville 1
    (5, 2),   # Ville 2
    (4, 5),
    (6, 7) ,
    (8, 9)     # Ville 3
]

# Calcul des distances entre villes
n = len(villes)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dx = villes[i][0] - villes[j][0]
            dy = villes[i][1] - villes[j][1]
            distances[i][j] = (dx**2 + dy**2)**0.5

# Résolution et affichage
distance, chemin = tsp_dp(distances)
print(f"Chemin optimal: {chemin}")
print(f"Distance totale: {distance:.2f} ")

# execution
plot_solution(villes, chemin)