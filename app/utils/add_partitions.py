from datetime import datetime

def add_partition(spark, db, table):
  right_now = datetime.now().strftime("%Y-%m-%d")
  spark.sql(f"""
    ALTER TABLE {db}.{table} ADD IF NOT EXISTS PARTITION(change_date='{right_now}') 
    LOCATION 'hdfs://localhost:9000/raw-data/finance-changes/change_date=2021-12-18';
  """)