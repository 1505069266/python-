# 类,对象
# 实例化
# 类最基本的作用: 封装


class Student:
    name = ''
    age = 0

    def print_file(self):
        print('name:' + self.name)
        print('age:' + str(self.age))


student = Student()

student.print_file()