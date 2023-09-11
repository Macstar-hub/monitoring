import redis
import datetime
import time 

def datetimeToEpoch (timedate): 
    epoch = (datetime.datetime.strptime(timedate, '%Y, %m, %d, %H, %M, %S, %f').timestamp()) * 1000
    return int(epoch)

def getAllField (key, host, port):
    redis_client = redis.Redis(host=host, port=port)
    values = []
    fields = redis_client.hkeys(key)
    for field in fields:
        field = field.decode()
        values.append(int(field))
        values.sort()
    return values

def getTimeSpan (startTimeDate, endTimeDate, key, host, port):
    redis_client = redis.Redis(host=host, port=port)
    statusCodeList = []
    startEpoch = datetimeToEpoch(startTimeDate)
    endEpoch   = datetimeToEpoch(endTimeDate)
    values = getAllField(key, host, port)
    for value in values:
        if value >= startEpoch and value <= endEpoch:
            value = (redis_client.hget(key, value).decode())
            statusCodeList.append(int(value))
    return statusCodeList

if __name__ == "__main__":
    startTimeDate = '2023, 9, 1, 04, 52, 00, 000'
    endTimeDate = '2023, 9, 02, 20, 00, 28, 348'
    key = 'urla'
    host = '127.0.0.1'
    port = '6379'
    while True:
        statusCodeList = getTimeSpan(startTimeDate, endTimeDate, key, host, port)
        time.sleep(1)
        print ("status code is: ", statusCodeList)
