import redis
import datetime
import time 
import os 
import psycopg2

def getAllField (key, host, port):
    redis_client = redis.Redis(host=host, port=port)
    conn = psycopg2.connect(host="127.0.0.1", port="5432", database="statuscode")
    cursor = conn.cursor()
    values = []
    fields = redis_client.hkeys(key)
    for field in fields:
        epoch = field.decode()
        statuscode = int(redis_client.hget(key, field))
        insert_statement = "INSERT INTO statuscount (url, statuscode, epochtime) VALUES (%s, %s, %s)"
        queryvalus = (key, statuscode, epoch)
        cursor.execute(insert_statement, queryvalus)
        conn.commit()
        print (epoch)
    cursor.close()
    conn.close()
    redis_client.flushall()
    return values

if __name__ == "__main__":
    key = 'urla'
    host = '127.0.0.1'
    port = '6379'
    value = getAllField (key, host, port)
