import streamlit as st
import numpy as np
import pickle

model = pickle.load(open("calorie_model.pkl", "rb"))

st.title("CaloriFit 🔥")
st.subheader("AI-Powered Calorie Burn Prediction")

age = st.number_input("Age", min_value=1, max_value=100)

gender = st.selectbox(
    "Gender",
    ["male", "female"]
)

height = st.number_input("Height (cm)", min_value=100.0)

weight = st.number_input("Weight (kg)", min_value=20.0)

duration = st.number_input("Duration (minutes)", min_value=1.0)

heart_rate = st.number_input("Heart Rate", min_value=40.0)

body_temp = st.number_input("Body Temperature (°C)", min_value=35.0)

gender = 0 if gender == "male" else 1

if st.button("Predict Calories"):

    features = np.array([
        gender,
        age,
        height,
        weight,
        duration,
        heart_rate,
        body_temp
    ]).reshape(1, -1)

    prediction = model.predict(features)

    st.success(
        f"🔥 Estimated Calories Burned: {prediction[0]:.2f} kcal"
    )