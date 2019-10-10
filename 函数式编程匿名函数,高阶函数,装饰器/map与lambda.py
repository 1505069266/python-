# map  lambda


list_x = [1, 2, 5, 4, 8, 5]


a = map(lambda x: x**2, list_x)

print(list(a))


list_y = [2, 5, 7, 4, 9, 6]

b = map(lambda x, y: x*x+y,list_x, list_y)

print(list(b))