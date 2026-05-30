def astar(graph, start, goal, heuristic):
    open_list = [(0, start)]
    closed_list = set()
    g = {start: 0}
    parent = {start: start}
    while open_list:
        open_list.sort()
        current = open_list.pop(0)[1]
        if current == goal:
            path = []
            while parent[current] != current:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path
        closed_list.add(current)
        for neighbor, cost in graph[current]:
            if neighbor in closed_list:
                continue
            new_g = g[current] + cost
            if neighbor not in g or new_g < g[neighbor]:
                g[neighbor] = new_g
                f = new_g + heuristic[neighbor]
                open_list.append((f, neighbor))
                parent[neighbor] = current
    return None
graph = {
    'A': [('B', 1), ('C', 3)],
    'B': [('A', 1), ('C', 1), ('D', 5)],
    'C': [('A', 3), ('B', 1), ('D', 2)],
    'D': [('B', 5), ('C', 2)]
}
heuristic = {
    'A': 4,
    'B': 3,
    'C': 1,
    'D': 0
}
path = astar(graph, 'A', 'D', heuristic)
print("Path Found:", path)
////////////////////////////////////////////////////////////////////////////////////////////////
import heapq
def heuristic(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])
def astar(grid, start, goal):
    rows = len(grid)
    cols = len(grid[0])
    open_list = []
    heapq.heappush(open_list, (0, start))
    came_from = {}
    g_score = {start: 0}
    while open_list:
        current = heapq.heappop(open_list)[1]
        if current == goal:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            path.reverse()
            return path
        x, y = current
        neighbors = [
            (x+1, y),
            (x-1, y),
            (x, y+1),
            (x, y-1)
        ]
        for nx, ny in neighbors:
            if 0 <= nx < rows and 0 <= ny < cols:
                if grid[nx][ny] == 1:
                    continue
                tentative_g = g_score[current] + 1
                if (nx, ny) not in g_score or tentative_g < g_score[(nx, ny)]:
                    g_score[(nx, ny)] = tentative_g
                    f_score = tentative_g + heuristic((nx, ny), goal)
                    heapq.heappush(
                        open_list,
                        (f_score, (nx, ny))
                    )
                    came_from[(nx, ny)] = current
    return None
grid = [
    [0,0,0,0],
    [1,1,0,1],
    [0,0,0,0],
    [0,1,1,0]
]
start = (0,0)
goal = (3,3)
path = astar(grid, start, goal)
print("Path:")
print(path)
////////////////////////////////////////////////////////////////////////////////////////////////
import heapq
GOAL = ((1, 2, 3),
        (4, 5, 6),
        (7, 8, 0))
goal_pos = {
    1: (0, 0), 2: (0, 1), 3: (0, 2),
    4: (1, 0), 5: (1, 1), 6: (1, 2),
    7: (2, 0), 8: (2, 1)
}
def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                x, y = goal_pos[value]
                distance += abs(i - x) + abs(j - y)
    return distance
def get_neighbors(state):
    state = [list(row) for row in state]
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                x, y = i, j
                break
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    neighbors = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[nx][ny] = (
                new_state[nx][ny],
                new_state[x][y]
            )
            neighbors.append(tuple(tuple(row) for row in new_state))
    return neighbors
def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start))
    parent = {}
    g_cost = {start: 0}
    while pq:
        f, g, current = heapq.heappop(pq)
        if current == GOAL:
            path = []
            while current in parent:
                path.append(current)
                current = parent[current]
            path.append(start)
            path.reverse()
            return path
        for neighbor in get_neighbors(current):
            new_g = g + 1
            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                h = manhattan(neighbor)
                heapq.heappush(pq, (new_g + h, new_g, neighbor))
                parent[neighbor] = current
    return None
# Example Start State
start = ((1, 2, 3),
         (4, 0, 6),
         (7, 5, 8))
solution = a_star(start)
if solution:
    print("Solution found in", len(solution) - 1, "moves\n")
    for step in solution:
        for row in step:
            print(row)
        print()
