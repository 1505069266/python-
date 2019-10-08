"""
 for循环
"""

a = [['apple', 'orange', 'banana', 'grape'], (1, 2, 3)]

for x in a:
    for j in x:
        print(j)
else:
    print('end')


a = [1, 2, 3, 4]

for x in a:
    if x == 2:
        continue
    print(x)
else:
    print('end')

for x in a:
    if x == 2:
        break
    print(x)
else:
    print('end')