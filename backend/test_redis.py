from redis import Redis
from urllib.parse import urlsplit, urlunsplit

from core.config import settings
from core.redis import normalize_redis_url

redis_url = normalize_redis_url(settings.REDIS_URL)
parts = urlsplit(redis_url)
if parts.password:
    netloc = parts.netloc.replace(parts.password, "***")
    display_url = urlunsplit((parts.scheme, netloc, parts.path, parts.query, parts.fragment))
else:
    display_url = redis_url

print("Connecting to:", display_url)

client = Redis.from_url(
    redis_url,
    decode_responses=True,
)

print(client.ping())
