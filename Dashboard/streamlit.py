import streamlit as st
import joblib
import pandas as pd

model = joblib.load("C:\Projects\Local-Churn-Analytics-Pipeline\ML\rf_churn_model.pkl")

st.title('Customer Churn Prediction Demo')

# Inputs 
tenure = st.slider('Customer Tenure (months)', 0, 72, 12)
monthly_charges = st.number_input('Monthly Charges', 10, 200, 70)

input_data = pd.DataFrame({
    'tenure': [tenure],
    'MonthlyCharges': [monthly_charges],
    # Add default or median values for all other features
})

prediction = model.predict(input_data)[0]
probability = model.predict_proba(input_data)[0][1]

st.write(f"Churn Prediction: {'Yes' if prediction else 'No'}")
st.write(f"Churn Probability: {probability:.2%}")
