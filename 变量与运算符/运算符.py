c = 1

c = c + 1

c += 1

print(c)

c -= 2

print(c)

c *= 3

print(c)

c **= 3

print(c)

# 关系运算符

print(1 == 1)

print(1 > 2)

print(1 >= 1)

print(1 >= 2)

print(1 != 2)

print(1 != 1)

# 逻辑运算符

if 1 > 0 and 1 > -2:
    print('and')

if 1 > 0 or 1 > 2:
    print('or')

if not 1 > 2:
    print('not')

# 成员运算符

list1 = [1, 2, 3, 5, 4]

print(1 in list1)

print(22 not in list1)

# 身份运算符

a = 1

b = 1

print(a == b)

print(a is b)

a = 1

b = 1.0

print(a == b)

print(a is b)  # 比较的是两个数的id()是否一样

a = {1, 2, 3}

b = {2, 1, 3}

print(a == b)  # True

print(a is b)  # False  id(a) == id(b)

print(id(a))

print(id(b))

a = (1, 2, 3)

b = (2, 1, 3)

print(a == b)

print(a is b)

a = (1,2,3)

print(type(a) == str)

print(isinstance(a, (int, str, dict)))

# 位运算符
a = 2

b = 3

print(a & b)

