
import redis.asyncio as redis
import os


async def clear_cache_by_key(key: str):
    cached_value = await redis_client.get(key)
    if cached_value:
        await redis_client.delete(key)
        return True 
    return False


redis_client = redis.Redis(
    host=os.getenv("REDIS_SERVER"),
    port=os.getenv("REDIS_PORT"),
    db=0,
    decode_responses=True
)