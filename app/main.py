from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from stream import producer
import subprocess
from models.query import Query

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
    return {"message": "Welcome to Big Data Platform!"}

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

@app.post("/make_query")
def make_query(query: Query):
  try:
    print(f"Query: {query}")
  except Exception:
    print(Exception.with_traceback)