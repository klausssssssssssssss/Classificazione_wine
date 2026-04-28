from fastapi import FastAPI
from app.model import Wine
import joblib
import pandas as pd
import numpy as np

app = FastAPI()

# carica modello (con pipeline inclusa)
mlr_model= joblib.load("models/mlr_model_pipe.joblib")
knn_model = joblib.load("models/knn_model_pipe.joblib")
columns = joblib.load("models/columns.joblib")

# -------------------------
# TEST ENDPOINT
# -------------------------

@app.get("/")
def read_root():
    return {"message": "Hello FastAPI"}


# -------------------------
# PREDICTION ENDPOINT
# -------------------------
@app.post("/predict/mlr")
def predict(data: Wine):
    df = pd.DataFrame([data.model_dump()]) 
    df = df[columns]

    pred = mlr_model.predict(df)[0]
    
    if isinstance(pred, np.generic):
        pred = pred.item()

    return {"Category": pred}



@app.post("/predict/knn")
def predict(data: Wine):
    df = pd.DataFrame([data.model_dump()]) 
    df = df[columns]

    pred = knn_model.predict(df)[0]
    
    if isinstance(pred, np.generic):
        pred = pred.item()

    return {"Category": pred}

 
    
# TO RUN ON TERMINAL DO : uvicorn app.main:app --reload