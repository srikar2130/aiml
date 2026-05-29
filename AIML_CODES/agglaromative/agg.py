from sklearn.datasets import load_iris
from sklearn.cluster import AgglomerativeClustering
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

# Agglomerative Clustering
agg = AgglomerativeClustering(
    n_clusters=3
)

clusters = agg.fit_predict(X)

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
plt.title("Agglomerative Clustering")

plt.show()


from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

linked = linkage(X.iloc[:, :-1], method='ward')

plt.figure(figsize=(10,5))

dendrogram(linked)

plt.title("Dendrogram")
plt.xlabel("Samples")
plt.ylabel("Distance")

plt.show()
from sklearn.metrics import silhouette_score

print("Silhouette Score:",
      silhouette_score(X, clusters))