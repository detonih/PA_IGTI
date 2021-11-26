FROM ubuntu:18.04

RUN apt-get update && apt-get install -y --no-install-recommends \
      openjdk-8-jdk \
      net-tools \
      curl \
      netcat \
      gnupg \
      libsnappy-dev \
      openssh-server \
      vim \
      nano \
      unzip \
      wget \
      rsync \
      zip \
      git \
    && rm -rf /var/lib/apt/lists/*
      
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/

##HADOOP
ENV HADOOP_VERSION=2.7.2
ENV HADOOP_URL https://archive.apache.org/dist/hadoop/common/hadoop-$HADOOP_VERSION/hadoop-$HADOOP_VERSION.tar.gz

RUN set -x \
    && curl -fSL "$HADOOP_URL" -o /tmp/hadoop.tar.gz \
    && tar -xvf /tmp/hadoop.tar.gz -C /opt/ \
    && rm /tmp/hadoop.tar.gz*

ENV HADOOP_HOME=/opt/hadoop-$HADOOP_VERSION
ENV HADOOP_CONF_DIR=$HADOOP_HOME/etc/hadoop
ENV HADOOP_MAPRED_HOME=$HADOOP_HOME
ENV HADOOP_COMMON_HOME=$HADOOP_HOME
ENV HADOOP_HDFS_HOME=$HADOOP_HOME
ENV YARN_HOME=$HADOOP_HOME
ENV HADOOP_COMMON_LIB_NATIVE_DIR=$HADOOP_HOME/lib/native
ENV HADOOP_OPTS="$HADOOP_OPTS -Djava.library.path=$HADOOP_HOME/lib/native"

COPY config/core-site.xml $HADOOP_HOME/etc/hadoop/
COPY config/hdfs-site.xml $HADOOP_HOME/etc/hadoop/
COPY config/mapred-site.xml $HADOOP_HOME/etc/hadoop/
COPY config/yarn-site.xml $HADOOP_HOME/etc/hadoop/

##HIVE
ENV HIVE_VERSION=2.1.0

RUN set -x \
	&& curl -fSL http://archive.apache.org/dist/hive/hive-$HIVE_VERSION/apache-hive-$HIVE_VERSION-bin.tar.gz -o /tmp/hive.tar.gz \
	&& tar -xvf /tmp/hive.tar.gz -C /opt/ \
    && rm /tmp/hive.tar.gz

ENV HIVE_HOME=/opt/apache-hive-$HIVE_VERSION-bin
COPY config/hive-site.xml $HIVE_HOME/conf/
COPY config/hive-env.sh $HIVE_HOME/conf/

##PYTHON
RUN apt-get update && apt-get install -y --no-install-recommends \
	python3.6 \
	python3.6-dev \
	python3-pip \
	python3.6-venv
RUN python3.6 -m pip install pip --upgrade
RUN python3.6 -m pip install wheel
RUN pip install pandas
RUN pip install setuptools
RUN pip install kafka-python
RUN pip install sseclient
RUN pip install yfinance
RUN pip install yahoofinancials
RUN pip install pyspark

##SPARK
ENV SPARK_VERSION=3.0.3
ENV SPARK_URL=https://www.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop2.7.tgz 
RUN set -x \
    && curl -fSL "$SPARK_URL" -o /tmp/spark.tar.gz \
    && tar -xvf /tmp/spark.tar.gz -C /opt/ \
    && rm /tmp/spark.tar.gz*
RUN wget -O /opt/spark-3.0.3-bin-hadoop2.7/jars/spark-sql-kafka-0-10_2.12-3.1.2.jar https://repo1.maven.org/maven2/org/apache/spark/spark-sql-kafka-0-10_2.12/3.1.2/spark-sql-kafka-0-10_2.12-3.1.2.jar
RUN wget -O /opt/spark-3.0.3-bin-hadoop2.7/jars/kafka-clients-3.0.0.jar https://repo1.maven.org/maven2/org/apache/kafka/kafka-clients/3.0.0/kafka-clients-3.0.0.jar
ENV SPARK_HOME=/opt/spark-$SPARK_VERSION-bin-hadoop2.7
ENV PYSPARK_PYTHON=python3.6

##Kafka
ENV KAFKA_VERSION=3.0.0
ENV SCALA_VERSION=2.12
ENV KAFKA_FILENAME=kafka_${SCALA_VERSION}-${KAFKA_VERSION}.tgz
RUN set -x \
    && curl -fSL https://dlcdn.apache.org/kafka/$KAFKA_VERSION/$KAFKA_FILENAME -o /tmp/kafka.tgz \
    && tar -xvf /tmp/kafka.tgz -C /opt/ \
    && rm /tmp/kafka.tgz
ENV KAFKA_HOME=/opt/kafka_$SCALA_VERSION-$KAFKA_VERSION

ENV PATH $PATH:$HADOOP_HOME/bin:$HIVE_HOME/bin:$SQOOP_HOME/bin:$SPARK_HOME/bin:$KAFKA_HOME/bin
ENV HADOOP_CLASSPATH=$HADOOP_CLASSPATH:$HIVE_HOME/lib/*

RUN \
  ssh-keygen -t rsa -P '' -f ~/.ssh/id_rsa && \
  cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys && \
  chmod 0600 ~/.ssh/authorized_keys

COPY config/env.sh /tmp/env.sh
RUN chmod a+x /tmp/env.sh
RUN /tmp/env.sh
RUN rm -f /tmp/env.sh

RUN mkdir -p /scripts/sh
RUN mkdir /raw-data

COPY config/start-zookeeper.sh config/start-kafka.sh config/create-topic.sh /tmp/
RUN chmod a+x /tmp/*.sh \
    && mv /tmp/start-zookeeper.sh /tmp/start-kafka.sh /tmp/create-topic.sh /usr/bin
RUN mkdir /logs

ADD start.sh /start.sh
RUN chmod a+x /start.sh

CMD ["sh", "-c", "/start.sh"]