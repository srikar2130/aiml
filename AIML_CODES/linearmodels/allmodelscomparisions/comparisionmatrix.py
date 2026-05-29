import numpy as np
import pandas as pd

from sklearn.datasets import make_regression
from sklearn.model_selection import KFold, cross_val_score
from sklearn.pipeline import Pipeline
from sklearn.feature_selection import SelectKBest, f_regression

from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet
from sklearn.metrics import make_scorer, mean_squared_error

# Sample data (replace with your dataset)
X, y = make_regression(n_samples=500, n_features=20, noise=10, random_state=42)

# Models
models = {
    "Linear Regression": LinearRegression(),
    "L1 (Lasso)": Lasso(alpha=0.1),
    "L2 (Ridge)": Ridge(alpha=1.0),
    "Elastic Net": ElasticNet(alpha=0.1, l1_ratio=0.5)
}

# k values = number of selected features
k_values = [2, 5, 10, 15, 20]

# CV setup
kf = KFold(n_splits=5, shuffle=True, random_state=42)

# Metric (RMSE)
rmse_scorer = make_scorer(mean_squared_error, squared=False)

# Result table
results = pd.DataFrame(index=models.keys(), columns=k_values)

# Loop
for k in k_values:
    for name, model in models.items():
        
        pipeline = Pipeline([
            ("feature_selection", SelectKBest(score_func=f_regression, k=k)),
            ("model", model)
        ])
        
        scores = cross_val_score(pipeline, X, y, cv=kf, scoring=rmse_scorer)
        results.loc[name, k] = np.mean(scores)

# Convert to float
results = results.astype(float)

print(results)