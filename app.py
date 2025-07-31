import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Load the trained model
model = joblib.load("model.pkl")

# App title
st.title("🏠 Melbourne Housing Price Predictor")
st.markdown("Enter property details to predict the selling price.")

# Input fields
rooms = st.number_input("Number of Rooms", min_value=1, max_value=10, value=3)
building_area = st.number_input("Building Area (in m²)", min_value=10, max_value=1000, value=120)

# Add more inputs here as per your model features
# Example: location, bathrooms, etc.

# When user clicks the button
if st.button("Predict Price"):
    input_data = pd.DataFrame([[rooms, building_area]], columns=["Rooms", "BuildingArea"])
    prediction = model.predict(input_data)[0]
    st.success(f"🏷️ Estimated Price: ${prediction:,.2f}")
