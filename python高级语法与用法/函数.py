
def f1():
    a = 10

    def f():
        a = 20
        print(a)  # 20

    print(a)  # 10

    f()

    print(a)  # 10


f1()

