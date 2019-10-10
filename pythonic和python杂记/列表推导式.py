# 列表推导式
# 集合推导式
# map filter
# set 也可以被推导
# dict 也可以被推导

a = [1, 2, 3, 4, 5, 6, 7, 8]

b = [i**3 for i in a if i >= 5]

c = {i**3 for i in a if i >= 5}

print(b)


# 字典的列表推导式

students = {
    '喜小乐': 18,
    '朱晓乐': 23,
    '郑璇': 17
}

b = {key for key, value in students.items()}

print(b)

for x in b:
    print(x)
