from sklearn.datasets import load_iris
from sklearn.cluster import KMeans
import pandas as pd
import matplotlib.pyplot as plt

# Load Dataset
iris = load_iris()

X = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

# K-Means Model
kmeans = KMeans(
    n_clusters=3,
    random_state=42
)

# Train and Predict Clusters
clusters = kmeans.fit_predict(X)

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
plt.title("K-Means Clustering")

plt.show()



# import pandas as pd
# from sklearn.cluster import KMeans

# df = pd.read_csv("data.csv")

# kmeans = KMeans(
#     n_clusters=3,
#     random_state=42
# )

# clusters = kmeans.fit_predict(df)

# print(clusters)


from sklearn.metrics import silhouette_score

print("Silhouette Score:",
      silhouette_score(X, clusters))