# -*- coding: utf-8 -*-
# @Time : 2020/3/7 18:20
# @Author : Louis
# @Software : PyCharm Edition

mypassword = '666'
password = input('欢迎~请输入登录密码：')
count = 3
while count:
    if password == mypassword:
        print('欢迎回来，祝您玩得愉快~')
        break
    while '*' in password:
        print('输入错误，密码中不能含有符号*，您还有',count,'次机会')
        password = input('请重新输入密码：')
    if password != mypassword:
        print('密码错误，您还剩',count-1,'次机会,',sep='',end='')
        count-=1
        if count == 0:
            print('输入错误，帐号已锁定')
            break
        else:
            password = input('请重新输入密码：')



#小甲鱼
# count = 3
# password = 'FishC.com'
#
# while count:
#     passwd = input('请输入密码：')
#     if passwd == password:
#         print('密码正确，进入程序......')
#         break
#     elif '*' in passwd:
#         print('密码中不能含有"*"号！您还有', count, '次机会！', end=' ')
#         continue
#     else:
#         print('密码输入错误！您还有', count-1, '次机会！', end=' ')
#     count -= 1