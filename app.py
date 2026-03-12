
import streamlit as st
import pickle
import numpy as np

# Load model
model = pickle.load(open("model.pkl","rb"))

st.title("IPL Score Predictor")

st.write("Enter match details")

overs = st.number_input("Overs Completed",0.0,20.0)
runs = st.number_input("Current Runs",0)
wickets = st.number_input("Wickets Lost",0,10)

if st.button("Predict Score"):

    features = np.array([[overs,runs,wickets]])

    prediction = model.predict(features)

    st.success(f"Predicted Final Score: {int(prediction[0])}")
