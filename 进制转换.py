# -*- coding: utf-8 -*-
# @Time : 2020/3/12 19:07
# @Author : Louis
# @Software : PyCharm Edition

while True:
    num = input('请输入一个整数(输入Q结束程序)：')
    if num.isdigit():
        num = int(num)
    elif num == 'Q' or num =='q':
        exit(1)
    else:
        print('输入类型非十进制整数！\n程序退出！')
        exit(0)

    print('十进制 -> 十六进制：%d -> %x'%(num,num))
    print('十进制 ->   八进制：%d -> %o'%(num,num))
    # num1 = bin(num)
    print('十进制 ->   二进制：%d -> '%num,bin(num))
