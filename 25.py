# -*- coding: utf-8 -*-
# @Time : 2020/3/31 19:41
# @Author : Louis
# @Software : PyCharm Edition

# a = {'F': 70, 'C': 67, 'h': 104, 'i': 105, 's': 115}
# print(a['C'])

def title():
    print('''|---欢迎进入通讯录程序---|
|--- 1:查询联系人资料 ---|
|--- 2:插入新的联系人 ---|
|--- 3:删除已有联系人 ---|
|--- 4:退出通讯录程序 ---|''')
contact = dict() #正确示范
def tong_xun():
    # contact = dict()  错误示范
    code = input('请输入相关的指令代码：')
    if code == '1':
        name = input('请输入联系人姓名：')
        if name in contact:
            print(name,'：', contact[name])
        else:
            print('您输入的用户名有误或不存在')
    elif code == '2':
        name = input('请输入联系人姓名：')
        if name in contact:
            print('您输入的联系人已存在 -->> ',contact[name])
            warn1 = input('是否修改联系人资料（YES/NO）：')
            if warn1 == 'YES':
                contact[name] = input('请输入联系人电话：')
            # else:
            #     print(name,':',contact[name])
        else:
            contact[name] = input('请输入联系人电话：')
            print(name,':',contact[name])
    elif code == '3':
        name = input('请输入联系人姓名：')
        if name in contact:
            contact.pop(name)
            # contact.pop('name') 错误示范
            # del(contact[name]) 也可用此方法
        else:
            print('您输入的联系人不存在。')
    elif code == '4':
        print('|--- 感谢您使用本通讯录 ---|')
        exit(1)
    else:
        print('输入有误，请重新输入')

title()
while 1:
    tong_xun()

