# 函数基本用法以及嵌套函数
def factorial(input):
    # validation check
    if not isinstance(input, int):
        raise Exception('input must be an integer.')
    if input < 0:
        raise Exception('input must be greater or equal to 0' )
    ...

    # 嵌套函数
    def inner_factorial(input):
        if input <= 1:
            return 1
        return input * inner_factorial(input-1)
    return inner_factorial(input)

print(factorial(5))



# 默认情况下，函数内不能修改函数外的变量，如果出现了赋值操作，那只会被认为是函数内部的局部变量
# 1. 函数要使用全局变量可以通过 global
# 2. 内部函数要使用外部函数的变量，可以通过 nonlocal
a = 1
def test():
    a = 2
    print(a) # 2

test()
print(a) # 1

def test1():
    global a
    a = 2
    print(a) # 2

test1()
print(a) # 2


# 闭包：内部函数，然后将内部函数作为变量返回
def nth_power(exponent):
    def exponent_of(base):
        return base ** exponent
    
    return exponent_of

square = nth_power(2)
print(square(3)) # 3 ^ 2 = 9
cube = nth_power(3) 
print(cube(4)) # 4 ^ 3 = 64

