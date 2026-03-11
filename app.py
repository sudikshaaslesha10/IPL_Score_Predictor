import streamlit as st
import pandas as pd
import pickle

# Load trained model
model = pickle.load(open("model.pkl", "rb"))

st.title("🏏 IPL Score Predictor")

st.write("Predict the final score of the first innings")

# Team list
teams = [
'Chennai Super Kings',
'Mumbai Indians',
'Royal Challengers Bangalore',
'Kolkata Knight Riders',
'Delhi Capitals',
'Sunrisers Hyderabad',
'Rajasthan Royals',
'Punjab Kings'
]

# UI Inputs
batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", teams)

current_score = st.number_input("Current Score", min_value=0)

balls_bowled = st.number_input("Balls Bowled", min_value=0, max_value=120)

wickets = st.number_input("Wickets Fallen", min_value=0, max_value=10)

runs_last_30 = st.number_input("Runs in Last 5 Overs", min_value=0)

wickets_last_30 = st.number_input("Wickets in Last 5 Overs", min_value=0, max_value=10)

# Prediction button
if st.button("Predict Score"):

    input_data = pd.DataFrame({
        'current_score':[current_score],
        'balls_bowled':[balls_bowled],
        'wickets':[wickets],
        'runs_last_30':[runs_last_30],
        'wickets_last_30':[wickets_last_30]
    })

    prediction = model.predict(input_data)

    st.success(f"Predicted Final Score: {int(prediction[0])}")