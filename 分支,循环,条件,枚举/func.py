"""
 一个小程序
"""

account = 'express'
password = "123456"

user_account = input('please input account:')
user_password = input('please input password:')

if account == user_account and password == user_password:
    print('success')
else:
    print('fail')