else:
    print("No solution found")
////////////////////////////////////////////////////////////////////////////////////////////////////////
class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
def minimax(node, maximizing_player):
    # Leaf node
    if len(node.children) == 0:
        return node.value
    if maximizing_player:
        best = float('-inf')
        for child in node.children:
            best = max(best, minimax(child, False))
        return best
    else:
        best = float('inf')
        for child in node.children:
            best = min(best, minimax(child, True))
        return best
# Create Tree
root = Node()
A = Node()
B = Node()
root.children = [A, B]
C = Node()
D = Node()
E = Node()
F = Node()
A.children = [C, D]
B.children = [E, F]
# Leaf Nodes
C.children = [Node(3), Node(5)]
D.children = [Node(6), Node(9)]
E.children = [Node(1), Node(2)]
F.children = [Node(0), Node(-1)]
result = minimax(root, True)
print("Optimal Value =", result)
/////////////////////////////////////////////////////////////////////////////////////////////////////
class Node:
    def __init__(self, value=None):
        self.value = value
        self.children = []
def alpha_beta(node, depth, alpha, beta, maximizing):
    # Leaf node
    if len(node.children) == 0:
        return node.value
    if maximizing:
        best = float('-inf')
        for child in node.children:
            value = alpha_beta(
                child,
                depth + 1,
                alpha,
                beta,
                False
            )
            best = max(best, value)
            alpha = max(alpha, best)
            # Pruning
            if beta <= alpha:
                break
        return best
    else:
        best = float('inf')
        for child in node.children:
            value = alpha_beta(
                child,
                depth + 1,
                alpha,
                beta,
                True
            )
            best = min(best, value)
            beta = min(beta, best)
            # Pruning
            if beta <= alpha:
                break
        return best
# Create Tree
root = Node()
A = Node()
B = Node()
root.children = [A, B]
C = Node()
D = Node()
E = Node()
F = Node()
A.children = [C, D]
B.children = [E, F]
C.children = [Node(3), Node(5)]
D.children = [Node(6), Node(9)]
E.children = [Node(1), Node(2)]
F.children = [Node(0), Node(-1)]
result = alpha_beta(
    root,
    0,
    float('-inf'),
    float('inf'),
    True
)
print("Optimal Value =", result)
///////////////////////////////////////////////////////////////////////////////////////////////////////////
def is_safe(vertex, graph, coloring, color):
    for neighbor in graph[vertex]:
        if neighbor in coloring and coloring[neighbor] == color:
            return False
    return True
def graph_coloring(graph, colors, coloring, vertices, index):
    if index == len(vertices):
        return True
    vertex = vertices[index]
    for color in colors:
        if is_safe(vertex, graph, coloring, color):
            coloring[vertex] = color
            if graph_coloring(graph, colors, coloring, vertices, index + 1):
                return True
            del coloring[vertex]
    return False
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}
colors = ['Red', 'Green', 'Blue']
coloring = {}
vertices = list(graph.keys())
if graph_coloring(graph, colors, coloring, vertices, 0):
    print("Solution:")
    for vertex, color in coloring.items():
        print(vertex, "->", color)
else:
    print("No solution exists")
