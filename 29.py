print('==='*20)

def new_flie():
    flie_name = input('请输入文件名：')
    flie_new = open(flie_name,'x')
    print('输入":w"以保存并退出')
    while True:
        content = input()
        if content == ':w':
            break
        else:
            flie_new.writelines('%s\n'%content)
    flie_new.close()

def find_different():
    file_0 = input('請輸入第一個文件名：')
    file_1 = input('請輸入第二個文件名：')
    target_0 = open(file_0, 'r')
    target_1 = open(file_1, 'r')
    line_number = 0
    for each_line0 in target_0:
        each_line1 = target_1.readline()
        # if each_line0 == each_line1:
        #     print('两份文件一致')
        #     break
        each_line1 = list(each_line1)
        line_number += 1
        address = 0
        for each_0 in each_line0:
            each_1 = each_line1[address]
            address += 1
            if each_0 != each_1:
                print('第%d行' % line_number, '第%d處' % address, '出现不一样')
                break
    target_0.close()
    target_1.close()

import os
import easygui as g
g.msgbox('666')