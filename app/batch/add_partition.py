from pyspark.sql import SparkSession
import  pyspark.sql.functions as F
# from utilities.add_partitions import add_partition_spark
import sys
from datetime import datetime

spark = (SparkSession
         .builder
         .appName('add-partition-finance')
         .enableHiveSupport()
         .getOrCreate())

db = sys.argv[1]
table = sys.argv[2]

def add_partition_spark(spark, db, table):
  right_now = datetime.now().strftime("%Y-%m-%d")
  print("========>", db, table, right_now)
  spark.sql(f"""
    ALTER TABLE {db}.{table} ADD IF NOT EXISTS PARTITION(change_date='{right_now}') 
    LOCATION 'hdfs://localhost:9000/raw-data/finance-changes/change_date={right_now}';
  """)

add_partition_spark(spark, db, table)

# spark.stop()
