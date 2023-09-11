import redis

def getAllField (key, host, port):
    redis_client = redis.Redis(host=host, port=port)
    values = []
    fields = redis_client.hkeys(key)
    for field in fields: 
        field = field.decode()
        values.append(int(field))
        values.sort()
    return values

def getTimeSpan (startEpoch, endEpoch, key, host, port):
    redis_client = redis.Redis(host=host, port=port)
    statusCodeList = []
    values = getAllField(key, host, port)
    for value in values:
        if value >= startEpoch and value <= endEpoch:
            value = (redis_client.hget(key, value).decode())
            statusCodeList.append(int(value))
    return statusCodeList

if __name__ == "__main__":
    key = "urla"
    host =  "127.0.0.1"
    port = "6379"
    startEpoch = 1693492228074
    endEpoch   = 1693492228438
    value = getTimeSpan(startEpoch, endEpoch, key, host, port)
    statusCodeList = getTimeSpan(startEpoch, endEpoch, key, host, port)
    print ("status code is: ", statusCodeList)
