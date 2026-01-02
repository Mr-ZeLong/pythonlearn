from concurrent import futures
import requests
from com_utils import process_time


def download_one(url):
    resp = requests.get(url)
    print('Read {} from {}'.format(len(resp.content), url))


def download_all(sites):
    # Python的解释器并不是线程安全的，为了解决由此带来的race condition等问题，
    # Python便引入了全局解释器锁，也就是同一时刻，只允许一个线程执行。
    # 当然，在执行I/O操作时，如果一个线程被block了，全局解释器锁便会被释放，
    # 从而让另一个线程能够继续执行，因此 这里 python 的多线程并不是并行，而是并发
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_one, sites)


def download_all_v2(sites):
    with futures.ThreadPoolExecutor(max_workers=5) as executor:
        to_do = []
        for site in sites:
            future = executor.submit(download_one, site)
            to_do.append(future)
            
        # as_completed(fs) 等待 所有 future 都有结果后，返回 future 迭代器
        for future in futures.as_completed(to_do):
            # result() 获取 future 执行的结果，默认一直等待
            future.result()


@process_time
def main():
    sites = [
        'https://en.wikipedia.org/wiki/Portal:Arts',
        'https://en.wikipedia.org/wiki/Portal:History',
        'https://en.wikipedia.org/wiki/Portal:Society',
        'https://en.wikipedia.org/wiki/Portal:Biography',
        'https://en.wikipedia.org/wiki/Portal:Mathematics',
        'https://en.wikipedia.org/wiki/Portal:Technology',
        'https://en.wikipedia.org/wiki/Portal:Geography',
        'https://en.wikipedia.org/wiki/Portal:Science',
        'https://en.wikipedia.org/wiki/Computer_science',
        'https://en.wikipedia.org/wiki/Python_(programming_language)',
        'https://en.wikipedia.org/wiki/Java_(programming_language)',
        'https://en.wikipedia.org/wiki/PHP',
        'https://en.wikipedia.org/wiki/Node.js',
        'https://en.wikipedia.org/wiki/The_C_Programming_Language',
        'https://en.wikipedia.org/wiki/Go_(programming_language)'
    ]
    # download_all(sites)
    download_all_v2(sites)

if __name__ == '__main__':
    main()