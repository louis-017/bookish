# -*- coding: utf-8 -*-
# @Time : 2020/3/11 20:02
# @Author : Louis
# @Software : PyCharm Edition


#1. 密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合
#2. 密码只能由字母开头
#3. 密码长度不能低于16位

# temp = '~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\\'
# warn1 = '您的密码级别过低，请按以下要求升级您的密码：\n1.密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合\n2.密码只能由字母开头\n3.密码长度不能低于16位'
# warn2 = '您的密码级别一般，请按以下要求升级您的密码：\n1.密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合\n2.密码只能由字母开头\n3.密码长度不能低于16位'
# warn0 = '设置成功，密码强度：高级'
# while True:
#     password = input('请输入注册密码：')
#     if len(password)<16:
#         print('密码长度不得小于16位！')
#     else:
#         while password.isalnum():#是否含数字或字母
#             while not password.isalpha():#是否不仅仅只含字母
#                 while not password.isdigit():#是否不仅仅只含数字
#                     for each in password:#是否含有指定特殊字符
#                         if each in temp:
#                             print(warn0)
#                         else:
#                             print(warn2)
#                     break
#                 break
#             break
#         while password.isdigit():#是否只含数字
#             print(warn1)
#             break
#         while password.isalpha():#是否只含字母
#             print(warn1)
#             break
#         break




temp = '~','!','@','#','$','%','^','&','*','(',')','_','=','-','/',',','.','?','<','>',';',':','[',']','{','}','|','\\'
warn1 = '您的密码级别过低，请按以下要求升级您的密码：\n1.密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合\n2.密码只能由字母开头\n3.密码长度不能低于16位'
warn2 = '您的密码级别一般，请按以下要求升级您的密码：\n1.密码必须由数字、字母及特殊字符（仅限：~!@#$%^&*()_=-/,.?<>;:[]{}|\）三种组合\n2.密码只能由字母开头\n3.密码长度不能低于16位'
warn0 = '设置成功，密码强度：高级'
while True:
    password = input('请输入注册密码：')
    if len(password)<16:
        print('密码长度不得小于16位！')
    else:
        while password.isalnum():#是否含数字或字母
            while not password.isalpha():#是否不仅仅只含字母
                while not password.isdigit():#是否不仅仅只含数字
                    for each in password:#是否含有指定特殊字符
                        if each in temp:
                            print(warn0)
                        else:
                            print(warn2)
                    break
                break
            break
        while password.isdigit():#是否只含数字
            print(warn1)
            break
        while password.isalpha():#是否只含字母
            print(warn1)
            break
        break
