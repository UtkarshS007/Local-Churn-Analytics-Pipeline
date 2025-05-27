#feature engineering
import pandas as pd
import sqlite3

Sqlconn = sqlite3.connect("C:/Projects/Local-Churn-Analytics-Pipeline/database/churn_data.db")

telco = pd.read_sql("SELECT * FROM raw_customer_churn", Sqlconn) 

telco.replace(' ', pd.NA, inplace=True)
telco.dropna(inplace=True)                   # dropping NA Columns

telco['SeniorCitizen'] = telco['SeniorCitizen'].map({0: 'No', 1: 'Yes'}) #encoding Senior Citizen 
telco['TotalCharges'] = pd.to_numeric(telco['TotalCharges']) 

# Limit categories for high-cardinality features
categorical_cols = telco.select_dtypes(include=['object']).columns
for col in categorical_cols:
    if telco[col].nunique() > 10:
        top_categories = telco[col].value_counts().nlargest(10).index
        telco[col] = telco[col].apply(lambda x: x if x in top_categories else 'Other')


categorical_cols = telco.select_dtypes(include=['object']).columns # Encoding categorical variables
telco_encoded = pd.get_dummies(telco, columns=categorical_cols, drop_first=True)

# Saving the transformed data back to SQLite
telco_encoded.to_sql("customer_churn_features", Sqlconn, if_exists="replace", index=False)

Sqlconn.close()
