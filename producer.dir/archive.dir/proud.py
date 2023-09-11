from kafka import KafkaProducer
from kafka.errors import KafkaError
import time

producer = KafkaProducer(bootstrap_servers=['88.99.21.177:9092'])

# Asynchronous by default
for i in range(10):
    #msg = producer.send('test-prod', key=b'http://test.local/a:' +i.to_bytes(1,byteorder='big'), value=b'302')
    #key_bytes = bytes(str(int(time.time()) % 1), 'utf-8')
    msg = producer.send('test-prod', key=b'monitoring parameter', value=b'302')
    result = msg.get(timeout=60)
    print (result)
