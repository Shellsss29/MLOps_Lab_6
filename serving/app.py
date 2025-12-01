import pickle
from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np

class IrisInput(BaseModel):
    features: list

app = FastAPI()

@app.on_event("startup")
def load_model():
    global model
    with open("/model/model.pkl", "rb") as f:
        model = pickle.load(f)
    print("Loaded model for inference.")

@app.post("/predict")
def predict(input: IrisInput):
    sample = np.array(input.features).reshape(1, -1)
    pred = model.predict(sample)
    return {"prediction": int(pred[0])}
