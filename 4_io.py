# 控制台IO
name = input("输入你的名字：")
gender = "男" if input("你是一个boy吗？（y/n）") == 'y' else "女"

welcome_prompt = f"Hello {name} ! Welcome to the Python World."
print(welcome_prompt)

# input() 输入的全是字符

a = input("输入第一个数：")
b = input("输入第二个数：")
print(type(a)) # <class 'str'>
print(type(b)) # <class 'str'>

sum = int(a) + int(b) # 需要转化为 int 类型
print(sum)

# 二、文件IO
# 通过一个简单的 NLP 任务学习 Python 文件 I/O 操作
# 1. 读取文件；
# 2. 去除所有标点符号和换行符，并把所有大写变成小写；
# 3. 合并相同的词，统计每个词出现的频率，并按照词频从大到小排序；
# 4. 将结果按行输出到文件 out.txt。

import re
from typing import Dict

# 修复变量未绑定的问题，并使用更安全的with语句
try:
    with open("./data/input_test.txt", "r", encoding="utf-8") as f:
        text = f.read()
except FileNotFoundError:
    print("文件未找到，请检查文件路径是否正确。")
    text = ""

# 2. 去除所有标点符号和换行符，并把所有大写变成小写
if text:
    # 去除标点符号和换行符，并转换为小写
    cleaned_text = re.sub(r'[^\w\s]', '', text.lower())
    # 分割成单词
    words = cleaned_text.split()
    
    # 3. 合并相同的词，统计每个词出现的频率
    word_count: Dict[str, int] = {}
    for word in words:
        word_count[word] = word_count.get(word, 0) + 1
    
    # 按照词频从大到小排序
    sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)
    
    # 4. 将结果按行输出到文件 out.txt
    with open("./data/out.txt", "w", encoding="utf-8") as f:
        for word, count in sorted_words:
            f.write(f"{word}: {count}\n")
    
    print("词频统计结果已保存到 out.txt")