import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

from sklearn.linear_model import LinearRegression
from sklearn.linear_model import RidgeCV, LassoCV, ElasticNetCV

# -------------------------
# DATA SPLIT
# -------------------------
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# -------------------------
# SCALING (IMPORTANT)
# -------------------------
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# -------------------------
# 1️⃣ LINEAR REGRESSION
# -------------------------
lin_model = LinearRegression()
lin_model.fit(X_train_scaled, y_train)
y_pred_lin = lin_model.predict(X_test_scaled)

# -------------------------
# 2️⃣ RIDGE (L2)
# -------------------------
alphas = np.logspace(-4, 4, 50)

ridge_model = RidgeCV(alphas=alphas, cv=5)
ridge_model.fit(X_train_scaled, y_train)
y_pred_ridge = ridge_model.predict(X_test_scaled)

# -------------------------
# 3️⃣ LASSO (L1)
# -------------------------
lasso_model = LassoCV(cv=5, max_iter=10000)
lasso_model.fit(X_train_scaled, y_train)
y_pred_lasso = lasso_model.predict(X_test_scaled)

# -------------------------
# 4️⃣ ELASTIC NET (L1 + L2)
# -------------------------
elastic_model = ElasticNetCV(
    l1_ratio=[0.1, 0.3, 0.5, 0.7, 0.9],
    alphas=np.logspace(-4, 2, 30),
    cv=5,
    max_iter=10000
)

elastic_model.fit(X_train_scaled, y_train)
y_pred_elastic = elastic_model.predict(X_test_scaled)

# -------------------------
# EVALUATION FUNCTION
# -------------------------
def evaluate(y_true, y_pred, name):
    mse = mean_squared_error(y_true, y_pred)
    rmse = np.sqrt(mse)
    r2 = r2_score(y_true, y_pred)
    print(f"{name} RMSE:", rmse)
    print(f"{name} R2:", r2)
    print("-" * 40)

# -------------------------
# RESULTS
# -------------------------
evaluate(y_test, y_pred_lin, "Linear")
evaluate(y_test, y_pred_ridge, "Ridge")
evaluate(y_test, y_pred_lasso, "Lasso")
evaluate(y_test, y_pred_elastic, "ElasticNet")

# -------------------------
# BEST PARAMETERS
# -------------------------
print("Best Ridge alpha:", ridge_model.alpha_)
print("Best Lasso alpha:", lasso_model.alpha_)
print("Best ElasticNet alpha:", elastic_model.alpha_)
print("Best ElasticNet l1_ratio:", elastic_model.l1_ratio_)