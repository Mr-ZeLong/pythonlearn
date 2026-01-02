from com_utils import process_time
from concurrent import futures

# python 多进程 并行执行 cpu 密集型任务
# 与多线程不同，多进程是并行执行的，每个进程都有自己的解释器和全局解释器锁，
# 因此，在执行 cpu 密集型任务时，多进程可以充分利用多核 cpu 的性能优势

def cpu_bound(number):
    print(sum(i * i for i in range(number)))

@process_time
def calculate_sums(numbers):
    with futures.ProcessPoolExecutor() as executor:
        executor.map(cpu_bound, numbers)

calculate_sums([10, 30, 70, 150])
