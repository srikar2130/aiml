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