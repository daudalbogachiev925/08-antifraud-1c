from fastapi import FastAPI
from rules import velocity, amount_outlier, off_hours

app = FastAPI()

@app.post("/check")
def check(tx: dict):
    results = [
        velocity.check(tx, HISTORY),
        amount_outlier.check(tx, HISTORY),
        off_hours.check(tx, HISTORY)]
    return {'alerts': [r for r in results if r['triggered']]}
