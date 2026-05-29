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