A = [1, 2, 3, 4]
B = [4, 5, 6]

print(A * 3 + B)

moonHero = ['新月打击', '苍白之瀑', '月神冲刺']

type1 = 'ddd'

print(type1)

a = '1'
a = 1
a = (1, 2, 3)
a = [1, 2, 3]
# python是动态语言
b = a

a[0] = 'ddd'

print(b)

a = 'hello'

b = a

print(id(a))

print(id(b))

print(a == b)

a = a + "world"

print(id(a))

print(a == b)

