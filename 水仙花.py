# -*- coding: utf-8 -*-
# @Time : 2020/3/8 20:46
# @Author : Louis
# @Software : PyCharm Edition

#转成字符串，然后利用字符串下标索引，再转成整型
for num in range(100, 1000):
    i = str(num)
    a = int(i[0])
    b = int(i[1])
    c = int(i[2])
    if num == a ** 3 + b ** 3 + c ** 3:
        print(num)
