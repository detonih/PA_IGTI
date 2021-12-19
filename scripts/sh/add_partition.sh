#!/bin/bash

db=$1
table=$2
right_now=$3

cd /

pwd=$(pwd)
echo "=========> ${pwd}"

hive -e "ALTER TABLE ${db}.${table} ADD IF NOT EXISTS PARTITION(change_date='${right_now}') LOCATION 'hdfs://localhost:9000/raw-data/finance-changes/change_date=${right_now}';"