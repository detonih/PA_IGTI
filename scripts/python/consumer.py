from pyspark.sql import SparkSession
from pyspark.sql.types import StringType
import  pyspark.sql.functions as F

spark = (SparkSession
         .builder
         .appName('finance-changes-event-consumer')
         .getOrCreate())
sc = spark.sparkContext

df = (spark
  .readStream
  .format("kafka")
  .option("kafka.bootstrap.servers", "localhost:9092") # kafka server
  .option("subscribe", "finance") # topic
  .option("startingOffsets", "earliest") # start from beginning 
  .load())

# Convert binary to string key and value
df1 = (df
    .withColumn("key", df["key"].cast(StringType()))
    .withColumn("value", df["value"].cast(StringType())))

schema = spark.read.option("multiline", "true").json("/raw-data/sample_schema.json").schema

df_finance = (df1
           # Sets schema for event data
           .withColumn("value", F.from_json("value", schema))
           .select(
             "*",
           F.to_date(F.from_unixtime(F.col("value.change_date"))).alias("change_date")
           )
          )

# Start query stream over stream dataframe
raw_path = "/raw-data/finance-changes"
checkpoint_path = "/raw-data/finance-changes-checkpoint"

queryStream =(
    df_finance
    .writeStream
    .format("parquet")
    .queryName("finance_changes_ingestion")
    .option("checkpointLocation", checkpoint_path)
    .option("path", raw_path)
    .outputMode("append")
    .partitionBy("change_date")
    .start())

queryStream.awaitTermination(10)