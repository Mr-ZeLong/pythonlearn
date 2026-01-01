import functools

# 一、函数装饰器
def my_decorator(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        # 表示可以接受任意数量和任意类型的变量
        print('wrapper of decorator')
        func(*args, **kwargs)
    return wrapper
    
@my_decorator
def greet(message):
    print(message)

@my_decorator
def say_hello(name, message):
    print(f'{name}, {message}')

# wrapper of decorator
# hello
greet('hello')

# wrapper of decorator
# zelon, hello
say_hello('zelon', 'hello')

# greet
print(greet.__name__)

# 函数装饰器还可以套多一层
def repeat(num):
    def my_decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(num):
                print('wrapper of decorator')
                func(*args, **kwargs)
        return wrapper
    return my_decorator

@repeat(2)
def say_goodbye(name):
    print(f'goodbye, {name}')

# wrapper of decorator
# goodbye, zelon
# wrapper of decorator
# goodbye, zelon
say_goodbye('zelon')
# say_goodbye
print(say_goodbye.__name__)

# 二、类装饰器
# 类装饰器主要依赖于函数__call__()，每当你调用一个类的示例时，
# 函数__call__()就会被执行一次。
class Count:
    def __init__(self, func):
        self.func = func
        self.num_calls = 0

    def __call__(self, *args, **kwargs):
        self.num_calls += 1
        print('num of calls is: {}'.format(self.num_calls))
        return self.func(*args, **kwargs)

@Count
def example():
    print("hello world")

# num of calls is: 1
# hello world
example()

# num of calls is: 2
# hello world
example()


# 三、装饰器套娃
def my_decorator1(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator1')
        func(*args, **kwargs)
        print("decorator1 end")
    return wrapper


def my_decorator2(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('execute decorator2')
        func(*args, **kwargs)
        print("decorator2 end")
    return wrapper


@my_decorator1
@my_decorator2
def hello(message):
    print(message)

# execute decorator1
# execute decorator2
# hello world
# decorator2 end
# decorator1 end
hello('hello world')