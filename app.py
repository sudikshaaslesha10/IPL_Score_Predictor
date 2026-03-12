# app.py
import streamlit as st
import pickle
import os

# -----------------------------
# 1. Load the model safely
# -----------------------------
# Local path (Windows)
local_model_path = r"C:\Users\Sudiksha Aslesha\ipl_score_predictor\model.pkl"

# Streamlit / Hugging Face: if deployed, assume model is in the repo root
deployed_model_path = "model.pkl"

# Choose correct path
if os.path.exists(local_model_path):
    model_path = local_model_path
elif os.path.exists(deployed_model_path):
    model_path = deployed_model_path
else:
    st.error("Model file not found. Please check the path!")
    st.stop()

# Load the model
with open(model_path, "rb") as f:
    model = pickle.load(f)

# -----------------------------
# 2. Streamlit app UI
# -----------------------------
st.title("IPL Score Predictor")

st.write("Enter match details to predict the final IPL score:")

# Example input fields
team1 = st.selectbox("Select Batting Team", ["Mumbai Indians", "Chennai Super Kings", "RCB", "KKR"])
team2 = st.selectbox("Select Bowling Team", ["Mumbai Indians", "Chennai Super Kings", "RCB", "KKR"])
overs = st.number_input("Overs Completed", min_value=0.0, max_value=20.0, step=0.1)
runs = st.number_input("Current Runs", min_value=0, step=1)
wickets = st.number_input("Wickets Lost", min_value=0, max_value=10, step=1)

# Predict button
if st.button("Predict Score"):
    # Replace this with actual feature preprocessing
    features = [[overs, runs, wickets]]  # Example: simple numeric input
    predicted_score = model.predict(features)[0]
    st.success(f"Predicted Final Score: {int(predicted_score)}")