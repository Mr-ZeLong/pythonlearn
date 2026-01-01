nums = range(100)
my_nums = [num if num == 0 else 0 for num in nums if num % 100 == 0]
print(my_nums)

my_list = [(x, y) for x in range(0, 10) if x != 5 for y in range(0, 10) if x != y]
print(my_list)

# 等价于嵌套循环
my_list1 = []
for x in range(10):
    for y in range(10):
        if x == y :
            continue
        my_list1.append((x, y))
print(my_list == my_list1) # True


# 遍历字典
d = {'mike': 10, 'lucy': 2, 'ben': 30}
keys = [key for key in d] # 默认获取的是 字典的key ['mike', 'lucy', 'ben']
vals = d.values() #  dict_values([10, 2, 30])
items = d.items() # dict_items([('mike', 10), ('lucy', 2), ('ben', 30)])

print(keys)
print(vals)
print(items)
