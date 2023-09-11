from kafka import KafkaConsumer
import redis
import time 

consumer = KafkaConsumer('test-prod',
                     bootstrap_servers=['kafka1:9092'],
                     auto_offset_reset='earliest',
                     group_id='monitoring')

redis_client = redis.Redis(host='127.0.0.1', 
                           port='6379')
                           #password=’<redis-password>’)

print ("Consuming messages from the given topic")
for message in consumer:
    #redis_client.set(message.key.decode(), message.value.decode())
    redis_client.set(time.time(), message.value)
    print (message.key, message.value)

print ("Quit")
