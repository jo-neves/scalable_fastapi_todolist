from redis.asyncio import Redis

_redis_client: Redis | None = None


def init_redis_client(redis_host: str, redis_port: int):
    global _redis_client
    if _redis_client is None:
        _redis_client = Redis(host=redis_host, port=redis_port, db=0)


def get_redis_client() -> Redis:
    if _redis_client is None:
        raise RuntimeError("Redis not initialized")

    return _redis_client


async def close_redis_async():
    global _redis_client
    if _redis_client:
        await _redis_client.close()
        _redis_client = None
