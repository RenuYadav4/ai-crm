import time


def say_hello(name: str):
    print(f"Starting job for {name}")

    time.sleep(5)

    print(f"Finished job for {name}")

    return f"Hello {name}"
