import random
poke = {'spade':['A','2','3','4','5','6','7','8','9','10','J','Q','K'],
        'hearts':['A','2','3','4','5','6','7','8','9','10','J','Q','K'],
        'diamond':['A','2','3','4','5','6','7','8','9','10','J','Q','K'],
        'plum blossom':['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        }


def in_put():
    player = []
    temp_num = 0
    while 1:
        temp = input("input your names one by one and enter 'ok' to star game: ")
        if temp == 'ok':
            break
        player.append(temp)
        temp_num += 1
    return player,temp_num


def game(play,num):
    three1 = []
    three5 = []  # 已出牌库的牌

    for i in enumerate(poke):  # 枚举
        temp1 = poke[i[1]]  # 选序号的list
        temp2 = i[1]  # 选花色
        for k in range(13):
            three2 = []
            three2.append(temp2)  # 花色
            three2.append(temp1[k])  # 序号
            three1.append(three2)

    for s in range(num):
        three3 = []
        three4 = []
        three4.append(play[s])
        m = 0
        while m < 3:
            tem1 = random.randint(0, 51)
            for j in three1:
                if three1[tem1] not in three5:
                    three5.append(three1[tem1])
                    three3.append(three1[tem1])
                    m += 1
        three4.append(three3)
        print(three4)
    return

a,b=in_put()
game(a,b)








