#!/bin/bash

/etc/init.d/ssh start

$HADOOP_HOME/bin/hadoop namenode -format
$HADOOP_HOME/sbin/start-dfs.sh
$HADOOP_HOME/sbin/start-yarn.sh
$HADOOP_HOME/sbin/hadoop-daemon.sh start namenode
$HADOOP_HOME/sbin/hadoop-daemon.sh start datanode
$HADOOP_HOME/sbin/yarn-daemon.sh start resourcemanager
$HADOOP_HOME/sbin/yarn-daemon.sh start nodemanager
$HADOOP_HOME/sbin/mr-jobhistory-daemon.sh start historyserver

hdfs dfs -mkdir -p  /user/hive/warehouse
hdfs dfs -chmod g+w /tmp
hdfs dfs -chmod g+w /user/hive/warehouse
hdfs dfs -mkdir /stage
hdfs dfs -chmod g+w /stage

$HIVE_HOME/bin/schematool -initSchema -dbType derby

nohup start-zookeeper.sh > /logs/start-zookeeper.log &
sleep 20
nohup start-kafka.sh > /logs/start-kafka.log &
sleep 20
create-topic-wiki.sh

tail -f /dev/null