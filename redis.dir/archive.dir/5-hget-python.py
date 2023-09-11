import redis
import datetime

def datetimeToEpoch (timedate): 
    epoch = (datetime.datetime.strptime(timedate, '%Y, %m, %d, %H, %M, %S, %f').timestamp()) * 1000
    return int(epoch)

def query_values_by_timestamp(key, host, port):
    redis_client = redis.Redis(host=host, port=port)
    epoch = datetimeToEpoch(timedate)
    value = redis_client.hget(key, epoch)
    return value

if __name__ == "__main__":
    timedate = '2023, 8, 31, 17, 00, 28, 714'
    key = 'urla'
    host = '127.0.0.1'
    port = '6379'
    value = query_values_by_timestamp(key, host, port)
    print(key + ":", value)
    epoch = datetimeToEpoch(timedate)
    print (int(epoch))
