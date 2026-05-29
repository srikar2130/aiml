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