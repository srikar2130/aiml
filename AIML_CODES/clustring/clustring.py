# ==========================================
# Clustering Demo: KMeans, Agglomerative, DBSCAN
# ==========================================

import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris, make_moons
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans, AgglomerativeClustering, DBSCAN
from sklearn.metrics import silhouette_score

# ---------------------------
# 1. Load Standard Datasets
# ---------------------------

# Dataset 1: Iris (real-world structured data)
iris = load_iris()
X1 = iris.data[:, :2]   # take 2 features for visualization

# Dataset 2: Non-linear dataset (for DBSCAN advantage)
X2, _ = make_moons(n_samples=300, noise=0.05, random_state=42)

datasets = {
    "Iris": X1,
    "Moons": X2
}

# ---------------------------
# 2. Clustering Algorithms
# ---------------------------

models = {
    "KMeans": KMeans(n_clusters=3, random_state=42),
    "Agglomerative": AgglomerativeClustering(n_clusters=3, linkage='ward'),
    "DBSCAN": DBSCAN(eps=0.3, min_samples=5)
}

# ---------------------------
# 3. Run & Visualize
# ---------------------------

plt.figure(figsize=(12, 8))
plot_num = 1

for name, X in datasets.items():

    # Normalize data
    X_scaled = StandardScaler().fit_transform(X)

    for model_name, model in models.items():

        # Fit model
        labels = model.fit_predict(X_scaled)

        # Plot
        plt.subplot(len(datasets), len(models), plot_num)
        plt.scatter(X_scaled[:, 0], X_scaled[:, 1], c=labels)

        plt.title(f"{model_name} ({name})")
        plt.xticks([])
        plt.yticks([])

        # Evaluation (skip DBSCAN if only 1 cluster)
        if len(set(labels)) > 1 and model_name != "DBSCAN":
            score = silhouette_score(X_scaled, labels)
            print(f"{model_name} on {name} Silhouette Score: {score:.3f}")
        elif model_name == "DBSCAN":
            unique_labels = set(labels)
            print(f"{model_name} on {name}: clusters={len(unique_labels)- (1 if -1 in labels else 0)}")

        plot_num += 1

plt.tight_layout()
plt.show()