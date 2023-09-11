from kafka import KafkaConsumer
import redis
import time 
import json

consumer = KafkaConsumer('test-prod-2',
                     bootstrap_servers=['kafka1:9092'],
                     auto_offset_reset='earliest',
                     group_id='monitoring'
                     )

redis_client = redis.Redis(host='127.0.0.1', port='6379')

print ("Consuming messages from the given topic")
for message in consumer:
    redis_client.hset(message.key ,message.timestamp , message.value)
    print (message.key, message.value, message.timestamp)

print ("Quit")
