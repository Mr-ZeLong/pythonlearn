import os
import psutil
import time

# 一、生成器是一种特殊的迭代器，不用提前生成所有元素，而是在需要的时候才生成，生成器的内存占用要比迭代器低得多

# 显示当前 python 程序占用的内存大小
def show_memory_info(hint):
    pid = os.getpid()
    p = psutil.Process(pid)
    
    info = p.memory_full_info()
    memory = info.uss / 1024. / 1024
    print('{} memory used: {} MB'.format(hint, memory))
def test_iterator():
    show_memory_info('initing iterator')
    list_1 = [i for i in range(100000000)]
    show_memory_info('after iterator initiated')
    print(sum(list_1))
    show_memory_info('after sum called')

def test_generator():
    show_memory_info('initing generator')
    list_2 = (i for i in range(100000000))
    show_memory_info('after generator initiated')
    print(sum(list_2))
    show_memory_info('after sum called')

# initing iterator memory used: 61.62890625 MB
# after iterator initiated memory used: 3886.44921875 MB
# 4999999950000000
# after sum called memory used: 3886.44921875 MB
# CPU times: user 2.28 s, sys: 5.25 s, total: 7.53 s
# Wall time: 6.68 s
# %time 是 IPython 的魔法命令，在普通 Python 文件中会报语法错误
# 这里改为直接调用函数，如需测时可使用 time 模块
start = time.time()
test_iterator()
end = time.time()
print('test_iterator 耗时: {:.2f} 秒'.format(end - start))


# initing generator memory used: 63.1015625 MB
# after generator initiated memory used: 63.1015625 MB
# 4999999950000000
# after sum called memory used: 63.1015625 MB
# CPU times: user 1.97 s, sys: 1.06 ms, total: 1.97 s
# Wall time: 2.04 s
start = time.time()
test_generator()
end = time.time()
print('test_generator 耗时: {:.2f} 秒'.format(end - start))



# 二、生成器搭配 yield 使用
def generator(k):
    i = 1
    while True:
        # 每次调用 yield 时，会暂停函数的执行，返回 i ** k
        yield i ** k
        i += 1

def get_sum(n):
    sum_1, sum_3 = 0, 0
    gen_1 = generator(1)
    gen_3 = generator(3)
    for i in range(n):
        # 每次调用 next 时，会从上次暂停的位置继续执行
        next_1 = next(gen_1)
        next_3 = next(gen_3)
        print('next_1 = {}, next_3 = {}'.format(next_1, next_3))
        sum_1 += next_1
        sum_3 += next_3
    print(sum_1 * sum_1, sum_3)

# next_1 = 1, next_3 = 1
# next_1 = 2, next_3 = 8
# next_1 = 3, next_3 = 27
# next_1 = 4, next_3 = 64
# next_1 = 5, next_3 = 125
# next_1 = 6, next_3 = 216
# next_1 = 7, next_3 = 343
# next_1 = 8, next_3 = 512
# 1296 1296
get_sum(8)

# 在列表种找到所有值为 target 的元素下标
def index_generator(L, target):
    for i, num in enumerate(L):
        if num == target:
            yield i

result_generator = index_generator([1, 6, 2, 4, 5, 2, 8, 6, 3, 2], 2)
# <class 'generator'>
print(type(result_generator))
# 转为列表后才能打印 [2, 5, 9]
result = list(result_generator)
print(result)