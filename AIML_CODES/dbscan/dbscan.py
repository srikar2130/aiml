from sklearn.datasets import load_iris
from sklearn.cluster import DBSCAN
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

# DBSCAN Model
dbscan = DBSCAN(
    eps=0.5,
    min_samples=5
)

# Train and Predict
clusters = dbscan.fit_predict(X)

# Add Cluster Labels
X['Cluster'] = clusters

print(X.head())

# Visualize Clusters
plt.scatter(
    X.iloc[:, 0],
    X.iloc[:, 1],
    c=clusters
)

plt.xlabel(iris.feature_names[0])
plt.ylabel(iris.feature_names[1])
plt.title("DBSCAN Clustering")

plt.show()


from sklearn.metrics import silhouette_score

print("Silhouette Score:",
      silhouette_score(X, clusters))