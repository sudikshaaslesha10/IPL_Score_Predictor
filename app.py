
import streamlit as st
import numpy as np
import joblib
# Load trained model

@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

st.title("🏏 IPL Score Predictor")

# Current IPL Teams
teams = [
'Chennai Super Kings',
'Delhi Capitals',
'Gujarat Titans',
'Kolkata Knight Riders',
'Lucknow Super Giants',
'Mumbai Indians',
'Punjab Kings',
'Rajasthan Royals',
'Royal Challengers Bengaluru',
'Sunrisers Hyderabad'
]

# Team encoding
team_encoding = {team:i for i,team in enumerate(teams)}

# Team selection
batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", teams)

# Match inputs
current_score = st.number_input("Current Score",0)
overs = st.number_input("Overs Completed",0,19)
balls = st.selectbox("Balls in Current Over",[0,1,2,3,4,5])

balls_bowled = overs*6 + balls

wickets_fallen = st.number_input("Wickets Fallen",0,10)
runs_last_30 = st.number_input("Runs in Last 30 Balls",0)
wickets_last_30 = st.number_input("Wickets in Last 30 Balls",0)

if st.button("Predict Score"):

    batting_team_encoded = team_encoding[batting_team]
    bowling_team_encoded = team_encoding[bowling_team]

    features = np.array([[batting_team_encoded,
                          bowling_team_encoded,
                          current_score,
                          balls_bowled,
                          wickets_fallen,
                          runs_last_30,
                          wickets_last_30]], dtype=float)

    prediction = model.predict(features)

    st.success(f"Predicted Final Score: {int(prediction[0])}")
