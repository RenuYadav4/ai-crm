from urllib.parse import urlsplit, urlunsplit

from redis import Redis

from core.config import settings


def normalize_redis_url(url: str) -> str:
    """
    Upstash Redis requires TLS. If the URL points to an Upstash host but uses
    the plain redis:// scheme, upgrade it to rediss:// so the handshake works.
    """
    parts = urlsplit(url)
    if parts.scheme == "redis" and parts.hostname and parts.hostname.endswith("upstash.io"):
        return urlunsplit(("rediss", parts.netloc, parts.path, parts.query, parts.fragment))
    return url


def get_redis_client() -> Redis:
    return Redis.from_url(normalize_redis_url(settings.REDIS_URL), decode_responses=True)
