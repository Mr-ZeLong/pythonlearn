import time
import functools


def process_time(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print('耗时: {:.2f} 秒'.format(end - start))
    return wrapper


# 装饰器，用于测量异步函数的执行时间
def process_time_async(func):
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        start = time.time()
        await func(*args, **kwargs)
        end = time.time()
        print('耗时: {:.2f} 秒'.format(end - start))
    return wrapper


# 默认情况下，导入模块时，会执行模块中的所有代码
# 但是，我们可以通过 __name__ 变量来判断当前模块是否是主模块
# 如果是主模块，那么 __name__ 变量的值就是 '__main__'
# 否则， __name__ 变量的值就是模块的名称，
# 因此，如果不想让模块中的代码在被导入时执行，可以将代码放到 if __name__ == '__main__': 中
if __name__ == '__main__':
    # 当本模块作为主模块运行时，执行以下代码
    pass
