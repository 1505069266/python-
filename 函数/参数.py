# 必须参数


def add(x, y):
    # x  y为必须参数,也叫形参
    return x + y


def add2(x=1, y=1):
    return x + y


print(add2())
