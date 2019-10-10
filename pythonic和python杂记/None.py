# None  空

# 误区: None不等于字符串   None不等于空的列表   None不等于0

print(None == 0)

print(None == {})

print(None == '')

print(type(None))


def func():
    return None


print(None == func())

# True False 对应关系

# 自定义的对象

# 实例默认是True


class Test:  # 实例是True还是False取决于类的__len__和__bool__方法   __bool__的返回值大于__len__
    def __len__(self):
        return 0

    def __bool__(self):
        return True


test = Test()

print(bool(test))
print(bool({}))
print(bool([]))
print(bool(0))
print(bool(None))
print(bool())

if test:
    print('T')
else:
    print('F')