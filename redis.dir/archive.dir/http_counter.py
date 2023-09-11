import redis
r = redis.StrictRedis(host='localhost', port=6379, db=0)
for key in r.scan_iter('http://test.local/a'):
    # delete the key
    print (key)
