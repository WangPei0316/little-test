from random import choice

# score_you = 0
# score_com = 0
score = [0,0]
direction = ['left', 'center', 'right', ]

def kick():
    print("====You Kick!====")
    print("Choose one side to shot:")  # 你选择射门方向
    print('left,center,right')
    you = input()
    print("You kicked " + you)
    com = choice(direction)  # 电脑随机扑救方向
    if you != com:
        print('You win')
        score[0] += 1
    else:
        print('Oops....')
    print('Score:Your score {}-Com score {}'.format(score[0], score[1]))

def save():
    print("====You Save!====")
    print("Choose one side to side:")  # 你选择扑救方向
    print('left,center,right')
    you = input()
    print("You saved " + you)
    com = choice(direction)  # 电脑随机射门方向
    if you == com:
        print('You Win')
    else:
        print('Oops....')
        score[1] += 1
    print('Score:Your score {}-Com score {}'.format(score[0], score[1]))

for i in range(5):
    print("====Round%d===="%(i+1))
    kick()
while(score[0]==score[1]):
    i += 1
    print("====Round%d====" % (i + 1))
    kick()

