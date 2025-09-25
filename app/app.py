import streamlit as st
import joblib
import pandas as pd

st.title("🏠 House Price Predictor")
locality_options = [
    "BTM Layout", "Attibele", "K R Puram", "Marathahalli",
    "Indiranagar", "Electronic City", "Yalahanka",
    "Malleshwaram", "Jayanagar", "Missing"
]
facing_options = ["North", "South", "East", "West", "Missing"]
parking_options= ['Bike', 'Bike and Car', 'Car', 'Missing']
model = joblib.load("../model.pkl")

with st.form("predict"):
    rent = st.number_input("Monthly Rent", value=15000)
    area = st.number_input("Square Feet", value=1000)
    locality = st.selectbox("Locality", locality_options, index=len(locality_options)-1)   
    BHK = st.number_input("Bedrooms", value=2, min_value=0, max_value=10, step=1)
    parking = st.selectbox("Parking", parking_options, index=len(parking_options)-1)
    bathrooms = st.number_input("Bathrooms", value=2, min_value=0, max_value=10, step=1)
    facing = st.selectbox("Facing", facing_options, index=0)
    submitted = st.form_submit_button("Predict")
    

if submitted:
    X = pd.DataFrame([{
        "rent": rent,
        "area": area,
        "locality": locality if locality else "Missing",
        "BHK": BHK,
        "parking": parking if parking else "Missing",
        "facing": facing if facing else "Missing",
        "bathrooms": bathrooms
    }])
    pred = model.predict(X)[0]
    st.success(f"Predicted Price: {pred:,.2f}")
