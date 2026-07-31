import numpy as np

def euclidean_distance(x, y):
    """Calcule la distance euclidienne entre deux points."""
    s = 0
    for i in range(len(x)):
        s += (x[i] - y[i]) ** 2
    return np.sqrt(s)

def argmin_dist(point, centroids):
    """Retourne l'index du centroïde le plus proche."""
    min_idx = 0
    mindist = euclidean_distance(point, centroids[0])
    
    for j in range(1, len(centroids)):
        dist = euclidean_distance(point, centroids[j])
        if dist < mindist:
            mindist = dist
            min_idx = j
    return min_idx

def mean_point(points):
    """
    Moyenne d'une liste de points.
    - points : list of list
    """
    if len(points) == 0:
        return []
        
    dim = len(points[0])
    m = [0] * dim
    
    for j in range(dim):
        # moyenne sur la coordonnée j
        m[j] = sum(p[j] for p in points) / len(points)
    return m

def kmeans(X, k, max_iters=10, seed=0):
    """
    K-means avec arrêt par nombre max d'itérations.
    - X : liste de points (list of list)
    - k : nombre de clusters
    """
    np.random.seed(seed)
    n = len(X)
    
    # Sélectionner aléatoirement k éléments distincts parmi n
    indices = np.random.choice(n, k, replace=False)
    centroids = [X[i][:] for i in indices]
    
    for i in range(max_iters):
        # 1) Affectation
        clusters = [0] * n
        for idx in range(n):
            clusters[idx] = argmin_dist(X[idx], centroids)
            
        # 2) Regroupement
        groups = [[] for _ in range(k)]
        for idx in range(n):
            groups[clusters[idx]].append(X[idx])
            
        # 3) Mise à jour des centroïdes
        for j in range(k):
            if len(groups[j]) > 0:
                centroids[j] = mean_point(groups[j])
                
    return centroids, clusters