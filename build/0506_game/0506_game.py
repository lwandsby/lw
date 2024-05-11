import random
import re

import cfg
import pygame
def main():
    pygame.init()
    pygame.display.set_mode(cfg.SCREENSIZE)
    pygame.display.set_caption('彩票游戏')

    t2 = '结束游戏'

    money = input('请输入投入的金豆： ')
    while not money.isdigit():
        print('输入错误')
        money = input('请输入投入的金豆： ')
    else:
        pass
    money = int(money)
    print('当前你的金豆数量为：%d个'%money)
    while 1:
        data1 = []
        for i in range(6):
            n = random.choice([0,1])
            data1.append(n)
        if int(money) < 2:
            print('你的金豆不足，请充值')
            m = input('请输入投入的金豆： ')
            if int(m) == 0:
                break
            else:
                money = int(m)
        while 1:
            j = input('请输入购买的彩票数量(2金豆一注): ')
            while j == 0 or not j.isdigit():
                print('输入错误，请重新输入')
                j = int(input('请输入购买的彩票数量(2金豆一注): '))
            else:
                pass
            j = int(j)
            if money - j*2<0:
                print('金豆不足，当前您的金豆数量为%d个,购买%d注需要%d金豆请重新输入: '%(money,j,j*2))
            else:
                money = money - j *2
                print('购买成功，当前您的金豆数量为: %d个,祝您好运！'%money)
                break
        print('提示：中奖号码有六位数，每位数为0或者1')
        n2 = input('请输入你的六位数号码：（输入的号码为0或者1）')
        while len(n2) !=6:
            print('输入错误请重新输入六位数号码')
            n2 = input('请输入你的六位数号码：（输入的号码为0或者1）')
        else:
            pass

        f = []
        for x in n2:
            f.append(x)
        f1 = str(f)
        f2 = f1.split("'")
        f3 = "".join(f2)
        print('你的号码为:%s'%f3)
        if f3 == str(data1):
            print('中奖号码为：',data1)
            print('恭喜你中大奖啦!!!')
            money = money + j*100
            print('当前你的金豆数量为%d个'%money)
        else:
            print('中奖号码为',data1)
            print('可惜了，这次没有中，继续加油')
        last = input('请问还有继续吗？退出请输入no,继续就输入任意字符：')
        if last == 'no':
            break
        data1=[]
    print(t2.center(50,'*'))
    print('当前你的金豆数量为：%d个，祝您好运！'%money)
if __name__ == '__main__':
    main()