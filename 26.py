# -*- coding: utf-8 -*-
# @Time : 2020/4/29 21:10
# @Author : Louis
# @Software : PyCharm Edition

def newuser():
    user = input('请输入用户名：')
    while userlist.get(user) != None:
        user = input('此用户名已被使用，请重新输入：')
    userlist[user] = input('请输入用户密码：')
    print('注册成功，快登录试试吧!~')

def login():
    user = input('请输入登录用户名：')
    while userlist.get(user) == None:
        user = input('您输入的用户名不存在，请重新输入：')
    password = input('请输入登录密码：')
    while userlist.get(user) != password:
        password = input('您输入的密码有误，请重新输入：')
    print('欢迎进入伊甸园，祝您玩得愉快！')
    exit(1)

# main
userlist = dict()

while True:
    print(''' ---新建用户N/n---
 ---登录帐号E/e---
 ---退出程序Q/q---''')
    dai_ma = input('---请输入指令代码---:')
    if dai_ma == 'N' or dai_ma == 'n':
        newuser()
    elif dai_ma == 'E' or dai_ma == 'e':
        login()
    elif dai_ma == 'Q' or dai_ma == 'q':
        print('谢谢访问，再会！')
        exit(1)
    else:
        print('指令有误，请重新输入!')