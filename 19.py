# -*- coding: utf-8 -*-
# @Time : 2020/3/17 19:22
# @Author : Louis
# @Software : PyCharm Edition

# def jugleHuiWen():
# #     while True:
# #         print('='*20, 'RESTART', '='*20,sep='')
# #         str0 = input('请输入一句话：')
# #         if str0 == 'Q' or 'q' and len(str0)==1:
# #             print('程序退出')
# #             exit(1)
# #         elif str0 == str0[::-1]:
# #             print('是回文联！\n')
# #         else:
# #             print('不是回文联！\n')
# #
# # jugleHuiWen()




def count(*str0):
    length = len(str0)
    a = 1
    for i in range(length):
        b = 0
        c = 0
        d = 0
        e = 0
        for each in str0[i]:
            if each.isalpha():
                b += 1
            elif each.isdigit():
                c += 1
            elif each == ' ':
                d += 1
            else:
                e = len(str0[i]) - (b+c+d)

        print('第%d个字符串共有：英文字母%d个，数字%d个，空格%d个，其他字符%d个'%(a,b,c,d,e))
        a += 1


count('啊啊啊，I Hate You!!!*3','38!GUN！！！','666')
