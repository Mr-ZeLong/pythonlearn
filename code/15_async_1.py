import asyncio
from com_utils import process_time_async


# 协程和多线程的区别，主要在于两点，
# 一是协程为单线程；
# 二是协程由用户判断，在哪些地方（阻塞）交出控制权，在哪些地方（操作共享数据）要一直执行到底

# 声明为异步函数
async def crawl_page(url):
    print('crawling {}'.format(url))
    sleep_time = int(url.split('_')[-1])
    # await 表示同步执行
    await asyncio.sleep(sleep_time)
    print('OK {}'.format(url))


@process_time_async
async def main(urls):
    for url in urls:
        # 同步执行
        await crawl_page(url)


urls = ['url_1', 'url_2', 'url_3', 'url_4']
print(main(urls)) # 声明为异步函数，返回一个协程对象，并不会执行

asyncio.run(main(urls)) # 耗时 10 s

print("----------------------------------")

@process_time_async
async def main_concurrent(urls):
    tasks = [asyncio.create_task(crawl_page(url)) for url in urls]
    await asyncio.gather(*tasks) # 同步等待所有任务执行完毕

asyncio.run(main_concurrent(urls)) # 耗时 4 s


print("----------------------------------")

async def worker_1():
    print('worker_1 start')
    await asyncio.sleep(1)
    print('worker_1 done')

async def worker_2():
    print('worker_2 start')
    await asyncio.sleep(2)
    print('worker_2 done')

@process_time_async
async def main_sync_worker():
    print('before await')
    await worker_1()
    print('awaited worker_1')
    await worker_2()
    print('awaited worker_2')

asyncio.run(main_sync_worker()) # 耗时 3 s

print("----------------------------------")

@process_time_async
async def main_cc_worker():
    task1 = asyncio.create_task(worker_1())
    task2 = asyncio.create_task(worker_2())
    print('before await')
    await task1
    print('awaited worker_1')
    await task2
    print('awaited worker_2')

asyncio.run(main_cc_worker()) # 耗时 2 s

print("----------------------------------")

async def worker_1_v2():
    await asyncio.sleep(1)
    return 1

async def worker_2_v2():
    await asyncio.sleep(2)
    return 2 / 0

async def worker_3_v2():
    await asyncio.sleep(3)
    return 3

@process_time_async
async def main_concurrent_v2():
    task_1 = asyncio.create_task(worker_1_v2())
    task_2 = asyncio.create_task(worker_2_v2())
    task_3 = asyncio.create_task(worker_3_v2())

    await asyncio.sleep(2)
    # 取消任务3
    task_3.cancel()

    # return_exceptions=True 会将异常捕获并返回,
    # 否则会抛出异常, 导致后面的程序(包括协程)无法执行.
    res = await asyncio.gather(task_1, task_2, task_3, return_exceptions=True)
    print(res)

asyncio.run(main_concurrent_v2()) # 耗时 2 s