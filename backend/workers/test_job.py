from workers.redis_queue import queue
from tasks.test_tasks import say_hello

job = queue.enqueue(
    say_hello,
    "Lokesh"
)

print("Job created")
print("Job ID:", job.id)