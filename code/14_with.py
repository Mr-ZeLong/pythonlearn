# with 语句用于解决资源管理问题，确保在使用资源后及时释放

# 一、基于类的上下文管理器（最常用，适合大型项目）
# 类上下文管理器需要实现 __init__, __enter__, __exit__ 方法
# 案例一：文件管理器
class FileManager:
    # __init__ 方法用于初始化上下文管理器，接收必要的参数
    def __init__(self, name, mode):
        print('calling __init__ method')
        self.name = name
        self.mode = mode 
        self.file = None

    # __enter__ 方法在 with 语句块开始时调用，返回资源对象    
    def __enter__(self):
        print('calling __enter__ method')
        self.file = open(self.name, self.mode)
        return self.file

    # __exit__ 方法在 with 语句块结束时调用，用于释放资源
    # 三个参数会在异常发生时传入：异常类型、异常值、异常跟踪信息
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('calling __exit__ method')
        if self.file:
            self.file.close()

# calling __init__ method
# calling __enter__ method
# ready to write to file
# calling __exit__ method
with FileManager('./data/test_with_file.txt', 'w') as f:
    print('ready to write to file')
    f.write('hello world\n')

# 案例二
class Foo:
    def __init__(self):
        print('__init__ called')        

    def __enter__(self):
        print('__enter__ called')
        return self
    
    # 需要传递的异常，如果确定处理完毕，则返回True, 不会继续抛出异常, 
    # 否则返回False, 将异常继续往上抛
    def __exit__(self, exc_type, exc_value, exc_tb):
        print('__exit__ called')
        if exc_type:
            print(f'exc_type: {exc_type}')
            print(f'exc_value: {exc_value}')
            print(f'exc_traceback: {exc_tb}')
            print('exception handled')
        return True
    
with Foo() as obj:
    raise Exception('exception raised').with_traceback(None)


# 二、基于生成器的上下文管理器（小型项目偶尔使用，但还是建议使用基于类的方式）
from contextlib import contextmanager
@contextmanager
def file_manager(name, mode):
    try:
        f = open(name, mode)
        yield f
    finally:
        f.close()
        
with file_manager('./data/test_with_file.txt', 'a') as f:
    f.write('hello world\n')