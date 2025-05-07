from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
from ollama import Client
import logging

logging.basicConfig(level=logging.INFO)

# Create FastAPI app
app = FastAPI(title="IPL Match Predictor with LLM & Score Prediction")

# === Load Models === #

# Match winner prediction model and encoder
WINNER_MODEL_PATH = os.path.abspath("../../models/match_winner_xgb_model.pkl")
ENCODER_PATH = os.path.abspath("../../models/team_label_encoder.pkl")
model = joblib.load(WINNER_MODEL_PATH)
encoder = joblib.load(ENCODER_PATH)

# Team score prediction model and encoders
SCORE_MODEL_PATH = os.path.abspath("../../models/score_predictor_model.pkl")
SCORE_ENCODERS_PATH = os.path.abspath("../../models/score_label_encoders.pkl")
score_model = joblib.load(SCORE_MODEL_PATH)
score_encoders = joblib.load(SCORE_ENCODERS_PATH)

# Ollama client
ollama_client = Client(host="http://localhost:11434")

# === Schemas === #

class MatchInput(BaseModel):
    team1: str
    team2: str
    team1_score: int

class ScoreInput(BaseModel):
    home_team: str
    away_team: str
    toss_won: str
    decision: str
    venue_name: str

# === Routes === #

@app.get("/")
def root():
    return {"message": "API is running"}

@app.post("/predict")
def predict_match(input: MatchInput):
    try:
        team1_encoded = encoder.transform([input.team1])[0]
        team2_encoded = encoder.transform([input.team2])[0]

        X = np.array([[team1_encoded, team2_encoded, input.team1_score]])
        prediction = model.predict(X)[0]

        predicted_team = input.team1 if prediction == 0 else input.team2

        return {
            "predicted_winner": predicted_team,
            "input": input.dict()
        }
    except Exception as e:
        return {"error": str(e)}

@app.post("/reason")
def reason_match(input: MatchInput):
    prompt = f"""
    In an IPL match:
    - {input.team1} batted first and scored {input.team1_score} runs
    - {input.team2} is yet to bat

    Based on this score and past IPL match dynamics, which team is more likely to win and why?
    Keep the explanation short and analytical.
    """

    try:
        response = ollama_client.chat(model="llama3", messages=[
            {"role": "user", "content": prompt}
        ])
        return {"llm_reasoning": response['message']['content'].strip()}
    except Exception as e:
        return {"error": str(e)}

@app.post("/predict-score")
def predict_score(data: ScoreInput):
    try:
        # Encode all input fields using saved label encoders
        encoded_input = []
        for field in data.dict():
            value = getattr(data, field)
            if field not in score_encoders:
                return {"error": f"Encoder missing for: {field}"}
            encoder = score_encoders[field]
            try:
                encoded_val = encoder.transform([value])[0]
            except ValueError:
                return {"error": f"Invalid input: '{value}' not recognized for '{field}'"}
            encoded_input.append(encoded_val)

        predicted_score = float(score_model.predict([encoded_input])[0])
        rounded_score = round(predicted_score, 2)

        logging.info(f"[Predict Score] Input: {data.dict()} → Encoded: {encoded_input} → Score: {rounded_score}")

        return {
            "predicted_score": rounded_score,
            "model_version": "1.0"
        }

    except Exception as e:
        return {"error": str(e)}

@app.get("/health")
def health_check():
    return {"status": "ok", "message": "Score predictor running"}
