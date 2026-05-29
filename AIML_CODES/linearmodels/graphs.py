
import numpy as np
import matplotlib.pyplot as plt

idx = np.argsort(y_test)

y_test_sorted = y_test.iloc[idx]
y_pred_sorted = y_pred[idx]

plt.figure(figsize=(10,5))

plt.plot(y_test_sorted.values, label='Actual')
plt.plot(y_pred_sorted, label='Predicted')

plt.xlabel('Samples')
plt.ylabel('Target Value')
plt.title('Actual vs Predicted')
plt.legend()

plt.show()




import numpy as np
import matplotlib.pyplot as plt

X_grid = np.linspace(X.min(), X.max(), 100).reshape(-1, 1)

y_grid_pred = poly_model.predict(poly.transform(X_grid))

plt.scatter(X, y, label='Actual Data')
plt.plot(X_grid, y_grid_pred, label='Polynomial Curve')

plt.legend()
plt.show()





