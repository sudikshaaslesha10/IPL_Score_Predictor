# IPL_Score_Predictor
# 🏏 IPL Score Predictor

A machine learning web app that predicts the final score of an IPL innings in real time — built with Python, Scikit-learn, and Streamlit.

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python) ![Streamlit](https://img.shields.io/badge/Streamlit-1.40%2B-red?logo=streamlit) ![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.4%2B-orange?logo=scikit-learn) ![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Overview

Enter live match details — batting team, bowling team, current score, overs bowled, wickets fallen, and recent run rate — and the app instantly predicts what the batting team is likely to finish on.

The model is trained on **IPL delivery-level data from 2008 to 2024** and automatically retrains itself on first launch if no compatible model file is found, so it always works regardless of the environment.

---

## 🚀 Live Demo

👉 [Open the App on Streamlit Cloud](https://iplscorepredictor-sdvh2z8jcdqcxal5jbhyn9.streamlit.app/)

---

## 🎯 Features

- 🔮 **Real-time score prediction** based on live match inputs
- 🤖 **Auto-retraining** — no need to manually manage `model.pkl`
- 📊 **Confidence range** shown alongside the predicted score
- 🏟️ Supports all **10 current IPL franchises**
- ⚡ Fast and lightweight — model compressed to under 5 MB
- ☁️ Fully deployable on **Streamlit Cloud** with zero config

---

## 🧠 How It Works

```
Live Match Inputs
      ↓
Feature Engineering (one-hot encoding, balls bowled, etc.)
      ↓
Random Forest Regressor (trained on 50,000 IPL deliveries)
      ↓
Predicted Final Score ± confidence range
```

### Input Features

| Feature | Description |
|---|---|
| Batting Team | One of 10 current IPL teams |
| Bowling Team | One of 10 current IPL teams |
| Current Score | Runs scored so far |
| Overs Completed | Full overs bowled |
| Balls in Current Over | 0–5 |
| Wickets Fallen | Total wickets lost |
| Runs in Last 30 Balls | Recent scoring rate (last 5 overs) |
| Wickets in Last 30 Balls | Recent wicket loss rate |

> ⚠️ Predictions are most accurate after **5 overs (30 balls)** have been bowled — this matches the training data range.

---

## 🗂️ Project Structure

```
ipl_score_predictor/
│
├── app.py                  # Main Streamlit app (includes auto-retrain logic)
├── ipl_cleaned_data.csv    # Preprocessed IPL dataset (2008–2024, 1st innings only)
├── requirements.txt        # Python dependencies
├── IPL_Score_Pred.ipynb    # Training notebook with full EDA and pipeline
└── README.md
```

> `model.pkl` is not committed to the repo. It is generated automatically on first run from `ipl_cleaned_data.csv`.


### Data Pipeline

- Source: Ball-by-ball IPL delivery data (2008–2024)
- Filtered to **1st innings only**
- Teams standardised (e.g. Delhi Daredevils → Delhi Capitals)
- Defunct franchises removed (Deccan Chargers, Pune Warriors, etc.)
- Early overs removed — only deliveries **after ball 30** used for training
- Final score computed as cumulative total per match

---

## 📈 Sample Prediction

```
Batting Team     : Chennai Super Kings
Bowling Team     : Mumbai Indians
Current Score    : 87
Overs Completed  : 10
Wickets Fallen   : 2
Runs Last 30     : 42
Wickets Last 30  : 1

🏏 Predicted Final Score: 172 runs
📊 Likely Range: 162 – 182 runs
```

---

## 🙋‍♀️ Author

**Sudiksha Aslesha**
Data Analyst | Python • SQL • Power BI • Machine Learning

[![LinkedIn](https://img.shields.io/badge/LinkedIn-sudiksha--aslesha-blue?logo=linkedin)](https://linkedin.com/in/sudiksha-aslesha)
[![GitHub](https://img.shields.io/badge/GitHub-sudikshaaslesha10-black?logo=github)](https://github.com/sudikshaaslesha10)

---
