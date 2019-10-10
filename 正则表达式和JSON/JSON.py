import json

json_str = '{"name": "zhuxiaole", "age": 18}'

# 反序列化  JSON转化成python语言

s = json.loads(json_str)

print(s)

print(type(s))

# JSON中的值转化到python中的格式会如下转化
# json   python
# object  dict
# array   list
# string  str
# number  int
# number  float
# true    True
# false   False
# null    None

# 序列化  python转化成JSON

student = [{'name': '朱晓乐', 'age': 18}, {'name': '郑璇', 'age': 18}]

j = json.dumps(student)

print(j)

