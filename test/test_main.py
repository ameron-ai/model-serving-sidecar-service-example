from service import main


def test_predict():
  features = main.Features(
      feature_one=1,
      feature_two=2,
      feature_three="3")

  request = main.PredictionRequest(features=features)

  response = main.predict(request)

  assert response is not None
  assert response.prediction is not None
  assert response.prediction.value is not None

  assert response.prediction.value['class'] == 'Cat'
