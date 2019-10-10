# reduce

from functools import reduce

# 连续计算,连续调用lambda
list_x = [2, 5, 6, 4]

r = reduce(lambda x, y: x*y, list_x)  # 求和
# ((2*5)*6)*4
print(r)

print(sum(list_x))