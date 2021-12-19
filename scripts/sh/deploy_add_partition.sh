#!/bin/bash

db=$1
table=$2

spark-submit \
--master local[*] \
--deploy-mode client \
--files $HIVE_HOME/conf/hive-site.xml \
/app/batch/add_partition.py $db $table