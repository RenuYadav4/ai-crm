# workers/clear_queue.py

from workers.redis_queue import queue

queue.empty()

print("Queue cleared")