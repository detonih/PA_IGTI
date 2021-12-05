# -*- coding: utf-8 -*-
import json
from kafka import KafkaProducer
from datetime import datetime
import yfinance as yf

producer = KafkaProducer(
  bootstrap_servers='localhost:9092', #Kafka server
  value_serializer=lambda v: json.dumps(v).encode('utf-8') # Serialize json messages
)
# TODO: condição de se quer infos ou dividendos, splits... etc...
# TODO: condição de qual empresa

def get_info(company):
    try:
        change = yf.Ticker(f"{company}").info
    except ValueError:
        pass
    else:
        right_now = datetime.now().strftime("%Y-%m-%d")
        print(f"{right_now} :: Sending messages to Kafka Topic")
        change["change_date"] = right_now
        future = producer.send('finance', change)
        result = future.get(timeout=60)
        return result
    
