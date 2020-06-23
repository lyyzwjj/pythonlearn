import random
# 1石头2剪刀3布
player = random.randint(1,3)
computer = random.randint(1,3)
print("玩家选的的是%d - 电脑选择的是%d" % (player, computer))
if ((player == 1 and computer == 2)
        or (player == 2 and computer == 3)
        or (player == 3 and computer == 1)):
    print("玩家胜利")
elif (player == computer):
    print("再战")
else:
    print("电脑胜利")
