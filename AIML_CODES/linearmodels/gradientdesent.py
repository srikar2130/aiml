import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

# -------------------------
# Prepare Data
# -------------------------
X_gd = X_scaled.values              # features
y_gd = y.values.reshape(-1, 1)      # target (column vector)

# -------------------------
# Add bias (intercept term)
# -------------------------
X_b = np.c_[np.ones((X_gd.shape[0], 1)), X_gd]

# -------------------------
# Initialize parameters
# -------------------------
np.random.seed(42)   # for reproducibility
theta = np.random.randn(X_b.shape[1], 1)

# -------------------------
# Hyperparameters
# -------------------------
learning_rate = 0.01
n_iterations = 1000
m = len(y_gd)

# -------------------------
# Gradient Descent
# -------------------------
for i in range(n_iterations):
    predictions = X_b.dot(theta)
    errors = predictions - y_gd
    
    gradients = (2/m) * X_b.T.dot(errors)
    theta = theta - learning_rate * gradients

# -------------------------
# Predictions
# -------------------------
y_pred = X_b.dot(theta)

# -------------------------
# Evaluation
# -------------------------
mse = mean_squared_error(y_gd, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_gd, y_pred)

print("Gradient Descent RMSE:", rmse)
print("Gradient Descent R2:", r2)