# def is_safe(v, graph, color, c):
#     for i in range(len(graph)):
#         if graph[v][i] == 1 and color[i] == c:
#             return False
#     return True
# def graph_coloring_util(graph, m, color, v):
#     if v == len(graph):
#         return True
#     for c in range(1, m + 1):
#         if is_safe(v, graph, color, c):
#             color[v] = c
#             if graph_coloring_util(graph, m, color, v + 1):
#                 return True
#             color[v] = 0
#     return False
# def graph_coloring(graph, m):
#     n = len(graph)
#     color = [0] * n
#     if not graph_coloring_util(graph, m, color, 0):
#         print("No solution exists")
#         return False
#     print("Solution Found:")
#     for i in range(n):
#         print(f"Vertex {i} ---> Color {color[i]}")
#     return True
# graph = [
#     [0, 1, 1, 1],
#     [1, 0, 1, 0],
#     [1, 1, 0, 1],
#     [1, 0, 1, 0]
# ]
# m = 3
# graph_coloring(graph, m)
///////////////////////////////////////////////////////////////////////////////////////////////////////
from collections import deque
def water_jug_bfs(cap1, cap2, target):
    visited = set()
    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        print((x, y))
        if x == target or y == target:
            print("Goal Reached")
            return
        next_states = [
            (cap1, y),
            (x, cap2),
            (0, y),
            (x, 0),
            (x - min(x, cap2-y),
             y + min(x, cap2-y)),
            (x + min(y, cap1-x),
             y - min(y, cap1-x))
        ]
        for state in next_states:
            if state not in visited:
                queue.append(state)
