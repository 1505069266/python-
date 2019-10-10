# 类型
# 绿钻, 黄钻, 红钻, 黑钻
# 1.绿钻
# 2.黄钻
# 3.红钻
# 4.黑钻

# 字典 枚举

from enum import Enum

a = {'yellow': 2, 'green': 3}


class VIP(Enum):
    yellow = 1
    green = 2
    black = 3
    red = 4


# 枚举类型
print(VIP.yellow)

print(type(VIP.yellow))

# 枚举的名字
print(VIP.yellow.name)

print(type(VIP.yellow.name))

# 枚举的值
print(VIP.yellow.value)

print(type(VIP.yellow.value))

for x in VIP:
    print(x)
    print(x.name)
    print(x.value)

result = VIP.green == VIP.green

print(result)


class VIP1(Enum):
    green: 2
    yellow: 3


a = 1

print(VIP(a))
