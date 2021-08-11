import random as rand

num = rand.randint(1,6)
print(num)
b = 0
a = 0
while a != num  :
    a =  int(input('주사위를 던져서 나온 숫자를 맞혀주세요.'))
    b = b + 1
    if a != num :
        print('틀렸습니다. 다시 맞혀주세요.')
print('정답입니다. %d 번 만에 맞혔습니다.'%b) 