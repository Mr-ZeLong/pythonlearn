s1 = 'hello'
s2 = "hello"
s3 = """hello"""
print(s1 == s2 == s3)
print(s1[0])
print(s1[1:3]) # 切片 [from, to) 

s4 = "I'm Joker"
s5 = "I'm \"呆瓜\""
print(s5)
s6 = """
I'm "呆瓜"
"""
print(s6)  # 和 s5 效果一样
