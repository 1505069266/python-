# filter 过滤

# 去除为1的值

list_x = [1,0,0,0,5,3,2,0,0,0,4]

a = filter(lambda x: True if x != 1 else False, list_x)

print(a)

print(list(a))

# 判断大小写  去除小写字母

list_u = ['d', "D", "q", "q", "e", "w", "E", "t", "O"]

b = filter(lambda x: False if x.islower() else True, list_u )

print(list(b))