water_jug_bfs(4, 3, 2)
///////////////////////////////////////////////////////////////////////////////////////////////////////////
# drop multiple columns at once
df = df.drop(columns=["col1", "col2", "col3"])
# errors calculation
from sklearn.metrics import mean_squared_error
mse = mean_squared_error(y_test, y_pred)
print(mse)
rmse = mean_squared_error(y_test, y_pred, squared=False)
print(rmse)
from sklearn.metrics import r2_score
r2 = r2_score(y_test, y_pred)
print(r2)
from sklearn.metrics import mean_absolute_error
mae = mean_absolute_error(y_test, y_pred)
df["name"] = df["name"].str.lower()
df["name"] = df["name"].str.upper()
df["name"] = df["name"].str.strip()   # remove spaces
df["name"] = df["name"].str.replace("old", "new")
import pandas as pd
df = pd.DataFrame({
    "price": ["1000 old", "2000 old", "3000 old"]
})
# Remove ' old' and convert to int
df["price"] = df["price"].str.replace(" old", "", regex=False).astype(int)
print(df)
df["price"] = df["price"].str.extract(r"(\d+)").astype(int)
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df["color"] = le.fit_transform(df["color"])
df = pd.get_dummies(df, columns=["color"])
df["city"] = df["city"].str.lower().str.strip()
df["city"] = df["city"].replace({"new york": "NY"})
df = pd.get_dummies(df, columns=["city"])
import numpy as np
df["column_name"] = df["column_name"].replace("?", np.nan)
df["column_name"] = pd.to_numeric(df["column_name"])
df["column_name"].fillna(df["column_name"].mean(), inplace=True)
df["column_name"].fillna(df["column_name"].median(), inplace=True)
df["column_name"].fillna(df["column_name"].mode()[0], inplace=True)
from sklearn.impute import SimpleImputer
imputer = SimpleImputer(strategy="mean")
df[["column_name"]] = imputer.fit_transform(df[["column_name"]])
df["column_name"].nunique()
df["column_name"].unique()
df["column_name"].value_counts()
df["column_name"].nunique(dropna=False)
order = ["low", "medium", "high"]
from sklearn.preprocessing import OrdinalEncoder
encoder = OrdinalEncoder(categories=[order])
df["priority"] = encoder.fit_transform(df[["priority"]])
mapping = {"low": 0, "medium": 1, "high": 2}
df["priority"] = df["priority"].map(mapping)
top_n = 5  # keep top 5 most frequent values
# get top categories
top_categories = df["column"].value_counts().nlargest(top_n).index
# replace others
df["column"] = df["column"].apply(
    lambda x: x if x in top_categories else "Other"
)
df = pd.get_dummies(df, columns=["column"])
threshold = 10  # minimum occurrences
counts = df["column"].value_counts()
df["column"] = df["column"].apply(
    lambda x: x if counts[x] >= threshold else "Other"
)
from sklearn.feature_selection import SelectKBest, f_classif
X = df.drop('target', axis=1)
y = df['target']
selector = SelectKBest(score_func=f_classif, k=3)
X_new = selector.fit_transform(X, y)
print("Selected Features:")
print(X.columns[selector.get_support()])
from sklearn.feature_selection import SelectKBest, f_regression
selector = SelectKBest(score_func=f_regression, k=3)
X_new = selector.fit_transform(X, y)
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(score_func=f_classif, k='all')
selector.fit(X, y)
feature_scores = pd.DataFrame({
    'Feature': X.columns,
    'Score': selector.scores_
})
print(feature_scores.sort_values(
    by='Score',
    ascending=False
))
//////////////////////////////////////////////////////////////////////////////////////////////////////////
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
# from sklearn.model_selection import train_test_split
# X = df.drop('target', axis=1)   # Features
# y = df['target']                # Target
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)
# -------------------------
# 6️⃣ FEATURE SCALING
# -------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
# Train model
model = LinearRegression()
model.fit(X_train, y_train)
# Predictions
y_pred = model.predict(X_test)
# Evaluation
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print("Linear Regression RMSE:", rmse)
print("Linear Regression R2:", r2)
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
# Train model
model = Lasso(alpha=0.1)   # alpha controls regularization strength
model.fit(X_train, y_train)
# Predictions
y_pred = model.predict(X_test)
# Evaluation
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print("Lasso (L1) RMSE:", rmse)
print("Lasso (L1) R2:", r2)
from sklearn.linear_model import Ridge
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
# Train model
model = Ridge(alpha=0.1)
model.fit(X_train, y_train)
# Predictions
y_pred = model.predict(X_test)
# Evaluation
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print("Ridge (L2) RMSE:", rmse)
print("Ridge (L2) R2:", r2)
from sklearn.linear_model import ElasticNet
from sklearn.metrics import mean_squared_error, r2_score
import numpy as np
# Train model
model = ElasticNet(alpha=0.1, l1_ratio=0.5)
model.fit(X_train, y_train)
# Predictions
y_pred = model.predict(X_test)
# Evaluation
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)
print("ElasticNet RMSE:", rmse)
print("ElasticNet R2:", r2)
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
# Features
X = df[['Area', 'Bedrooms', 'Age']]
# Target
y = df['Price']
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
poly = PolynomialFeatures(degree=2)
X_train_poly = poly.fit_transform(X_train)
X_test_poly = poly.transform(X_test)
model = LinearRegression()
model.fit(X_train_poly, y_train)
y_pred = model.predict(X_test_poly)
/////////////////////////////////////////////////////////////////////////////////////////////
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, precision_score, recall_score, classification_report
# -------------------------
# 1️⃣ LOAD DATA
# -------------------------
df = pd.read_csv("your_dataset.csv")
# -------------------------
# 2️⃣ HANDLE MISSING VALUES
# -------------------------
df = df.dropna()   # or use fillna()
# -------------------------
# 3️⃣ SEPARATE FEATURES & TARGET
# -------------------------
X = df.drop("target_column", axis=1)
y = df["target_column"]
# -------------------------
# 4️⃣ ENCODE CATEGORICAL DATA
# -------------------------
for col in X.columns:
    if X[col].dtype == "object":
        le = LabelEncoder()
        X[col] = le.fit_transform(X[col])
# Encode target if needed
if y.dtype == "object":
    le = LabelEncoder()
    y = le.fit_transform(y)
