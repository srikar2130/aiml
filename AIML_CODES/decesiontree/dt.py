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