import copy

# == 和 is 的区别
# == 一般都进行了重载, 执行的是__eq__方法, 递归遍历内部的值是否相等
# is 比较的是内存地址是否相等，一般用于单例模式判断和 is None 判断

a = None
print(a is None) # True

# 浅拷贝(只拷贝引用地址)
# 深拷贝(递归拷贝所有对象)
l1 = [1, 2, 3]
l2 = list(l1) 
l2[0] = 100
print(l1 == l2) # False

l1 = [[1, 2], (30, 40)]
l2 = list(l1) # 浅拷贝
l3 = copy.copy(l1) # 浅拷贝
l4 = copy.deepcopy(l1) # 深拷贝
print(l1 == l2 == l3 == l4) # True
print(l1[0] is l2[0] and l1[1] is l2[1]) # True
print(l1[0] is l3[0] and l1[1] is l3[1]) # True
print(l1[0] is l4[0] and l1[1] is l4[1]) # False

l1.append(100)
l1[0].append(3)
print(l1) # [[1, 2, 3], (30, 40), 100]
print(l2) # [[1, 2, 3], (30, 40)]
print(l3) # [[1, 2, 3], (30, 40)]
print(l4) # [[1, 2], (30, 40)]

# 元组是不可变类型，所以会重新创建一个元组，然后赋值给 l1[1]
l1[1] += (50,)
print(l1) # [[1, 2, 3], (30, 40, 50), 100]
print(l2) # [[1, 2, 3], (30, 40)]
print(l3) # [[1, 2, 3], (30, 40)]
print(l4) # [[1, 2], (30, 40)]


def func(d):
    d['a'] = 10
    d['b'] = 20

d = {'a': 1, 'b': 2}
func(d)
print(d)
