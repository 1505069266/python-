class Student:
    name = ''
    age = 0
    # 一个班级里所有学生的总数
    sum1 = 0
    __score = 0

    # 实例方法
    def __init__(self, name, age):
        # 构造函数 实例化的时候会运行这里的代码
        self.name = name
        self.age = age
        self.__class__.sum1 += 1
        print("当前班级人数:" + str(self.__class__.sum1))
        # print('我是:' + name)
        # print("我是:" + self.name)

    # 行为与特征

    def marking(self, score):
        if score < 0:
            score = 0
        self.__score = score

    # 这是一个私有方法
    def __myName(self):
        print(self.name)


# 模板

student1 = Student('zhuxiaole', 23)

student1.marking(95)

student1.__score = -1  # 为什么不会报错  这里是给student1新添加了一个__score属性 所有不会报错

print(student1.__score)

print(student1._Student__score)  # 还是可以读取,但是不建议这样操作

print(student1.__dict__)  # 保存着student1中的所有变量

print(Student.__dict__)  # 保存着Student中的所有变量和方法

# 公开的 public  私有的 private
# python私有方法  __方法名
# python私有属性  __属性名
