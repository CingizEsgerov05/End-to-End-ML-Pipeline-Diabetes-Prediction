from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np
import os

app = FastAPI()

# Load model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "../model/diabetes_model.pkl")

with open(MODEL_PATH, "rb") as f:
    model, scaler = pickle.load(f)

# Request body structure
class Features(BaseModel):
    data: list  # JSON body: {"data": [...]}

@app.get("/")
def home():
    return {"message": "Diabetes Prediction API"}

@app.post("/predict")
async def predict(input: Features):
    try:
        features = np.array(input.data).reshape(1, -1)
        features_scaled = scaler.transform(features)
        prediction = model.predict(features_scaled)[0]
        return {"prediction": int(prediction)}
    except Exception as e:
        return {"error": str(e)}
