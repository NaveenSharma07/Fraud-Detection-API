import pandas as pd
import joblib
from sklearn.ensemble import IsolationForest

df = pd.read_csv("app/dataset/creditcard.csv")

X = df.drop("Class", axis=1)

model = IsolationForest(
    contamination=0.002,
    random_state=42
)

model.fit(X)

joblib.dump(model,"app/ml/fraud_model.pkl")

print("Model Saved")