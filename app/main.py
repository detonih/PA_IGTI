from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from stream import producer
import subprocess

app = FastAPI()

origins = [
    "http://localhost:3001",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

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
  try:
      subprocess.call(["bash", "../scripts/sh/deploy_spark_consumer.sh"])
      return {"status": "OK"}
  except Exception:
    print(Exception.with_traceback)