# -*- coding:utf-8 -*-



# f = open('OpenMe.mp3')
# for each_line in f:
#     print(each_line,end='')
# f.close()

# file1 = open('OpenMe.mp3')
# file2 = open('OpenMe.txt', 'wt')
# file2.write(file1.read())
# file1.close()
# file2.close()
#
# file2 = open('OpenMe.txt','r')
# for each_line in file2:
#     print(each_line,end='')
# file2.close()

# f = open('OpenMe.txt')
# for each_line in f:
#     print(each_line,end='')
# f.close()


import os1
生命值=10
经验值=0
法力值=50
暴击槽=0
a=1
b=0
c=0
d=0
e=0
f=0
def 判断():
    global 生命值
    global 经验值
    global a
    global b
    if a==1:
        if 经验值>=10:
            print('恭喜升级！当前生命值为100！获得技能"旋风斩"！')
            生命值=100
            b=1
            a=0
while e==0:
    生命值=str(生命值)
    while True:
        选择=input('欢迎回家!1.打小怪2.挑战boss（当前生命值为：'+生命值+'）\n')
        if 选择=='1' or 选择=='2':
            break
    i=os.system("cls")
    生命值=int(生命值)
    选择=int(选择)
    if 选择==1:
        print('野生的蚂蚱出现了！')
        print('你把它打死了，生命值-1，经验值+3！')
        生命值=生命值-1
        经验值=经验值+3
        判断()
        if 生命值<=0:
            print('你死了！游戏结束！解锁成就_骚年好毅力')
            e=1
            break
    if 选择==2:
        print('boss:你竟敢挑战我？我可不会手下留情！')
        boss血量=180
        while True:
            while True:
                生命值=str(生命值)
                战斗=input('1.攻击2.释放旋风斩3.叫爸爸4.嘲讽'+'(当前生命值为'+生命值+'\n')
                if 战斗=='1' or 战斗=='2' or 战斗=='3' or 战斗=='4':
                    break
            生命值=int(生命值)
            i=os.system("cls")
            战斗=int(战斗)
            if 战斗==1 and 暴击槽==3:
                print('暴击！你打出了20点伤害！')
                print('boss:mmp!')
                boss血量-=20
                暴击槽=0
            if 战斗==1 and 暴击槽!=3:
                print('你对boss造成了3点伤害~')
                print('boss:没吃饭？搁这刮痧呢妹妹~')
                boss血量-=3
                暴击槽+=1
            if 战斗==2 and 法力值>=25 and b==1:
                print('player:吃劳资一记旋风斩！')
                print('boss:你干嘛啊~哎呦~(造成50点伤害！效果拔群！)')
                boss血量-=50
                法力值-=25
            if 战斗==2 and 法力值<25 and b==1:
                print('法力值不足~')
            if 战斗==2 and 法力值<25 and b!=1:
                print('你还没学会此技能，所以你打了个趔趄摔跤了！(hp-1)')
                生命值-=1
            if 战斗==3:
                print('player:爸爸！')
                print('(boss回予你一个冷笑，士气-1)')
            if 战斗==4:
                print('player:嘿！孙贼！')
                print('(你把boss激怒了！)')
                c=1
            if boss血量<=0:
                print('player win!恭喜!')
                e=1
                break
            if c==1 and b==1:
                print('boss愤怒地扇了你一巴掌！生命值-50~')
                生命值-=50
                判断()
            elif c==1 and b==0:
                if f==0:
                    print('你太弱了，躲过了boss的攻击！解锁成就_侏儒症')
                    f+=1
                print('你头上冒出了miss的字眼~')
                判断()
            else:
                print('boss:我的回合！(生命值-8)')
                生命值-=8
                判断()
            if 生命值<=0:
                print('你死了！游戏结束！')
                e=1
                break
            boss血量=str(boss血量)
            print('Boss当前剩余血量为'+boss血量)
            boss血量=int(boss血量)
d=input('按任意键退出......')
