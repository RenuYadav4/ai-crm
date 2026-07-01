from redis import Redis
from rq import Queue
from core.config import settings
from core.redis import normalize_redis_url

redis_conn = Redis.from_url(normalize_redis_url(settings.REDIS_URL))

queue = Queue(
    "default",
    connection=redis_conn
)