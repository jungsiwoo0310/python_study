import random

input("엔터키를 누르면 주사위를 던집니다.")
dice1 = random.randint(1,6)
dice2 = random.randint(1,6)
dice3 = (dice1 + dice2) *2
dice4 = (dice1 + dice2) *3
dice5 = (dice1 + dice2) *4
dice = dice1 + dice2

print("첫번째 주사위 :%d "%dice1)
print("두번쨰 주사위 :%d"%dice2)

if dice1 == dice2 :
    if dice1 % 3 == 0 and dice2 % 3 == 0 :
            print("%d 칸 이동하세요!!"%dice5)
    elif dice1 == dice2 :
        print("%d 칸 이동하세요!!"%dice3)


elif dice1 % 3 == 0 and dice2 % 3 == 0 :
    print("%d 칸 이동하세요!!"%dice4)

else :
    print("%d 칸 이동하세요!!"%dice)

            