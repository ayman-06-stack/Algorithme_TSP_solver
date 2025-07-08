# 🚀 Traveling Salesman Problem (TSP) Solver

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

Une implémentation efficace du problème du voyageur de commerce utilisant la programmation dynamique avec l'algorithme de Held-Karp.

## 📋 Table des matières

- [À propos](#à-propos)
- [Fonctionnalités](#fonctionnalités)
- [Installation](#installation)
- [Utilisation](#utilisation)
- [Algorithme](#algorithme)
- [Exemples](#exemples)
- [Structure du projet](#structure-du-projet)
- [Contribution](#contribution)
- [Licence](#licence)

## 📖 À propos

Le problème du voyageur de commerce (TSP) est un problème d'optimisation combinatoire classique. Ce projet propose une solution utilisant la programmation dynamique pour trouver le chemin le plus court visitant toutes les villes exactement une fois et revenant au point de départ.

### Complexité
- **Temps**: O(n² × 2ⁿ)
- **Espace**: O(n × 2ⁿ)

## ✨ Fonctionnalités

- ✅ Résolution exacte du TSP avec programmation dynamique
- ✅ Visualisation graphique du chemin optimal
- ✅ Calcul automatique des distances euclidiennes
- ✅ Interface simple et intuitive
- ✅ Support pour un nombre variable de villes
- ✅ Annotations des villes sur le graphique

## 🔧 Installation

### Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

### Installation des dépendances

```bash
# Cloner le repository
git clone https://github.com/votre-username/tsp-solver.git
cd tsp-solver

# Installer les dépendances
pip install -r requirements.txt
```

### Installation avec environnement virtuel (recommandé)

```bash
# Créer un environnement virtuel
python -m venv venv

# Activer l'environnement virtuel
# Sur Windows
venv\Scripts\activate
# Sur macOS/Linux
source venv/bin/activate

# Installer les dépendances
pip install -r requirements.txt
```

## 🚀 Utilisation

### Utilisation de base

```python
from tsp_solver import tsp_dp, plot_solution

# Définir les coordonnées des villes
villes = [
    (0, 0),   # Ville 0 (départ)
    (2, 3),   # Ville 1
    (5, 2),   # Ville 2
    (4, 5),   # Ville 3
    (6, 7),   # Ville 4
    (8, 9)    # Ville 5
]

# Calculer les distances
n = len(villes)
distances = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i != j:
            dx = villes[i][0] - villes[j][0]
            dy = villes[i][1] - villes[j][1]
            distances[i][j] = (dx**2 + dy**2)**0.5

# Résoudre le TSP
distance_optimale, chemin_optimal = tsp_dp(distances)

# Afficher les résultats
print(f"Chemin optimal: {chemin_optimal}")
print(f"Distance totale: {distance_optimale:.2f}")

# Visualiser la solution
plot_solution(villes, chemin_optimal)
```

### Exécution directe

```bash
python tsp_solver.py
```

## 🧮 Algorithme

Ce projet utilise l'algorithme de **Held-Karp** basé sur la programmation dynamique :

1. **Initialisation** : Calcul des distances directes de la ville de départ vers toutes les autres villes
2. **Récurrence** : Pour chaque sous-ensemble de villes, calcul du chemin optimal vers chaque ville du sous-ensemble
3. **Solution finale** : Sélection du chemin minimal qui revient à la ville de départ

### Formule de récurrence

```
dp[S][i] = min(dp[S\{i}][j] + distance[j][i])
```

Où :
- `S` est un sous-ensemble de villes
- `i` est la ville de destination
- `j` est la ville intermédiaire

## 📊 Exemples

### Exemple 1 : 4 villes
```python
villes = [(0, 0), (2, 3), (5, 2), (4, 5)]
# Résultat : Chemin optimal et distance calculée
```

### Exemple 2 : 6 villes (exemple par défaut)
```python
villes = [(0, 0), (2, 3), (5, 2), (4, 5), (6, 7), (8, 9)]
# Visualisation graphique automatique
```

## 📁 Structure du projet

```
tsp-solver/
│
├── tsp_solver.py          # Code principal
├── requirements.txt       # Dépendances
├── README.md             # Documentation
├── LICENSE               # Licence MIT
├── .gitignore           # Fichiers à ignorer

```

## 🧪 Tests

Exécuter les tests unitaires :

```bash
python -m pytest tests/
```

## 📈 Performance

| Nombre de villes | Temps d'exécution | Mémoire utilisée |
|------------------|-------------------|------------------|
| 4                | < 1ms            | < 1MB           |
| 6                | < 10ms           | < 5MB           |
| 8                | < 100ms          | < 20MB          |
| 10               | < 1s             | < 100MB         |

⚠️ **Note** : La complexité exponentielle limite l'utilisation pratique à environ 15-20 villes.

## 🤝 Contribution

Les contributions sont les bienvenues ! Voici comment contribuer :

1. **Fork** le projet
2. Créer une **branche** pour votre fonctionnalité (`git checkout -b feature/AmazingFeature`)
3. **Commit** vos changements (`git commit -m 'Add some AmazingFeature'`)
4. **Push** vers la branche (`git push origin feature/AmazingFeature`)
5. Ouvrir une **Pull Request**

### Guidelines de contribution

- Suivre les conventions de codage Python (PEP 8)
- Ajouter des tests pour les nouvelles fonctionnalités
- Mettre à jour la documentation si nécessaire
- Respecter la structure existante du projet

## 🐛 Signaler des bugs

Si vous trouvez un bug, veuillez ouvrir une [issue](https://github.com/ayman-06-stack/tsp-solver) avec :
- Une description détaillée du problème
- Les étapes pour reproduire le bug
- Votre environnement (OS, version Python, etc.)

## 📄 Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## 👨‍💻 Auteur

**Votre Nom**
- GitHub: [@votre-username](https://github.com/ayman-06-stack)
- Email: aymanguendouz07@gmail.com

## 🙏 Remerciements

- Inspiration tirée des algorithmes classiques d'optimisation
- Merci à la communauté Python pour les excellentes bibliothèques
- Ressources académiques sur le TSP et la programmation dynamique

---

⭐ **N'hésitez pas à donner une étoile si ce projet vous a aidé !**
