from kafka import KafkaProducer
from kafka.errors import KafkaError
import time

producer = KafkaProducer(bootstrap_servers=['88.99.21.177:9092'])

# Asynchronous by default
for i in range(1000000000):
    msg = producer.send('test-prod-2', key=b'urla', value=b'202')
    result = msg.get(timeout=60)
    print (result)
    time.sleep(0.8)
