import json
from kafka import KafkaProducer
from datetime import datetime
import yfinance as yf

producer = KafkaProducer(
  bootstrap_servers='localhost:9092', #Kafka server
  value_serializer=lambda v: json.dumps(v).encode('utf-8') # Serialize json messages
)

try:
    change = yf.Ticker("GOOGL").info
    print(type(change))
except KeyboardInterrupt:
    print("process interrupted")
except ValueError:
    pass
else:
    right_now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    print(f"{right_now} :: Sending messages to Kafka Topic \n {change}")
    future = producer.send('finance', change)
    result = future.get(timeout=60)

