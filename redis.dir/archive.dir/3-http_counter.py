import redis

def query_values_by_timestamp(key, from_timestamp, to_timestamp, host, port):

    redis_client = redis.Redis(host=host, port=port)
    values = redis_client.ts.range(key, from_timestamp, to_timestamp)
    return values

if __name__ == "__main__":
    key = "http://test.local/a"
    from_timestamp = 1693341010000
    to_timestamp = 1693345454000
    host = '127.0.0.1'
    port = '6379'
    values = query_values_by_timestamp(key, from_timestamp, to_timestamp, host, port)
    print(values)
