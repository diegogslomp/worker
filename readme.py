# Worker

### Run sync/async tasks from a queue

### Instead of creating a loop to run a task on each item in a list
### ```python
### import time
### import random

### while True:
###     random_numbers = []
###     for _ in range(10):
###         random_numbers.append(random.uniform(0.05, 1.0))

###     for sleep_for in random_numbers:
###         time.sleep(sleep_for)
### ```

### Create workers to do the task from a queue of items
### ```python
from asyncio import Queue
from worker import Work
import asyncio
import logging
import random


def feeder(queue: Queue) -> None:
    for _ in range(10):
        sleep_for = random.uniform(0.05, 1.0)
        queue.put_nowait(sleep_for)


async def run() -> None:
    work = Work(name="sleep", task=asyncio.sleep)

    feeder(work.queue)
    await work.run_once(num_of_workers=3)

    await work.run_forever(num_of_workers=3, queue_feeder=feeder)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG, format="%(message)s")
    try:
        asyncio.run(run())
    except (KeyboardInterrupt, SystemExit):
        pass

### ```

### Test code above
### ```
### python readme.py
### ```
