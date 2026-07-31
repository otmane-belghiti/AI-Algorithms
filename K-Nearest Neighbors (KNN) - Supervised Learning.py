import math

def euclidean_distance(x, y):
    """Calcule la distance euclidienne entre deux points."""
    s = 0
    for i in range(len(x)):
        s += (x[i] - y[i]) ** 2
    return math.sqrt(s)

def triSelection(L):
    """
    Tri par sélection en place d'une liste de tuples (distance, label) 
    selon la distance, sans utiliser sorted().
    """
    n = len(L)
    for i in range(n - 1):
        min_idx = i
        for j in range(i + 1, n):
            if L[j][0] < L[min_idx][0]:
                min_idx = j
        # Échange des éléments
        L[i], L[min_idx] = L[min_idx], L[i]
    return L

def frequent(labels):
    """Trouve le label de fréquence maximale."""
    F = {}
    for label in labels:
        if label in F:
            F[label] += 1
        else:
            F[label] = 1
            
    # Trouver le label de frequence maximale
    max_count = 0
    maxlabel = None
    for label, count in F.items():
        if count > max_count:
            max_count = count
            maxlabel = label
    return maxlabel

def knn(X_train, y_train, X_test, k):
    """
    Prédit les labels pour X_test par KNN (classification).
    - X_train : liste de points (list of list)
    - y_train : liste de labels (list)
    - X_test  : liste de points (list of list)
    - k       : entier
    """
    predictions = []
    
    for test_point in X_test:
        # 1. Calcul des distances
        distances = []
        for i in range(len(X_train)):
            dist = euclidean_distance(test_point, X_train[i])
            distances.append((dist, y_train[i]))
            
        # 2. Tri des distances
        triSelection(distances)
        
        # 3. Récupérer les k labels
        k_labels = [label[1] for label in distances[:k]]
        
        # 4. Trouver le label le plus fréquent parmi les k voisins
        predictions.append(frequent(k_labels))
        
    return predictions