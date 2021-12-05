#!/bin/bash

spark-submit \
--master local[*] \
--deploy-mode client \
--jars /opt/spark-${SPARK_VERSION}-bin-hadoop2.7/jars/spark-sql-kafka-0-10_2.12-3.1.2.jar,/opt/spark-${SPARK_VERSION}-bin-hadoop2.7/jars/kafka-clients-3.0.0.jar,/opt/spark-${SPARK_VERSION}-bin-hadoop2.7/jars/spark-token-provider-kafka-0-10_2.12-3.1.2.jar,/opt/spark-${SPARK_VERSION}-bin-hadoop2.7/jars/commons-pool2-2.6.2.jar \
--driver-class-path /opt/spark-${SPARK_VERSION}-bin-hadoop2.7/jars/spark-sql-kafka-0-10_2.12-3.1.2.jar,/opt/spark-${SPARK_VERSION}-bin-hadoop2.7/jars/kafka-clients-3.0.0.jar,/opt/spark-${SPARK_VERSION}-bin-hadoop2.7/jars/spark-token-provider-kafka-0-10_2.12-3.1.2.jar,/opt/spark-${SPARK_VERSION}-bin-hadoop2.7/jars/commons-pool2-2.6.2.jar \
--packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.1.2 \
/app/stream/consumer.py