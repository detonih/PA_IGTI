from fastapi import FastAPI
from stream import producer
import subprocess

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/info/{company}")
def get_info(company: str):
    try:
      result = producer.get_info(company)
      return result
      
    except Exception:
      print(Exception.with_traceback)

@app.get("/start_consumer")
def start_consumer():
  subprocess.call(["bash", "../scripts/sh/deploy_spark_consumer.sh"])