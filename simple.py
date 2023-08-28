from fastapi import FastAPI

app = FastAPI()

# Define a root `/` endpoint
@app.get('/')
def index():
    return {'ok': True}

@app.get('/predict')
def predict(day_of_week, time):
    wait_prediction = int(day_of_week) * int(time)
    return {'wait': wait_prediction}
