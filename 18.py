# -*- coding: utf-8 -*-
# @Time : 2020/3/16 19:52
# @Author : Louis
# @Software : PyCharm Edition




# 编写一个符合以下要求的函数：
#  a) 计算打印所有参数的和乘以基数（base=3）的结果
#  b) 如果参数中最后一个参数为（base=5），则设定基数为5，基数不参与求和计算。

# def jisuan(*i,base = 3):
#     if i[len(i)-1] == 5:
#         base = 5
#         print('计算结果=', (sum(i)-5) * base, sep='')
#     else:
#         print('计算结果=',sum(i)*base,sep='')
#
# jisuan(10,1,2,3,4,5,3,5)


# 寻找水仙花数
# 题目要求：如果一个3位数等于其各位数字的立方和，则称这个数为水仙花数。例如153 = 1 ^ 3 + 5 ^ 3 + 3 ^ 3，因此153是一个水仙花数。编写一个程序，找出所有的水仙花数。
# def flower():
#     for num in range(100,1000):
#         i = str(num)
#         a = int(i[0])
#         b = int(i[1])
#         c = int(i[2])
#         if a**3+b**3+c**3 == num:
#             print(num,end=' ')
# flower()


# 编写一个函数 findstr()，该函数统计一个长度为 2 的子字符串在另一个字符串中出现的次数。例如：假定输入的字符串为“You cannot improve your past, but you can improve your future. Once time is wasted, life is wasted.”，子字符串为“im”，函数执行后打印“子字母串在目标字符串中共出现 3 次”。
def findstr():
    str0 = input('目标字符串：')
    str1 = input('子字符串（两个字符）：')
    while len(str1) != 2:
        str1 = input('输入错误，请输入两个字符长度的子字符串：')
    i = str0.count(str1)
    print('子字符串在目标字符串中共出现',i,'次',sep='')

findstr()