# -------------------------
# 5️⃣ TRAIN-TEST SPLIT
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# -------------------------
# 6️⃣ FEATURE SCALING
# -------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# -------------------------
# 7️⃣ TRAIN LOGISTIC REGRESSION
# -------------------------
model = LogisticRegression()
model.fit(X_train, y_train)
# -------------------------
# 8️⃣ PREDICTIONS
# -------------------------
y_pred = model.predict(X_test)
# -------------------------
# 9️⃣ EVALUATION
# -------------------------
accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred, average='binary')
recall = recall_score(y_test, y_pred, average='binary')
print("Accuracy:", accuracy)
print("Precision:", precision)
print("Recall:", recall)
print("\nDetailed Report:\n")
print(classification_report(y_test, y_pred))
from sklearn.metrics import confusion_matrix
cm = confusion_matrix(y_test, y_pred)
print(cm)
///////////////////////////////////////////////////////////////////////////////////////////////
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report,precision_score,recall_score
# Naive Bayes models
from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
# Preprocessing
from sklearn.preprocessing import StandardScaler, Binarizer
from sklearn.feature_extraction.text import CountVectorizer
# =========================================================
# 1️⃣ GAUSSIAN NAIVE BAYES (for continuous data)
# =========================================================
# Example numeric dataset
X = np.random.rand(200, 5)   # features
y = np.random.randint(0, 2, 200)  # labels
# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# Scaling (important for Gaussian NB)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
# Train
gnb = GaussianNB()
gnb.fit(X_train_scaled, y_train)
# Predict
y_pred_gnb = gnb.predict(X_test_scaled)
print("GaussianNB Accuracy:", accuracy_score(y_test, y_pred_gnb))
print(classification_report(y_test, y_pred_gnb))
# =========================================================
# 2️⃣ MULTINOMIAL NAIVE BAYES (for count data / text)
# =========================================================
# Example text data
texts = [
    "I love machine learning",
    "Naive Bayes is simple",
    "I hate bugs in code",
    "Debugging is fun",
    "I love coding",
    "Machine learning is powerful"
]
labels = [1, 1, 0, 1, 1, 1]
# Convert text → count features
vectorizer = CountVectorizer()
X_counts = vectorizer.fit_transform(texts)
# Split
X_train, X_test, y_train, y_test = train_test_split(X_counts, labels, test_size=0.2, random_state=42)
# Train
mnb = MultinomialNB()
mnb.fit(X_train, y_train)
# Predict
y_pred_mnb = mnb.predict(X_test)
print("\nMultinomialNB Accuracy:", accuracy_score(y_test, y_pred_mnb))
print(classification_report(y_test, y_pred_mnb))
# =========================================================
# 3️⃣ BERNOULLI NAIVE BAYES (for binary features)
# =========================================================
# Example numeric data
X = np.random.rand(200, 5)
y = np.random.randint(0, 2, 200)
# Convert to binary (0/1)
binarizer = Binarizer(threshold=0.5)
X_binary = binarizer.fit_transform(X)
# Split
X_train, X_test, y_train, y_test = train_test_split(X_binary, y, test_size=0.2, random_state=42)
# Train
bnb = BernoulliNB()
bnb.fit(X_train, y_train)
# Predict
y_pred_bnb = bnb.predict(X_test)
print("\nBernoulliNB Accuracy:", accuracy_score(y_test, y_pred_bnb))
print(classification_report(y_test, y_pred_bnb))
////////////////////////////////////////////////////////////////////////////////////////////////////////
from sklearn.preprocessing import LabelEncoder
le = LabelEncoder()
df['species'] = le.fit_transform(df['species'])
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
model = SVC(kernel='rbf')
model.fit(X_train, y_train)
y_pred = model.predict(X_test)
print("Accuracy:", accuracy_score(y_test, y_pred))
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report
# Features and Target
X = df.iloc[:, :-1]
y = df.iloc[:, -1]
# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)
# SVM Model
model = SVC(kernel='linear')
# Train
model.fit(X_train, y_train)
# Predict
y_pred = model.predict(X_test)
# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))
print("\nClassification Report:")
print(classification_report(y_test, y_pred))
//////////////////////////////////////////////////////////////////////////////////
import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
# -------------------------
# 1️⃣ LOAD DATASET
# -------------------------
digits = datasets.load_digits()
X = digits.data       # pixel features
y = digits.target     # labels (0–9)
# -------------------------
# 2️⃣ TRAIN-TEST SPLIT
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
# -------------------------
# 3️⃣ FEATURE SCALING
# -------------------------
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)
# -------------------------
# 4️⃣ TRAIN SVM MODEL
# -------------------------
model = SVC(kernel='rbf', C=1, gamma='scale')
model.fit(X_train, y_train)
# -------------------------
# 5️⃣ PREDICTIONS
# -------------------------
y_pred = model.predict(X_test)
# -------------------------
# 6️⃣ EVALUATION
# -------------------------
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))
print("\nConfusion Matrix:\n")
print(confusion_matrix(y_test, y_pred))
# -------------------------
# 7️⃣ VISUALIZE PREDICTIONS
# -------------------------
plt.figure(figsize=(8,5))
for i in range(5):
    plt.subplot(1,5,i+1)
    plt.imshow(X_test[i].reshape(8,8), cmap='gray')
    plt.title(f"Pred: {y_pred[i]}")
    plt.axis('off')
