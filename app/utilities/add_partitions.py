from datetime import datetime
import subprocess

def add_partition_spark(spark, db, table):
  right_now = datetime.now().strftime("%Y-%m-%d")
  spark.sql(f"""
    ALTER TABLE {db}.{table} ADD IF NOT EXISTS PARTITION(change_date='{right_now}') 
    LOCATION 'hdfs://localhost:9000/raw-data/finance-changes/change_date={right_now}';
  """)

def add_partition_hive(command):
  # result = subprocess.call(["hive", "-e", f"\"ALTER TABLE {db}.{table} ADD IF NOT EXISTS PARTITION(change_date='{right_now}') LOCATION 'hdfs://localhost:9000/raw-data/finance-changes/change_date={right_now}';\""])  
  process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
  stdout, stderr = process.communicate()
  return stdout, stderr

