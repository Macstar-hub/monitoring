from kafka import KafkaProducer
from kafka.errors import KafkaError
import time
import random

randomStatusCode = [200, 202, 300, 303, 400, 401, 403, 500, 502, 503]
producer = KafkaProducer(bootstrap_servers=['88.99.21.177:9092'])
# Asynchronous by default
for i in range(1000000000):

    msg = producer.send('test-prod-2', key=b'urla', value=bytes(str(random.choice(randomStatusCode)), 'utf-8'))
    result = msg.get(timeout=60)
    print (result)
    time.sleep(0.8)
