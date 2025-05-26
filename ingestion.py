#this file codes out for loading the data from CSV to SQLite Database 
import pandas as pd
import sqlite3
import os

telco = pd.read_csv("C:\Users\Utkarsh Singh\Downloads\WA_Fn-UseC_-Telco-Customer-Churn.csv")

os.makedirs("../database", exist_ok=True) #to ensure that a folder with the target name exists 


Sqlconn = sqlite3.connect("../database/churn_data.db") # Establishing SqLite connection

# Write to SQLite DB
telco.to_sql("raw_customer_churn", Sqlconn, if_exists="replace", index=False)

Sqlconn.close()
