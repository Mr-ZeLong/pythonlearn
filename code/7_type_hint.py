# 类型提示，一般用在函数参数和返回值上

# 可以是 int 或 str 类型
from typing import List, Set, Tuple, Dict, Optional


my_list: List[int | str] = [1, 2, 3, '4', '5']

# 元组必须指定每个元素的类型
my_tuple: Tuple[int, str, str] = (1, '2', 'str')

my_set: Set[int] = {1, 2, 3}

# 字典指定Key和value的类型
my_dict: Dict[str, int] = {'a': 1, 'b': 2, 'c': 3}

# 可选参数，默认值为 None
def func(arg: Optional[int | str] = None) -> Optional[int | str]:
    if arg is None:
        return 0
    return arg

print(func())
print(func(100))
print(func('100'))