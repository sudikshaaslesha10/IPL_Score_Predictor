
import streamlit as st
import pandas as pd
import joblib

# Load trained model
try:
    model = joblib.load("model.pkl")
except Exception as e:
    st.error(f"❌ Failed to load model: {e}")
    st.stop()

st.title("🏏 IPL Score Predictor")

# Must match training data exactly
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

# UI Inputs
batting_team = st.selectbox("Batting Team", teams)
bowling_team = st.selectbox("Bowling Team", [t for t in teams if t != batting_team])

current_score   = st.number_input("Current Score", min_value=0, step=1)
overs           = st.number_input("Overs Completed", min_value=0, max_value=19, step=1)
balls           = st.selectbox("Balls in Current Over", [0, 1, 2, 3, 4, 5])
balls_bowled    = int(overs) * 6 + int(balls)
wickets_fallen  = st.number_input("Wickets Fallen", min_value=0, max_value=10, step=1)
runs_last_30    = st.number_input("Runs in Last 30 Balls", min_value=0, step=1)
wickets_last_30 = st.number_input("Wickets in Last 30 Balls", min_value=0, max_value=10, step=1)

if st.button("Predict Score"):

    if balls_bowled < 30:
        st.warning("⚠️ Model works best after 5 overs (30 balls). Please enter more match data.")
        st.stop()

    # Build input dict with numeric features
    input_dict = {
        'current_score':   int(current_score),
        'balls_bowled':    balls_bowled,
        'wickets_fallen':  int(wickets_fallen),
        'runs_last_30':    int(runs_last_30),
        'wickets_last_30': int(wickets_last_30),
    }

    # One-hot encode batting team (10 columns)
    for team in teams:
        input_dict[f'batting_team_{team}'] = 1 if batting_team == team else 0

    # One-hot encode bowling team (10 columns)
    for team in teams:
        input_dict[f'bowling_team_{team}'] = 1 if bowling_team == team else 0

    # Align columns to exact model order
    input_df = pd.DataFrame([input_dict])[model.feature_names_in_]

    # Predict
    try:
        prediction = model.predict(input_df)
        predicted  = int(prediction[0])

        st.success(f"🏏 Predicted Final Score: **{predicted} runs**")
        st.info(f"📊 Likely Range: **{predicted - 10} – {predicted + 10} runs**")

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")
