from workers.redis_queue import queue
from tasks.csv_tasks import process_csv

job = queue.enqueue(
    process_csv,
    "uploads/leads.csv"
)

print("Job Created")
print("Job ID:", job.id)