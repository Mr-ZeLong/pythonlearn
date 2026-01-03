# 列表
my_list: list = []
my_list.append(0)
my_list.append("sdfs") # 指点中的元素可以是不用类型
my_list.pop()
print(my_list)

# 元组不可修改
my_tuple = (0, 2, 3 ,4)
print(my_tuple)
# my_tuple[0] = 2 # 报错


# 字典
empty_dic: dict[str, int] = {}
d1 = {'name': 'jason', 'age': 20, 'gender': 'male'}
d2 = dict({'name': 'jason', 'age': 20, 'gender': 'male'})
d3 = dict([('name', 'jason'), ('age', 20), ('gender', 'male')])
d4 = dict(name='jason', age=20, gender='male')

print(d1 == d2 == d3 == d4) # True

my_dic = {"name":"呆瓜", "age":20}
my_dic["money"] = 234234
print(my_dic)
print(my_dic["age"])
# 删除字典元素
my_dic.pop("age")
print(my_dic.get("birthday", "null")) # 不会报错，不存在就得这种使用方式
print(my_dic["birthday"]) # KeyError: 'birthday'


my_dict: dict = {}  # 创建的是空字典
print(type(my_dict)) # 创建的是空字典，而不是空集合
my_set: set[str] = set() # 只有这种创建空集合的方式
print(type(my_set))

my_set.add("sdfsdf")
my_set.add("val")

print("val" in my_set) # True
print("sdfsdfsdf" in my_set) # False

my_set.remove("val")
# my_set.pop() # 删除集合最后一个元素，一般不知道最后一个元素是什么，所以不用
print(my_set)

