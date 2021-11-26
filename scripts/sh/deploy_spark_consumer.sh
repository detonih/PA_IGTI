#!/bin/bash

spark-submit \
--master local[*] \
--deploy-mode client \
--jars /opt/spark-3.0.3-bin-hadoop2.7/jars/spark-sql-kafka-0-10_2.12-3.1.2.jar \
--driver-class-path /opt/spark-3.0.3-bin-hadoop2.7/jars/spark-sql-kafka-0-10_2.12-3.1.2.jar \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 \
/scripts/python/consumer.py