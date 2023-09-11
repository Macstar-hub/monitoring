from kafka import KafkaProducer
from kafka.errors import KafkaError
import time
import json

producer = KafkaProducer(bootstrap_servers=['88.99.21.177:9092'])
producer.value_serializer = lambda x: json.dumps(x).encode('utf-8')

for i in range(10):
    #message = {'key':int(time.time()), 'value':'http://test.local/a'+ str(i)}
    message = {'key':int(time.time()), "value":{"url":"test.local/a","status":"200"}}
    msg = producer.send('test-prod-2', value=json.dumps(message).encode('utf-8'))
    result = msg.get(timeout=60)
    print (result)
    time.sleep(0.5)



