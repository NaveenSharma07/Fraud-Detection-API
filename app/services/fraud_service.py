from app.ml.predictor import get_score

HIGH_RISK_COUNTRIES = ["RU","KP","IR"]

def predict_transaction(tx):

    score = 40

    reasons = []

    if tx.amount > 50000:
        score += 20
        reasons.append("Large amount")

    if tx.country in HIGH_RISK_COUNTRIES:
        score += 25
        reasons.append("High-risk country")

    if tx.device == "new":
        score += 10
        reasons.append("New device")

    score = min(score,100)

    if score > 80:
        risk = "High"
    elif score > 50:
        risk = "Medium"
    else:
        risk = "Low"

    return {
        "fraud_score":score,
        "risk":risk,
        "reasons":reasons
    }