from redis import Redis
from rq import Worker, Queue
from core.config import settings
from core.redis import normalize_redis_url

redis_conn = Redis.from_url(normalize_redis_url(settings.REDIS_URL))

worker = Worker(
    [Queue("default", connection=redis_conn)],
    connection=redis_conn
)

worker.work()