import psycopg2
import redis

def flushDatabase(key, redishost, redisport):
    redis_client = redis.Redis(host=redishost, port=redisport)
    values = []
    fields = redis_client.hkeys('urla')
    print (fields)
#    for field in fields:
#        field = field.decode()
#        values.append(int(field))
#    print (field)
#    return values

#def flushDatabase(redisHost, redisPort, key):
#    redis_client = redis.Redis(host=redisHost, port=redisPort)
#    values = []
#    fields = redis_client.hkeys(key)
#    for field in fields:
#        values.append(redis_client(key, field))


def insertQuery(url, statusCode, count):
    conn = psycopg2.connect(host=host, port=port, database=database)
    cursor = conn.cursor()
    insert_statement = "INSERT INTO statuscount (url, statuscode, epochtime) VALUES (%s, %s, %s)"
    values = ("urla", 200, 10)
    cursor.execute(insert_statement, values)
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == "__main__":
    redishost = '127.0.0.1'
    redisport = '6379'
    key = 'urla'
    #host = 'localhost'
    #port = 5432
    #database = "statuscode"
    #url = 'urla'
    #statusCode = 200 
    #count = 10
    flush = flushDatabase(redishost, redisport, key)
    #insert = insertQuery(url, statusCode, count)
