import redis

def query_values_by_timestamp(key, from_timestamp, to_timestamp):
    """
    Query values of a key from to specific timestamp in Redis.

    Args:
        key: The key to query.
        from_timestamp: The start timestamp.
        to_timestamp: The end timestamp.

    Returns:
        A list of values for the key in the specified timestamp range.
    """

    redis_client = redis.Redis()
    values = redis_client.ts.range(key, from_timestamp, to_timestamp)
    return values

if __name__ == "__main__":
    key = "my_key"
    from_timestamp = 1656688733000
    to_timestamp = 1656688734000
    values = query_values_by_timestamp(key, from_timestamp, to_timestamp)
    print(values)
