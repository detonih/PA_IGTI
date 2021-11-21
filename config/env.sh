#!/bin/bash

echo "
export JAVA_HOME=${JAVA_HOME}
export HADOOP_HOME=${HADOOP_HOME}
export HADOOP_CONF_DIR=${HADOOP_CONF_DIR}
" >> ${HADOOP_HOME}/etc/hadoop/hadoop-env.sh

sed -i '99 i permission javax.management.MBeanTrustPermission "register";' /usr/lib/jvm/java-8-openjdk-amd64/jre/lib/security/java.policy
