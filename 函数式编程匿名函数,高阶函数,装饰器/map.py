# map


def square(x):
    return x**2


list_x = [1, 2, 5, 4, 8, 5]


a = map(square, list_x)

print(list(a))