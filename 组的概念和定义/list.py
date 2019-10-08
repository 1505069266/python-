arr = [1, 2, 3, 4, 5, 6]

print(type(arr))

arr.append('ddd')

print(arr)

arr1 = [[1, 2], [3, 4], 5]

print(arr1)

print(arr1[0][1])

newMoon = ['新月打击', '苍白之瀑', '月之降临', '月神冲刺']

print(newMoon[0])

print(newMoon[0:])

hero = newMoon + ['点燃', '虚弱']

print(hero)

# 元组
yuan = (1, 2, 3, 4, 5)

print(yuan[2])

print(yuan + (8,9,74))

print(type(yuan))

print(type('hello'))

print(type(1))

# python中一个括号包裹着元素,会判断你是在做数学运算,所以是int和str类型,默认把()去掉了

# 一个元素的元组  (1,)  一个元素的没用的元组 ()

print(type((1,)))

print(type(()))

print(type([1]))

print(3 not in [1, 2, 5, 4])

print(3 in [1, 2, 3, 4, 5])

print(len(yuan))

print(max("yuan"))

print(min(yuan))

print(ord("y"))