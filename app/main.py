from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from stream import producer
import subprocess
from models.query import Query
from models.partition import Partition
from utilities.add_partitions import *
from utilities.queries import execute_query

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
  except Exception as e:
    print(e)
    print(Exception.with_traceback)

@app.get("/start_consumer")
def start_consumer():
  try:
      subprocess.call(["bash", "../scripts/sh/deploy_spark_consumer.sh"])
      return {"status": "OK"}
  except Exception as e:
    print(e)
    print(Exception.with_traceback)

@app.post("/add_partition")
def add_partition(partition: Partition):
  try:
    right_now = datetime.now().strftime("%Y-%m-%d")

    db, table = partition.db, partition.table
    command = f'hive -e "ALTER TABLE {db}.{table} ADD IF NOT EXISTS PARTITION(change_date=\'{right_now}\') LOCATION \'hdfs://localhost:9000/raw-data/finance-changes/change_date={right_now}\';"'

    result = add_partition_hive(command)
    return result
  except Exception as e:
    print(e)
    print(Exception.with_traceback)

@app.post("/make_query")
def make_query(query: Query):
  try:
    print(f"Query: {query.query}")
  except Exception as e:
    print(e)
    print(Exception.with_traceback)