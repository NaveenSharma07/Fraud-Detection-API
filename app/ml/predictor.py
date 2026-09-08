import joblib

model = joblib.load("app/ml/fraud_model.pkl")

def get_score(features):

    prediction = model.predict([features])[0]

    return prediction