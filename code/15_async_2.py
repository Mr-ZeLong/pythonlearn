import asyncio
import random
from com_utils import process_time_async

# 协程实现生产者消费者模型

async def producer(id, que):
    print(f"produder {id} start")
    for i in range(5):
        num = random.randint(0, 100)
        await que.put(num)
        print(f"produder {id} put {num}")
        await asyncio.sleep(1)
    print(f"produder {id} done")

async def consumer(id, que):
    print(f"consumer {id} start")
    while True:
        num = await que.get()
        print(f"consumer {id} get {num}")
        await asyncio.sleep(0.5)

@process_time_async
async def main():
    que = asyncio.Queue()
    producers = [asyncio.create_task(producer(id, que)) for id in range(2)]
    consumers = [asyncio.create_task(consumer(id, que)) for id in range(2)]
    await asyncio.sleep(10)
    for con in consumers:
        con.cancel()
    result = await asyncio.gather(*producers, *consumers, return_exceptions=True)
    print(result)


asyncio.run(main())