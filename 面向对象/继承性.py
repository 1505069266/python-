class People:
    def __init__(self, gender):
        self.gender = gender

    def running(self):
        print(self.name + 'running')


class Student(People):
    sum = 0

    def __init__(self, gender, name, age):
        # People.__init__(self, gender)  # 普通的方法调用, 调用父类的方法  所以要传self  这样只能针对People父类   不可取
        super(Student, self).__init__(gender)  # 正确的调用父类的__init__方法使用 super
        self.name = name
        self.age = age
        self.__score = 0
        self.__class__.sum += 1

    def do_homework(self):
        super(Student, self).running()  # 子类调用父类的方法running
        print(self.name + " 在做作业")


zhuxiaole = Student('男', '朱晓乐', 23)

zhuxiaole.do_homework()

print(zhuxiaole.gender)

zhuxiaole.running()
