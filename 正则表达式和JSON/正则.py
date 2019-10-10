import re

a = 'eAAAAqw12wq5765eqwsd5wqe523t67wet'

r = re.findall('7', a)

print(r)

d = re.findall('[^A-Z]', a)

print(d)
# 'Python' 普通字符  '\d' 元字符

s = 'abc,acc,asd,csd,weq,adc,sdc'

r = re.findall('a[^cfd]c', s)

print(r)

# 概括字符集

# \d 所有的数字   \D  所有的非数字
# \w 所有的单词字符  == [A-Za-z0-9_]      \W 所有的非单词字符  除了[A-Za-z0-9_]
# \s 所有的空白字符   \S 所有的非空白字符
# . 匹配除换行符\n之外其他所有字符

import re

a = 'python12\r32ja\tvae3 2__&*-+dwejs'

r = re.findall('\s', a)

# 数量词
a = 'python12\r32java\tvae3 2php__&*-+dwejs'

r = re.findall('[a-z]{3,6}', a)  # 匹配3到6个字符的连一起字符  遵循贪婪匹配  能多就不少  也就是能有6个连一起的 就不会找3个的

print(r)

# 贪婪  非 贪婪  能多匹配就不少匹配  非贪婪模式在后面加上 '?'
a = 'python12\r32java\tvae3 2php__&*-+dwejs'

r = re.findall('[\d]{1,10}?', a)

print(r)

# * 匹配0次或者无限多次

a = 'pytho0python1pythonn2'

r = re.findall('python*', a)

print(r)

# + 匹配1次或者无限多次

r = re.findall('python+', a)

print(r)

# ?匹配0次或1次

r = re.findall('python?', a)

print(r)

# 边界匹配
# ^ 匹配字符串的开头
# $ 匹配字符串的结尾

qq = '150569223236'

r = re.findall('^\d{4,8}$', qq)

print(r)

# 组

a = 'PythonPythonPythonPythonPythonJS'

r = re.findall('(Python){3}(JS)', a)

print(r)

# 模式  re.I(忽略大小写)  re.S(匹配所有字符)

language = 'PythonJavaC#javascriptC#C#c#'

r = re.findall('python', language, re.I | re.S)

print(r)

# re模块的函数
# 替换
r = re.sub('C#', 'GO', language, 0, re.I)

# l = language.replace("C#", 'GO')
#
# print(l)

print(r)


def convert(value):
    return '!!ddd!!'


r = re.sub('C#', convert, language, 0, re.I)

print(r)

# 找出一段字符中的数字,大于5的变成9  小于5的变成0

s = 'AADQEQ3235768DEW43327'


def convert(value):
    matched = value.group()
    if int(matched) >= 5:
        return '9'
    else:
        return '0'


r = re.sub('\d', convert, s, 0)

print(r)

s = 'A433D3D312QWQ3'

r = re.search('\d', s)  # 搜索第一个满足的字符 不匹配返回None

print(r)

r = re.match('\d', s)  # 从字符串的开头去匹配  不匹配返回None

print(r)

s = 'life is short, i use python dwe python'

r = re.search('life(.*)python(.*)python', s)


print(r.group(1))
print(r.group(2))

r = re.findall('life(.*)python', s)

print(r)

