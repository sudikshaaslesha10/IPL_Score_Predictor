
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("IPL Score Predictor")

# Team list
teams = [
"Chennai Super Kings",
"Delhi Capitals",
"Kings XI Punjab",
"Kolkata Knight Riders",
"Mumbai Indians",
"Rajasthan Royals",
"Royal Challengers Bangalore",
"Sunrisers Hyderabad"
]

# Team selection
batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", teams)

overs = st.number_input("Overs Completed",0.0,20.0)
runs = st.number_input("Current Runs",0)
wickets = st.number_input("Wickets Lost",0,10)

if st.button("Predict Score"):

    features = np.array([[overs,runs,wickets]])

    prediction = model.predict(features)

    st.success(f"Predicted Final Score: {int(prediction[0])}")
