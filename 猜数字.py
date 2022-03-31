# -*- coding: utf-8 -*-
# @Time : 2020/2/25 19:33
# @Author : Qin
# @Software : PyCharm Edition

import random
num = random.randint(0,9)
scrf = input('请输入一个个位阿拉伯数字：')
guess = int(scrf)
while guess != num:
    scrf = input('it\'s wrong,try again：')
    guess = int(scrf)
    if scrf == num:
        print('very good!')
print('Congratulations!\nYou did it!')
