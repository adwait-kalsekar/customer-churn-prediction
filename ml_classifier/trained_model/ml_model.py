import numpy as np
import pandas as pd
import joblib

from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier

df = pd.read_csv("ml_classifier/trained_model/Churn_Modelling.csv")

X = df.drop(["Exited", "RowNumber", "CustomerId", "Surname"], axis=1)
y = df.Exited

X_object_type = X.select_dtypes(include='object')

X_numeric_type = X.select_dtypes(exclude='object')

X_object_dummies = pd.get_dummies(X_object_type, drop_first=True)

X = pd.concat([X_numeric_type, X_object_dummies], axis=1)

# {'C': 3792.690190732246, 'penalty': 'l1', 'solver': 'liblinear'}
np.random.seed(111)
final_model_1 = LogisticRegression(solver='liblinear', penalty='l1', C=3792.690190732246)
final_model_1.fit(X, y)

# 
final_model_2 = RandomForestClassifier()
final_model_2.fit(X, y)

score_1 = final_model_1.score(X, y)
score_2 = final_model_2.score(X,y)

# def get_scores():
#     score_1 = final_model_1.score(X, y)
#     score_2 = final_model_2.score(X,y)

#     return (score_1, score_2)

joblib.dump(final_model_1, 'ml_classifier/trained_model/final_model_1.pkl')
joblib.dump(final_model_2, 'ml_classifier/trained_model/final_model_2.pkl')
joblib.dump((score_1, score_2), 'ml_classifier/trained_model/get_scores.pkl')
joblib.dump(list(X.columns), 'ml_classifier/trained_model/col_names.pkl')