from functools import reduce


square = lambda x : x ** 2
arg = range(10)

# 下面两个操作是等价的
nums = [square(num) for num in arg]
nums1 = [(lambda x : x ** 2)(num) for num in arg]
nums2 = list(map(square, arg))

print(arg) # range(0, 10)
print(nums) # [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(nums == nums1 == nums2) # True

# 其他的数据处理函数
nums3 = list(filter(lambda x : x % 2 == 0, arg))
print(nums3) # [0, 2, 4, 6, 8]
nums4 = reduce(lambda x,y : x + y, arg) # 45
print(nums4) # 45


d = {'mike': 10, 'lucy': 2, 'ben': 30}
# 根据字典的 value 逆序排序, 注意一定要使用 items() 方法获取 键值对，否则默认是获取 key 列表
sorted_items = sorted(d.items(), key=lambda item : item[1], reverse=True)
print(sorted_items) # [('ben', 30), ('mike', 10), ('lucy', 2)]

