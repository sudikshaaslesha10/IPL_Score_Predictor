
import streamlit as st
import numpy as np
import joblib

# Load trained model
model = joblib.load("model.pkl")

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
team_encoding = {team: i for i, team in enumerate(teams)}

# Team selection
batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", [t for t in teams if t != batting_team])

# Match inputs
current_score = st.number_input("Current Score", min_value=0, step=1)
overs = st.number_input("Overs Completed", min_value=0, max_value=19, step=1)
balls = st.selectbox("Balls in Current Over", [0, 1, 2, 3, 4, 5])
balls_bowled = int(overs) * 6 + int(balls)
wickets_fallen = st.number_input("Wickets Fallen", min_value=0, max_value=10, step=1)
runs_last_30 = st.number_input("Runs in Last 30 Balls", min_value=0, step=1)
wickets_last_30 = st.number_input("Wickets in Last 30 Balls", min_value=0, max_value=10, step=1)

if st.button("Predict Score"):

    # Guard: must have bowled at least 1 ball
    if balls_bowled == 0:
        st.warning("⚠️ Please enter at least 1 ball bowled before predicting.")
    elif batting_team == bowling_team:
        st.warning("⚠️ Batting and Bowling teams cannot be the same.")
    else:
        batting_encoded = team_encoding[batting_team]
        bowling_encoded = team_encoding[bowling_team]

        # Derived features
        runs_per_ball = current_score / balls_bowled if balls_bowled > 0 else 0
        wickets_remaining = 10 - int(wickets_fallen)

        # Build feature array — edit this block to match your training features exactly
        features = np.array([[
            batting_encoded,
            bowling_encoded,
            int(current_score),
            balls_bowled,
            int(wickets_fallen),
            int(runs_last_30),
            int(wickets_last_30),
            round(runs_per_ball, 4),
            wickets_remaining
        ]], dtype=float)

        # Debug line — remove after fixing
        st.write(f"🔍 Features passed: {features.shape[1]} | Model expects: {model.n_features_in_}")

        if features.shape[1] != model.n_features_in_:
            st.error(
                f"❌ Feature mismatch: app is sending {features.shape[1]} features "
                f"but model expects {model.n_features_in_}. "
                f"Adjust the features array to match your training data."
            )
        else:
            prediction = model.predict(features)
            predicted = int(prediction[0])

            st.success(f"🏏 Predicted Final Score: **{predicted} runs**")

            # Confidence range
            st.info(f"📊 Likely Range: **{predicted - 10} – {predicted + 10} runs**")
