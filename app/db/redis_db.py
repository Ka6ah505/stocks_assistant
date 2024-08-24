from redis import asyncio as aioredis
from config import REDIS_HOST, REDIS_PORT

LINK_CONNECT_TO_REDIS = f'redis://{REDIS_HOST}:{REDIS_PORT}'

redis = aioredis.from_url(
    LINK_CONNECT_TO_REDIS,
    encoding='utf8',
    decode_responses=True,
)
