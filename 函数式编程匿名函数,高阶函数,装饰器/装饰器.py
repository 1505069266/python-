# 装饰器
# 特性 注释

import time

#
# def f1():
#     print(time.time())
#     print('This is now time')
#
#
# f1()


# 对修改是封闭的  对扩展是开放的


def decrator(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper


def f1():
    print('This is now time')


f = decrator(f1)

f()

# 语法糖装饰器

def decrator1(func):
    def wrapper():
        print(time.time())
        func()
    return wrapper

@decrator1
def f1():
    print('This is now time')


f1()


