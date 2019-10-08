for x in range(1, 10):
    print(x)


for x in range(10, 0, -2):
    print(x)


a = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(a), 2):
    print(a[i], end="|")


b = a[0:len(a):2]

print(b)