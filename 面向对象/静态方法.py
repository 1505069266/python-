class Student:
    name = ''
    age = 0
    # 一个班级里所有学生的总数
    sum1 = 0

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

    def myNameAge(self):
        print(self.name)
        print(self.age)

    @classmethod  # 类方法  下面方法的参数为cls
    def plus_sum(cls):
        cls.sum1 += 1
        print(cls.sum1)

    @staticmethod  # 静态方法
    def add(x, y):
        # print(self.sum1)  # 报错
        print('这是静态方法!')


# 模板

student1 = Student('zhuxiaole', 23)

Student.plus_sum()

Student.add(1, 2)

print(student1.__dict__)  # 保存着student1中的所有变量

print(Student.__dict__)  # 保存着Student中的所有变量和方法
