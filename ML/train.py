import sqlite3
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, roc_auc_score
import joblib

Sqlconn = sqlite3.connect("../database/churn_data.db")
telco = pd.read_sql("SELECT * FROM customer_churn_features", Sqlconn)
Sqlconn.close()

X = telco.drop('Churn_Yes', axis=1)
y = telco['Churn_Yes']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

# Train RandomForest
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print("ROC AUC Score:", roc_auc_score(y_test, model.predict_proba(X_test)[:,1]))

# Save Model
joblib.dump(model, 'rf_churn_model.pkl')
