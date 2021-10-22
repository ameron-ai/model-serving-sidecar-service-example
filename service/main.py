import datetime
import logging
from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import List, Optional


class Features(BaseModel):
  feature_one: int
  feature_two: int
  feature_three: str


class PredictionRequest(BaseModel):
  features: Features


class Prediction(BaseModel):
  modelName: str
  modelVersion: str

  executedAt: datetime.datetime
  timeTakenInMs: int
  value: dict


class PredictionResponse(BaseModel):
  prediction: Prediction
  secondaryPredictions: Optional[List[Prediction]]


app = FastAPI()


@app.post("/predict")
def predict(prediction_request: PredictionRequest):
  logging.info("Predicting for Features %s", prediction_request)

  # Your prediction code would be called from here
  model_prediction = {'class': 'Cat'}

  prediction = Prediction(
      modelName="test",
      modelVersion="1.0.0",

      executedAt=datetime.datetime.now(),
      timeTakenInMs=10,
      value=model_prediction)

  return PredictionResponse(prediction=prediction)
