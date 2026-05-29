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