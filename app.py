from fastapi import FastAPI
import pandas as pd

app = FastAPI()

df = pd.read_csv("hospital_data.csv")

@app.get("/")
def home():
    return {"message": "Hospital Analytics API Running"}

@app.get("/data")
def get_data():
    return df.to_dict(orient="records")

