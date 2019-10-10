# 优化装饰器

import time


def decorator(func):
    # key word
    def wrapper(*args, **kw):
        print(time.time())
        func(*args, **kw)
    return wrapper


@decorator
def f1(func_name):
    print('this is function' + func_name)


@decorator
def f2(func_name1, func_name2):
    print('this is a function' + func_name1 + func_name2)


f2('朱晓乐', '笨蛋')