import redis

def query_values(key, host, port):
    """
    Query values of a key from to specific timestamp in Redis.

    Args:
        key: The key to query.
        from_timestamp: The start timestamp.
        to_timestamp: The end timestamp.

    Returns:
        A list of values for the key in the specified timestamp range.
    """

    redis_client = redis.Redis(host=host, port=port)
    values = redis_client.keys(key)
    #values = redis_client.mget(key)
    return values

if __name__ == "__main__":
    key = "*.169.*"
    host = '127.0.0.1'
    port = '6379'
    values = query_values(key, host, port)
    print(values)
