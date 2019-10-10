# 旅行者

# 起点 x = 0

# 每次走路都是在上次的基础上加上去


# 非闭包方案
step = 0


def running(a):
    global step
    new_step = step + a
    step = new_step
    return step


print(running(2))
print(running(33))


# 闭包方案

origin = 0


def travel(pos):
    def run(a):
        nonlocal pos
        new_pos = pos + a
        pos = new_pos
        return new_pos
    return run


people = travel(origin)

print(people(2))

print(people(2))
