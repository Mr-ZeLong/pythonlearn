try:
    a = int(input("请输入一个整数："))
    b = int(input("请输入另一个整数："))
    result = a / b
    print(result)
except ValueError:
    print("请输入一个整数")
except ZeroDivisionError:
    print("除0错误")