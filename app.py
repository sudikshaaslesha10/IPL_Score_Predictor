
import streamlit as st
import joblib
import numpy as np

# Load model
model = joblib.load("model.pkl")

st.title("IPL Score Predictor")

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

batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", teams)

# Overs and balls
overs = st.number_input("Overs Completed", min_value=0, max_value=19, step=1)
balls = st.selectbox("Balls in current over", [0,1,2,3,4,5])

balls_bowled = overs*6 + balls

current_score = st.number_input("Current Score",0)
wickets_fallen = st.number_input("Wickets Fallen",0,10)

runs_last_30 = st.number_input("Runs in Last 30 Balls",0)
wickets_last_30 = st.number_input("Wickets in Last 30 Balls",0)

if st.button("Predict Score"):

    features = np.array([[batting_team,
                          bowling_team,
                          current_score,
                          balls_bowled,
                          wickets_fallen,
                          runs_last_30,
                          wickets_last_30]])

    prediction = model.predict(features)

    st.success(f"Predicted Score: {int(prediction[0])}")