plt.show()
///////////////////////////////////////////////////////////////////////////////////////////
# ================================
# Decision Tree vs Ensemble Methods
# ================================
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import BaggingClassifier, RandomForestClassifier, AdaBoostClassifier, StackingClassifier
from sklearn.linear_model import LogisticRegression
# ----------------
# 1. Load Dataset
# ----------------
data = load_iris()
X, y = data.data, data.target
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)
results = {}
# ----------------
# 2. Decision Trees (Variants)
# ----------------
# (a) Default Decision Tree
dt = DecisionTreeClassifier(random_state=42)
dt.fit(X_train, y_train)
results["Decision Tree"] = accuracy_score(y_test, dt.predict(X_test))
# (b) Shallow Tree (Underfitting)
dt_shallow = DecisionTreeClassifier(max_depth=2, random_state=42)
dt_shallow.fit(X_train, y_train)
results["Shallow Tree"] = accuracy_score(y_test, dt_shallow.predict(X_test))
# (c) Deep Tree (Overfitting)
dt_deep = DecisionTreeClassifier(max_depth=None, random_state=42)
dt_deep.fit(X_train, y_train)
results["Deep Tree"] = accuracy_score(y_test, dt_deep.predict(X_test))
# (d) Pruned Tree (Balanced)
dt_pruned = DecisionTreeClassifier(max_depth=4, min_samples_split=5, random_state=42)
dt_pruned.fit(X_train, y_train)
results["Pruned Tree"] = accuracy_score(y_test, dt_pruned.predict(X_test))
# ----------------
# 3. Ensemble Methods
# ----------------
# (a) Bagging
bag = BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=50,
    random_state=42
)
bag.fit(X_train, y_train)
results["Bagging"] = accuracy_score(y_test, bag.predict(X_test))
# (b) Random Forest
rf = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)
rf.fit(X_train, y_train)
results["Random Forest"] = accuracy_score(y_test, rf.predict(X_test))
# (c) Boosting (AdaBoost)
boost = AdaBoostClassifier(
    estimator=DecisionTreeClassifier(max_depth=1),
    n_estimators=50,
    random_state=42
)
boost.fit(X_train, y_train)
results["AdaBoost"] = accuracy_score(y_test, boost.predict(X_test))
# (d) Stacking
stack = StackingClassifier(
    estimators=[
        ('dt', DecisionTreeClassifier()),
        ('rf', RandomForestClassifier()),
        ('bag', BaggingClassifier())
    ],
    final_estimator=LogisticRegression()
)
stack.fit(X_train, y_train)
results["Stacking"] = accuracy_score(y_test, stack.predict(X_test))
# ----------------
# 4. Print Results
# ----------------
print("\nModel Performance Comparison:\n")
for model, acc in results.items():
    print(f"{model:20s}: {acc:.4f}")
# ----------------
# 5. Best Model
# ----------------
best_model = max(results, key=results.get)
print(f"\nBest Model: {best_model} with accuracy {results[best_model]:.4f}")
///////////////////////////////////////////////////////////////////////////////////////////////////////////
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
/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
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